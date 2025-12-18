#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Stable Diffusion 3.5 Large Turbo model implementation
A text-to-image model that generates high-resolution images
with fine details. It supports various artistic styles and
produces diverse outputs from the same prompt, with a focus
on fewer inference steps
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


class StableDiffusionLargeTurbo(BaseModel):
    """Stable Diffusion 3.5 Large Turbo model implementation"""

    @property
    def capabilities(self) -> ModelCapability:
        """Stable Diffusion 3.5 Large Turbo supports editing and generation"""
        return ModelCapability.BOTH

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.WEBP

    @property
    def description(self) -> str:
        """Model description"""
        return _("Stability AI's high-resolution image generation model")

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Stable Diffusion 3.5 Large Turbo")

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
        return "stability-ai/stable-diffusion-3.5-large-turbo"

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
        image = ""
        if isinstance(main_image, bytes):
            image = io.BytesIO(main_image)
        else:
            image = main_image

        params = self.build_parameters_dict(user_settings or {})

        for key, value in kwargs.items():
            if key in params:
                params[key] = value

        model_input = {
            "prompt": prompt,
            "negative_prompt": params["negative_prompt"],
            "aspect_ratio": params["aspect_ratio"],
            "cfg": params["cfg"],
            "image": image,
            "prompt_strength": params["prompt_strength"],
            "seed": params["seed"],
            "output_format": params["output_format"],
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
            "negative_prompt": params["negative_prompt"],
            "aspect_ratio": params["aspect_ratio"],
            "cfg": params["cfg"],
            "prompt_strength": params["prompt_strength"],
            "output_format": params["output_format"],
        }

        if params.get("seed", -1) != -1:
            model_input["seed"] = params["seed"]

        if reference_images:
            model_input["image"] = reference_images[0]

        return {k: v for k, v in model_input.items() if v is not None}

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """Get list of configurable parameters for Stable Diffusion 3.5"""
        return [
            ParameterDefinition(
                name="negative_prompt",
                param_type=ParameterType.STRING,
                default_value="",
                label=_("Negative Prompt"),
                description=_("What you do not want to see in the image"),
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="1:1",
                label=_("Aspect Ratio"),
                description=_("Control aspect ratio of generated images"),
                choices=[
                    "16:9",
                    "1:1",
                    "21:9",
                    "2:3",
                    "3:2",
                    "4:5",
                    "5:4",
                    "9:16",
                    "9:21",
                ],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="cfg",
                param_type=ParameterType.FLOAT,
                default_value=1,
                label=_("Cfg"),
                description=_("How similar the output should be to the prompt"),
                min_value=1,
                max_value=10,
                step=0.1,
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="prompt_strength",
                param_type=ParameterType.FLOAT,
                default_value=0.85,
                label=_("Prompt Strength"),
                description=_("Prompt strength (or denoising strength)"),
                min_value=0,
                max_value=1,
                step=0.01,
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
                description=_("Format of the output images"),
                choices=["webp", "jpg", "png"],
                supported_modes=[ParameterMode.BOTH],
            ),
        ]


stable_diffusion_large_turbo = StableDiffusionLargeTurbo()
register_model(stable_diffusion_large_turbo)
