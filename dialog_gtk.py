#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GTK UI components for Dream Prompter dialog
Handles all GTK interface creation and layout
"""

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

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
        self.prompt_textview = None
        self.prompt_buffer = None
        self.file_chooser_btn = None
        self.files_info_label = None
        self.clear_files_btn = None
        self.files_listbox = None
        self.images_help_label = None
        self.cancel_btn = None
        self.generate_btn = None
        self.status_label = None
        self.progress_bar = None
        self.model_dropdown = None
        self.model_description_label = None
        self.model_settings_section = None
        self.model_settings_widgets = {}

    def build_interface(self, parent_dialog):
        """Build the main plugin interface"""
        if not parent_dialog:
            return

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
        main_box.set_margin_top(16)
        main_box.set_margin_bottom(16)
        main_box.set_margin_start(16)
        main_box.set_margin_end(16)

        try:
            api_key_section = self._create_api_key_section()
            main_box.pack_start(api_key_section, False, False, 0)

            model_section = self._create_model_selection_section()
            main_box.pack_start(model_section, False, False, 0)

            model_settings_section = self._create_model_settings_section()
            main_box.pack_start(model_settings_section, False, False, 0)

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

    def get_selected_model(self):
        """Get the currently selected model name"""
        if self.model_dropdown:
            return self.model_dropdown.get_active_id()
        return None

    def hide_progress(self):
        """Hide progress bar and show status message"""
        if self.progress_bar:
            self.progress_bar.set_visible(False)
        if self.status_label:
            self.status_label.set_text(_("Ready"))

    def set_selected_model(self, model_name):
        """Set the selected model"""
        if self.model_dropdown and model_name:
            self.model_dropdown.set_active_id(model_name)
            from models.factory import get_model_by_name
            model = get_model_by_name(model_name)
            if model:
                self.update_model_description(model)
                self.update_model_settings_ui(model)


    def set_ui_enabled(self, enabled=True):
        """Enable/disable UI controls"""
        if self.api_key_entry:
            self.api_key_entry.set_sensitive(enabled)
        if self.toggle_visibility_btn:
            self.toggle_visibility_btn.set_sensitive(enabled)
        if self.model_dropdown:
            self.model_dropdown.set_sensitive(enabled)
        if self.edit_mode_radio:
            self.edit_mode_radio.set_sensitive(enabled)
        if self.generate_mode_radio:
            self.generate_mode_radio.set_sensitive(enabled)
        if self.prompt_textview:
            self.prompt_textview.set_sensitive(enabled)
        if self.file_chooser_btn:
            self.file_chooser_btn.set_sensitive(enabled)
        if self.clear_files_btn:
            self.clear_files_btn.set_sensitive(enabled)
        if self.generate_btn:
            self.generate_btn.set_sensitive(enabled)

    def toggle_api_key_visibility(self, button):
        """Toggle API key visibility and update button icon"""
        if not self.api_key_entry:
            return

        is_visible = button.get_active()
        self.api_key_entry.set_visibility(is_visible)

        icon_name = "view-reveal-symbolic" if is_visible else "view-conceal-symbolic"
        button.get_image().set_from_icon_name(icon_name, Gtk.IconSize.BUTTON)

    def update_files_display(self):
        """Update the files display"""
        if not self.selected_files:
            self._update_empty_files_display()
        else:
            self._update_files_with_content()

    def update_model_description(self, model):
        """Update the model description help text"""
        if self.model_description_label and model:
            markup = f'<small>{model.description}</small>'
            self.model_description_label.set_markup(markup)

    def update_model_settings_ui(self, model, current_mode=None):
        """Update the model settings UI for the selected model"""
        if not self.model_settings_section:
            return

        if current_mode is None and self.event_handler:
            current_mode = self.event_handler.dialog.get_current_mode()

        for child in self.model_settings_section.get_children():
            self.model_settings_section.remove(child)
        self.model_settings_widgets.clear()

        if not model:
            self.model_settings_section.hide()
            return

        param_definitions = model.get_parameter_definitions()
        if not param_definitions:
            self.model_settings_section.set_visible(False)
            return

        filtered_params = []
        if current_mode:
            for param_def in param_definitions:
                if param_def.supports_mode(current_mode):
                    filtered_params.append(param_def)
        else:
            filtered_params = param_definitions

        if not filtered_params:
            self.model_settings_section.set_visible(False)
            return

        title_label = Gtk.Label()
        title_label.set_markup(f"<b>{_('Model Settings')}</b>")
        title_label.set_halign(Gtk.Align.START)
        self.model_settings_section.pack_start(title_label, False, False, 0)

        from model_settings import ModelParameterManager
        try:
            manager = ModelParameterManager(model.name)
            current_values = manager.get_all_parameter_values()
        except Exception as e:
            print(f"Error loading model settings: {e}")
            current_values = {}

        for param_def in filtered_params:
            param_name = param_def.name
            current_value = current_values.get(param_name)
            param_container = self._create_parameter_widget(param_def, current_value)
            if param_container:
                self.model_settings_section.pack_start(
                    param_container, False, False, 0
                )

        self.model_settings_section.set_visible(True)
        self.model_settings_section.show_all()

    def update_status(self, message, percentage=None):
        """Update status display"""
        if self.status_label:
            self.status_label.set_text(message)

        if percentage is not None:
            if self.progress_bar:
                self.progress_bar.set_fraction(percentage)
                self.progress_bar.set_visible(True)
        else:
            if self.progress_bar:
                self.progress_bar.pulse()
                self.progress_bar.set_visible(True)

    def _clear_existing_file_rows(self):
        """Clear existing file rows from the listbox"""
        if self.files_listbox:
            for child in self.files_listbox.get_children():
                self.files_listbox.remove(child)

    def _create_additional_images_section(self):
        """Create additional images selection section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        title_label = Gtk.Label()
        title_label.set_markup(f"<b>{_('Additional Images (Optional)')}</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        files_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)

        self.file_chooser_btn = Gtk.Button()
        self.file_chooser_btn.set_label(_("Select Images..."))
        icon = Gtk.Image.new_from_icon_name("document-open-symbolic",
                                            Gtk.IconSize.BUTTON)
        self.file_chooser_btn.set_image(icon)
        files_container.pack_start(self.file_chooser_btn, False, False, 0)

        self.files_info_label = Gtk.Label()
        self.files_info_label.set_text(_("No additional images selected"))
        self.files_info_label.set_halign(Gtk.Align.START)
        style_context = self.files_info_label.get_style_context()
        style_context.add_class("dim-label")
        files_container.pack_start(self.files_info_label, True, True, 0)

        self.clear_files_btn = Gtk.Button()
        clear_icon = Gtk.Image.new_from_icon_name("edit-clear-symbolic",
                                                  Gtk.IconSize.BUTTON)
        self.clear_files_btn.set_image(clear_icon)
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

    def _create_file_rows(self):
        """Create rows for each selected file"""
        if not self.files_listbox:
            return

        for file_path in self.selected_files:
            row = self._create_single_file_row(file_path)
            self.files_listbox.add(row)

    def _create_model_selection_section(self):
        """Create AI model selection section"""
        from models.factory import model_factory

        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        title_label = Gtk.Label()
        title_label.set_markup(f"<b>{_('AI Model')}</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        self.model_dropdown = Gtk.ComboBoxText()

        available_models = model_factory.get_available_models()

        for model_name, model in available_models.items():
            display_text = f"{model.display_name}"
            self.model_dropdown.append(model_name, display_text)

        section_box.pack_start(self.model_dropdown, False, False, 0)

        self.model_description_label = Gtk.Label()
        self.model_description_label.set_halign(Gtk.Align.START)
        self.model_description_label.set_line_wrap(True)
        self.model_description_label.get_style_context().add_class("dim-label")
        section_box.pack_start(self.model_description_label, False, False, 0)

        tree_model = self.model_dropdown.get_model()
        if tree_model and len(tree_model) > 0:
            self.model_dropdown.set_active(0)
            from models.factory import get_model_by_name
            first_model_id = self.model_dropdown.get_active_id()
            if first_model_id:
                model = get_model_by_name(first_model_id)
                if model:
                    self.update_model_description(model)

        return section_box

    def _create_model_settings_section(self):
        """Create model-specific settings section"""
        orientation = Gtk.Orientation.VERTICAL
        self.model_settings_section = Gtk.Box(orientation=orientation, spacing=6)
        return self.model_settings_section

    def _create_parameter_widget(self, param_def, current_value):
        """Create a widget for a single parameter"""
        from models import ParameterType

        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)

        label = Gtk.Label()
        label.set_text(param_def.label + ":")
        label.set_halign(Gtk.Align.START)
        label.set_xalign(0.0)
        label.set_size_request(120, -1)
        container.pack_start(label, False, False, 0)

        widget = None

        if param_def.param_type == ParameterType.CHOICE:
            widget = Gtk.ComboBoxText()
            for choice in param_def.choices:
                widget.append(str(choice), str(choice))
            if current_value is not None:
                widget.set_active_id(str(current_value))
            else:
                widget.set_active_id(str(param_def.default_value))
            widget.connect('changed', self._on_parameter_changed,
                           param_def.name)

        elif param_def.param_type == ParameterType.BOOLEAN:
            widget = Gtk.CheckButton()
            default_val = param_def.default_value
            value = bool(current_value) if current_value is not None else default_val
            widget.set_active(value)
            widget.connect('toggled', self._on_parameter_changed,
                           param_def.name)

        elif param_def.param_type == ParameterType.INTEGER:
            min_val = param_def.min_value if param_def.min_value is not None else 0
            max_val = param_def.max_value if param_def.max_value is not None else 10000
            step = param_def.step if param_def.step is not None else 1

            default_val = param_def.default_value
            value = current_value if current_value is not None else default_val
            adjustment = Gtk.Adjustment(
                value=value,
                lower=min_val,
                upper=max_val,
                step_increment=step,
                page_increment=step * 10
            )
            widget = Gtk.SpinButton()
            widget.set_adjustment(adjustment)
            widget.set_digits(0)
            widget.connect('value-changed',
                           self._on_parameter_changed, param_def.name)

        elif param_def.param_type == ParameterType.FLOAT:
            min_val = param_def.min_value if param_def.min_value is not None else 0.0
            max_val = param_def.max_value if param_def.max_value is not None else 100.0
            step = param_def.step if param_def.step is not None else 0.1

            default_val = param_def.default_value
            value = current_value if current_value is not None else default_val
            adjustment = Gtk.Adjustment(
                value=value,
                lower=min_val,
                upper=max_val,
                step_increment=step,
                page_increment=step * 10
            )
            widget = Gtk.SpinButton()
            widget.set_adjustment(adjustment)
            widget.set_digits(2)
            widget.connect('value-changed',
                           self._on_parameter_changed, param_def.name)

        elif param_def.param_type == ParameterType.STRING:
            widget = Gtk.Entry()
            text_value = (str(current_value) if current_value is not None
                          else str(param_def.default_value))
            widget.set_text(text_value)
            widget.connect('changed', self._on_parameter_changed,
                           param_def.name)

        if widget:
            container.pack_start(widget, True, True, 0)
            self.model_settings_widgets[param_def.name] = widget

            if param_def.description:
                widget.set_tooltip_text(param_def.description)
                label.set_tooltip_text(param_def.description)

        return container

    def _on_parameter_changed(self, widget, param_name):
        """Handle parameter value changes"""
        try:
            selected_model_name = self.get_selected_model()
            if not selected_model_name:
                return

            from models import ParameterType
            from models.factory import get_model_by_name
            from model_settings import ModelParameterManager

            model = get_model_by_name(selected_model_name)
            if not model:
                return

            manager = ModelParameterManager(selected_model_name)

            param_def = None
            for p in model.get_parameter_definitions():
                if p.name == param_name:
                    param_def = p
                    break

            if not param_def:
                return

            if param_def.param_type == ParameterType.CHOICE:
                value = widget.get_active_id()
            elif param_def.param_type == ParameterType.BOOLEAN:
                value = widget.get_active()
            elif param_def.param_type in [ParameterType.INTEGER, ParameterType.FLOAT]:
                value = widget.get_value()
                if param_def.param_type == ParameterType.INTEGER:
                    value = int(value)
            elif param_def.param_type == ParameterType.STRING:
                value = widget.get_text()
            else:
                return

            manager.set_parameter_value(param_name, value)

        except Exception as e:
            print(f"Error handling parameter change: {e}")

    def _create_api_key_section(self):
        """Create API key input section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        title_label = Gtk.Label()
        title_label.set_markup(f"<b>{_('Replicate API Key')}</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        key_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)

        self.api_key_entry = Gtk.Entry()
        placeholder = _("Enter your Replicate API key")
        self.api_key_entry.set_placeholder_text(placeholder)
        self.api_key_entry.set_visibility(False)
        self.api_key_entry.set_input_purpose(Gtk.InputPurpose.PASSWORD)
        key_container.pack_start(self.api_key_entry, True, True, 0)

        self.toggle_visibility_btn = Gtk.ToggleButton()
        self.toggle_visibility_btn.set_image(
            Gtk.Image.new_from_icon_name("view-conceal-symbolic", Gtk.IconSize.BUTTON)
        )
        tooltip_text = _("Show/Hide API key")
        self.toggle_visibility_btn.set_tooltip_text(tooltip_text)
        key_container.pack_start(self.toggle_visibility_btn, False, False, 0)

        section_box.pack_start(key_container, False, False, 0)

        help_label = Gtk.Label()
        help_url = "https://replicate.com/account/api-tokens"
        help_text = _('Get your API key from <a href="{url}">Replicate</a>')
        help_text = help_text.format(url=help_url)
        help_label.set_markup(f'<small>{help_text}</small>')
        help_label.set_halign(Gtk.Align.START)
        help_label.set_line_wrap(True)
        section_box.pack_start(help_label, False, False, 0)

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
        self.generate_btn.set_label(_("Generate Edit"))
        gen_icon = Gtk.Image.new_from_icon_name("applications-graphics-symbolic",
                                                Gtk.IconSize.BUTTON)
        self.generate_btn.set_image(gen_icon)
        generate_style = self.generate_btn.get_style_context()
        generate_style.add_class("suggested-action")
        self.generate_btn.set_size_request(150, -1)
        buttons_box.pack_start(self.generate_btn, False, False, 0)

        return buttons_box

    def _create_file_box(self, filename, file_path):
        """Create the horizontal box for a file entry"""
        orientation = Gtk.Orientation.HORIZONTAL
        file_box = Gtk.Box(orientation=orientation, spacing=8)
        file_box.set_margin_top(3)
        file_box.set_margin_bottom(3)
        file_box.set_margin_start(6)
        file_box.set_margin_end(6)

        icon = Gtk.Image.new_from_icon_name("image-x-generic-symbolic",
                                            Gtk.IconSize.SMALL_TOOLBAR)
        file_box.pack_start(icon, False, False, 0)

        label = Gtk.Label()
        label.set_text(filename)
        label.set_halign(Gtk.Align.START)
        label.set_ellipsize(Pango.EllipsizeMode.END)
        file_box.pack_start(label, True, True, 0)

        remove_btn = self._create_remove_button(file_path)
        file_box.pack_start(remove_btn, False, False, 0)

        return file_box

    def _create_mode_section(self):
        """Create mode selection section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        title_label = Gtk.Label()
        title_label.set_markup(f"<b>{_('Operation Mode')}</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        radio_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)

        self.edit_mode_radio = Gtk.RadioButton.new_with_label(None, _("Edit Image"))
        radio_box.pack_start(self.edit_mode_radio, False, False, 0)

        self.generate_mode_radio = Gtk.RadioButton.new_with_label_from_widget(
            self.edit_mode_radio, _("Generate Image")
        )
        radio_box.pack_start(self.generate_mode_radio, False, False, 0)

        section_box.pack_start(radio_box, False, False, 0)

        return section_box

    def _create_prompt_section(self):
        """Create prompt input section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

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

        return section_box

    def _create_remove_button(self, file_path):
        """Create remove button for a file"""
        remove_btn = Gtk.Button()
        del_icon = Gtk.Image.new_from_icon_name("edit-delete-symbolic",
                                                Gtk.IconSize.MENU)
        remove_btn.set_image(del_icon)
        remove_btn.set_relief(Gtk.ReliefStyle.NONE)

        if self.event_handler:
            remove_btn.connect("clicked",
                               self.event_handler.on_remove_file, file_path)

        return remove_btn

    def _create_single_file_row(self, file_path):
        """Create a single file row widget"""
        filename = self._get_display_filename(file_path)

        row = Gtk.ListBoxRow()
        file_box = self._create_file_box(filename, file_path)
        row.add(file_box)
        return row

    def _create_status_section(self):
        """Create status display section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        self.status_label = Gtk.Label()
        self.status_label.set_text(_("Ready"))
        self.status_label.set_halign(Gtk.Align.START)
        self.status_label.get_style_context().add_class("dim-label")
        section_box.pack_start(self.status_label, False, False, 0)

        self.progress_bar = Gtk.ProgressBar()
        self.progress_bar.set_show_text(False)
        self.progress_bar.set_visible(False)
        section_box.pack_start(self.progress_bar, False, False, 0)

        return section_box

    def _get_display_filename(self, file_path):
        """Get filename with size info for display"""
        filename = os.path.basename(file_path)

        try:
            file_size = os.path.getsize(file_path)
            size_mb = file_size / (1024 * 1024)

            if size_mb > 7:
                size_warning = _("⚠️ ({size:.1f} MB - Max Size Exceeded)")
                filename += " " + size_warning.format(size=size_mb)
            elif size_mb >= 0.1:
                size_text = _("({size:.1f} MB)").format(size=size_mb)
                filename += " " + size_text
            else:
                size_kb = file_size / 1024
                filename += " " + _("({size:.0f} KB)").format(size=size_kb)
        except Exception:
            pass

        return filename

    def _show_files_list(self):
        """Make the files list visible"""
        if self.files_listbox:
            self.files_listbox.set_visible(True)
            self.files_listbox.show_all()

    def _update_empty_files_display(self):
        """Update display when no files are selected"""
        if self.files_info_label:
            self.files_info_label.set_text(_("No additional images selected"))
        if self.files_listbox:
            self.files_listbox.set_visible(False)
        if self.clear_files_btn:
            self.clear_files_btn.set_sensitive(False)

    def _update_files_info_label(self):
        """Update the info label with file count"""
        if not self.files_info_label:
            return

        count = len(self.selected_files)
        if count == 1:
            text = _("{count} image selected").format(count=count)
        else:
            text = _("{count} images selected").format(count=count)

        self.files_info_label.set_text(text)

        if self.clear_files_btn:
            self.clear_files_btn.set_sensitive(True)

    def _update_files_with_content(self):
        """Update display when files are selected"""
        self._update_files_info_label()
        self._clear_existing_file_rows()
        self._create_file_rows()
        self._show_files_list()
