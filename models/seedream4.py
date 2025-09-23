#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Seedream 4 model implementation
ByteDance's unified text-to-image generation and editing model
Available through Replicate API
"""

import io
from typing import List, Dict, Any, Optional

from . import BaseModel, OutputFormat, register_model
from i18n import _

class Seedream4Model(BaseModel):
    """ByteDance Seedream 4 model implementation for Replicate"""

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "bytedance/seedream-4"

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Seedream 4")

    @property
    def description(self) -> str:
        """Model description"""
        return _("ByteDance's unified generation and editing model")

    @property
    def max_reference_images(self) -> int:
        """Maximum number of reference images for generation"""
        return 10

    @property
    def max_reference_images_edit(self) -> int:
        """Maximum number of reference images for editing"""
        return 9

    @property
    def max_file_size_mb(self) -> int:
        """Maximum file size in MB for reference images"""
        return 10

    @property
    def supported_mime_types(self) -> List[str]:
        """List of supported MIME types for reference images"""
        return ['image/png', 'image/jpeg', 'image/webp']

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.PNG

    def build_generation_input(self, prompt: str, reference_images: Optional[List] = None, **kwargs) -> Dict[str, Any]:
        """
        Build input dictionary for image generation

        Args:
            prompt: Text prompt for generation
            reference_images: Optional list of reference image file objects
            **kwargs: Additional parameters like size, aspect_ratio, max_images

        Returns:
            Dictionary of input parameters for the Replicate API
        """
        model_input = {
            "prompt": prompt,
            "size": kwargs.get("size", "2K"),
            "width": kwargs.get("width", 2048),
            "height": kwargs.get("height", 2048),
            "aspect_ratio": kwargs.get("aspect_ratio", "1:1"),
            "max_images": kwargs.get("max_images", 5),
            "sequential_image_generation": kwargs.get("sequential_image_generation", "auto"),
            "image_input": reference_images or []
        }

        return {k: v for k, v in model_input.items() if v is not None}

    def build_edit_input(self, prompt: str, main_image, reference_images: Optional[List] = None, **kwargs) -> Dict[str, Any]:
        """
        Build input dictionary for image editing

        Args:
            prompt: Text prompt for editing (e.g., "Remove the boy in this picture")
            main_image: Main image to edit (file object or bytes)
            reference_images: Optional list of reference image file objects
            **kwargs: Additional parameters

        Returns:
            Dictionary of input parameters for the Replicate API
        """
        image_input = []
        if isinstance(main_image, bytes):
            image_input.append(io.BytesIO(main_image))
        else:
            image_input.append(main_image)

        if reference_images:
            image_input.extend(reference_images[:self.max_reference_images_edit])

        model_input = {
            "prompt": prompt,
            "size": kwargs.get("size", "2K"),
            "width": kwargs.get("width", 2048),
            "height": kwargs.get("height", 2048),
            "aspect_ratio": kwargs.get("aspect_ratio", "1:1"),
            "max_images": kwargs.get("max_images", 1),
            "sequential_image_generation": kwargs.get("sequential_image_generation", "disabled"),
            "image_input": image_input
        }

        return {k: v for k, v in model_input.items() if v is not None}

    def validate_reference_image_count(self, count: int, is_edit: bool = False) -> bool:
        """
        Validate reference image count for Seedream 4

        Args:
            count: Number of reference images
            is_edit: Whether this is for editing (vs generation)

        Returns:
            True if count is valid, False otherwise
        """
        max_count = self.max_reference_images_edit if is_edit else self.max_reference_images
        return 0 <= count <= max_count

seedream4 = Seedream4Model()
register_model(seedream4)
