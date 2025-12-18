#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Imagen 4 model implementation
Available through Replicate API
"""

from typing import List, Dict, Any, Optional

from . import (
    BaseModel,
    ModelCapability,
    OutputFormat,
    ParameterDefinition,
    ParameterType,
    ParameterMode,
    register_model,
)
from i18n import _


class ImagenModel(BaseModel):
    """Google's Imagen 4 model implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Imagen 4 only supports generation"""
        return ModelCapability.GENERATE

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.JPEG

    @property
    def description(self) -> str:
        """Model description"""
        return _("Google's advanced image generation model")

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Imagen 4")

    @property
    def max_file_size_mb(self) -> int:
        """Maximum file size in MB for reference images"""
        return 7

    @property
    def max_reference_images(self) -> int:
        """Maximum number of reference images for generation"""
        return 0

    @property
    def max_reference_images_edit(self) -> int:
        """Maximum number of reference images for editing"""
        return 0

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "google/imagen-4"

    @property
    def supported_mime_types(self) -> List[str]:
        """List of supported MIME types for reference images"""
        return []

    def build_edit_input(
        self,
        prompt: str,
        main_image,
        reference_images: Optional[List] = None,
        user_settings: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
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

        return {}

    def build_generation_input(
        self,
        prompt: str,
        reference_images: Optional[List] = None,
        user_settings: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
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

        default_format = self.get_output_format_string(
            self.default_output_format
        )
        output_format = params.get("output_format", default_format)
        aspect_ratio = params.get("aspect_ratio", "1:1")
        safety_filter_level = params.get(
            "safety_filter_level", "block_only_high"
        )
        model_input = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "safety_filter_level": safety_filter_level,
            "output_format": output_format,
        }

        return model_input

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """Get list of configurable parameters for Imagen 4"""
        return [
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="1:1",
                label=_("Aspect Ratio"),
                description=_("Control aspect ratio of generated images"),
                choices=["1:1", "9:16", "16:9", "3:4", "4:3"],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="output_format",
                param_type=ParameterType.CHOICE,
                default_value="jpg",
                label=_("Output Format"),
                description=_("Format of the output image"),
                choices=["jpg", "png"],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="safety_filter_level",
                param_type=ParameterType.CHOICE,
                default_value="block_only_high",
                label=_("Safety Filter Level"),
                description=_("Control safety of generated images"),
                choices=[
                    "block_low_and_above",
                    "block_medium_and_above",
                    "block_only_high",
                ],
                supported_modes=[ParameterMode.GENERATE],
            ),
        ]


imagen = ImagenModel()
register_model(imagen)
