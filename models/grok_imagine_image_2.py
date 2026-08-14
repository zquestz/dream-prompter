"""
Grok Imagine Image 2 model implementation
xAI's general-purpose image generation and editing model with support
for real-world entities, brands, places, and named objects
Available through Replicate API
"""

import io
from typing import Any, Literal

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


class GrokImagineImage2Model(BaseModel):
    """xAI Grok Imagine Image 2 model implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Grok Imagine Image 2 supports generation and editing"""
        return ModelCapability.BOTH

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.PNG

    @property
    def description(self) -> str:
        """Model description"""
        return _(
            "xAI's general-purpose image generation and editing model"
        )

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Grok Imagine Image 2")

    @property
    def file_encoding_strategy(self) -> Literal["base64", "url"] | None:
        """The runner rejects extensionless upload URLs, so send data
        URIs, which carry the MIME type inline"""
        return "base64"

    @property
    def max_file_size_mb(self) -> int:
        """Maximum file size in MB for reference images"""
        return 10

    @property
    def max_reference_images(self) -> int:
        """
        Maximum number of reference images for generation

        The model accepts a single image input; when provided, the
        prompt is applied to that image instead of generating from
        scratch.
        """
        return 1

    @property
    def max_reference_images_edit(self) -> int:
        """
        Maximum number of reference images for editing

        The model accepts a single image, which the edited image occupies.
        """
        return 0

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "xai/grok-imagine-image-2"

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
            reference_images: Unused, the model accepts a single image
            user_settings: User's saved settings for this model
            **kwargs: Additional parameters (override user_settings)

        Returns:
            Dictionary of input parameters for the Replicate API
        """
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
            "image": image,
            "resolution": params.get("resolution", "2k"),
            "quality": params.get("quality", "medium"),
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
            reference_images: Optional single reference image; when
                provided, the prompt is applied to it and the aspect
                ratio setting is ignored by the API
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
            "resolution": params.get("resolution", "2k"),
            "quality": params.get("quality", "medium"),
        }

        if reference_images and len(reference_images) > 0:
            model_input["image"] = reference_images[0]
        else:
            # The API ignores aspect_ratio when an image is provided
            model_input["aspect_ratio"] = params.get("aspect_ratio", "1:1")

        return {k: v for k, v in model_input.items() if v is not None}

    def get_parameter_definitions(self) -> list[ParameterDefinition]:
        """Get list of configurable parameters for Grok Imagine Image 2"""
        return [
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="1:1",
                label=_("Aspect Ratio"),
                description=_("Aspect ratio of the generated image"),
                choices=[
                    "1:1",
                    "16:9",
                    "9:16",
                    "4:3",
                    "3:4",
                    "3:2",
                    "2:3",
                    "2:1",
                    "1:2",
                    "19.5:9",
                    "9:19.5",
                    "20:9",
                    "9:20",
                    "auto",
                ],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="resolution",
                param_type=ParameterType.CHOICE,
                default_value="2k",
                label=_("Resolution"),
                description=_("Resolution of the generated image"),
                choices=["1k", "2k"],
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="quality",
                param_type=ParameterType.CHOICE,
                default_value="medium",
                label=_("Quality"),
                description=_(
                    "Generation quality. Medium produces the best "
                    "results, low is faster and cheaper."
                ),
                choices=["low", "medium"],
                supported_modes=[ParameterMode.BOTH],
            ),
        ]


grok_imagine_image_2 = GrokImagineImage2Model()
register_model(grok_imagine_image_2)
