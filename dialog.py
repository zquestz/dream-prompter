#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dream Prompter Dialog UI
"""

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GimpUi', '3.0')
gi.require_version('GLib', '2.0')
import os

from gi.repository import GimpUi, Gtk, GLib
from settings import load_settings, store_settings
from i18n import _

class DreamPrompterDialog(GimpUi.Dialog):
    """Main dialog window for the Dream Prompter plugin"""

    def __init__(self, procedure, image, drawable):
        super().__init__(
            title=_("Dream Prompter - Nano Banana AI Image Creator/Editor"),
            role="dream-prompter-dialog",
            use_header_bar=True
        )

        self.procedure = procedure
        self.image = image
        self.drawable = drawable

        self.set_default_size(600, 600)
        self.set_resizable(True)

        self.selected_files = []

        self._build_interface()
        self._connect_signals()
        self._set_initial_mode()
        self._load_settings()

    def _build_interface(self):
        """Build the main plugin interface"""
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        main_box.set_margin_top(12)
        main_box.set_margin_bottom(12)
        main_box.set_margin_start(12)
        main_box.set_margin_end(12)

        api_key_section = self._create_api_key_section()
        main_box.pack_start(api_key_section, False, False, 0)

        mode_section = self._create_mode_section()
        main_box.pack_start(mode_section, False, False, 0)

        prompt_section = self._create_prompt_section()
        main_box.pack_start(prompt_section, True, True, 0)

        images_section = self._create_additional_images_section()
        main_box.pack_start(images_section, False, False, 0)

        buttons_section = self._create_buttons_section()
        main_box.pack_start(buttons_section, False, False, 0)

        status_section = self._create_status_section()
        main_box.pack_start(status_section, False, False, 0)

        self.get_content_area().add(main_box)

    def _create_api_key_section(self):
        """Create API key input section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        title_label = Gtk.Label()
        title_label.set_markup(f"<b>{_('Google Gemini API Key')}</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        key_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        self.api_key_entry = Gtk.Entry()
        self.api_key_entry.set_placeholder_text(_("Enter your Google Gemini API key..."))
        self.api_key_entry.set_visibility(False)
        self.api_key_entry.set_input_purpose(Gtk.InputPurpose.PASSWORD)
        key_container.pack_start(self.api_key_entry, True, True, 0)

        self.toggle_visibility_btn = Gtk.ToggleButton()
        self.toggle_visibility_btn.set_image(Gtk.Image.new_from_icon_name("view-conceal-symbolic", Gtk.IconSize.BUTTON))
        self.toggle_visibility_btn.set_tooltip_text(_("Show/Hide API key"))
        key_container.pack_start(self.toggle_visibility_btn, False, False, 0)

        section_box.pack_start(key_container, False, False, 0)

        help_label = Gtk.Label()
        help_url = "https://console.cloud.google.com/"
        help_text = _('Get your API key from <a href="{url}">Google Cloud Console</a>').format(url=help_url)
        help_label.set_markup(f'<small>{help_text}</small>')
        help_label.set_halign(Gtk.Align.START)
        help_label.set_line_wrap(True)
        section_box.pack_start(help_label, False, False, 0)

        return section_box

    def _create_mode_section(self):
        """Create mode selection section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        title_label = Gtk.Label()
        title_label.set_markup(f"<b>{_('Operation Mode')}</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        radio_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)

        self.edit_mode_radio = Gtk.RadioButton.new_with_label(None, _("Edit existing image"))
        radio_box.pack_start(self.edit_mode_radio, False, False, 0)

        self.generate_mode_radio = Gtk.RadioButton.new_with_label_from_widget(
            self.edit_mode_radio, _("Generate new image")
        )
        radio_box.pack_start(self.generate_mode_radio, False, False, 0)

        section_box.pack_start(radio_box, False, False, 0)

        self.mode_description = Gtk.Label()
        self.mode_description.set_halign(Gtk.Align.START)
        self.mode_description.get_style_context().add_class("dim-label")
        section_box.pack_start(self.mode_description, False, False, 0)

        return section_box

    def _create_prompt_section(self):
        """Create prompt input section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        title_label = Gtk.Label()
        title_label.set_markup(f"<b>{_('AI Prompt')}</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        scroll_window = Gtk.ScrolledWindow()
        scroll_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll_window.set_min_content_height(120)

        self.prompt_textview = Gtk.TextView()
        self.prompt_textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.prompt_buffer = self.prompt_textview.get_buffer()

        scroll_window.add(self.prompt_textview)
        section_box.pack_start(scroll_window, True, True, 0)

        self.examples_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
        self._update_prompt_examples()
        section_box.pack_start(self.examples_box, False, False, 0)

        return section_box

    def _update_prompt_examples(self):
        """Update prompt examples based on current mode"""
        for child in self.examples_box.get_children():
            self.examples_box.remove(child)

        examples_label = Gtk.Label()
        examples_label.set_markup(f'<small><b>{_("Example prompts:")}</b></small>')
        examples_label.set_halign(Gtk.Align.START)
        self.examples_box.pack_start(examples_label, False, False, 0)

        if self.edit_mode_radio.get_active():
            example_texts = [
                _("• Change the background to a medieval castle"),
                _("• Make this person wear a red dress instead"),
                _("• Add snow falling in the scene"),
                _("• Transform this into a painting style")
            ]
        else:
            example_texts = [
                _("• A majestic dragon flying over a mountain range"),
                _("• Portrait of a woman in Victorian dress"),
                _("• Cyberpunk cityscape at night with neon lights"),
                _("• Peaceful forest clearing with sunbeams")
            ]

        for example in example_texts:
            example_label = Gtk.Label()
            example_label.set_markup(f'<small><i>{example}</i></small>')
            example_label.set_halign(Gtk.Align.START)
            self.examples_box.pack_start(example_label, False, False, 0)

        self.examples_box.show_all()

    def _create_additional_images_section(self):
        """Create additional images selection section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        title_label = Gtk.Label()
        title_label.set_markup(f"<b>{_('Additional Images (Optional)')}</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        files_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        self.file_chooser_btn = Gtk.Button()
        self.file_chooser_btn.set_label(_("Select Images..."))
        self.file_chooser_btn.set_image(Gtk.Image.new_from_icon_name("document-open-symbolic", Gtk.IconSize.BUTTON))
        files_container.pack_start(self.file_chooser_btn, False, False, 0)

        self.files_info_label = Gtk.Label()
        self.files_info_label.set_text(_("No additional images selected"))
        self.files_info_label.set_halign(Gtk.Align.START)
        self.files_info_label.get_style_context().add_class("dim-label")
        files_container.pack_start(self.files_info_label, True, True, 0)

        self.clear_files_btn = Gtk.Button()
        self.clear_files_btn.set_image(Gtk.Image.new_from_icon_name("edit-clear-symbolic", Gtk.IconSize.BUTTON))
        self.clear_files_btn.set_tooltip_text(_("Clear selected files"))
        self.clear_files_btn.set_sensitive(False)
        files_container.pack_start(self.clear_files_btn, False, False, 0)

        section_box.pack_start(files_container, False, False, 0)

        self.files_listbox = Gtk.ListBox()
        self.files_listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.files_listbox.get_style_context().add_class("content")
        self.files_listbox.set_visible(False)
        section_box.pack_start(self.files_listbox, False, False, 0)

        self.images_help_label = Gtk.Label()
        self.images_help_label.set_markup(f'<small>{_("Select additional images to merge or reference in your AI edit")}</small>')
        self.images_help_label.set_halign(Gtk.Align.START)
        self.images_help_label.set_line_wrap(True)
        section_box.pack_start(self.images_help_label, False, False, 0)

        return section_box

    def _create_buttons_section(self):
        """Create action buttons section"""
        buttons_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        buttons_box.set_halign(Gtk.Align.CENTER)

        self.cancel_btn = Gtk.Button()
        self.cancel_btn.set_label(_("Cancel"))
        self.cancel_btn.set_size_request(100, -1)
        buttons_box.pack_start(self.cancel_btn, False, False, 0)

        self.generate_btn = Gtk.Button()
        self.generate_btn.set_label(_("Generate AI Edit"))
        self.generate_btn.set_image(Gtk.Image.new_from_icon_name("applications-graphics-symbolic", Gtk.IconSize.BUTTON))
        self.generate_btn.get_style_context().add_class("suggested-action")
        self.generate_btn.set_size_request(150, -1)
        buttons_box.pack_start(self.generate_btn, False, False, 0)

        return buttons_box

    def _create_status_section(self):
        """Create status display section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.status_label = Gtk.Label()
        self.status_label.set_text(_("Ready"))
        self.status_label.set_halign(Gtk.Align.START)
        self.status_label.get_style_context().add_class("dim-label")
        section_box.pack_start(self.status_label, False, False, 0)

        self.progress_bar = Gtk.ProgressBar()
        self.progress_bar.set_show_text(True)
        self.progress_bar.set_visible(False)
        section_box.pack_start(self.progress_bar, False, False, 0)

        return section_box

    def _connect_signals(self):
        """Connect UI signals to handlers"""
        self.edit_mode_radio.connect("toggled", self._on_mode_changed)
        self.generate_mode_radio.connect("toggled", self._on_mode_changed)

        self.toggle_visibility_btn.connect("toggled", self._on_toggle_visibility)

        self.file_chooser_btn.connect("clicked", self._on_select_files)
        self.clear_files_btn.connect("clicked", self._on_clear_files)

        self.cancel_btn.connect("clicked", self._on_cancel)
        self.generate_btn.connect("clicked", self._on_generate)

        self.prompt_buffer.connect("changed", self._on_prompt_changed)
        self.api_key_entry.connect("changed", self._on_api_key_changed)

    def _set_initial_mode(self):
        """Set initial mode based on available image/drawable"""
        if not self.image or not self.drawable:
            self.generate_mode_radio.set_active(True)
            self.edit_mode_radio.set_sensitive(False)
            self.mode_description.set_text(_("No image open - only generation mode available"))
        else:
            self.edit_mode_radio.set_active(True)
            self.edit_mode_radio.set_sensitive(True)
            self.generate_mode_radio.set_sensitive(True)
            self.mode_description.set_text(_("Edit the current layer using AI"))

        self._on_mode_changed(None)

    def _load_settings(self):
        """Load settings from config file"""
        settings = load_settings()

        if settings.get("api_key"):
            self.api_key_entry.set_text(settings["api_key"])

        if settings.get("api_key_visible"):
            self.toggle_visibility_btn.set_active(True)

        stored_mode = settings.get("mode", "edit")
        if self.image and self.drawable:
            if stored_mode == "generate":
                self.generate_mode_radio.set_active(True)
            else:
                self.edit_mode_radio.set_active(True)

        if settings.get("prompt"):
            self.prompt_buffer.set_text(settings["prompt"])

    def _store_settings(self):
        """Store settings to config file"""
        prompt_text = self.prompt_buffer.get_text(
            self.prompt_buffer.get_start_iter(),
            self.prompt_buffer.get_end_iter(),
            False
        ).strip()

        api_key = self.api_key_entry.get_text().strip()
        mode = "edit" if self.edit_mode_radio.get_active() else "generate"
        api_key_visible = self.toggle_visibility_btn.get_active()

        store_settings(api_key, mode, prompt_text, api_key_visible)

    def _on_mode_changed(self, radio_button):
        """Handle mode selection changes"""
        if self.edit_mode_radio.get_active():
            if self.drawable:
                self.mode_description.set_text(_("Edit the current layer using AI"))
            else:
                self.mode_description.set_text(_("No layer available to edit"))
            self.generate_btn.set_label(_("Generate AI Edit"))
            self.images_help_label.set_markup(f'<small>{_("Select additional images to merge or reference in your AI edit")}</small>')
        else:
            if self.image:
                self.mode_description.set_text(_("Create a new image and add it as a layer to the current project"))
            else:
                self.mode_description.set_text(_("Create a new image in a new GIMP project"))
            self.generate_btn.set_label(_("Generate New Image"))
            self.images_help_label.set_markup(f'<small>{_("Select reference images to influence the style or composition of your new image")}</small>')

        self._update_prompt_examples()
        self._update_generate_button_state()

    def _on_toggle_visibility(self, button):
        """Toggle API key visibility"""
        if button.get_active():
            self.api_key_entry.set_visibility(True)
            button.set_image(Gtk.Image.new_from_icon_name("view-reveal-symbolic", Gtk.IconSize.BUTTON))
            button.set_tooltip_text(_("Hide API key"))
        else:
            self.api_key_entry.set_visibility(False)
            button.set_image(Gtk.Image.new_from_icon_name("view-conceal-symbolic", Gtk.IconSize.BUTTON))
            button.set_tooltip_text(_("Show API key"))

    def _on_select_files(self, button):
        """Handle file selection"""
        dialog = Gtk.FileChooserDialog(
            title=_("Select Additional Images"),
            parent=self,
            action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            _("Cancel"), Gtk.ResponseType.CANCEL,
            _("Select"), Gtk.ResponseType.OK
        )

        filter_images = Gtk.FileFilter()
        filter_images.set_name(_("Image files"))
        filter_images.add_mime_type("image/jpeg")
        filter_images.add_mime_type("image/png")
        filter_images.add_mime_type("image/gif")
        dialog.add_filter(filter_images)

        dialog.set_select_multiple(True)

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            files = dialog.get_filenames()
            self.selected_files.extend(files)
            self._update_files_display()

        dialog.destroy()

    def _on_clear_files(self, button):
        """Clear selected files"""
        self.selected_files.clear()
        self._update_files_display()

    def _update_files_display(self):
        """Update the files display"""
        if not self.selected_files:
            self.files_info_label.set_text(_("No additional images selected"))
            self.files_listbox.set_visible(False)
            self.clear_files_btn.set_sensitive(False)
        else:
            count = len(self.selected_files)
            # Use ngettext for proper plural handling
            if count == 1:
                text = _("{count} image selected").format(count=count)
            else:
                text = _("{count} images selected").format(count=count)
            self.files_info_label.set_text(text)
            self.clear_files_btn.set_sensitive(True)

            for child in self.files_listbox.get_children():
                self.files_listbox.remove(child)

            for file_path in self.selected_files:
                filename = os.path.basename(file_path)
                row = Gtk.ListBoxRow()

                file_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
                file_box.set_margin_top(3)
                file_box.set_margin_bottom(3)
                file_box.set_margin_start(6)
                file_box.set_margin_end(6)

                icon = Gtk.Image.new_from_icon_name("image-x-generic-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
                file_box.pack_start(icon, False, False, 0)

                label = Gtk.Label()
                label.set_text(filename)
                label.set_halign(Gtk.Align.START)
                label.set_ellipsize(3)  # Pango.EllipsizeMode.END
                file_box.pack_start(label, True, True, 0)

                remove_btn = Gtk.Button()
                remove_btn.set_image(Gtk.Image.new_from_icon_name("edit-delete-symbolic", Gtk.IconSize.SMALL_TOOLBAR))
                remove_btn.set_relief(Gtk.ReliefStyle.NONE)
                remove_btn.connect("clicked", self._on_remove_file, file_path)
                file_box.pack_start(remove_btn, False, False, 0)

                row.add(file_box)
                self.files_listbox.add(row)

            self.files_listbox.set_visible(True)
            self.files_listbox.show_all()

    def _on_remove_file(self, button, file_path):
        """Remove a specific file from selection"""
        if file_path in self.selected_files:
            self.selected_files.remove(file_path)
            self._update_files_display()

    def _on_prompt_changed(self, buffer):
        """Handle prompt text changes"""
        self._update_generate_button_state()

    def _on_api_key_changed(self, entry):
        """Handle API key changes"""
        self._update_generate_button_state()

    def _update_generate_button_state(self):
        """Update generate button sensitivity based on input state"""
        text = self.prompt_buffer.get_text(
            self.prompt_buffer.get_start_iter(),
            self.prompt_buffer.get_end_iter(),
            False
        ).strip()

        has_text = bool(text)
        has_api_key = bool(self.api_key_entry.get_text().strip())

        if self.edit_mode_radio.get_active():
            has_drawable = self.drawable is not None
            self.generate_btn.set_sensitive(has_text and has_api_key and has_drawable)
        else:
            self.generate_btn.set_sensitive(has_text and has_api_key)

    def _on_cancel(self, button):
        """Handle cancel button"""
        self.response(Gtk.ResponseType.CANCEL)

    def _on_generate(self, button):
        """Handle generate button - this is where we'll integrate the API later"""
        api_key = self.api_key_entry.get_text().strip()
        prompt_text = self.prompt_buffer.get_text(
            self.prompt_buffer.get_start_iter(),
            self.prompt_buffer.get_end_iter(),
            False
        ).strip()

        if not api_key:
            self._show_error(_("Please enter your Google Gemini API key"))
            return

        if not prompt_text:
            self._show_error(_("Please enter a prompt"))
            return

        if self.edit_mode_radio.get_active() and not self.drawable:
            self._show_error(_("Edit mode requires a selected layer"))
            return

        self._store_settings()

        mode = _("Edit") if self.edit_mode_radio.get_active() else _("Generate")
        self._set_status(_("Processing {mode} request...").format(mode=mode.lower()))
        self.progress_bar.set_visible(True)
        self.progress_bar.pulse()

        # TODO: Replace this simulation with actual Gemini API call
        # - Send image + prompt to Google Gemini API
        # - Handle response and create new layer with result
        # - Maintain consistency for multi-turn editing
        print(f"Mode: {mode}")
        print(f"API Key: {'*' * len(api_key)}")
        print(f"Prompt: {prompt_text}")
        print(f"Additional files: {self.selected_files}")
        print(f"Current image: {self.image}")
        print(f"Current drawable: {self.drawable}")

        GLib.timeout_add_seconds(2, self._finish_processing)

    def _finish_processing(self):
        """Finish the processing simulation"""
        mode = _("edit") if self.edit_mode_radio.get_active() else _("generation")
        self._set_status(_("Ready for API integration! (Last: {mode} mode)").format(mode=mode))
        self.progress_bar.set_visible(False)
        return False  # Don't repeat the timeout

    def _show_error(self, message):
        """Show error message"""
        dialog = Gtk.MessageDialog(
            parent=self,
            flags=Gtk.DialogFlags.MODAL,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=message
        )
        dialog.run()
        dialog.destroy()

    def _set_status(self, message):
        """Update status message"""
        self.status_label.set_text(message)
