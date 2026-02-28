#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nano Banana 2 (Google Gemini 3.1 Flash Image) model implementation
Google's fast image generation model with conversational editing,
multi-image fusion, and character consistency.
Available through Replicate API
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


class NanaBanana2Model(BaseModel):
    """Google's Nano Banana 2 model implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Nano Banana 2 supports editing and generation"""
        return ModelCapability.BOTH

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.JPEG

    @property
    def description(self) -> str:
        """Model description"""
        return _(
            "Google's fast image generation model with conversational "
            "editing, multi-image fusion, and character consistency"
        )

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Nano Banana 2 (Gemini 3.1 Flash Image)")

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
        return "google/nano-banana-2"

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
            "resolution": params.get("resolution", "1K"),
            "aspect_ratio": "match_input_image",
            "output_format": params.get("output_format", "jpg"),
            "google_search": params.get("google_search", False),
            "image_search": params.get("image_search", False),
        }

        return model_input

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
            "resolution": params.get("resolution", "1K"),
            "aspect_ratio": params.get("aspect_ratio", "1:1"),
            "output_format": params.get("output_format", "jpg"),
            "google_search": params.get("google_search", False),
            "image_search": params.get("image_search", False),
        }

        return model_input

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """Get list of configurable parameters for Nano Banana 2"""
        return [
            ParameterDefinition(
                name="resolution",
                param_type=ParameterType.CHOICE,
                default_value="1K",
                label=_("Resolution"),
                description=_(
                    "Resolution of the generated image. "
                    "Higher resolutions take longer to generate."
                ),
                choices=["1K", "2K", "4K"],
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="1:1",
                label=_("Aspect Ratio"),
                description=_("Aspect ratio of the generated image"),
                choices=[
                    "1:1",
                    "1:4",
                    "1:8",
                    "2:3",
                    "3:2",
                    "3:4",
                    "4:1",
                    "4:3",
                    "4:5",
                    "5:4",
                    "8:1",
                    "9:16",
                    "16:9",
                    "21:9",
                ],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="output_format",
                param_type=ParameterType.CHOICE,
                default_value="jpg",
                label=_("Output Format"),
                description=_("Format of the output image"),
                choices=["jpg", "png"],
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="google_search",
                param_type=ParameterType.BOOLEAN,
                default_value=False,
                label=_("Google Search"),
                description=_(
                    "Use Google Web Search grounding to generate images "
                    "based on real-time information"
                ),
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="image_search",
                param_type=ParameterType.BOOLEAN,
                default_value=False,
                label=_("Image Search"),
                description=_(
                    "Use Google Image Search grounding to find web images "
                    "as visual context for generation"
                ),
                supported_modes=[ParameterMode.BOTH],
            ),
        ]


nano_banana_2 = NanaBanana2Model()
register_model(nano_banana_2)