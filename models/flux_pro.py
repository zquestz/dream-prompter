#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Flux 2 Pro model implementation
High-quality image generation and editing with support for
eight reference images. Available through Replicate API
"""

import io
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
    """Flux 2 Pro implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Flux 2 Pro supports both generation and editing"""
        return ModelCapability.BOTH

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.WEBP

    @property
    def description(self) -> str:
        """Model description"""
        return _("High-quality image generation and editing model")

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Flux 2 Pro")

    @property
    def max_file_size_mb(self) -> int:
        """Maximum file size in MB for reference images"""
        return 10

    @property
    def max_reference_images(self) -> int:
        """Maximum number of reference images for generation"""
        return 8

    @property
    def max_reference_images_edit(self) -> int:
        """Maximum number of reference images for editing"""
        return 7

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "black-forest-labs/flux-2-pro"

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
                (e.g., "Replace the background with a beach")
            main_image: Main image to edit (file object or bytes)
            reference_images: Optional list of reference image file objects
            user_settings: User's saved settings for this model
            **kwargs: Additional parameters (override user_settings)

        Returns:
            Dictionary of input parameters for the Replicate API
        """
        input_images = []

        if isinstance(main_image, bytes):
            input_images.append(io.BytesIO(main_image))
        else:
            input_images.append(main_image)

        if reference_images:
            input_images.extend(
                reference_images[: self.max_reference_images_edit]
            )

        params = self.build_parameters_dict(user_settings or {})

        for key, value in kwargs.items():
            if key in params:
                params[key] = value

        model_input = {
            "prompt": prompt,
            "input_images": input_images,
            "aspect_ratio": "match_input_image",
            "resolution": params["resolution"],
            "safety_tolerance": params["safety_tolerance"],
            "output_format": params["output_format"],
            "output_quality": params["output_quality"],
        }

        if params.get("seed", -1) != -1:
            model_input["seed"] = params["seed"]

        return {k: v for k, v in model_input.items() if v is not None}

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
            "resolution": params["resolution"],
            "width": params["width"],
            "height": params["height"],
            "safety_tolerance": params["safety_tolerance"],
            "output_format": params["output_format"],
            "output_quality": params["output_quality"],
        }

        if params.get("seed", -1) != -1:
            model_input["seed"] = params["seed"]

        if reference_images and len(reference_images) > 0:
            model_input["input_images"] = reference_images

        return {k: v for k, v in model_input.items() if v is not None}

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """Get list of configurable parameters for Flux 2 Pro"""
        return [
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="1:1",
                label=_("Aspect Ratio"),
                description=_("Aspect ratio for the generated image"),
                choices=[
                    "match_input_image",
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
                name="resolution",
                param_type=ParameterType.CHOICE,
                default_value="1 MP",
                label=_("Resolution"),
                description=_(
                    "Resolution in megapixels. Up to 4 MP is possible, "
                    "but 2 MP or below is recommended."
                ),
                choices=[
                    "match_input_image",
                    "0.5 MP",
                    "1 MP",
                    "2 MP",
                    "4 MP",
                ],
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="width",
                param_type=ParameterType.INTEGER,
                default_value=1024,
                label=_("Width"),
                description=_(
                    "Width of the generated image. Only used when "
                    "aspect_ratio=custom. Must be a multiple of 32."
                ),
                min_value=256,
                max_value=2048,
                step=32,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="height",
                param_type=ParameterType.INTEGER,
                default_value=1024,
                label=_("Height"),
                description=_(
                    "Height of the generated image. Only used when "
                    "aspect_ratio=custom. Must be a multiple of 32."
                ),
                min_value=256,
                max_value=2048,
                step=32,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="safety_tolerance",
                param_type=ParameterType.INTEGER,
                default_value=2,
                label=_("Safety Tolerance"),
                description=_(
                    "Safety tolerance, 1 is most strict and 5 is most "
                    "permissive"
                ),
                min_value=1,
                max_value=5,
                supported_modes=[ParameterMode.BOTH],
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
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="output_format",
                param_type=ParameterType.CHOICE,
                default_value="webp",
                label=_("Output Format"),
                description=_("Format of the output images."),
                choices=["png", "jpg", "webp"],
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="output_quality",
                param_type=ParameterType.INTEGER,
                default_value=80,
                label=_("Output Quality"),
                description=_("Quality when saving the output image"),
                min_value=0,
                max_value=100,
                supported_modes=[ParameterMode.BOTH],
            ),
        ]


flux_pro = FluxProModel()
register_model(flux_pro)
