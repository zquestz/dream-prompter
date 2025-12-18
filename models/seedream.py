#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Seedream 4.5 model implementation
ByteDance's upgraded image model with stronger spatial understanding
and world knowledge. Available through Replicate API
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


class SeedreamModel(BaseModel):
    """ByteDance Seedream 4.5 model implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Seedream 4.5 supports editing and generation"""
        return ModelCapability.BOTH

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.PNG

    @property
    def description(self) -> str:
        """Model description"""
        return _(
            "ByteDance's upgraded model with stronger spatial understanding"
        )

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Seedream 4.5")

    @property
    def max_file_size_mb(self) -> int:
        """Maximum file size in MB for reference images"""
        return 10

    @property
    def max_reference_images(self) -> int:
        """Maximum number of reference images for generation"""
        return 14

    @property
    def max_reference_images_edit(self) -> int:
        """Maximum number of reference images for editing"""
        return 13

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "bytedance/seedream-4.5"

    @property
    def supported_mime_types(self) -> List[str]:
        """List of supported MIME types for reference images"""
        return ["image/png", "image/jpeg", "image/webp"]

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
        image_input = []
        if isinstance(main_image, bytes):
            image_input.append(io.BytesIO(main_image))
        else:
            image_input.append(main_image)

        if reference_images:
            image_input.extend(
                reference_images[: self.max_reference_images_edit]
            )

        params = self.build_parameters_dict(user_settings or {})

        for key, value in kwargs.items():
            if key in params:
                params[key] = value

        model_input = {
            "prompt": prompt,
            "image_input": image_input,
            "size": params["size"],
            "aspect_ratio": "match_input_image",
            "width": params["width"],
            "height": params["height"],
            "sequential_image_generation": (
                params["sequential_image_generation"]
            ),
            "max_images": params["max_images"],
        }

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
            "image_input": reference_images or [],
            "size": params["size"],
            "aspect_ratio": params["aspect_ratio"],
            "width": params["width"],
            "height": params["height"],
            "sequential_image_generation": (
                params["sequential_image_generation"]
            ),
            "max_images": params["max_images"],
        }

        return {k: v for k, v in model_input.items() if v is not None}

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """Get list of configurable parameters for Seedream 4.5"""
        return [
            ParameterDefinition(
                name="size",
                param_type=ParameterType.CHOICE,
                default_value="2K",
                label=_("Image Size"),
                description=_(
                    "Resolution preset: 2K (2048px), 4K (4096px), or custom"
                ),
                choices=["2K", "4K", "custom"],
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="width",
                param_type=ParameterType.INTEGER,
                default_value=2048,
                label=_("Width"),
                description=_(
                    "Custom width in pixels (only used when size='custom')"
                ),
                min_value=1024,
                max_value=4096,
                step=1,
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="height",
                param_type=ParameterType.INTEGER,
                default_value=2048,
                label=_("Height"),
                description=_(
                    "Custom height in pixels (only used when size='custom')"
                ),
                min_value=1024,
                max_value=4096,
                step=1,
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="match_input_image",
                label=_("Aspect Ratio"),
                description=_("Control aspect ratio of generated images"),
                choices=[
                    "match_input_image",
                    "1:1",
                    "4:3",
                    "3:4",
                    "16:9",
                    "9:16",
                    "3:2",
                    "2:3",
                    "21:9",
                ],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="max_images",
                param_type=ParameterType.INTEGER,
                default_value=1,
                label=_("Max Images"),
                description=_("Maximum number of images to generate"),
                min_value=1,
                max_value=15,
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="sequential_image_generation",
                param_type=ParameterType.CHOICE,
                default_value="disabled",
                label=_("Sequential Generation"),
                description=_("Generate images sequentially or in parallel"),
                choices=["disabled", "auto"],
                supported_modes=[ParameterMode.BOTH],
            ),
        ]


seedream = SeedreamModel()
register_model(seedream)
