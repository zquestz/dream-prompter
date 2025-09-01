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

try:
    from google import genai
    from google.genai import types
except ImportError:
    genai = None
    types = None
    print("Warning: google-genai not installed. Install with: pip install google-genai")

class GeminiAPI:
    """Google AI client for image generation and editing"""

    def __init__(self, api_key):
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
            GdkPixbuf.Pixbuf: Generated image as pixbuf, or None if failed
        """
        if not self.client or not types:
            print("Error: Nano Banana API not available. Please install google-genai")
            return None

        if progress_callback:
            progress_callback(_("Generating image with Nano Banana..."))

        try:
            contents = [prompt]
            self._add_reference_images(contents, reference_images, max_count=3)

            if progress_callback:
                progress_callback(_("Sending request to Nano Banana..."))

            response = self.client.models.generate_content(
                model='gemini-2.5-flash-image-preview',
                contents=contents
            )

            if progress_callback:
                progress_callback(_("Processing Nano Banana response..."))

            pixbuf = self._parse_image_response(response)
            if not pixbuf:
                print("Error: No image found in Nano Banana response")

            return pixbuf

        except Exception as e:
            print(f"Error generating image with Nano Banana: {e}")
            return None

    def edit_image(self, image, prompt, reference_images=None, progress_callback=None):
        """
        Edit an image from a text prompt using Nano Banana

        Args:
            image (Gimp.Image): Image to edit
            prompt (str): Text description of the edits to make
            reference_images (list): Optional list of image file paths for reference (max 2)
            progress_callback (callable): Optional callback for progress updates

        Returns:
            GdkPixbuf.Pixbuf: Edited image as pixbuf, or None if failed
        """
        if not self.client or not types:
            print("Error: Nano Banana API not available. Please install google-genai")
            return None

        if not image:
            print("Error: No GIMP image provided for editing")
            return None

        if progress_callback:
            progress_callback(_("Preparing current image for Nano Banana..."))

        try:
            current_image_data = integrator.export_gimp_image_to_bytes(image)
            if not current_image_data:
                print("Error: Failed to export current image")
                return None

            if progress_callback:
                progress_callback(_("Building Nano Banana edit request..."))

            contents = []
            current_image_part = types.Part.from_bytes(
                data=current_image_data,
                mime_type='image/png'
            )
            contents.append(current_image_part)
            contents.append(prompt)

            self._add_reference_images(contents, reference_images, max_count=2)

            if progress_callback:
                progress_callback(_("Sending edit request to Nano Banana..."))

            response = self.client.models.generate_content(
                model='gemini-2.5-flash-image-preview',
                contents=contents
            )

            if progress_callback:
                progress_callback(_("Processing Nano Banana edit response..."))

            pixbuf = self._parse_image_response(response)
            if not pixbuf:
                print("Error: No edited image found in Nano Banana response")

            return pixbuf

        except Exception as e:
            print(f"Error editing image with Nano Banana: {e}")
            return None

    def _validate_reference_image(self, img_path, max_size_mb=7):
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

            mime_type, _encoding = mimetypes.guess_type(img_path)
            if mime_type not in ['image/png', 'image/jpeg', 'image/webp']:
                print(f"Warning: Image {img_path} has unsupported MIME type {mime_type}. Skipping.")
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
            GdkPixbuf.Pixbuf: Generated image as pixbuf, or None if failed
        """
        if not response.candidates or len(response.candidates) == 0:
            print("Error: No candidates in API response")
            return None

        candidate = response.candidates[0]
        if not candidate.content or not candidate.content.parts:
            print("Error: No content parts in API response")
            return None

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
                        return pixbuf
                except Exception as e:
                    print(f"Error converting image data to pixbuf: {e}")

        return None
