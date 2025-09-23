#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nano Banana (Google Gemini 2.5 Flash Image Preview) model implementation
Available through Replicate API
"""

import io
from typing import List, Dict, Any, Optional

from . import (BaseModel, OutputFormat, ParameterDefinition,
               ParameterType, register_model)
from i18n import _


class NanaBananaModel(BaseModel):
    """Google's Nano Banana model implementation for Replicate"""

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "google/nano-banana"

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Nano Banana (Gemini 2.5 Flash Image Preview)")

    @property
    def description(self) -> str:
        """Model description"""
        return _("Google's advanced image generation and editing model")

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
        return 7

    @property
    def supported_mime_types(self) -> List[str]:
        """List of supported MIME types for reference images"""
        return ['image/png', 'image/jpeg', 'image/webp']

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.PNG

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """Get list of configurable parameters for Nano Banana"""
        return [
            ParameterDefinition(
                name="output_format",
                param_type=ParameterType.CHOICE,
                default_value="png",
                label=_("Output Format"),
                description=_("Format for generated images"),
                choices=["png", "jpg"]
            )
        ]

    def build_generation_input(self, prompt: str,
                               reference_images: Optional[List] = None,
                               user_settings: Optional[Dict[str, Any]] = None,
                               **kwargs) -> Dict[str, Any]:
        """
        Build input dictionary for image generation

        Args:
            prompt: Text prompt for generation
            reference_images: Optional list of reference image file objects
            user_settings: User's saved settings for this model
            **kwargs: Additional parameters (override user_settings)

        Returns:
            Dictionary of input parameters for the Replicate API
        """
        params = self.build_parameters_dict(user_settings or {})

        for key, value in kwargs.items():
            if key in params:
                params[key] = value

        default_format = self.get_output_format_string(self.default_output_format)
        output_format = params.get("output_format", default_format)
        model_input = {
            "prompt": prompt,
            "image_input": reference_images or [],
            "output_format": output_format
        }

        return model_input

    def build_edit_input(self, prompt: str, main_image,
                         reference_images: Optional[List] = None,
                         user_settings: Optional[Dict[str, Any]] = None,
                         **kwargs) -> Dict[str, Any]:
        """
        Build input dictionary for image editing

        Args:
            prompt: Text prompt for editing
            main_image: Main image to edit (file object or bytes)
            reference_images: Optional list of reference image file objects
            user_settings: User's saved settings for this model
            **kwargs: Additional parameters (override user_settings)

        Returns:
            Dictionary of input parameters for the Replicate API
        """
        image_input = []

        if isinstance(main_image, bytes):
            image_input.append(io.BytesIO(main_image))
        else:
            image_input.append(main_image)

        if reference_images:
            image_input.extend(reference_images)

        params = self.build_parameters_dict(user_settings or {})

        for key, value in kwargs.items():
            if key in params:
                params[key] = value

        default_format = self.get_output_format_string(self.default_output_format)
        output_format = params.get("output_format", default_format)
        model_input = {
            "prompt": prompt,
            "image_input": image_input,
            "output_format": output_format
        }

        return model_input


nano_banana = NanaBananaModel()
register_model(nano_banana)
