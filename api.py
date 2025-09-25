#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Replicate API integration for Dream Prompter plugin.

This module provides the ReplicateAPI class for communicating with Replicate's
API to perform image generation and editing operations using various AI models.
"""

import io
import mimetypes
import os
import urllib.request
from contextlib import contextmanager
from typing import Callable, List, Optional, Tuple, Union

from gi.repository import GdkPixbuf, Gimp

import integrator
from i18n import _
from models.factory import get_default_model, get_model_by_name
from settings import get_model_settings

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
    print("Warning: replicate package not installed. "
          "Run: pip install replicate")


class ReplicateAPI:
    """Handles Replicate API communication for image generation and editing."""

    def __init__(self, api_key: str, model_name: Optional[str] = None) -> None:
        """
        Initialize the Replicate API client.

        Args:
            api_key: Replicate API key from user settings
            model_name: Model to use (defaults to default model)

        Raises:
            ImportError: If Replicate API is not available
            ValueError: If API key is invalid or model not found
        """
        if not REPLICATE_AVAILABLE:
            raise ImportError(
                _("Replicate API not available. Please install replicate")
            )

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
        progress_callback: Optional[
            Callable[[str, Optional[float]], bool]
        ] = None
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """
        Edit an image using AI model based on text prompt.

        Args:
            image: GIMP image to edit
            prompt: Text description of the edits to make
            reference_images: List of image file paths for reference
            progress_callback: Progress callback function that receives
                (message: str, percentage: float | None) and returns
                True to continue, False to cancel

        Returns:
            Tuple of (pixbufs, error_message):
            - If successful: (List[GdkPixbuf.Pixbuf], None)
            - If failed: (None, error_message)
            - If cancelled: (None, "Operation cancelled")
        """
        if not self.client:
            return None, _(
                "Replicate API not available. Please install replicate"
            )

        if not image:
            return None, _("No GIMP image provided for editing")

        try:
            if (progress_callback and not progress_callback(
                _("Preparing current image for Replicate..."),
                PROGRESS_PREPARE
            )):
                return None, _("Operation cancelled")

            current_image_data = integrator.export_current_region_to_bytes(
                image
            )
            if not current_image_data:
                return None, _("Failed to export current image")

            with self._prepare_reference_images(
                reference_images, self.model.max_reference_images_edit
            ) as ref_files:
                if (progress_callback and not progress_callback(
                    _("Building Replicate edit request..."), PROGRESS_UPLOAD
                )):
                    return None, _("Operation cancelled")

                user_settings = get_model_settings(self.model.name)
                model_input = self.model.build_edit_input(
                    prompt=prompt,
                    main_image=io.BytesIO(current_image_data),
                    reference_images=ref_files if ref_files else None,
                    user_settings=user_settings
                )

                if (progress_callback and not progress_callback(
                    _("Sending edit request to Replicate..."), PROGRESS_PROCESS
                )):
                    return None, _("Operation cancelled")

                output = self._execute_api_call(model_input)
                if isinstance(output, str):
                    return None, output

            return self._process_response(output, progress_callback)

        except Exception as e:
            return None, _("Unexpected error: {error}").format(error=str(e))

    def generate_image(
        self,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        progress_callback: Optional[
            Callable[[str, Optional[float]], bool]
        ] = None
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """
        Generate a new image using AI model based on text prompt.

        Args:
            prompt: Text description of the image to generate
            reference_images: List of image file paths for reference
            progress_callback: Progress callback function that receives
                (message: str, percentage: float | None) and returns
                True to continue, False to cancel

        Returns:
            Tuple of (pixbufs, error_message):
            - If successful: (List[GdkPixbuf.Pixbuf], None)
            - If failed: (None, error_message)
            - If cancelled: (None, "Operation cancelled")
        """
        if not self.client:
            return None, _(
                "Replicate API not available. Please install replicate"
            )

        try:
            with self._prepare_reference_images(
                reference_images, self.model.max_reference_images
            ) as ref_files:
                if (progress_callback and not progress_callback(
                    _("Generating image with Replicate..."), PROGRESS_PREPARE
                )):
                    return None, _("Operation cancelled")

                user_settings = get_model_settings(self.model.name)
                model_input = self.model.build_generation_input(
                    prompt=prompt,
                    reference_images=ref_files if reference_images else None,
                    user_settings=user_settings
                )

                if (progress_callback and not progress_callback(
                    _("Sending request to Replicate..."), PROGRESS_PROCESS
                )):
                    return None, _("Operation cancelled")

                output = self._execute_api_call(model_input)
                if isinstance(output, str):
                    return None, output

            return self._process_response(output, progress_callback)

        except Exception as e:
            return None, _("Unexpected error: {error}").format(error=str(e))

    def _bytes_to_pixbuf(
        self, image_bytes: bytes
    ) -> Optional[GdkPixbuf.Pixbuf]:
        """
        Convert image bytes to GdkPixbuf.

        Args:
            image_bytes: Image data as bytes

        Returns:
            GdkPixbuf.Pixbuf object, or None if conversion failed
        """
        try:
            loader = GdkPixbuf.PixbufLoader()
            loader.write(image_bytes)
            loader.close()
            return loader.get_pixbuf()

        except Exception as e:
            print(f"Error converting bytes to pixbuf: {e}")
            return None

    def _download_from_url(self, url: str) -> Optional[bytes]:
        """
        Download image data from URL.

        Args:
            url: Image URL to download

        Returns:
            Image data as bytes, or None if download failed
        """
        try:
            with urllib.request.urlopen(url) as url_response:
                return url_response.read()
        except Exception as e:
            print(f"Error downloading from URL {url}: {e}")
            return None

    def _execute_api_call(self, model_input: dict) -> Union[object, str]:
        """
        Execute API call with proper error handling.

        Args:
            model_input: Input parameters for the model

        Returns:
            API response object or error message string
        """
        try:
            return self.client.run(self.model.name, input=model_input)

        except ModelError as e:
            error_msg = _("Model error: {error}").format(error=str(e))
            if hasattr(e, 'prediction') and e.prediction:
                if hasattr(e.prediction, 'logs') and e.prediction.logs:
                    error_msg += f"\n{_('Logs')}: {e.prediction.logs}"
            return error_msg

        except ReplicateError as e:
            return _("Replicate API error: {error}").format(error=str(e))

    @contextmanager
    def _prepare_reference_images(
        self,
        reference_images: Optional[List[str]],
        max_count: int
    ):
        """
        Context manager for preparing reference images.

        Args:
            reference_images: List of image file paths
            max_count: Maximum number of images to process

        Yields:
            List of file objects for Replicate API
        """
        if not reference_images:
            yield []
            return

        file_handles = []
        try:
            for img_path in reference_images[:max_count]:
                if self._validate_reference_image(img_path):
                    try:
                        file_handle = open(img_path, 'rb')
                        file_handles.append(file_handle)
                    except (OSError, IOError) as e:
                        print(f"Warning: Could not open reference image "
                              f"{img_path}: {e}")

            yield file_handles

        finally:
            for file_handle in file_handles:
                try:
                    file_handle.close()
                except Exception as e:
                    print(f"Error closing file handle: {e}")

    def _process_api_response(self, output) -> List[bytes]:
        """
        Process API response and extract image bytes.

        Args:
            output: API response object

        Returns:
            List of image data as bytes
        """
        image_bytes_list = []

        if isinstance(output, str):
            image_bytes_list.append(self._download_from_url(output))
        elif isinstance(output, bytes):
            image_bytes_list.append(output)
        elif isinstance(output, (list, tuple)):
            for item in output:
                if isinstance(item, str):
                    downloaded_bytes = self._download_from_url(item)
                    if downloaded_bytes:
                        image_bytes_list.append(downloaded_bytes)
                elif isinstance(item, bytes):
                    image_bytes_list.append(item)
                elif hasattr(item, 'read'):
                    try:
                        image_bytes_list.append(item.read())
                    except Exception as e:
                        print(f"Error reading from file-like object: {e}")
        elif hasattr(output, '__iter__'):
            try:
                chunk_bytes = b''.join(chunk for chunk in output)
                if chunk_bytes:
                    image_bytes_list.append(chunk_bytes)
            except (TypeError, ValueError) as e:
                print(f"Error processing iterable output: {e}")

        return [img_bytes for img_bytes in image_bytes_list if img_bytes]

    def _process_response(
        self,
        output,
        progress_callback: Optional[
            Callable[[str, Optional[float]], bool]
        ] = None
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """
        Process API response and convert to pixbufs.

        Args:
            output: API response object
            progress_callback: Progress callback function

        Returns:
            Tuple of (pixbufs, error_message)
        """
        if (progress_callback and not progress_callback(
            _("Processing Replicate response..."), PROGRESS_DOWNLOAD
        )):
            return None, _("Operation cancelled")

        if not output:
            return None, _("No output received from API")

        if (progress_callback and not progress_callback(
            _("Downloading result..."), PROGRESS_DOWNLOAD
        )):
            return None, _("Operation cancelled")

        image_bytes_list = self._process_api_response(output)
        if not image_bytes_list:
            return None, _("No valid image data in API response")

        pixbufs = []
        for image_bytes in image_bytes_list:
            if image_bytes and isinstance(image_bytes, bytes):
                pixbuf = self._bytes_to_pixbuf(image_bytes)
                if pixbuf:
                    pixbufs.append(pixbuf)

        if not pixbufs:
            return None, _("Failed to convert any images from API response")

        if progress_callback:
            operation_complete_msg = (
                _("Image editing complete!")
                if hasattr(self, '_is_edit_operation')
                else _("Image generation complete!")
            )
            progress_callback(operation_complete_msg, PROGRESS_COMPLETE)

        return pixbufs, None

    def _validate_reference_image(self, img_path: str) -> bool:
        """
        Validate a reference image file.

        Args:
            img_path: Path to the image file

        Returns:
            True if valid, False otherwise
        """
        try:
            if not os.path.exists(img_path):
                print(f"Warning: Image file {img_path} does not exist. "
                      "Skipping.")
                return False

            file_size = os.path.getsize(img_path)
            if not self.model.validate_file_size(file_size):
                file_size_mb = file_size / (1024 * 1024)
                max_size_mb = self.model.max_file_size_mb
                print(f"Warning: Image {img_path} is {file_size_mb:.1f} MB, "
                      f"exceeds {max_size_mb} MB limit. Skipping.")
                return False

            mime_type, encoding = mimetypes.guess_type(img_path)
            if not mime_type:
                print(f"Warning: Could not determine MIME type for "
                      f"{img_path}. Skipping.")
                return False

            if not self.model.validate_mime_type(mime_type):
                print(f"Warning: Image {img_path} has unsupported MIME type "
                      f"{mime_type}. Skipping.")
                return False

            return True

        except Exception as e:
            print(f"Warning: Could not validate reference image "
                  f"{img_path}: {e}")
            return False
