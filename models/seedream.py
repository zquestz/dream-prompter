"""
Seedream 5 Pro model implementation
ByteDance's flagship image generation and editing model, producing sharp
1K and 2K images. Available through Replicate API
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


class SeedreamModel(BaseModel):
    """ByteDance Seedream 5 Pro model implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Seedream 5 Pro supports editing and generation"""
        return ModelCapability.BOTH

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.PNG

    @property
    def description(self) -> str:
        """Model description"""
        return _(
            "ByteDance's flagship model for sharp 1K and 2K images"
        )

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Seedream 5 Pro")

    @property
    def max_file_size_mb(self) -> int:
        """Plugin size limit per reference file in MiB, not GIMP exports."""
        return 10

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
        return "bytedance/seedream-5-pro"

    @property
    def supported_mime_types(self) -> list[str]:
        """Input formats accepted by the plugin for this model."""
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
            "output_format": params["output_format"],
        }

        return {k: v for k, v in model_input.items() if v is not None}

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
            "size": params["size"],
            "aspect_ratio": params["aspect_ratio"],
            "output_format": params["output_format"],
        }

        return {k: v for k, v in model_input.items() if v is not None}

    def get_parameter_definitions(self) -> list[ParameterDefinition]:
        """Get list of configurable parameters for Seedream 5 Pro"""
        return [
            ParameterDefinition(
                name="size",
                param_type=ParameterType.CHOICE,
                default_value="2K",
                label=_("Image Size"),
                description=_(
                    "Image resolution: 1K (~2 megapixels) or 2K "
                    "(~4 megapixels)"
                ),
                choices=["1K", "2K"],
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
                name="output_format",
                param_type=ParameterType.CHOICE,
                default_value="png",
                label=_("Output Format"),
                description=_("Format of the output images"),
                choices=["png", "jpeg"],
                supported_modes=[ParameterMode.BOTH],
            ),
        ]


seedream = SeedreamModel()
register_model(seedream)
