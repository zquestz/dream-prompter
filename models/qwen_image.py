#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Qwen Image model implementation
Qwen's advanced image generation model
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


class QwenImageModel(BaseModel):
    """Qwen Image model implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Qwen Image supports generation only"""
        return ModelCapability.GENERATE

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.WEBP

    @property
    def description(self) -> str:
        """Model description"""
        return _("Qwen's advanced image generation model")

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Qwen Image")

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
        return "qwen/qwen-image"

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
            "aspect_ratio": params.get("aspect_ratio", "16:9"),
            "image_size": params.get("image_size", "optimize_for_quality"),
            "guidance": params.get("guidance", 3),
            "num_inference_steps": params.get("num_inference_steps", 30),
            "go_fast": params.get("go_fast", True),
            "enhance_prompt": params.get("enhance_prompt", False),
            "negative_prompt": params.get("negative_prompt", " "),
            "output_format": params.get("output_format", "webp"),
            "output_quality": params.get("output_quality", 80),
            "disable_safety_checker": params.get(
                "disable_safety_checker", False
            ),
        }

        if params.get("seed", -1) != -1:
            model_input["seed"] = params["seed"]

        if reference_images and len(reference_images) > 0:
            model_input["image"] = reference_images[0]
            model_input["strength"] = params.get("strength", 0.9)

        return {k: v for k, v in model_input.items() if v is not None}

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """Get list of configurable parameters for Qwen Image"""
        return [
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="16:9",
                label=_("Aspect Ratio"),
                description=_("Aspect ratio for the generated image"),
                choices=[
                    "1:1",
                    "16:9",
                    "9:16",
                    "4:3",
                    "3:4",
                    "3:2",
                    "2:3",
                ],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="image_size",
                param_type=ParameterType.CHOICE,
                default_value="optimize_for_quality",
                label=_("Image Size"),
                description=_("Image size optimization mode"),
                choices=["optimize_for_quality", "optimize_for_speed"],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="guidance",
                param_type=ParameterType.FLOAT,
                default_value=3,
                label=_("Guidance"),
                description=_(
                    "Guidance scale. Lower values give more realistic images. "
                    "Good values: 2, 2.5, 3, 3.5"
                ),
                min_value=0,
                max_value=10,
                step=0.5,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="num_inference_steps",
                param_type=ParameterType.INTEGER,
                default_value=30,
                label=_("Inference Steps"),
                description=_(
                    "Number of denoising steps. "
                    "Recommended range is 28-50."
                ),
                min_value=1,
                max_value=50,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="strength",
                param_type=ParameterType.FLOAT,
                default_value=0.9,
                label=_("Strength"),
                description=_(
                    "Strength for img2img (only used with reference image)"
                ),
                min_value=0,
                max_value=1,
                step=0.05,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="go_fast",
                param_type=ParameterType.BOOLEAN,
                default_value=True,
                label=_("Go Fast"),
                description=_(
                    "Run faster predictions with additional optimizations."
                ),
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="enhance_prompt",
                param_type=ParameterType.BOOLEAN,
                default_value=False,
                label=_("Enhance Prompt"),
                description=_("Enhance the prompt with positive magic."),
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="negative_prompt",
                param_type=ParameterType.STRING,
                default_value="",
                label=_("Negative Prompt"),
                description=_("Negative prompt for generated image"),
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
                name="output_format",
                param_type=ParameterType.CHOICE,
                default_value="webp",
                label=_("Output Format"),
                description=_("Format of the output images"),
                choices=["webp", "jpg", "png"],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="output_quality",
                param_type=ParameterType.INTEGER,
                default_value=80,
                label=_("Output Quality"),
                description=_(
                    "Quality when saving the output images, from 0 to 100. "
                    "Not relevant for .png outputs"
                ),
                min_value=0,
                max_value=100,
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="disable_safety_checker",
                param_type=ParameterType.BOOLEAN,
                default_value=False,
                label=_("Disable Safety Checker"),
                description=_("Disable safety checker for generated images."),
                supported_modes=[ParameterMode.GENERATE],
            ),
        ]


qwen_image = QwenImageModel()
register_model(qwen_image)
