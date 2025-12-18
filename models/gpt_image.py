#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GPT Image 1.5 model implementation
OpenAI's image generation model
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


class GPTImageModel(BaseModel):
    """OpenAI's GPT Image 1.5 model implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """GPT Image 1.5 supports generation only"""
        return ModelCapability.GENERATE

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.WEBP

    @property
    def description(self) -> str:
        """Model description"""
        return _("OpenAI's advanced image generation model")

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("GPT Image 1.5")

    @property
    def max_file_size_mb(self) -> int:
        """Maximum file size in MB for reference images"""
        return 10

    @property
    def max_reference_images(self) -> int:
        """Maximum number of reference images for generation"""
        return 10

    @property
    def max_reference_images_edit(self) -> int:
        """Maximum number of reference images for editing"""
        return 0

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "openai/gpt-image-1.5"

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

        This model does not support editing.
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
            "aspect_ratio": params.get("aspect_ratio", "1:1"),
            "input_fidelity": params.get("input_fidelity", "low"),
            "number_of_images": params.get("number_of_images", 1),
            "quality": params.get("quality", "auto"),
            "background": params.get("background", "auto"),
            "output_compression": params.get("output_compression", 90),
            "output_format": params.get("output_format", "webp"),
            "moderation": params.get("moderation", "auto"),
        }

        if params.get("openai_api_key"):
            model_input["openai_api_key"] = params["openai_api_key"]

        if reference_images and len(reference_images) > 0:
            model_input["input_images"] = reference_images

        return {k: v for k, v in model_input.items() if v is not None}

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """Get list of configurable parameters for GPT Image 1.5"""
        return [
            ParameterDefinition(
                name="openai_api_key",
                param_type=ParameterType.STRING,
                default_value="",
                label=_("OpenAI API Key"),
                description=_(
                    "Your OpenAI API key (optional - uses proxy if not "
                    "provided)"
                ),
                supported_modes=[ParameterMode.GENERATE],
                is_secret=True,
            ),
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="1:1",
                label=_("Aspect Ratio"),
                description=_("The aspect ratio of the generated image"),
                choices=["1:1", "3:2", "2:3"],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="input_fidelity",
                param_type=ParameterType.CHOICE,
                default_value="low",
                label=_("Input Fidelity"),
                description=_(
                    "Control how much effort the model will exert to match "
                    "the style and features of input images"
                ),
                choices=["low", "high"],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="number_of_images",
                param_type=ParameterType.INTEGER,
                default_value=1,
                label=_("Number of Images"),
                description=_("Number of images to generate (1-10)"),
                min_value=1,
                max_value=10,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="quality",
                param_type=ParameterType.CHOICE,
                default_value="auto",
                label=_("Quality"),
                description=_("The quality of the generated image"),
                choices=["low", "medium", "high", "auto"],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="background",
                param_type=ParameterType.CHOICE,
                default_value="auto",
                label=_("Background"),
                description=_(
                    "Set whether the background is transparent or opaque"
                ),
                choices=["auto", "transparent", "opaque"],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="output_compression",
                param_type=ParameterType.INTEGER,
                default_value=90,
                label=_("Output Compression"),
                description=_("Compression level (0-100%)"),
                min_value=0,
                max_value=100,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="output_format",
                param_type=ParameterType.CHOICE,
                default_value="webp",
                label=_("Output Format"),
                description=_("Format of the output image"),
                choices=["png", "jpeg", "webp"],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="moderation",
                param_type=ParameterType.CHOICE,
                default_value="auto",
                label=_("Moderation"),
                description=_("Content moderation level"),
                choices=["auto", "low"],
                supported_modes=[ParameterMode.GENERATE],
            ),
        ]


gpt_image = GPTImageModel()
register_model(gpt_image)
