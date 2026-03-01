#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Event handlers for Dream Prompter dialog
Handles all user interactions and UI events
"""

from gi.repository import Gtk, GLib

from dialog_threads import DreamPrompterThreads
from i18n import _
from models.factory import get_default_model, get_model_by_name
from settings import store_settings, load_settings


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

        # Initialize Google API key visibility
        if self.ui.toggle_google_visibility_btn and self.ui.google_api_key_entry:
            is_visible = settings.get("api_key_visible", False)
            self.ui.toggle_google_visibility_btn.set_active(is_visible)
            self.on_toggle_google_visibility(self.ui.toggle_google_visibility_btn)

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

        if self.ui.api_provider_dropdown:
            self.ui.api_provider_dropdown.connect("changed", self.on_api_provider_changed)

        if self.ui.toggle_visibility_btn:
            self.ui.toggle_visibility_btn.connect(
                "toggled", self.on_toggle_visibility
            )

        if self.ui.toggle_google_visibility_btn:
            self.ui.toggle_google_visibility_btn.connect(
                "toggled", self.on_toggle_google_visibility
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
        if self.ui.google_api_key_entry:
            self.ui.google_api_key_entry.connect("changed", self.on_api_key_changed)
        
        # Template controls
        if self.ui.template_dropdown:
            self.ui.template_dropdown.connect("changed", self.on_template_changed)
        if self.ui.save_template_btn:
            self.ui.save_template_btn.connect("clicked", self.on_save_template)
        if self.ui.delete_template_btn:
            self.ui.delete_template_btn.connect("clicked", self.on_delete_template)

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
        api_provider = self.dialog.get_api_provider()
        replicate_api_key = self.dialog.get_api_key()
        google_api_key = self.dialog.get_google_api_key()
        prompt_text = self.dialog.get_prompt()

        # Determine which API key to use based on provider
        if api_provider == "google_cloud":
            if not google_api_key:
                self.show_error(_("Please enter your Google API key"))
                return
            api_key = google_api_key
        else:
            if not replicate_api_key:
                self.show_error(_("Please enter your Replicate API key"))
                return
            api_key = replicate_api_key

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
        num_images = self.dialog.get_num_images()
        
        store_settings(
            replicate_api_key, mode, prompt_text, api_key_visible, 
            selected_model_name, None, google_api_key, api_provider
        )

        if self.ui.status_label:
            self.ui.status_label.set_text(_("Initializing API request..."))

        if mode == "edit":
            self.threads.start_edit_thread(
                api_key,
                prompt_text,
                self.ui.selected_files,
                selected_model_name,
                api_provider,
                num_images,
            )
        else:
            self.threads.start_generate_thread(
                api_key,
                prompt_text,
                self.ui.selected_files,
                selected_model_name,
                api_provider,
                num_images,
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
                
                
                # Auto-switch API provider based on model requirements
                if self.ui.api_provider_dropdown:
                    from models import APIProvider
                    required_provider = new_model.api_provider
                    if required_provider == APIProvider.GOOGLE_CLOUD:
                        provider_id = "google_cloud"
                    else:
                        provider_id = "replicate"
                    
                    # Only switch if different from current
                    current_provider = self.ui.api_provider_dropdown.get_active_id()
                    if current_provider != provider_id:
                        self.ui.api_provider_dropdown.set_active_id(provider_id)
                        # Trigger the provider changed event to update UI
                        self.on_api_provider_changed(self.ui.api_provider_dropdown)
                # Auto-detect aspect ratio if in edit mode and model supports it
                if current_mode == "edit" and hasattr(new_model, 'parameters'):
                    # Check if model has aspect_ratio parameter
                    has_aspect_ratio = any(p.name == "aspect_ratio" for p in new_model.parameters)
                    if has_aspect_ratio:
                        self._auto_detect_aspect_ratio()

    def on_mode_changed(self, _radio_button):
        """Handle mode selection changes"""
        if not self.ui.edit_mode_radio:
            return

        if self.ui.edit_mode_radio.get_active():
            max_edit_files = self.model.max_reference_images_edit
            if len(self.ui.selected_files) > max_edit_files:
                self.ui.selected_files = self.ui.selected_files[:max_edit_files]
                self.ui.update_files_display()
                message = _("Reduced to {max} reference images for edit mode")
                print(message.format(max=max_edit_files))

            if self.ui.generate_btn:
                self.ui.generate_btn.set_label(_("Generate Edit"))
            
            # Auto-detect aspect ratio when switching to edit mode
            self._auto_detect_aspect_ratio()
        else:
            if self.ui.generate_btn:
                self.ui.generate_btn.set_label(_("Generate Image"))

        self.update_ui_limits()
        self.update_generate_button_state()

        if self.model:
            current_mode = self.dialog.get_current_mode()
            self.ui.update_model_settings_ui(self.model, current_mode)
    
    def _auto_detect_aspect_ratio(self):
        """Auto-detect and set aspect ratio based on current image dimensions"""
        if not self.image:
            return
        
        # Get image dimensions
        width = self.image.get_width()
        height = self.image.get_height()
        
        if width == 0 or height == 0:
            return
        
        # For edit mode with Nano Banana Pro, prefer "original" to keep exact dimensions
        # This omits the aspect_ratio parameter in the API call
        print(f"[DEBUG] Image size: {width}x{height}")
        print(f"[DEBUG] Auto-selected aspect ratio: Original (Auto) - keeps original dimensions")
        
        # Set the aspect ratio in model settings
        from model_settings import ModelParameterManager
        try:
            manager = ModelParameterManager(self.model.name)
            manager.set_parameter_value("aspect_ratio", "original")
            
            # Find and update the aspect_ratio dropdown widget directly
            self._update_aspect_ratio_widget("original")
        except Exception as e:
            print(f"[WARNING] Could not auto-set aspect ratio: {e}")
    
    def _update_aspect_ratio_widget(self, aspect_ratio_value):
        """Update the aspect_ratio dropdown widget to show the selected value"""
        if not self.ui.model_settings_section:
            return
        
        # Search through the model settings widgets to find the aspect_ratio dropdown
        for child in self.ui.model_settings_section.get_children():
            if not isinstance(child, Gtk.Box):
                continue
            
            # Check if this box contains our aspect_ratio widget
            for widget in child.get_children():
                if isinstance(widget, Gtk.ComboBoxText):
                    # Check if this is the aspect_ratio dropdown by checking its parent's label
                    parent_children = child.get_children()
                    if len(parent_children) >= 2:
                        label = parent_children[0]
                        if isinstance(label, Gtk.Label):
                            label_text = label.get_text().lower()
                            if "aspect" in label_text or "ratio" in label_text:
                                # Found it! Set the active value
                                print(f"[DEBUG] Setting aspect_ratio dropdown to: {aspect_ratio_value}")
                                widget.set_active_id(aspect_ratio_value)
                                return

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
                max_total_files = self.model.max_reference_images_edit
            else:
                max_total_files = self.model.max_reference_images

            max_new_files = max_total_files - len(self.ui.selected_files)
            if max_new_files > 0:
                self.ui.selected_files.extend(files[:max_new_files])
                self.ui.update_files_display()
            elif files:
                if current_mode == "edit":
                    max_refs = self.model.max_reference_images_edit
                    message = _(
                        "Cannot add {count} files. Maximum {max} "
                        "reference images allowed in edit mode."
                    )
                    print(message.format(count=len(files), max=max_refs))
                else:
                    max_refs = self.model.max_reference_images
                    message = _(
                        "Cannot add {count} files. Maximum {max} "
                        "reference images allowed."
                    )
                    print(message.format(count=len(files), max=max_refs))

        dialog.destroy()

    def on_toggle_visibility(self, button):
        """Handle Replicate API key visibility toggle"""
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

    def on_toggle_google_visibility(self, button):
        """Handle Google API key visibility toggle"""
        if not self.ui.google_api_key_entry:
            return

        if button.get_active():
            self.ui.google_api_key_entry.set_visibility(True)
            icon = Gtk.Image.new_from_icon_name(
                "view-reveal-symbolic", Gtk.IconSize.BUTTON
            )
            button.set_image(icon)
            button.set_tooltip_text(_("Hide API key"))
        else:
            self.ui.google_api_key_entry.set_visibility(False)
            icon = Gtk.Image.new_from_icon_name(
                "view-conceal-symbolic", Gtk.IconSize.BUTTON
            )
            button.set_image(icon)
            button.set_tooltip_text(_("Show API key"))

    def on_api_provider_changed(self, combo_box):
        """Handle API provider selection change"""
        provider = combo_box.get_active_id()
        
        if provider == "google_cloud":
            # Show Google fields, hide Replicate fields
            if self.ui.google_key_box:
                self.ui.google_key_box.set_visible(True)
            if self.ui.replicate_key_box:
                self.ui.replicate_key_box.set_visible(False)
        else:
            # Show Replicate fields, hide Google fields
            if self.ui.replicate_key_box:
                self.ui.replicate_key_box.set_visible(True)
            if self.ui.google_key_box:
                self.ui.google_key_box.set_visible(False)
        
        # Update the generate button state
        self.update_generate_button_state()

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
            self.ui.generate_btn,
        ]
        if not all(required_widgets):
            return

        prompt_text = self.dialog.get_prompt()
        current_mode = self.dialog.get_current_mode()
        
        # Check the correct API key based on provider selection
        api_provider = self.dialog.get_api_provider()
        if api_provider == "google_cloud":
            api_key = self.dialog.get_google_api_key()
        else:
            api_key = self.dialog.get_api_key()

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
        if not self.model:
            return

        current_mode = self.dialog.get_current_mode()
        if current_mode == "edit":
            if self.ui.images_help_label:
                max_imgs = self.model.max_reference_images_edit
                text = _("Select up to {max} additional images").format(
                    max=max_imgs
                )
                markup = f"<small>{text}</small>"
                self.ui.images_help_label.set_markup(markup)
        else:
            if self.ui.images_help_label:
                max_imgs = self.model.max_reference_images
                text = _("Select up to {max} additional images").format(
                    max=max_imgs
                )
                markup = f"<small>{text}</small>"
                self.ui.images_help_label.set_markup(markup)
    
    def on_template_changed(self, combo_box):
        """Handle template selection change"""
        template_name = combo_box.get_active_id()
        
        # Enable/disable delete button based on selection
        if self.ui.delete_template_btn:
            self.ui.delete_template_btn.set_sensitive(bool(template_name))
        
        if not template_name:
            return
        
        # Load the selected template
        from prompt_templates import get_template
        template = get_template(template_name)
        
        if template:
            # Set the text buffers
            if self.ui.prefix_buffer:
                self.ui.prefix_buffer.set_text(template.prefix)
            if self.ui.prompt_buffer:
                self.ui.prompt_buffer.set_text(template.main)
            if self.ui.suffix_buffer:
                self.ui.suffix_buffer.set_text(template.suffix)
    
    def on_save_template(self, _button):
        """Handle save template button"""
        # Show input dialog to get template name
        dialog = Gtk.MessageDialog(
            transient_for=self.dialog,
            flags=0,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.OK_CANCEL,
            text=_("Save Prompt Template"),
        )
        dialog.format_secondary_text(_("Enter a name for this template:"))
        
        # Add text entry to dialog
        content_area = dialog.get_content_area()
        entry = Gtk.Entry()
        entry.set_placeholder_text(_("Template name"))
        
        # Pre-fill with current selection if any
        if self.ui.template_dropdown:
            current_name = self.ui.template_dropdown.get_active_id()
            if current_name:
                entry.set_text(current_name)
        
        content_area.pack_end(entry, False, False, 0)
        dialog.show_all()
        
        response = dialog.run()
        template_name = entry.get_text().strip()
        dialog.destroy()
        
        if response == Gtk.ResponseType.OK and template_name:
            # Save the template
            from prompt_templates import PromptTemplate, save_template
            
            template = PromptTemplate(
                name=template_name,
                prefix=self.dialog.get_prompt_prefix(),
                main=self.dialog.get_prompt_main(),
                suffix=self.dialog.get_prompt_suffix(),
            )
            
            save_template(template)
            
            # Reload templates in dropdown
            self.dialog._load_templates()
            
            # Select the newly saved template
            if self.ui.template_dropdown:
                self.ui.template_dropdown.set_active_id(template_name)
            
            self.show_info(_("Template '{name}' saved successfully!").format(name=template_name))
    
    def on_delete_template(self, _button):
        """Handle delete template button"""
        if not self.ui.template_dropdown:
            return
        
        template_name = self.ui.template_dropdown.get_active_id()
        if not template_name:
            return
        
        # Confirm deletion
        dialog = Gtk.MessageDialog(
            transient_for=self.dialog,
            flags=0,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.YES_NO,
            text=_("Delete Template?"),
        )
        dialog.format_secondary_text(
            _("Are you sure you want to delete the template '{name}'?").format(name=template_name)
        )
        
        response = dialog.run()
        dialog.destroy()
        
        if response == Gtk.ResponseType.YES:
            # Delete the template
            from prompt_templates import delete_template
            delete_template(template_name)
            
            # Reload templates in dropdown
            self.dialog._load_templates()
            
            # Clear the fields
            if self.ui.prefix_buffer:
                self.ui.prefix_buffer.set_text("")
            if self.ui.prompt_buffer:
                self.ui.prompt_buffer.set_text("")
            if self.ui.suffix_buffer:
                self.ui.suffix_buffer.set_text("")
            
            self.show_info(_("Template '{name}' deleted.").format(name=template_name))
    
    def show_info(self, message):
        """Show an informational message"""
        if self.ui.status_label:
            self.ui.status_label.set_text(message)
        print(f"INFO: {message}")