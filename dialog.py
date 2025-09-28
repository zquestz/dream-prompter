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
    get_default_model, get_model_by_name, get_models_for_context
)
from settings import load_settings


class DreamPrompterDialog(GimpUi.Dialog):
    """Main dialog window for the Dream Prompter plugin"""

    def __init__(self, procedure, image, drawable):
        super().__init__(
            title=_("Dream Prompter - AI Image Creator/Editor"),
            role="dream-prompter-dialog",
            use_header_bar=True
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
        """Get the API key from the UI"""
        if self.ui.api_key_entry:
            return self.ui.api_key_entry.get_text().strip()
        return ""

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
        """Get the current prompt text"""
        if self.ui.prompt_buffer:
            start_iter = self.ui.prompt_buffer.get_start_iter()
            end_iter = self.ui.prompt_buffer.get_end_iter()
            return self.ui.prompt_buffer.get_text(
                start_iter, end_iter, False
            ).strip()
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

            if settings.get("api_key") and self.ui.api_key_entry:
                self.ui.api_key_entry.set_text(str(settings["api_key"]))

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
                            self.ui.update_mode_sensitivity(
                                model, current_mode
                            )

            if settings.get("prompt") and self.ui.prompt_buffer:
                self.ui.prompt_buffer.set_text(str(settings["prompt"]))

        except Exception as e:
            print(f"Error loading settings: {e}")

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
