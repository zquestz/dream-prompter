#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dream Prompter Dialog - Main coordinator
"""

from gi.repository import GimpUi

from dialog_events import DreamPrompterEventHandler
from dialog_gtk import DreamPrompterUI
from i18n import _
from models.factory import (
    get_default_model,
    get_model_by_name,
    get_models_for_context,
)
from settings import load_settings


class DreamPrompterDialog(GimpUi.Dialog):
    """Main dialog window for the Dream Prompter plugin"""

    def __init__(self, procedure, image, drawable):
        super().__init__(
            title=_("Dream Prompter - AI Image Creator/Editor"),
            role="dream-prompter-dialog",
            use_header_bar=True,
        )

        self.procedure = procedure
        self.image = image
        self.drawable = drawable

        self.set_resizable(True)
        self.set_size_request(650, -1)

        self.ui = DreamPrompterUI()
        self.events = DreamPrompterEventHandler(self, self.ui, image, drawable)

        self._initialize()

    def get_api_key(self):
        """Get the Replicate API key from the UI"""
        if self.ui.api_key_entry:
            return self.ui.api_key_entry.get_text().strip()
        return ""

    def get_google_api_key(self):
        """Get the Google API key from the UI"""
        if self.ui.google_api_key_entry:
            return self.ui.google_api_key_entry.get_text().strip()
        return ""
    
    def get_num_images(self):
        """Get the number of images to generate from the UI"""
        if self.ui.num_images_spinbutton:
            return int(self.ui.num_images_spinbutton.get_value())
        return 3  # Default to 3 if not set

    def get_api_provider(self):
        """Get the selected API provider from the UI"""
        if self.ui.api_provider_dropdown:
            return self.ui.api_provider_dropdown.get_active_id() or "replicate"
        return "replicate"

    def get_api_key_visible(self):
        """Get the API key visibility state"""
        if self.ui.toggle_visibility_btn:
            return self.ui.toggle_visibility_btn.get_active()
        return False

    def get_current_mode(self):
        """Get the currently selected mode"""
        generate_radio = self.ui.generate_mode_radio
        if generate_radio and generate_radio.get_active():
            return "generate"
        return "edit"

    def get_prompt(self):
        """Get the current prompt text (combined from prefix + main + suffix)"""
        parts = []
        
        # Get prefix
        if self.ui.prefix_buffer:
            start_iter = self.ui.prefix_buffer.get_start_iter()
            end_iter = self.ui.prefix_buffer.get_end_iter()
            prefix = self.ui.prefix_buffer.get_text(start_iter, end_iter, False).strip()
            if prefix:
                parts.append(prefix)
        
        # Get main prompt
        if self.ui.prompt_buffer:
            start_iter = self.ui.prompt_buffer.get_start_iter()
            end_iter = self.ui.prompt_buffer.get_end_iter()
            main = self.ui.prompt_buffer.get_text(start_iter, end_iter, False).strip()
            if main:
                parts.append(main)
        
        # Get suffix
        if self.ui.suffix_buffer:
            start_iter = self.ui.suffix_buffer.get_start_iter()
            end_iter = self.ui.suffix_buffer.get_end_iter()
            suffix = self.ui.suffix_buffer.get_text(start_iter, end_iter, False).strip()
            if suffix:
                parts.append(suffix)
        
        return " ".join(parts)
    
    def get_prompt_prefix(self):
        """Get just the prefix part"""
        if self.ui.prefix_buffer:
            start_iter = self.ui.prefix_buffer.get_start_iter()
            end_iter = self.ui.prefix_buffer.get_end_iter()
            return self.ui.prefix_buffer.get_text(start_iter, end_iter, False).strip()
        return ""
    
    def get_prompt_main(self):
        """Get just the main prompt part"""
        if self.ui.prompt_buffer:
            start_iter = self.ui.prompt_buffer.get_start_iter()
            end_iter = self.ui.prompt_buffer.get_end_iter()
            return self.ui.prompt_buffer.get_text(start_iter, end_iter, False).strip()
        return ""
    
    def get_prompt_suffix(self):
        """Get just the suffix part"""
        if self.ui.suffix_buffer:
            start_iter = self.ui.suffix_buffer.get_start_iter()
            end_iter = self.ui.suffix_buffer.get_end_iter()
            return self.ui.suffix_buffer.get_text(start_iter, end_iter, False).strip()
        return ""

    def _initialize(self):
        """Initialize the dialog"""
        self.ui.build_interface(self)
        self.events.connect_all_signals()
        self._set_initial_mode()
        self._load_settings()

    def _load_settings(self):
        """Load settings from config file"""
        try:
            settings = load_settings()

            # Load API provider
            if self.ui.api_provider_dropdown:
                provider = str(settings.get("api_provider", "replicate"))
                self.ui.api_provider_dropdown.set_active_id(provider)
                # Update visibility of API key fields
                self.events.on_api_provider_changed(self.ui.api_provider_dropdown)

            # Load Replicate API key
            if settings.get("api_key") and self.ui.api_key_entry:
                self.ui.api_key_entry.set_text(str(settings["api_key"]))

            # Load Google API key
            if settings.get("google_api_key") and self.ui.google_api_key_entry:
                self.ui.google_api_key_entry.set_text(str(settings["google_api_key"]))

            if "api_key_visible" in settings and self.ui.toggle_visibility_btn:
                api_key_visible = bool(settings["api_key_visible"])
                self.ui.toggle_visibility_btn.set_active(api_key_visible)

            stored_mode = settings.get("mode", "edit")
            if self.image and self.drawable:
                if stored_mode == "generate" and self.ui.generate_mode_radio:
                    self.ui.generate_mode_radio.set_active(True)
                elif self.ui.edit_mode_radio:
                    self.ui.edit_mode_radio.set_active(True)

            if self.ui.model_dropdown:
                available_models = get_models_for_context(self.ui.has_image)

                stored_model = settings.get("model")
                model_to_select = None

                if stored_model and stored_model in available_models:
                    model_to_select = stored_model
                else:
                    default_model = get_default_model()
                    if default_model.name in available_models:
                        model_to_select = default_model.name
                    elif available_models:
                        model_to_select = next(iter(available_models.keys()))

                if model_to_select:
                    self.ui.set_selected_model(model_to_select)

                if self.ui.model_dropdown:
                    selected_model_name = self.ui.get_selected_model()
                    if selected_model_name:
                        model = get_model_by_name(selected_model_name)
                        if model:
                            current_mode = self.get_current_mode()
                            self.ui.update_mode_sensitivity(model, current_mode)

            if settings.get("prompt") and self.ui.prompt_buffer:
                self.ui.prompt_buffer.set_text(str(settings["prompt"]))
            
            if settings.get("prompt_prefix") and self.ui.prefix_buffer:
                self.ui.prefix_buffer.set_text(str(settings["prompt_prefix"]))
            
            if settings.get("prompt_suffix") and self.ui.suffix_buffer:
                self.ui.suffix_buffer.set_text(str(settings["prompt_suffix"]))
            
            # Load templates into dropdown
            if self.ui.template_dropdown:
                self._load_templates()

        except Exception as e:
            print(f"Error loading settings: {e}")
    
    def _load_templates(self):
        """Load template names into dropdown"""
        try:
            from prompt_templates import get_template_names
            
            # Clear existing items except the first (-- No Template --)
            self.ui.template_dropdown.remove_all()
            self.ui.template_dropdown.append("", _("-- No Template --"))
            
            # Add all template names
            template_names = get_template_names()
            for name in template_names:
                self.ui.template_dropdown.append(name, name)
            
            self.ui.template_dropdown.set_active_id("")
        except Exception as e:
            print(f"Error loading templates: {e}")

    def _set_initial_mode(self):
        """Set initial mode based on available image/drawable"""
        if not self.image or not self.drawable:
            if self.ui.generate_mode_radio:
                self.ui.generate_mode_radio.set_active(True)
            if self.ui.edit_mode_radio:
                self.ui.edit_mode_radio.set_sensitive(False)
        else:
            if self.ui.edit_mode_radio:
                self.ui.edit_mode_radio.set_active(True)
                self.ui.edit_mode_radio.set_sensitive(True)
            if self.ui.generate_mode_radio:
                self.ui.generate_mode_radio.set_sensitive(True)

        try:
            self.events.on_mode_changed(None)
        except Exception as e:
            print(f"Error setting initial mode: {e}")
