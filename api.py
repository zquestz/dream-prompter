#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Google AI image generation integration for Dream Prompter plugin
Real Gemini API implementation using modern google-genai library
"""

import base64
import integrator
import mimetypes
import os

from gi.repository import GdkPixbuf
from i18n import _

MAX_FILE_SIZE_MB = 7
MAX_REFERENCE_IMAGES_GENERATE = 3
MAX_REFERENCE_IMAGES_EDIT = 2
SUPPORTED_MIME_TYPES = ['image/png', 'image/jpeg', 'image/webp']

try:
    from google import genai
    from google.genai import types, errors
except ImportError:
    genai = None
    types = None
    errors = None
    print("Warning: google-genai not installed. Install with: pip install google-genai")

class GeminiAPI:
    """Google AI client for image generation and editing"""

    def __init__(self, api_key):
        """
        Initialize the Gemini API client

        Args:
            api_key (str): Google Gemini API key for authentication
        """
        self.api_key = api_key
        if genai:
            self.client = genai.Client(api_key=api_key)
        else:
            self.client = None

    def generate_image(self, prompt, reference_images=None, progress_callback=None):
        """
        Generate a new image from a text prompt using Nano Banana

        Args:
            prompt (str): Text description of the image to generate
            reference_images (list): Optional list of image file paths for reference (max 3)
            progress_callback (callable): Optional callback for progress updates

        Returns:
            tuple: (GdkPixbuf.Pixbuf or None, error_message or None)
        """
        if not self.client or not types or not errors:
            return None, _("Nano Banana API not available. Please install google-genai")

        if progress_callback:
            progress_callback(_("Generating image with Nano Banana..."), 0.1)

        try:
            contents = [prompt]
            self._add_reference_images(contents, reference_images, max_count=MAX_REFERENCE_IMAGES_GENERATE)

            if progress_callback:
                progress_callback(_("Sending request to Nano Banana..."), 0.5)

            response = self.client.models.generate_content(
                model='gemini-2.5-flash-image-preview',
                contents=contents
            )

            if progress_callback:
                progress_callback(_("Processing Nano Banana response..."), 0.9)

            pixbuf, error_msg = self._parse_image_response(response)
            return pixbuf, error_msg

        except errors.APIError as e:
            return None, e.message
        except Exception as e:
            return None, str(e)

    def edit_image(self, image, prompt, reference_images=None, progress_callback=None):
        """
        Edit an image from a text prompt using Nano Banana

        Args:
            image (Gimp.Image): Image to edit
            prompt (str): Text description of the edits to make
            reference_images (list): Optional list of image file paths for reference (max 2)
            progress_callback (callable): Optional callback for progress updates

        Returns:
            tuple: (GdkPixbuf.Pixbuf or None, error_message or None)
        """
        if not self.client or not types or not errors:
            return None, _("Nano Banana API not available. Please install google-genai")

        if not image:
            return None, _("No GIMP image provided for editing")

        if progress_callback:
            progress_callback(_("Preparing current image for Nano Banana..."), 0.1)

        try:
            current_image_data = integrator.export_gimp_image_to_bytes(image)
            if not current_image_data:
                return None, _("Failed to export current image")

            if progress_callback:
                progress_callback(_("Building Nano Banana edit request..."), 0.3)

            contents = []
            current_image_part = types.Part.from_bytes(
                data=current_image_data,
                mime_type='image/png'
            )
            contents.append(current_image_part)
            contents.append(prompt)

            self._add_reference_images(contents, reference_images, max_count=MAX_REFERENCE_IMAGES_EDIT)

            if progress_callback:
                progress_callback(_("Sending edit request to Nano Banana..."), 0.5)

            response = self.client.models.generate_content(
                model='gemini-2.5-flash-image-preview',
                contents=contents
            )

            if progress_callback:
                progress_callback(_("Processing Nano Banana edit response..."), 0.9)

            pixbuf, error_msg = self._parse_image_response(response)
            return pixbuf, error_msg
        except errors.APIError as e:
            return None, e.message
        except Exception as e:
            return None, str(e)

    def _validate_reference_image(self, img_path, max_size_mb=MAX_FILE_SIZE_MB):
        """
        Validate and load a reference image file

        Args:
            img_path (str): Path to the image file
            max_size_mb (int): Maximum file size in MB

        Returns:
            tuple: (image_part, success) where image_part is types.Part or None
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

            image_part = types.Part.from_bytes(data=image_data, mime_type=mime_type)
            return image_part, True

        except Exception as e:
            print(f"Warning: Could not load reference image {img_path}: {e}")
            return None, False

    def _add_reference_images(self, contents, reference_images, max_count):
        """
        Add reference images to the content list

        Args:
            contents (list): List to append image parts to
            reference_images (list): List of image file paths
            max_count (int): Maximum number of images to add
        """
        if not reference_images or not types:
            return

        for img_path in reference_images[:max_count]:
            image_part, success = self._validate_reference_image(img_path)
            if success and image_part:
                contents.append(image_part)

    def _parse_image_response(self, response):
        """
        Parse the API response and extract the generated image

        Args:
            response: API response object

        Returns:
            tuple: (GdkPixbuf.Pixbuf or None, error_message or None)
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

                try:
                    loader = GdkPixbuf.PixbufLoader()
                    loader.write(image_bytes)
                    loader.close()
                    pixbuf = loader.get_pixbuf()

                    if pixbuf:
                        return pixbuf, None
                except Exception as e:
                    return None, _("Error converting image data to pixbuf: {error}").format(error=str(e))

        return None, _("No image data found in response")
