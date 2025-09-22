#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Replicate API integration for Dream Prompter plugin
Real Nano Banana API implementation using Replicate
"""

import base64
import io
import mimetypes
import os
from typing import Optional, Callable, Tuple, List

from gi.repository import GdkPixbuf, Gimp

import integrator
from i18n import _

MAX_FILE_SIZE_MB = 7
MAX_REFERENCE_IMAGES_EDIT = 9
MAX_REFERENCE_IMAGES_GENERATE = 10
PROGRESS_COMPLETE = 1.0
PROGRESS_DOWNLOAD = 0.9
PROGRESS_PREPARE = 0.1
PROGRESS_PROCESS = 0.7
PROGRESS_UPLOAD = 0.5
SUPPORTED_MIME_TYPES = ['image/png', 'image/jpeg', 'image/webp']

try:
    from replicate.client import Client
    from replicate.exceptions import ModelError, ReplicateError
    REPLICATE_AVAILABLE = True
except ImportError:
    REPLICATE_AVAILABLE = False
    print("Warning: replicate package not installed. Run: pip install replicate")

class ReplicateAPI:
    """Handles Replicate API communication for image generation and editing"""

    def __init__(self, api_key: str) -> None:
        """
        Initialize the Replicate API client

        Args:
            api_key (str): Replicate API key from user settings
        """
        if not REPLICATE_AVAILABLE:
            raise ImportError(_("Replicate API not available. Please install replicate"))

        if not api_key or not api_key.strip():
            raise ValueError(_("API key is required"))

        self.api_key = api_key.strip()
        self.client = Client(api_token=self.api_key)

    def edit_image(
        self,
        image: Gimp.Image,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        progress_callback: Optional[Callable[[str, Optional[float]], bool]] = None
    ) -> Tuple[Optional[GdkPixbuf.Pixbuf], Optional[str]]:
        """
        Edit an image from a text prompt using Nano Banana

        Args:
            image (Gimp.Image): Image to edit
            prompt (str): Text description of the edits to make
            reference_images (list, optional): List of image file paths for reference (max 9)
            progress_callback (callable, optional): Progress callback function.
                Called with (message: str, percentage: float | None).
                Should return True to continue, False to cancel.

        Returns:
            tuple: (GdkPixbuf.Pixbuf | None, str | None)
                - If successful: (pixbuf, None)
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

            image_input = [io.BytesIO(current_image_data)]

            if reference_images:
                ref_files = self._prepare_reference_images(reference_images, MAX_REFERENCE_IMAGES_EDIT)
                image_input.extend(ref_files)

            model_input = {
                "prompt": prompt,
                "image_input": image_input,
                "output_format": "png"
            }

            if progress_callback and not progress_callback(_("Sending edit request to Replicate..."), PROGRESS_PROCESS):
                return None, _("Operation cancelled")

            try:
                output = self.client.run(
                    "google/nano-banana",
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

            result_bytes = None
            if isinstance(output, str):
                import urllib.request
                with urllib.request.urlopen(output) as url_response:
                    result_bytes = url_response.read()
            elif isinstance(output, bytes):
                result_bytes = output
            elif hasattr(output, '__iter__'):
                try:
                    result_bytes = b''.join(chunk for chunk in output)
                except (TypeError, ValueError):
                    return None, _("Failed to process iterable response")
            else:
                return None, _("Unexpected response format from API")

            if not result_bytes or not isinstance(result_bytes, bytes):
                return None, _("No valid image data in API response")

            pixbuf = self._bytes_to_pixbuf(result_bytes)
            if not pixbuf:
                return None, _("Failed to convert result to image")

            if progress_callback:
                progress_callback(_("Image editing complete!"), PROGRESS_COMPLETE)

            return pixbuf, None

        except Exception as e:
            return None, _("Unexpected error: {error}").format(error=str(e))

    def generate_image(
        self,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        progress_callback: Optional[Callable[[str, Optional[float]], bool]] = None
    ) -> Tuple[Optional[GdkPixbuf.Pixbuf], Optional[str]]:
        """
        Generate a new image from a text prompt using Nano Banana

        Args:
            prompt (str): Text description of the image to generate
            reference_images (list, optional): List of image file paths for reference (max 10)
            progress_callback (callable, optional): Progress callback function.
                Called with (message: str, percentage: float | None).
                Should return True to continue, False to cancel.

        Returns:
            tuple: (GdkPixbuf.Pixbuf | None, str | None)
                - If successful: (pixbuf, None)
                - If failed: (None, error_message)
                - If cancelled: (None, "Operation cancelled")
        """
        if not self.client:
            return None, _("Replicate API not available. Please install replicate")

        if progress_callback and not progress_callback(_("Generating image with Replicate..."), PROGRESS_PREPARE):
            return None, _("Operation cancelled")

        try:
            image_input = []

            if reference_images:
                ref_files = self._prepare_reference_images(reference_images, MAX_REFERENCE_IMAGES_GENERATE)
                image_input.extend(ref_files)

            model_input = {
                "prompt": prompt,
                "image_input": image_input,
                "output_format": "png"
            }

            if progress_callback and not progress_callback(_("Sending request to Replicate..."), PROGRESS_PROCESS):
                return None, _("Operation cancelled")

            try:
                output = self.client.run(
                    "google/nano-banana",
                    input=model_input
                )

                if progress_callback and not progress_callback(_("Processing Replicate response..."), PROGRESS_DOWNLOAD):
                    return None, _("Operation cancelled")

                if not output:
                    return None, _("No output received from API")

                if progress_callback and not progress_callback(_("Downloading result..."), PROGRESS_DOWNLOAD):
                    return None, _("Operation cancelled")

                result_bytes = None
                if isinstance(output, str):
                    import urllib.request
                    with urllib.request.urlopen(output) as url_response:
                        result_bytes = url_response.read()
                elif isinstance(output, bytes):
                    result_bytes = output
                elif hasattr(output, '__iter__'):
                    try:
                        result_bytes = b''.join(chunk for chunk in output)
                    except (TypeError, ValueError):
                        return None, _("Failed to process iterable response")
                else:
                    return None, _("Unexpected response format from API")

                if not result_bytes or not isinstance(result_bytes, bytes):
                    return None, _("No valid image data in API response")

                pixbuf = self._bytes_to_pixbuf(result_bytes)
                if not pixbuf:
                    return None, _("Failed to convert result to image")

                if progress_callback:
                    progress_callback(_("Image generation complete!"), PROGRESS_COMPLETE)

                return pixbuf, None

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
                valid_files.append(open(img_path, 'rb'))

        return valid_files

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

    def _validate_reference_image(
        self,
        img_path: str,
        max_size_mb: int = MAX_FILE_SIZE_MB
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
            file_size = os.path.getsize(img_path)
            if file_size > max_size_mb * 1024 * 1024:
                print(f"Warning: Image {img_path} is {file_size / (1024*1024):.1f} MB, exceeds {max_size_mb} MB limit. Skipping.")
                return False

            mime_type, encoding = mimetypes.guess_type(img_path)
            if mime_type not in SUPPORTED_MIME_TYPES:
                print(f"Warning: Image {img_path} has unsupported MIME type {mime_type} with encoding {encoding}. Skipping.")
                return False

            return True

        except Exception as e:
            print(f"Warning: Could not validate reference image {img_path}: {e}")
            return False
