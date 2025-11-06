#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Flux 1.1 Pro model implementation
Faster, better FLUX Pro. Text-to-image model with excellent image quality,
prompt adherence, and output diversity.
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


class FluxProModel(BaseModel):
    """Flux 1.1 Pro implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Flux 1.1 Pro supports image generation"""
        return ModelCapability.GENERATE

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.WEBP

    @property
    def description(self) -> str:
        """Model description"""
        return _("Text-to-image model with excellent image quality")

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Flux 1.1 Pro")

    @property
    def max_file_size_mb(self) -> int:
        """Maximum file size in MB for reference images"""
        return 10

    @property
    def max_reference_images(self) -> int:
        """Maximum number of reference images for generation"""
        return 1

    @property
    def max_reference_images_edit(self) -> int:
        """Maximum number of reference images for editing"""
        return 0

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "black-forest-labs/flux-1.1-pro"

    @property
    def supported_mime_types(self) -> List[str]:
        """List of supported MIME types for reference images"""
        return ["image/gif", "image/png", "image/jpeg", "image/webp"]

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
                (e.g., "Remove the boy in this picture")
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

        model_input = {
            "prompt": prompt,
            "aspect_ratio": params["aspect_ratio"],
            "width": params["width"],
            "height": params["height"],
            "safety_tolerance": params["safety_tolerance"],
            "prompt_upsampling": params["prompt_upsampling"],
            "output_format": params["output_format"],
            "output_quality": params["output_quality"],
        }

        if params.get("seed", -1) != -1:
            model_input["seed"] = params["seed"]

        if reference_images and len(reference_images) > 0:
            model_input["image_input"] = reference_images[0]

        return {k: v for k, v in model_input.items() if v is not None}

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """Get list of configurable parameters for Flux 1.1 Pro"""
        return [
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="1:1",
                label=_("Aspect Ratio"),
                description=_("Aspect ratio for the generated image"),
                choices=[
                    "custom",
                    "1:1",
                    "16:9",
                    "3:2",
                    "2:3",
                    "4:5",
                    "5:4",
                    "9:16",
                    "3:4",
                    "4:3",
                ],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="width",
                param_type=ParameterType.INTEGER,
                default_value=1440,
                label=_("Width"),
                description=_(
                    "Width of the generated image in text-to-image mode."
                ),
                min_value=256,
                max_value=1440,
                step=32,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="height",
                param_type=ParameterType.INTEGER,
                default_value=1440,
                label=_("Height"),
                description=_(
                    "Height of the generated image in text-to-image mode."
                ),
                min_value=256,
                max_value=1440,
                step=32,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="safety_tolerance",
                param_type=ParameterType.INTEGER,
                default_value=2,
                label=_("Safety Tolerance"),
                description=_(
                    "Safety tolerance, 1 is most strict and 6 is most "
                    "permissive"
                ),
                min_value=1,
                max_value=6,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="seed",
                param_type=ParameterType.INTEGER,
                default_value=-1,
                label=_("Seed"),
                description=_("Set a seed for reproducibility (-1 = random)"),
                step=1,
                min_value=-1,
                max_value=999999999,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="prompt_upsampling",
                param_type=ParameterType.BOOLEAN,
                default_value=False,
                label=_("Prompt Upsampling"),
                description=_(
                    "Automatically modify the prompt for more creative "
                    "generation"
                ),
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="output_format",
                param_type=ParameterType.CHOICE,
                default_value="webp",
                label=_("Output Format"),
                description=_("Format of the output images."),
                choices=["png", "jpg", "webp"],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="output_quality",
                param_type=ParameterType.INTEGER,
                default_value=80,
                label=_("Output Quality"),
                description=_("Quality when saving the output image"),
                min_value=0,
                max_value=100,
                supported_modes=[ParameterMode.GENERATE],
            ),
        ]


flux_pro = FluxProModel()
register_model(flux_pro)
