"""
Nano Banana (Google Gemini 2.5 Flash Image) model implementation
Google's state-of-the-art image generation and editing model designed for
fast, conversational, and multi-turn creative workflows.
Available through Replicate API
"""

import io
from typing import Any

from i18n import _

from . import (
    BaseModel,
    ModelCapability,
    OutputFormat,
    ParameterDefinition,
    ParameterMode,
    ParameterType,
    register_model,
)


class NanaBananaModel(BaseModel):
    """Google's Nano Banana model implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Nano Banana supports editing and generation"""
        return ModelCapability.BOTH

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.JPEG

    @property
    def description(self) -> str:
        """Model description"""
        return _(
            "Google's state-of-the-art image generation and editing model "
            "for fast, conversational workflows"
        )

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Nano Banana (Gemini 2.5 Flash Image)")

    @property
    def max_file_size_mb(self) -> int:
        """Maximum file size in MB for reference images"""
        return 7

    @property
    def max_reference_images(self) -> int:
        """Maximum number of reference images for generation"""
        return 10

    @property
    def max_reference_images_edit(self) -> int:
        """Maximum number of reference images for editing"""
        return 9

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "google/nano-banana"

    @property
    def supported_mime_types(self) -> list[str]:
        """List of supported MIME types for reference images"""
        return ["image/png", "image/jpeg", "image/webp"]

    def build_edit_input(
        self,
        prompt: str,
        main_image,
        reference_images: list | None = None,
        user_settings: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
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

        model_input = {
            "prompt": prompt,
            "image_input": image_input,
            "aspect_ratio": "match_input_image",
            "output_format": params.get("output_format", "jpg"),
        }

        return model_input

    def build_generation_input(
        self,
        prompt: str,
        reference_images: list | None = None,
        user_settings: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
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
            "aspect_ratio": params.get("aspect_ratio", "1:1"),
            "output_format": params.get("output_format", "jpg"),
        }

        return model_input

    def get_parameter_definitions(self) -> list[ParameterDefinition]:
        """Get list of configurable parameters for Nano Banana"""
        return [
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="1:1",
                label=_("Aspect Ratio"),
                description=_("Aspect ratio of the generated image"),
                choices=[
                    "1:1",
                    "2:3",
                    "3:2",
                    "3:4",
                    "4:3",
                    "4:5",
                    "5:4",
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
        ]


nano_banana = NanaBananaModel()
register_model(nano_banana)
