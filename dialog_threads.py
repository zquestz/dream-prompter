#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Threading operations for Dream Prompter dialog
Handles all background AI processing and image operations
"""

import threading
from typing import Dict, Callable, Optional, Any, List

from gi.repository import GLib, GdkPixbuf

import integrator
from api import ReplicateAPI
from dialog_gtk import DreamPrompterUI
from i18n import _


class DreamPrompterThreads:
    """Handles all background threading operations"""

    def __init__(
        self, ui: DreamPrompterUI, image: Optional[Any], drawable: Optional[Any]
    ) -> None:
        """
        Initialize thread manager

        Args:
            ui: The UI controller instance
            image: GIMP image object (optional for generation mode)
            drawable: GIMP drawable object (optional for generation mode)

        Raises:
            ValueError: If ui is None
        """
        if not ui:
            raise ValueError("UI object is required")

        self.ui = ui
        self.image = image
        self.drawable = drawable
        self._callbacks: Dict[str, Callable] = {}
        self._processing: bool = False
        self._cancel_requested: bool = False
        self._current_thread: Optional[threading.Thread] = None

    def cancel_processing(self) -> None:
        """Request cancellation of current processing"""
        self._cancel_requested = True
        self.ui.update_status(_("Cancelling..."))

    def is_processing(self) -> bool:
        """Check if image processing is currently running"""
        return self._processing

    def set_callbacks(self, callbacks: Dict[str, Callable]) -> None:
        """
        Set callback functions for thread completion

        Args:
            callbacks: Dictionary containing 'on_success' and/or 'on_error'
                callbacks

        Raises:
            ValueError: If callbacks is not a dictionary
        """
        if not isinstance(callbacks, dict):
            raise ValueError("Callbacks must be a dictionary")

        valid_keys = {"on_success", "on_error"}
        for key in callbacks.keys():
            if key not in valid_keys:
                error_msg = (
                    f"Invalid callback key: {key}. Valid keys: {valid_keys}"
                )
                raise ValueError(error_msg)

        self._callbacks = callbacks

    def start_edit_thread(
        self,
        api_key: str,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        model_name: Optional[str] = None,
    ) -> None:
        """
        Start image editing in background thread

        Args:
            api_key: Replicate API key
            prompt: Text prompt for image editing
            reference_images: Optional list of reference image paths
            model_name: Optional model name to use
        """
        if not self.ui or self._processing:
            return

        if not self.drawable:
            self._handle_error(_("No layer available for editing"))
            return

        if not self.image:
            self._handle_error(_("No image available for editing"))
            return

        if not api_key or not api_key.strip():
            self._handle_error(_("API key is required"))
            return

        if not prompt or not prompt.strip():
            self._handle_error(_("Prompt is required"))
            return

        self._processing = True
        self._cancel_requested = False
        self.ui.set_ui_enabled(False)

        self._current_thread = threading.Thread(
            target=self._edit_image_worker,
            args=(api_key, prompt, reference_images, model_name),
        )
        self._current_thread.daemon = True
        self._current_thread.start()

    def start_generate_thread(
        self,
        api_key: str,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        model_name: Optional[str] = None,
    ) -> None:
        """
        Start image generation in background thread

        Args:
            api_key: Replicate API key
            prompt: Text prompt for image generation
            reference_images: Optional list of reference image paths
            model_name: Optional model name to use
        """
        if not self.ui or self._processing:
            return

        if not api_key or not api_key.strip():
            self._handle_error(_("API key is required"))
            return

        if not prompt or not prompt.strip():
            self._handle_error(_("Prompt is required"))
            return

        self._processing = True
        self._cancel_requested = False
        self.ui.set_ui_enabled(False)

        self._current_thread = threading.Thread(
            target=self._generate_image_worker,
            args=(api_key, prompt, reference_images, model_name),
        )
        self._current_thread.daemon = True
        self._current_thread.start()

    def _edit_image_worker(
        self,
        api_key: str,
        prompt: str,
        reference_images: Optional[List[str]],
        model_name: Optional[str],
    ) -> None:
        """
        Edit image in background thread

        Args:
            api_key: Replicate API key
            prompt: Text prompt for image editing
            reference_images: List of reference image paths
            model_name: Optional model name to use
        """
        try:
            if self._cancel_requested:
                GLib.idle_add(self._handle_cancelled)
                return

            if not self.image:
                GLib.idle_add(
                    self._handle_error, _("No image available for editing")
                )
                return

            api = ReplicateAPI(api_key, model_name)

            def progress_callback(
                message: str, percentage: Optional[float] = None
            ) -> bool:
                """Progress callback for API operations"""
                if self._cancel_requested:
                    return False
                GLib.idle_add(self.ui.update_status, message, percentage)
                return True

            pixbufs, error_msg = api.edit_image(
                image=self.image,
                prompt=prompt,
                reference_images=reference_images,
                progress_callback=progress_callback,
            )

            if self._cancel_requested:
                GLib.idle_add(self._handle_cancelled)
                return

            if error_msg:
                GLib.idle_add(self._handle_error, error_msg)
                return

            if not pixbufs:
                GLib.idle_add(
                    self._handle_error, _("No image data received from API")
                )
                return

            layer_name = self._generate_layer_name(prompt)
            GLib.idle_add(self._handle_edited_images, pixbufs, layer_name)

        except (ImportError, ValueError) as e:
            GLib.idle_add(self._handle_error, str(e))
        except Exception as e:
            error_text = _("Unexpected error during image editing: {error}")
            error_msg = error_text.format(error=str(e))
            GLib.idle_add(self._handle_error, error_msg)

    def _generate_image_worker(
        self,
        api_key: str,
        prompt: str,
        reference_images: Optional[List[str]],
        model_name: Optional[str],
    ) -> None:
        """
        Generate image in background thread

        Args:
            api_key: Replicate API key
            prompt: Text prompt for image generation
            reference_images: List of reference image paths
            model_name: Optional model name to use
        """
        try:
            if self._cancel_requested:
                GLib.idle_add(self._handle_cancelled)
                return

            api = ReplicateAPI(api_key, model_name)

            def progress_callback(
                message: str, percentage: Optional[float] = None
            ) -> bool:
                """Progress callback for API operations"""
                if self._cancel_requested:
                    return False
                GLib.idle_add(self.ui.update_status, message, percentage)
                return True

            pixbufs, error_msg = api.generate_image(
                prompt=prompt,
                reference_images=reference_images,
                progress_callback=progress_callback,
            )

            if self._cancel_requested:
                GLib.idle_add(self._handle_cancelled)
                return

            if error_msg:
                GLib.idle_add(self._handle_error, error_msg)
                return

            if not pixbufs:
                GLib.idle_add(
                    self._handle_error, _("No image data received from API")
                )
                return

            GLib.idle_add(self._handle_generated_images, pixbufs, prompt)

        except (ImportError, ValueError) as e:
            GLib.idle_add(self._handle_error, str(e))
        except Exception as e:
            error_text = _("Unexpected error during image generation: {error}")
            error_msg = error_text.format(error=str(e))
            GLib.idle_add(self._handle_error, error_msg)

    def _generate_layer_name(self, prompt: str) -> str:
        """
        Generate a name for the new layer

        Args:
            prompt: The AI prompt used for generation

        Returns:
            A descriptive name for the new layer
        """
        if self.drawable and prompt:
            original_name = self.drawable.get_name()
            truncated_prompt = (
                prompt[:30] + "..." if len(prompt) > 30 else prompt
            )
            return _("{original} (AI Edit: {prompt})").format(
                original=original_name, prompt=truncated_prompt
            )
        elif prompt:
            truncated_prompt = (
                prompt[:30] + "..." if len(prompt) > 30 else prompt
            )
            return _("AI Generated: {prompt}").format(prompt=truncated_prompt)
        else:
            return _("AI Layer")

    def _handle_cancelled(self) -> None:
        """Handle cancelled operation"""
        self._processing = False
        self._current_thread = None
        self.ui.reset_progress()
        self.ui.set_ui_enabled(True)

    def _handle_edited_images(
        self, pixbufs: List[GdkPixbuf.Pixbuf], base_layer_name: str
    ) -> None:
        """
        Handle multiple edited images by creating layers

        Args:
            pixbufs: List of edited image data
            base_layer_name: Base name for the new layers
        """
        try:
            for i, pixbuf in enumerate(pixbufs):
                if len(pixbufs) > 1:
                    layer_name = f"{base_layer_name} {i + 1}"
                else:
                    layer_name = base_layer_name

                status_msg = _("Adding layer {num}...").format(num=i + 1)
                progress = 0.8 + (0.1 * i / len(pixbufs))
                self.ui.update_status(status_msg, progress)

                layer = integrator.create_edit_layer(
                    self.image, self.drawable, pixbuf, layer_name
                )
                if not layer:
                    print(f"Warning: Failed to create layer {i + 1}")
                    continue

            count_msg = _("Added {count} layers").format(count=len(pixbufs))
            self.ui.update_status(count_msg, 1.0)
            self._handle_success()

        except Exception as e:
            error_msg = _("Error adding layers: {error}").format(error=str(e))
            self._handle_error(error_msg)

    def _handle_generated_images(
        self, pixbufs: List[GdkPixbuf.Pixbuf], prompt: str
    ) -> None:
        """
        Handle multiple generated images by creating separate files

        Args:
            pixbufs: List of generated image data
            prompt: The prompt used for generation
        """
        try:
            for i, pixbuf in enumerate(pixbufs):
                status_msg = _("Creating image {num}...").format(num=i + 1)
                progress = 0.8 + (0.1 * i / len(pixbufs))
                self.ui.update_status(status_msg, progress)

                if len(pixbufs) > 1:
                    layer_name = _("AI Generated {num}").format(num=i + 1)
                else:
                    layer_name = _("AI Generated")

                image = integrator.create_new_image(pixbuf, layer_name)
                if not image:
                    print(f"Warning: Failed to create image {i + 1}")
                    continue

            count_msg = _("Generated {count} images").format(count=len(pixbufs))
            self.ui.update_status(count_msg, 1.0)
            self._handle_success()

        except Exception as e:
            error_msg = _("Error creating images: {error}").format(error=str(e))
            self._handle_error(error_msg)

    def _handle_error(self, error_message: str) -> None:
        """
        Handle error during processing

        Args:
            error_message: The error message to display
        """
        self._processing = False
        self._current_thread = None
        self.ui.reset_progress()
        self.ui.set_ui_enabled(True)

        if self._callbacks.get("on_error"):
            self._callbacks["on_error"](error_message)

    def _handle_success(self) -> None:
        """Handle successful processing"""
        self._processing = False
        self._current_thread = None
        self.ui.reset_progress()
        self.ui.set_ui_enabled(True)

        if self._callbacks.get("on_success"):
            self._callbacks["on_success"]()
