#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Threading operations for Dream Prompter dialog
Handles all background AI processing and image operations
"""

import gimp_integration
import threading

from api import GeminiAPI
from gi.repository import GLib
from i18n import _

class DreamPrompterThreads:
    """Handles all background threading operations"""

    def __init__(self, ui, image, drawable):
        if not ui:
            raise ValueError("UI object is required")

        self.ui = ui
        self.image = image
        self.drawable = drawable
        self._callbacks = {}

    def set_callbacks(self, callbacks):
        """Set callback functions for thread completion"""
        if not isinstance(callbacks, dict):
            return

        self._callbacks = callbacks

    def start_generate_thread(self, api_key, prompt, reference_images):
        """Start image generation in background thread"""
        if not self.ui:
            return

        self._disable_ui()

        thread = threading.Thread(
            target=self._generate_image_worker,
            args=(api_key, prompt, reference_images)
        )
        thread.daemon = True
        thread.start()

    def start_edit_thread(self, api_key, prompt, reference_images):
        """Start image editing in background thread"""
        if not self.ui:
            return

        self._disable_ui()

        thread = threading.Thread(
            target=self._edit_image_worker,
            args=(api_key, prompt, reference_images)
        )
        thread.daemon = True
        thread.start()

    def _generate_image_worker(self, api_key, prompt, reference_images):
        """Generate image in background thread"""
        try:
            api = GeminiAPI(api_key)

            def progress_callback(message):
                GLib.idle_add(self._update_status, message)

            image_data = api.generate_image(
                prompt=prompt,
                reference_images=reference_images,
                progress_callback=progress_callback
            )

            if image_data:
                GLib.idle_add(self._handle_generated_image, image_data)
            else:
                GLib.idle_add(self._handle_error, _("No image data received from API"))

        except Exception as e:
            error_msg = str(e)
            GLib.idle_add(self._handle_error, error_msg)

    def _edit_image_worker(self, api_key, prompt, reference_images):
        """Edit image in background thread"""
        try:
            api = GeminiAPI(api_key)

            def progress_callback(message):
                GLib.idle_add(self._update_status, message)

            # Call API to edit/generate image (same API call as generation for now)
            # TODO: When we have a dedicated edit API, we can pass the current image data
            image_data = api.generate_image(
                prompt=prompt,
                reference_images=reference_images,
                progress_callback=progress_callback
            )

            if image_data:
                GLib.idle_add(self._handle_edited_image, image_data)
            else:
                GLib.idle_add(self._handle_error, _("No image data received from API"))

        except Exception as e:
            error_msg = str(e)
            GLib.idle_add(self._handle_error, error_msg)

    def _handle_generated_image(self, image_data):
        """Handle generated image on main thread"""
        try:
            self._update_status(_("Creating GIMP image..."))

            image = gimp_integration.create_new_image(image_data)
            if not image:
                self._handle_error(_("Failed to create GIMP image"))
                return

            self._update_status(_("Image generated successfully!"))
            self._schedule_success_callback()

        except Exception as e:
            self._handle_error(_("Error creating GIMP image: {error}").format(error=str(e)))

    def _handle_edited_image(self, image_data=None):
        """Handle edited image on main thread"""
        try:
            self._update_status(_("Adding edit layer..."))

            layer = gimp_integration.create_edit_layer(self.image, self.drawable, image_data)
            if not layer:
                self._handle_error(_("Failed to create edit layer"))
                return

            self._update_status(_("Edit layer created!"))
            self._schedule_success_callback()

        except Exception as e:
            self._handle_error(_("Error creating edit layer: {error}").format(error=str(e)))

    def _disable_ui(self):
        """Disable UI elements during processing"""
        if self.ui.generate_btn:
            self.ui.generate_btn.set_sensitive(False)
        if self.ui.cancel_btn:
            self.ui.cancel_btn.set_sensitive(False)
        if self.ui.progress_bar:
            self.ui.progress_bar.set_visible(True)
            self.ui.progress_bar.pulse()

    def _enable_ui(self):
        """Re-enable UI elements after processing"""
        if self.ui.generate_btn:
            self.ui.generate_btn.set_sensitive(True)
        if self.ui.cancel_btn:
            self.ui.cancel_btn.set_sensitive(True)
        if self.ui.progress_bar:
            self.ui.progress_bar.set_visible(False)

    def _update_status(self, message):
        """Update status message on UI thread"""
        if self.ui.status_label:
            self.ui.status_label.set_text(message)

    def _handle_error(self, error_message):
        """Handle error on main thread"""
        self._enable_ui()

        if 'on_error' in self._callbacks:
            self._callbacks['on_error'](error_message)

    def _schedule_success_callback(self):
        """Schedule success callback after delay"""
        GLib.timeout_add_seconds(1, self._on_success_timeout)

    def _on_success_timeout(self):
        """Handle success timeout"""
        self._enable_ui()

        if 'on_success' in self._callbacks:
            self._callbacks['on_success']()

        return False
