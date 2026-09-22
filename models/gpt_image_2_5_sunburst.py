"""
GPT Image 2.5 Sunburst model implementation
OpenAI's image generation and editing model with precise editing control
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


class GPTImage25SunburstModel(BaseModel):
    """OpenAI's GPT Image 2.5 Sunburst implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Sunburst supports generation and editing"""
        return ModelCapability.BOTH

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.WEBP

    @property
    def description(self) -> str:
        """Model description"""
        return _(
            "OpenAI's image generation and editing model with precise "
            "editing control"
        )

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("GPT Image 2.5 Sunburst")

    @property
    def max_file_size_mb(self) -> int:
        """Plugin reference file limit; the API schema specifies no limit"""
        return 10

    @property
    def max_reference_images(self) -> int:
        """Plugin input image limit; the API schema specifies no limit"""
        return 10

    @property
    def max_reference_images_edit(self) -> int:
        """Reserve one of the plugin's input image slots for the main image"""
        return 9

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "openai/gpt-image-2.5-sunburst"

    @property
    def supported_mime_types(self) -> list[str]:
        """Reference image formats accepted by the plugin"""
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
        Build an edit request with the current image or selected region first.

        Args:
            prompt: Text instructions for editing
            main_image: Exported GIMP image or region (file object or bytes)
            reference_images: Optional additional reference image files
            user_settings: User's saved settings for this model
            **kwargs: Additional parameters (override user_settings)

        Returns:
            Dictionary of input parameters for the Replicate API
        """
        if isinstance(main_image, bytes):
            main_image = io.BytesIO(main_image)
            main_image.name = "image.png"

        input_images = [main_image]
        if reference_images:
            input_images.extend(
                reference_images[: self.max_reference_images_edit]
            )

        return self.build_generation_input(
            prompt,
            reference_images=input_images,
            user_settings=user_settings,
            **kwargs,
        )

    def build_generation_input(
        self,
        prompt: str,
        reference_images: list | None = None,
        user_settings: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Build a generation request with optional reference images.

        Sunburst processes input images at high fidelity automatically;
        there is no input_fidelity parameter.

        Args:
            prompt: Text prompt for generation
            reference_images: Optional reference image file objects
            user_settings: User's saved settings for this model
            **kwargs: Additional parameters (override user_settings)

        Returns:
            Dictionary of input parameters for the Replicate API
        """
        params = self.build_parameters_dict({**(user_settings or {}), **kwargs})
        model_input = {"prompt": prompt, **params}

        for optional_parameter in ("openai_api_key", "user_id"):
            if not model_input[optional_parameter]:
                del model_input[optional_parameter]

        if reference_images:
            model_input["input_images"] = reference_images[
                : self.max_reference_images
            ]

        return model_input

    def get_parameter_definitions(self) -> list[ParameterDefinition]:
        """Configurable Sunburst parameters shared by generation and editing"""
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
                supported_modes=[ParameterMode.BOTH],
                is_secret=True,
            ),
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="1:1",
                label=_("Image Size"),
                description=_(
                    "Aspect ratio or pixel dimensions. Auto lets the model "
                    "choose. Sizes above 2560x1440 are experimental."
                ),
                choices=[
                    "1:1",
                    "3:2",
                    "2:3",
                    "4:3",
                    "3:4",
                    "16:9",
                    "9:16",
                    "auto",
                    "1024x1024",
                    "1536x1024",
                    "1024x1536",
                    "1536x1152",
                    "1152x1536",
                    "2048x2048",
                    "2048x1152",
                    "1152x2048",
                    "3840x2160",
                    "2160x3840",
                ],
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="number_of_images",
                param_type=ParameterType.INTEGER,
                default_value=1,
                label=_("Number of Images"),
                description=_("Number of images to generate (1-10)"),
                min_value=1,
                max_value=10,
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="quality",
                param_type=ParameterType.CHOICE,
                default_value="auto",
                label=_("Quality"),
                description=_("Higher quality takes longer and costs more."),
                choices=["low", "medium", "high", "xhigh", "max", "auto"],
                supported_modes=[ParameterMode.BOTH],
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
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="output_compression",
                param_type=ParameterType.INTEGER,
                default_value=90,
                label=_("Output Compression"),
                description=_("Compression level (0-100%)"),
                min_value=0,
                max_value=100,
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="output_format",
                param_type=ParameterType.CHOICE,
                default_value="webp",
                label=_("Output Format"),
                description=_("Format of the output image"),
                choices=["png", "jpeg", "webp"],
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="moderation",
                param_type=ParameterType.CHOICE,
                default_value="auto",
                label=_("Moderation"),
                description=_("Content moderation level"),
                choices=["auto", "low"],
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="user_id",
                param_type=ParameterType.STRING,
                default_value="",
                label=_("User ID"),
                description=_(
                    "Optional end-user identifier for OpenAI abuse monitoring"
                ),
                supported_modes=[ParameterMode.BOTH],
            ),
        ]


gpt_image_2_5_sunburst = GPTImage25SunburstModel()
register_model(gpt_image_2_5_sunburst)
