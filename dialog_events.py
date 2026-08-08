"""
Event handlers for Dream Prompter dialog
Handles all user interactions and UI events
"""

from gi.repository import GLib, Gtk

from dialog_threads import DreamPrompterThreads
from i18n import _, ngettext
from models.factory import get_default_model, get_model_by_name
from settings import load_settings, store_settings

MIME_TYPE_LABELS = {
    "image/gif": "GIF",
    "image/jpeg": "JPEG",
    "image/png": "PNG",
    "image/webp": "WebP",
}


class DreamPrompterEventHandler:
    """Handles all events for the Dream Prompter dialog"""

    def __init__(self, dialog, ui, image=None, drawable=None):
        """Initialize event handler"""
        self.dialog = dialog
        self.ui = ui
        self.image = image
        self.drawable = drawable
        self.ui.event_handler = self
        self.model = get_default_model()

        self.threads = DreamPrompterThreads(ui, image, drawable)
        self.threads.set_callbacks(
            {"on_success": self.close_on_success, "on_error": self.show_error}
        )

        settings = load_settings()
        if self.ui.toggle_visibility_btn and self.ui.api_key_entry:
            is_visible = settings.get("api_key_visible", False)
            self.ui.toggle_visibility_btn.set_active(is_visible)
            self.on_toggle_visibility(self.ui.toggle_visibility_btn)

        def after_init():
            if self.ui.api_key_entry:
                self.ui.api_key_entry.select_region(0, 0)
            if self.ui.prompt_textview:
                self.ui.prompt_textview.grab_focus()

            # Update self.model to match the selected model in the dropdown
            if self.ui.model_dropdown:
                selected_model_name = self.ui.model_dropdown.get_active_id()
                if selected_model_name:
                    selected_model = get_model_by_name(selected_model_name)
                    if selected_model:
                        self.model = selected_model

            self.update_ui_limits()
            self.update_generate_button_state()

        GLib.idle_add(after_init)

    def close_on_success(self):
        """Close dialog on successful completion"""
        self.dialog.response(Gtk.ResponseType.OK)

    def connect_all_signals(self):
        """Connect all UI signals to handlers"""
        if self.ui.model_dropdown:
            self.ui.model_dropdown.connect("changed", self.on_model_changed)

        if self.ui.edit_mode_radio:
            self.ui.edit_mode_radio.connect("toggled", self.on_mode_changed)
        if self.ui.generate_mode_radio:
            self.ui.generate_mode_radio.connect("toggled", self.on_mode_changed)

        if self.ui.toggle_visibility_btn:
            self.ui.toggle_visibility_btn.connect(
                "toggled", self.on_toggle_visibility
            )

        if self.ui.file_chooser_btn:
            self.ui.file_chooser_btn.connect("clicked", self.on_select_files)
        if self.ui.clear_files_btn:
            self.ui.clear_files_btn.connect("clicked", self.on_clear_files)

        if self.ui.cancel_btn:
            self.ui.cancel_btn.connect("clicked", self.on_cancel)
        if self.ui.generate_btn:
            self.ui.generate_btn.connect("clicked", self.on_generate)

        if self.ui.prompt_buffer:
            self.ui.prompt_buffer.connect("changed", self.on_prompt_changed)
        if self.ui.api_key_entry:
            self.ui.api_key_entry.connect("changed", self.on_api_key_changed)

    def on_api_key_changed(self, _entry):
        """Handle API key changes"""
        self.update_generate_button_state()

    def on_cancel(self, _button):
        """Handle cancel button click"""
        if self.threads.is_processing():
            self.threads.cancel_processing()
        else:
            self.dialog.response(Gtk.ResponseType.CANCEL)

    def on_clear_files(self, _button):
        """Clear selected files"""
        self.ui.selected_files.clear()
        self.ui.update_files_display()

    def on_generate(self, _button):
        """Handle generate button - main AI processing entry point"""
        api_key = self.dialog.get_api_key()
        prompt_text = self.dialog.get_prompt()

        if not api_key:
            self.show_error(_("Please enter your Replicate API key"))
            return

        if not prompt_text:
            self.show_error(_("Please enter a prompt"))
            return

        edit_radio = self.ui.edit_mode_radio
        edit_active = edit_radio and edit_radio.get_active()
        if edit_active and not self.drawable:
            self.show_error(_("Edit mode requires a selected layer"))
            return

        mode = self.dialog.get_current_mode()
        api_key_visible = self.dialog.get_api_key_visible()
        selected_model_name = self.ui.get_selected_model()
        store_settings(
            api_key, mode, prompt_text, api_key_visible, selected_model_name
        )

        if self.ui.status_label:
            self.ui.status_label.set_text(_("Initializing API request..."))

        if mode == "edit":
            self.threads.start_edit_thread(
                api_key,
                prompt_text,
                self.ui.selected_files,
                selected_model_name,
            )
        else:
            self.threads.start_generate_thread(
                api_key,
                prompt_text,
                self.ui.selected_files,
                selected_model_name,
            )

    def on_model_changed(self, combo_box):
        """Handle model selection changes"""
        selected_model_name = combo_box.get_active_id()
        if selected_model_name:
            new_model = get_model_by_name(selected_model_name)
            if new_model:
                self.model = new_model
                self.update_ui_limits()
                self.ui.update_model_description(new_model)
                self.ui.update_model_settings_ui(new_model)

                current_mode = self.dialog.get_current_mode()
                self.ui.update_mode_sensitivity(new_model, current_mode)

    def on_mode_changed(self, _radio_button):
        """Handle mode selection changes"""
        if not self.ui.edit_mode_radio:
            return

        if self.ui.edit_mode_radio.get_active():
            max_edit_files = self.model.max_reference_images_edit
            if len(self.ui.selected_files) > max_edit_files:
                self.ui.selected_files = self.ui.selected_files[:max_edit_files]
                self.ui.update_files_display()
                message = ngettext(
                    "Reduced to {max} reference image for edit mode",
                    "Reduced to {max} reference images for edit mode",
                    max_edit_files,
                )
                print(message.format(max=max_edit_files))

            if self.ui.generate_btn:
                self.ui.generate_btn.set_label(_("Generate Edit"))
        else:
            if self.ui.generate_btn:
                self.ui.generate_btn.set_label(_("Generate Image"))

        self.update_ui_limits()
        self.update_generate_button_state()

        if self.model:
            current_mode = self.dialog.get_current_mode()
            self.ui.update_model_settings_ui(self.model, current_mode)

    def on_prompt_changed(self, _buffer):
        """Handle prompt text changes"""
        self.update_generate_button_state()

    def on_remove_file(self, _button, file_path):
        """Remove a specific file from selection"""
        if file_path in self.ui.selected_files:
            self.ui.selected_files.remove(file_path)
            self.ui.update_files_display()

    def on_select_files(self, _button):
        """Open file chooser for reference images"""
        dialog = Gtk.FileChooserDialog(
            title=_("Select Reference Images"),
            parent=self.dialog,
            action=Gtk.FileChooserAction.OPEN,
        )

        dialog.add_button(_("Cancel"), Gtk.ResponseType.CANCEL)
        dialog.add_button(_("Select"), Gtk.ResponseType.OK)

        mime_types = self.model.supported_mime_types
        if mime_types:
            image_filter = Gtk.FileFilter()
            labels = ", ".join(
                MIME_TYPE_LABELS.get(m, m.split("/")[-1].upper())
                for m in mime_types
            )
            image_filter.set_name(
                _("Supported Images ({formats})").format(formats=labels)
            )
            for mime_type in mime_types:
                image_filter.add_mime_type(mime_type)
            dialog.add_filter(image_filter)

        dialog.set_select_multiple(True)

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            files = dialog.get_filenames()

            current_mode = self.dialog.get_current_mode()
            if current_mode == "edit":
                max_total_files = self.model.max_reference_images_edit
            else:
                max_total_files = self.model.max_reference_images

            max_new_files = max_total_files - len(self.ui.selected_files)
            if max_new_files > 0:
                self.ui.selected_files.extend(files[:max_new_files])
                self.ui.update_files_display()
            elif files:
                rejected = ngettext(
                    "Cannot add {count} file.",
                    "Cannot add {count} files.",
                    len(files),
                ).format(count=len(files))

                if current_mode == "edit":
                    max_refs = self.model.max_reference_images_edit
                    limit = ngettext(
                        "Maximum {max} reference image allowed in edit "
                        "mode.",
                        "Maximum {max} reference images allowed in edit "
                        "mode.",
                        max_refs,
                    ).format(max=max_refs)
                else:
                    max_refs = self.model.max_reference_images
                    limit = ngettext(
                        "Maximum {max} reference image allowed.",
                        "Maximum {max} reference images allowed.",
                        max_refs,
                    ).format(max=max_refs)

                print(f"{rejected} {limit}")

        dialog.destroy()

    def on_toggle_visibility(self, button):
        """Handle API key visibility toggle"""
        if not self.ui.api_key_entry:
            return

        if button.get_active():
            self.ui.api_key_entry.set_visibility(True)
            icon = Gtk.Image.new_from_icon_name(
                "view-reveal-symbolic", Gtk.IconSize.BUTTON
            )
            button.set_image(icon)
            button.set_tooltip_text(_("Hide API key"))
        else:
            self.ui.api_key_entry.set_visibility(False)
            icon = Gtk.Image.new_from_icon_name(
                "view-conceal-symbolic", Gtk.IconSize.BUTTON
            )
            button.set_image(icon)
            button.set_tooltip_text(_("Show API key"))

    def show_error(self, message):
        """Show error message and enable interface"""
        if self.ui.status_label:
            self.ui.status_label.set_text(message)

        dialog = Gtk.MessageDialog(
            parent=self.dialog,
            modal=True,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=message,
        )
        dialog.run()
        dialog.destroy()

    def update_generate_button_state(self):
        """Update generate button sensitivity based on input state"""
        required_widgets = [
            self.ui.prompt_buffer,
            self.ui.api_key_entry,
            self.ui.generate_btn,
        ]
        if not all(required_widgets):
            return

        prompt_text = self.dialog.get_prompt()
        api_key = self.dialog.get_api_key()
        current_mode = self.dialog.get_current_mode()

        has_text = bool(prompt_text)
        has_api_key = bool(api_key)

        if current_mode == "edit":
            has_drawable = self.drawable is not None
            enabled = has_text and has_api_key and has_drawable
            self.ui.generate_btn.set_sensitive(enabled)
        else:
            sensitive = has_text and has_api_key
            self.ui.generate_btn.set_sensitive(sensitive)

    def update_ui_limits(self):
        """Update UI text to reflect current model limits"""
        if not self.model or not self.ui.images_help_label:
            return

        current_mode = self.dialog.get_current_mode()
        if current_mode == "edit":
            max_imgs = self.model.max_reference_images_edit
        else:
            max_imgs = self.model.max_reference_images

        if max_imgs > 0:
            text = ngettext(
                "Select up to {max} additional image",
                "Select up to {max} additional images",
                max_imgs,
            ).format(max=max_imgs)
        else:
            text = _("This model does not support reference images")

        markup = f"<small>{text}</small>"
        self.ui.images_help_label.set_markup(markup)
