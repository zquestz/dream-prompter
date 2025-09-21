#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Event handlers for Dream Prompter dialog
Handles all user interactions and UI events
"""

from gi.repository import Gtk, GLib

from dialog_threads import DreamPrompterThreads
from i18n import _
from settings import store_settings, load_settings

class DreamPrompterEventHandler:
    """Handles all dialog events and user interactions"""

    def __init__(self, dialog, ui, image, drawable):
        self.dialog = dialog
        self.ui = ui
        self.image = image
        self.drawable = drawable
        self.ui.event_handler = self

        self.threads = DreamPrompterThreads(ui, image, drawable)
        self.threads.set_callbacks({
            'on_success': self.close_on_success,
            'on_error': self.show_error
        })

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

            self.update_generate_button_state()

        GLib.idle_add(after_init)

    def close_on_success(self):
        """Close dialog on successful completion"""
        self.dialog.response(Gtk.ResponseType.OK)

    def connect_all_signals(self):
        """Connect all UI signals to handlers"""
        if self.ui.edit_mode_radio:
            self.ui.edit_mode_radio.connect("toggled", self.on_mode_changed)
        if self.ui.generate_mode_radio:
            self.ui.generate_mode_radio.connect("toggled", self.on_mode_changed)

        if self.ui.toggle_visibility_btn:
            self.ui.toggle_visibility_btn.connect("toggled", self.on_toggle_visibility)

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
            self.show_error(_("Please enter your Google Gemini API key"))
            return

        if not prompt_text:
            self.show_error(_("Please enter a prompt"))
            return

        if self.ui.edit_mode_radio and self.ui.edit_mode_radio.get_active() and not self.drawable:
            self.show_error(_("Edit mode requires a selected layer"))
            return

        mode = self.dialog.get_current_mode()
        api_key_visible = self.dialog.get_api_key_visible()
        store_settings(api_key, mode, prompt_text, api_key_visible)

        if self.ui.status_label:
            self.ui.status_label.set_text(_("Initializing API request..."))

        if mode == "edit":
            self.threads.start_edit_thread(api_key, prompt_text, self.ui.selected_files)
        else:
            self.threads.start_generate_thread(api_key, prompt_text, self.ui.selected_files)

    def on_mode_changed(self, radio_button):
        """Handle mode selection changes"""
        if not self.ui.edit_mode_radio:
            return

        if self.ui.edit_mode_radio.get_active():
            if len(self.ui.selected_files) > 2:
                self.ui.selected_files = self.ui.selected_files[:2]
                self.ui.update_files_display()
                print(_("Reduced to 2 reference images for edit mode"))

            if self.ui.generate_btn:
                self.ui.generate_btn.set_label(_("Generate Edit"))
            if self.ui.images_help_label:
                self.ui.images_help_label.set_markup(f'<small>{_("Select up to 2 additional images")}</small>')
        else:
            if self.ui.generate_btn:
                self.ui.generate_btn.set_label(_("Generate Image"))
            if self.ui.images_help_label:
                self.ui.images_help_label.set_markup(f'<small>{_("Select up to 3 additional images")}</small>')

        self.update_generate_button_state()


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
            action=Gtk.FileChooserAction.OPEN
        )

        dialog.add_button(_("Cancel"), Gtk.ResponseType.CANCEL)
        dialog.add_button(_("Select"), Gtk.ResponseType.OK)

        image_filter = Gtk.FileFilter()
        image_filter.set_name(_("Supported Images (PNG, JPEG, WebP)"))
        image_filter.add_mime_type("image/png")
        image_filter.add_mime_type("image/jpeg")
        image_filter.add_mime_type("image/webp")
        dialog.add_filter(image_filter)

        dialog.set_select_multiple(True)

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            files = dialog.get_filenames()

            current_mode = self.dialog.get_current_mode()
            if current_mode == "edit":
                max_total_files = 2
            else:
                max_total_files = 3

            max_new_files = max_total_files - len(self.ui.selected_files)
            if max_new_files > 0:
                self.ui.selected_files.extend(files[:max_new_files])
                self.ui.update_files_display()
            elif files:
                if current_mode == "edit":
                    print(_("Cannot add {count} files. Maximum 2 reference images allowed in edit mode.").format(count=len(files)))
                else:
                    print(_("Cannot add {count} files. Maximum 3 reference images allowed.").format(count=len(files)))

        dialog.destroy()

    def on_toggle_visibility(self, button):
        """Handle API key visibility toggle"""
        if not self.ui.api_key_entry:
            return

        if button.get_active():
            self.ui.api_key_entry.set_visibility(True)
            button.set_image(Gtk.Image.new_from_icon_name("view-reveal-symbolic", Gtk.IconSize.BUTTON))
            button.set_tooltip_text(_("Hide API key"))
        else:
            self.ui.api_key_entry.set_visibility(False)
            button.set_image(Gtk.Image.new_from_icon_name("view-conceal-symbolic", Gtk.IconSize.BUTTON))
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
            text=message
        )
        dialog.run()
        dialog.destroy()

    def update_generate_button_state(self):
        """Update generate button sensitivity based on input state"""
        if not self.ui.prompt_buffer or not self.ui.api_key_entry or not self.ui.generate_btn:
            return

        prompt_text = self.dialog.get_prompt()
        api_key = self.dialog.get_api_key()
        current_mode = self.dialog.get_current_mode()

        has_text = bool(prompt_text)
        has_api_key = bool(api_key)

        if current_mode == "edit":
            has_drawable = self.drawable is not None
            self.ui.generate_btn.set_sensitive(has_text and has_api_key and has_drawable)
        else:
            self.ui.generate_btn.set_sensitive(has_text and has_api_key)
