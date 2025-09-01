#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GTK UI components for Dream Prompter dialog
Handles all GTK interface creation and layout
"""

import gi
gi.require_version('Gtk', '3.0')
import os

from gi.repository import Gtk
from i18n import _

class DreamPrompterUI:
    """Handles all GTK UI creation and layout"""

    def __init__(self):
        self.selected_files = []
        self.event_handler = None

        self.api_key_entry = None
        self.toggle_visibility_btn = None
        self.edit_mode_radio = None
        self.generate_mode_radio = None
        self.mode_description = None
        self.prompt_textview = None
        self.prompt_buffer = None
        self.examples_box = None
        self.file_chooser_btn = None
        self.files_info_label = None
        self.clear_files_btn = None
        self.files_listbox = None
        self.images_help_label = None
        self.cancel_btn = None
        self.generate_btn = None
        self.status_label = None
        self.progress_bar = None

    def build_interface(self, parent_dialog):
        """Build the main plugin interface"""
        if not parent_dialog:
            return

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        main_box.set_margin_top(12)
        main_box.set_margin_bottom(12)
        main_box.set_margin_start(12)
        main_box.set_margin_end(12)

        try:
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

            parent_dialog.get_content_area().add(main_box)
        except Exception as e:
            print(f"Error building interface: {e}")

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
        section_box.pack_start(self.examples_box, False, False, 0)

        return section_box

    def update_prompt_examples(self, edit_mode_active):
        """Update prompt examples based on current mode"""
        if self.examples_box is None:
            return

        for child in self.examples_box.get_children():
            self.examples_box.remove(child)

        examples_label = Gtk.Label()
        examples_label.set_markup(f'<small><b>{_("Example prompts:")}</b></small>')
        examples_label.set_halign(Gtk.Align.START)
        self.examples_box.pack_start(examples_label, False, False, 0)

        if edit_mode_active:
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
        self.images_help_label.set_halign(Gtk.Align.START)
        self.images_help_label.set_line_wrap(True)
        section_box.pack_start(self.images_help_label, False, False, 0)

        return section_box

    def update_files_display(self):
        """Update the files display"""
        if not self.selected_files:
            if self.files_info_label:
                self.files_info_label.set_text(_("No additional images selected"))
            if self.files_listbox:
                self.files_listbox.set_visible(False)
            if self.clear_files_btn:
                self.clear_files_btn.set_sensitive(False)
        else:
            count = len(self.selected_files)
            if count == 1:
                text = _("{count} image selected").format(count=count)
            else:
                text = _("{count} images selected").format(count=count)

            if self.files_info_label:
                self.files_info_label.set_text(text)
            if self.clear_files_btn:
                self.clear_files_btn.set_sensitive(True)

            if self.files_listbox:
                for child in self.files_listbox.get_children():
                    self.files_listbox.remove(child)

            for file_path in self.selected_files:
                filename = os.path.basename(file_path)

                try:
                    file_size = os.path.getsize(file_path)
                    size_mb = file_size / (1024 * 1024)
                    if size_mb > 7:
                        filename += " " + _("⚠️ ({size:.1f} MB - Max Size Exceeded)").format(size=size_mb)
                    elif size_mb > 1:
                        filename += " " + _("({size:.1f} MB)").format(size=size_mb)
                except:
                    pass

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
                label.set_ellipsize(3)
                file_box.pack_start(label, True, True, 0)

                remove_btn = Gtk.Button()
                remove_btn.set_image(Gtk.Image.new_from_icon_name("edit-delete-symbolic", Gtk.IconSize.SMALL_TOOLBAR))
                remove_btn.set_relief(Gtk.ReliefStyle.NONE)
                remove_btn.file_path = file_path

                if self.event_handler:
                    remove_btn.connect("clicked", self.event_handler.on_remove_file, file_path)

                file_box.pack_start(remove_btn, False, False, 0)

                row.add(file_box)
                if self.files_listbox:
                    self.files_listbox.add(row)

            if self.files_listbox:
                self.files_listbox.set_visible(True)
                self.files_listbox.show_all()

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
