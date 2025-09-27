#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Qwen Image Edit Plus model implementation
Qwen's advanced image editing model with generation capabilities
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


class QwenImageEditModel(BaseModel):
    """Qwen Image Edit Plus model implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Qwen Image Edit Plus only supports editing, not generation"""
        return ModelCapability.EDIT

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.PNG

    @property
    def description(self) -> str:
        """Model description"""
        return _("Qwen's advanced image editing model")

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Qwen Image Edit Plus")

    @property
    def max_file_size_mb(self) -> int:
        """Maximum file size in MB for reference images"""
        return 10

    @property
    def max_reference_images(self) -> int:
        """Maximum number of reference images for generation"""
        return 9

    @property
    def max_reference_images_edit(self) -> int:
        """Maximum number of reference images for editing"""
        return 9

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "qwen/qwen-image-edit-plus"

    @property
    def supported_mime_types(self) -> List[str]:
        """List of supported MIME types for reference images"""
        return ["image/gif","image/png", "image/jpeg", "image/webp"]

    def build_edit_input(
        self, prompt: str, main_image,
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
        image = []
        if isinstance(main_image, bytes):
            image.append(io.BytesIO(main_image))
        else:
            image.append(main_image)

        if reference_images:
            image.extend(
                reference_images[:self.max_reference_images_edit]
            )

        params = self.build_parameters_dict(user_settings or {})

        for key, value in kwargs.items():
            if key in params:
                params[key] = value

        model_input = {
            "prompt": prompt,
            "image": image
        }

        if params.get("go_fast") is not None:
            model_input["go_fast"] = params["go_fast"]
        if params.get("seed", 0) != 0:
            model_input["seed"] = params["seed"]
        if params.get("output_format"):
            model_input["output_format"] = params["output_format"]
        if params.get("output_quality") and params.get("output_format") == "jpg":
            model_input["output_quality"] = params["output_quality"]
        if params.get("disable_safety_checker") is not None:
            model_input["disable_safety_checker"] = params["disable_safety_checker"]

        return {k: v for k, v in model_input.items() if v is not None}

    def build_generation_input(
        self, prompt: str,
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

        return {}

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """Get list of configurable parameters for Qwen Image Edit Plus"""
        return [
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="match_input_image",
                label=_("Aspect Ratio"),
                description=_("Control aspect ratio of generated images"),
                choices=["match_input_image", "1:1", "4:3", "3:4", "16:9", "9:16"],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="go_fast",
                param_type=ParameterType.BOOLEAN,
                default_value=True,
                label=_("Go Fast"),
                description=_("Enable speed optimizations"),
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="seed",
                param_type=ParameterType.INTEGER,
                default_value=0,
                label=_("Seed"),
                description=_("Random seed for reproducible results (0 = random)"),
                min_value=0,
                max_value=999999999,
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="output_format",
                param_type=ParameterType.CHOICE,
                default_value="png",
                label=_("Output Format"),
                description=_("Output image format"),
                choices=["jpg", "png", "webp"],
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="output_quality",
                param_type=ParameterType.INTEGER,
                default_value=95,
                label=_("Output Quality"),
                description=_("JPEG quality (0-100, ignored for PNG)"),
                min_value=0,
                max_value=100,
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="disable_safety_checker",
                param_type=ParameterType.BOOLEAN,
                default_value=True,
                label=_("Disable Safety Checker"),
                description=_("Bypass safety checks"),
                supported_modes=[ParameterMode.BOTH],
            ),
        ]


qwen_image_edit = QwenImageEditModel()
register_model(qwen_image_edit)
