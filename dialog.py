#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dream Prompter Dialog - Main coordinator
"""

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GimpUi', '3.0')

from dialog_events import DreamPrompterEventHandler
from dialog_gtk import DreamPrompterUI
from gi.repository import GimpUi
from i18n import _
from settings import load_settings

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

        self.ui = DreamPrompterUI()
        self.events = DreamPrompterEventHandler(self, self.ui, image, drawable)

        self._initialize()

    def _initialize(self):
        """Initialize the dialog"""
        self.ui.build_interface(self)
        self.events.connect_all_signals()
        self._set_initial_mode()
        self._load_settings()

    def _set_initial_mode(self):
        """Set initial mode based on available image/drawable"""
        if not self.image or not self.drawable:
            if self.ui.generate_mode_radio:
                self.ui.generate_mode_radio.set_active(True)
            if self.ui.edit_mode_radio:
                self.ui.edit_mode_radio.set_sensitive(False)
            if self.ui.mode_description:
                self.ui.mode_description.set_text(_("No image open - only generation mode available"))
        else:
            if self.ui.edit_mode_radio:
                self.ui.edit_mode_radio.set_active(True)
                self.ui.edit_mode_radio.set_sensitive(True)
            if self.ui.generate_mode_radio:
                self.ui.generate_mode_radio.set_sensitive(True)
            if self.ui.mode_description:
                self.ui.mode_description.set_text(_("Edit the current layer using AI"))

        try:
            self.events.on_mode_changed(None)
        except Exception as e:
            print(f"Error setting initial mode: {e}")

    def _load_settings(self):
        """Load settings from config file"""
        try:
            settings = load_settings()

            if settings.get("api_key") and self.ui.api_key_entry:
                self.ui.api_key_entry.set_text(settings["api_key"])

            if settings.get("api_key_visible") and self.ui.toggle_visibility_btn:
                self.ui.toggle_visibility_btn.set_active(True)

            stored_mode = settings.get("mode", "edit")
            if self.image and self.drawable:
                if stored_mode == "generate" and self.ui.generate_mode_radio:
                    self.ui.generate_mode_radio.set_active(True)
                elif self.ui.edit_mode_radio:
                    self.ui.edit_mode_radio.set_active(True)

            if settings.get("prompt") and self.ui.prompt_buffer:
                self.ui.prompt_buffer.set_text(settings["prompt"])

        except Exception as e:
            print(f"Error loading settings: {e}")
