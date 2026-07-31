"""
Qwen Image 2 Pro model implementation
Qwen's next-generation image generation and editing model with enhanced
text rendering, realism and semantic adherence
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


class QwenImageModel(BaseModel):
    """Qwen Image 2 Pro model implementation for Replicate"""

    @property
    def capabilities(self) -> ModelCapability:
        """Qwen Image 2 Pro supports generation and editing"""
        return ModelCapability.BOTH

    @property
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        return OutputFormat.WEBP

    @property
    def description(self) -> str:
        """Model description"""
        return _(
            "Qwen's next-generation model with enhanced text rendering"
        )

    @property
    def display_name(self) -> str:
        """Human-readable model name"""
        return _("Qwen Image 2 Pro")

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
        """
        Maximum number of reference images for editing

        The model accepts a single image, which the edited image occupies.
        """
        return 0

    @property
    def name(self) -> str:
        """Model name/identifier"""
        return "qwen/qwen-image-2-pro"

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
            "match_input_image": True,
            "enable_prompt_expansion": params.get(
                "enable_prompt_expansion", True
            ),
            "negative_prompt": params.get("negative_prompt", ""),
        }

        if params.get("seed", -1) != -1:
            model_input["seed"] = params["seed"]

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
            "aspect_ratio": params.get("aspect_ratio", "1:1"),
            "enable_prompt_expansion": params.get(
                "enable_prompt_expansion", True
            ),
            "negative_prompt": params.get("negative_prompt", ""),
        }

        if params.get("seed", -1) != -1:
            model_input["seed"] = params["seed"]

        if reference_images and len(reference_images) > 0:
            model_input["image"] = reference_images[0]
            model_input["match_input_image"] = params.get(
                "match_input_image", False
            )

        return {k: v for k, v in model_input.items() if v is not None}

    def get_parameter_definitions(self) -> list[ParameterDefinition]:
        """Get list of configurable parameters for Qwen Image 2 Pro"""
        return [
            ParameterDefinition(
                name="aspect_ratio",
                param_type=ParameterType.CHOICE,
                default_value="1:1",
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
                    "2:1",
                    "1:2",
                ],
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="match_input_image",
                param_type=ParameterType.BOOLEAN,
                default_value=False,
                label=_("Match Reference Image"),
                description=_(
                    "Use the reference image's aspect ratio and resolution "
                    "instead of the aspect ratio setting"
                ),
                supported_modes=[ParameterMode.GENERATE],
            ),
            ParameterDefinition(
                name="enable_prompt_expansion",
                param_type=ParameterType.BOOLEAN,
                default_value=True,
                label=_("Expand Prompt"),
                description=_(
                    "Automatically expand and optimize the prompt for "
                    "better results"
                ),
                supported_modes=[ParameterMode.BOTH],
            ),
            ParameterDefinition(
                name="negative_prompt",
                param_type=ParameterType.STRING,
                default_value="",
                label=_("Negative Prompt"),
                description=_("Negative prompt for generated image"),
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
                max_value=2147483647,
                supported_modes=[ParameterMode.BOTH],
            ),
        ]


qwen_image = QwenImageModel()
register_model(qwen_image)
