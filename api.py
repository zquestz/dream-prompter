#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Google AI image generation integration for Dream Prompter plugin
Real Gemini API implementation using modern google-genai library
"""

import base64
import mimetypes
import os
from typing import Optional, Callable, Tuple, List

from gi.repository import GdkPixbuf, Gimp

import integrator
from i18n import _

MAX_FILE_SIZE_MB = 7
MAX_REFERENCE_IMAGES_EDIT = 2
MAX_REFERENCE_IMAGES_GENERATE = 3
PROGRESS_COMPLETE = 1.0
PROGRESS_DOWNLOAD = 0.9
PROGRESS_PREPARE = 0.1
PROGRESS_PROCESS = 0.7
PROGRESS_UPLOAD = 0.5
SUPPORTED_MIME_TYPES = ['image/png', 'image/jpeg', 'image/webp']

try:
    from google import genai
    from google.genai import types, errors
    GENAI_AVAILABLE = True
except ImportError:
    genai = None
    types = None
    errors = None
    GENAI_AVAILABLE = False
    print("Warning: google-genai not installed. Install with: pip install google-genai")

class GeminiAPI:
    """Google AI client for image generation and editing"""

    def __init__(self, api_key: str) -> None:
        """
        Initialize the Gemini API client

        Args:
            api_key (str): Google Gemini API key for authentication

        Raises:
            ImportError: If google-genai package is not available
            ValueError: If API key is invalid
        """
        if not GENAI_AVAILABLE:
            raise ImportError(_("Nano Banana API not available. Please install google-genai"))

        if not api_key or not api_key.strip():
            raise ValueError(_("API key is required"))

        self.api_key = api_key.strip()
        self.client = genai.Client(api_key=self.api_key) if genai else None

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
            reference_images (list, optional): List of image file paths for reference (max 2)
            progress_callback (callable, optional): Progress callback function.
                Called with (message: str, percentage: float | None).
                Should return True to continue, False to cancel.

        Returns:
            tuple: (GdkPixbuf.Pixbuf | None, str | None)
                - If successful: (pixbuf, None)
                - If failed: (None, error_message)
                - If cancelled: (None, "Operation cancelled")
        """
        if not self.client or not types or not errors:
            return None, _("Nano Banana API not available. Please install google-genai")

        if not image:
            return None, _("No GIMP image provided for editing")

        if progress_callback and not progress_callback(_("Preparing current image for Nano Banana..."), PROGRESS_PREPARE):
            return None, _("Operation cancelled")

        try:
            current_image_data = integrator.export_current_region_to_bytes(image)
            if not current_image_data:
                return None, _("Failed to export current image")

            if progress_callback and not progress_callback(_("Building Nano Banana edit request..."), PROGRESS_UPLOAD):
                return None, _("Operation cancelled")

            contents = []

            current_image_part = types.Part(
                inline_data=types.Blob(
                    data=current_image_data,
                    mime_type='image/png'
                )
            )
            contents.append(current_image_part)

            self._add_reference_images(contents, reference_images, MAX_REFERENCE_IMAGES_EDIT)

            contents.append(prompt)

            if progress_callback and not progress_callback(_("Sending edit request to Nano Banana..."), PROGRESS_PROCESS):
                return None, _("Operation cancelled")

            response = self.client.models.generate_content(
                model='gemini-2.5-flash-image-preview',
                contents=contents
            )

            if progress_callback and not progress_callback(_("Processing Nano Banana edit response..."), PROGRESS_DOWNLOAD):
                return None, _("Operation cancelled")

            pixbuf, error_msg = self._parse_image_response(response)

            if progress_callback and pixbuf:
                progress_callback(_("Image editing complete!"), PROGRESS_COMPLETE)

            return pixbuf, error_msg

        except errors.APIError as e:
            return None, _("Nano Banana API error: {error}").format(error=e.message)
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
            reference_images (list, optional): List of image file paths for reference (max 3)
            progress_callback (callable, optional): Progress callback function.
                Called with (message: str, percentage: float | None).
                Should return True to continue, False to cancel.

        Returns:
            tuple: (GdkPixbuf.Pixbuf | None, str | None)
                - If successful: (pixbuf, None)
                - If failed: (None, error_message)
                - If cancelled: (None, "Operation cancelled")
        """
        if not self.client or not types or not errors:
            return None, _("Nano Banana API not available. Please install google-genai")

        if progress_callback and not progress_callback(_("Generating image with Nano Banana..."), PROGRESS_PREPARE):
            return None, _("Operation cancelled")

        try:
            if reference_images:
                contents = []

                prompt_part = types.Part(text=prompt)
                contents.append(prompt_part)

                self._add_reference_images(contents, reference_images, MAX_REFERENCE_IMAGES_GENERATE)
            else:
                contents = prompt

            if progress_callback and not progress_callback(_("Sending request to Nano Banana..."), PROGRESS_PROCESS):
                return None, _("Operation cancelled")

            response = self.client.models.generate_content(
                model='gemini-2.5-flash-image-preview',
                contents=contents
            )

            if progress_callback and not progress_callback(_("Processing Nano Banana response..."), PROGRESS_DOWNLOAD):
                return None, _("Operation cancelled")

            pixbuf, error_msg = self._parse_image_response(response)

            if progress_callback and pixbuf:
                progress_callback(_("Image generation complete!"), PROGRESS_COMPLETE)

            return pixbuf, error_msg

        except errors.APIError as e:
            return None, _("Nano Banana API error: {error}").format(error=e.message)
        except Exception as e:
            return None, _("Unexpected error: {error}").format(error=str(e))

    def _add_reference_images(
        self,
        contents: List,
        reference_images: Optional[List[str]],
        max_count: int
    ) -> None:
        """
        Add reference images to the contents list

        Args:
            contents (list): List to append image parts to
            reference_images (list, optional): List of image file paths
            max_count (int): Maximum number of images to add
        """
        if not reference_images or not types:
            return

        for img_path in reference_images[:max_count]:
            image_part, success = self._validate_reference_image(img_path)
            if success and image_part:
                contents.append(image_part)

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

    def _parse_image_response(self, response) -> Tuple[Optional[GdkPixbuf.Pixbuf], Optional[str]]:
        """
        Parse the API response and extract the generated image

        Args:
            response: API response object

        Returns:
            tuple: (GdkPixbuf.Pixbuf | None, str | None)
                - If successful: (pixbuf, None)
                - If failed: (None, error_message)
        """
        if hasattr(response, 'error') and response.error:
            return None, str(response.error)

        if hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'finish_reason') and candidate.finish_reason:
                if candidate.finish_reason not in ['STOP', 'MAX_TOKENS']:
                    return None, _("Generation stopped: {reason}").format(reason=candidate.finish_reason)

        if not response.candidates:
            return None, _("No candidates in API response")

        candidate = response.candidates[0]
        if not candidate.content or not candidate.content.parts:
            return None, _("No content parts in API response")

        for part in candidate.content.parts:
            if hasattr(part, 'inline_data') and part.inline_data:
                image_bytes = part.inline_data.data
                if isinstance(image_bytes, str):
                    image_bytes = base64.b64decode(image_bytes)

                pixbuf = self._bytes_to_pixbuf(image_bytes)
                if pixbuf:
                    return pixbuf, None

        return None, _("No image data found in response")

    def _validate_reference_image(
        self,
        img_path: str,
        max_size_mb: int = MAX_FILE_SIZE_MB
    ) -> Tuple[Optional[object], bool]:
        """
        Validate and load a reference image file

        Args:
            img_path (str): Path to the image file
            max_size_mb (int): Maximum file size in MB

        Returns:
            tuple: (image_part | None, success: bool)
        """
        if not types:
            print("Error: types module not found")
            return None, False

        try:
            file_size = os.path.getsize(img_path)
            if file_size > max_size_mb * 1024 * 1024:
                print(f"Warning: Image {img_path} is {file_size / (1024*1024):.1f} MB, exceeds {max_size_mb} MB limit. Skipping.")
                return None, False

            with open(img_path, 'rb') as img_file:
                image_data = img_file.read()

            mime_type, encoding = mimetypes.guess_type(img_path)
            if mime_type not in SUPPORTED_MIME_TYPES:
                print(f"Warning: Image {img_path} has unsupported MIME type {mime_type} with encoding {encoding}. Skipping.")
                return None, False

            image_part = types.Part(
                inline_data=types.Blob(
                    data=image_data,
                    mime_type=mime_type
                )
            )
            return image_part, True

        except Exception as e:
            print(f"Warning: Could not load reference image {img_path}: {e}")
            return None, False
