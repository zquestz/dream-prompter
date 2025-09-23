#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Replicate API integration for Dream Prompter plugin
Multi-model API implementation using Replicate
"""

import io
import mimetypes
import os
import urllib.request
from typing import Optional, Callable, Tuple, List

from gi.repository import GdkPixbuf, Gimp

import integrator
from i18n import _
from models import BaseModel
from models.factory import get_default_model, get_model_by_name

PROGRESS_COMPLETE = 1.0
PROGRESS_DOWNLOAD = 0.9
PROGRESS_PREPARE = 0.1
PROGRESS_PROCESS = 0.7
PROGRESS_UPLOAD = 0.5

try:
    from replicate.client import Client
    from replicate.exceptions import ModelError, ReplicateError
    REPLICATE_AVAILABLE = True
except ImportError:
    REPLICATE_AVAILABLE = False
    print("Warning: replicate package not installed. Run: pip install replicate")

class ReplicateAPI:
    """Handles Replicate API communication for image generation and editing"""

    model: BaseModel

    def __init__(self, api_key: str, model_name: Optional[str] = None) -> None:
        """
        Initialize the Replicate API client

        Args:
            api_key (str): Replicate API key from user settings
            model_name (str, optional): Model to use (defaults to default model)
        """
        if not REPLICATE_AVAILABLE:
            raise ImportError(_("Replicate API not available. Please install replicate"))

        if not api_key or not api_key.strip():
            raise ValueError(_("API key is required"))

        self.api_key = api_key.strip()
        self.client = Client(api_token=self.api_key)

        if model_name:
            model = get_model_by_name(model_name)
            if not model:
                raise ValueError(f"Model '{model_name}' not found")
            self.model = model
        else:
            self.model = get_default_model()

    def edit_image(
        self,
        image: Gimp.Image,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        progress_callback: Optional[Callable[[str, Optional[float]], bool]] = None
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """
        Edit an image from a text prompt using the selected AI model

        Args:
            image (Gimp.Image): Image to edit
            prompt (str): Text description of the edits to make
            reference_images (list, optional): List of image file paths for reference
            progress_callback (callable, optional): Progress callback function.
                Called with (message: str, percentage: float | None).
                Should return True to continue, False to cancel.

        Returns:
            tuple: (List[GdkPixbuf.Pixbuf] | None, str | None)
                - If successful: (pixbufs, None)
                - If failed: (None, error_message)
                - If cancelled: (None, "Operation cancelled")
        """
        if not self.client:
            return None, _("Replicate API not available. Please install replicate")

        if not image:
            return None, _("No GIMP image provided for editing")

        if progress_callback and not progress_callback(_("Preparing current image for Replicate..."), PROGRESS_PREPARE):
            return None, _("Operation cancelled")

        try:
            current_image_data = integrator.export_current_region_to_bytes(image)
            if not current_image_data:
                return None, _("Failed to export current image")

            if progress_callback and not progress_callback(_("Building Replicate edit request..."), PROGRESS_UPLOAD):
                return None, _("Operation cancelled")

            ref_files = []
            if reference_images:
                ref_files = self._prepare_reference_images(reference_images, self.model.max_reference_images_edit)

            model_input = self.model.build_edit_input(
                prompt=prompt,
                main_image=io.BytesIO(current_image_data),
                reference_images=ref_files if ref_files else None
            )

            if progress_callback and not progress_callback(_("Sending edit request to Replicate..."), PROGRESS_PROCESS):
                return None, _("Operation cancelled")

            try:
                output = self.client.run(
                    self.model.name,
                    input=model_input
                )
            except ModelError as e:
                error_msg = _("Model error: {error}").format(error=str(e))
                if hasattr(e, 'prediction') and e.prediction:
                    if hasattr(e.prediction, 'logs') and e.prediction.logs:
                        error_msg += f"\n{_('Logs')}: {e.prediction.logs}"
                return None, error_msg
            except ReplicateError as e:
                return None, _("Replicate API error: {error}").format(error=str(e))

            if progress_callback and not progress_callback(_("Processing Replicate edit response..."), PROGRESS_DOWNLOAD):
                return None, _("Operation cancelled")

            if not output:
                return None, _("No output received from API")

            if progress_callback and not progress_callback(_("Downloading result..."), PROGRESS_DOWNLOAD):
                return None, _("Operation cancelled")

            image_bytes_list = self._process_api_response(output)

            if not image_bytes_list:
                return None, _("No valid image data in API response")

            pixbufs = []
            for i, image_bytes in enumerate(image_bytes_list):
                if not image_bytes or not isinstance(image_bytes, bytes):
                    continue

                pixbuf = self._bytes_to_pixbuf(image_bytes)
                if pixbuf:
                    pixbufs.append(pixbuf)

            if not pixbufs:
                return None, _("Failed to convert any images from API response")

            if progress_callback:
                progress_callback(_("Image editing complete!"), PROGRESS_COMPLETE)

            return pixbufs, None

        except Exception as e:
            return None, _("Unexpected error: {error}").format(error=str(e))

    def generate_image(
        self,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        progress_callback: Optional[Callable[[str, Optional[float]], bool]] = None
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """
        Generate a new image from a text prompt using the selected AI model

        Args:
            prompt (str): Text description of the image to generate
            reference_images (list, optional): List of image file paths for reference
            progress_callback (callable, optional): Progress callback function.
                Called with (message: str, percentage: float | None).
                Should return True to continue, False to cancel.

        Returns:
            tuple: (List[GdkPixbuf.Pixbuf] | None, str | None)
                - If successful: (pixbufs, None)
                - If failed: (None, error_message)
                - If cancelled: (None, "Operation cancelled")
        """
        if not self.client:
            return None, _("Replicate API not available. Please install replicate")

        if progress_callback and not progress_callback(_("Generating image with Replicate..."), PROGRESS_PREPARE):
            return None, _("Operation cancelled")

        try:
            ref_files = []
            if reference_images:
                ref_files = self._prepare_reference_images(reference_images, self.model.max_reference_images)

            model_input = self.model.build_generation_input(
                prompt=prompt,
                reference_images=ref_files if reference_images else None
            )

            if progress_callback and not progress_callback(_("Sending request to Replicate..."), PROGRESS_PROCESS):
                return None, _("Operation cancelled")

            try:
                output = self.client.run(
                    self.model.name,
                    input=model_input
                )

                if progress_callback and not progress_callback(_("Processing Replicate response..."), PROGRESS_DOWNLOAD):
                    return None, _("Operation cancelled")

                if not output:
                    return None, _("No output received from API")

                if progress_callback and not progress_callback(_("Downloading result..."), PROGRESS_DOWNLOAD):
                    return None, _("Operation cancelled")

                image_bytes_list = self._process_api_response(output)

                if not image_bytes_list:
                    return None, _("No valid image data in API response")

                pixbufs = []
                for i, image_bytes in enumerate(image_bytes_list):
                    if not image_bytes or not isinstance(image_bytes, bytes):
                        continue

                    pixbuf = self._bytes_to_pixbuf(image_bytes)
                    if pixbuf:
                        pixbufs.append(pixbuf)

                if not pixbufs:
                    return None, _("Failed to convert any images from API response")

                if progress_callback:
                    progress_callback(_("Image generation complete!"), PROGRESS_COMPLETE)

                return pixbufs, None

            except ModelError as e:
                error_msg = _("Model error: {error}").format(error=str(e))
                if hasattr(e, 'prediction') and e.prediction:
                    if hasattr(e.prediction, 'logs') and e.prediction.logs:
                        error_msg += f"\n{_('Logs')}: {e.prediction.logs}"
                return None, error_msg

            except ReplicateError as e:
                return None, _("Replicate API error: {error}").format(error=str(e))

        except Exception as e:
            return None, _("Unexpected error: {error}").format(error=str(e))

    def _bytes_to_pixbuf(self, image_bytes: bytes) -> Optional[GdkPixbuf.Pixbuf]:
        """
        Convert image bytes to GdkPixbuf

        Args:
            image_bytes (bytes): Image data

        Returns:
            GdkPixbuf.Pixbuf: Pixbuf object, or None if conversion failed
        """
        try:
            loader = GdkPixbuf.PixbufLoader()
            loader.write(image_bytes)
            loader.close()

            pixbuf = loader.get_pixbuf()
            return pixbuf

        except Exception as e:
            print(f"Error converting bytes to pixbuf: {e}")
            return None

    def _prepare_reference_images(
        self,
        reference_images: List[str],
        max_count: int
    ) -> List:
        """
        Prepare reference images for Replicate API

        Args:
            reference_images (list): List of image file paths
            max_count (int): Maximum number of images to process

        Returns:
            list: List of file objects for Replicate API
        """
        valid_files = []

        for img_path in reference_images[:max_count]:
            if self._validate_reference_image(img_path):
                try:
                    valid_files.append(open(img_path, 'rb'))
                except (OSError, IOError) as e:
                    print(f"Warning: Could not open reference image {img_path}: {e}")

        return valid_files

    def _process_api_response(self, output) -> List[bytes]:
        """Process API response and return list of image bytes"""
        image_bytes_list = []

        if isinstance(output, str):
            with urllib.request.urlopen(output) as url_response:
                image_bytes_list.append(url_response.read())
        elif isinstance(output, bytes):
            image_bytes_list.append(output)
        elif isinstance(output, (list, tuple)):
            for item in output:
                if isinstance(item, str):
                    with urllib.request.urlopen(item) as url_response:
                        image_bytes_list.append(url_response.read())
                elif isinstance(item, bytes):
                    image_bytes_list.append(item)
                elif hasattr(item, 'read'):
                    image_bytes_list.append(item.read())
        elif hasattr(output, '__iter__'):
            try:
                chunk_bytes = b''.join(chunk for chunk in output)
                image_bytes_list.append(chunk_bytes)
            except (TypeError, ValueError):
                pass

        return image_bytes_list

    def _validate_reference_image(
        self,
        img_path: str,
        max_size_mb: Optional[int] = None
    ) -> bool:
        """
        Validate a reference image file

        Args:
            img_path (str): Path to the image file
            max_size_mb (int): Maximum file size in MB

        Returns:
            bool: True if valid, False otherwise
        """
        try:
            if not os.path.exists(img_path):
                print(f"Warning: Image file {img_path} does not exist. Skipping.")
                return False

            file_size = os.path.getsize(img_path)
            if not self.model.validate_file_size(file_size):
                print(f"Warning: Image {img_path} is {file_size / (1024*1024):.1f} MB, exceeds {self.model.max_file_size_mb} MB limit. Skipping.")
                return False

            mime_type, encoding = mimetypes.guess_type(img_path)
            if mime_type and not self.model.validate_mime_type(mime_type):
                print(f"Warning: Image {img_path} has unsupported MIME type {mime_type} with encoding {encoding}. Skipping.")
                return False
            elif not mime_type:
                print(f"Warning: Could not determine MIME type for {img_path}. Skipping.")
                return False

            return True

        except Exception as e:
            print(f"Warning: Could not validate reference image {img_path}: {e}")
            return False
