"""
Model classes for Dream Prompter plugin
Defines interfaces and implementations for different AI models
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Literal


class ModelCapability(Enum):
    """Model capabilities for different operations"""

    GENERATE = "generate"
    EDIT = "edit"
    BOTH = "both"


class OutputFormat(Enum):
    """Supported output formats"""

    PNG = "png"
    JPEG = "jpg"
    WEBP = "webp"


class ParameterMode(Enum):
    """Modes where parameters are supported"""

    GENERATE = "generate"
    EDIT = "edit"
    BOTH = "both"


class ParameterType(Enum):
    """Types of configurable parameters"""

    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"
    BOOLEAN = "boolean"
    CHOICE = "choice"
    RANGE = "range"


class ParameterDefinition:
    """Definition of a configurable parameter"""

    def __init__(
        self,
        name: str,
        param_type: ParameterType,
        default_value: Any,
        label: str | None = None,
        description: str | None = None,
        choices: list[Any] | None = None,
        min_value: Any = None,
        max_value: Any = None,
        step: Any = None,
        supported_modes: list[ParameterMode] | None = None,
        is_secret: bool = False,
    ):
        self.name = name
        self.param_type = param_type
        self.default_value = default_value
        self.label = label or name
        self.description = description or ""
        self.choices = choices or []
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.supported_modes = supported_modes or [ParameterMode.BOTH]
        self.is_secret = is_secret

    def supports_mode(self, mode: str) -> bool:
        """Check if this parameter supports the given mode"""
        if not mode or not isinstance(mode, str):
            return False

        if ParameterMode.BOTH in self.supported_modes:
            return True

        if mode == "generate":
            mode_enum = ParameterMode.GENERATE
        elif mode == "edit":
            mode_enum = ParameterMode.EDIT
        else:
            return False

        return mode_enum in self.supported_modes

    def validate_value(self, value: Any) -> Any:
        """Validate and convert a value for this parameter"""
        if value is None:
            return self.default_value

        if self.param_type == ParameterType.INTEGER:
            return self._validate_integer(value)
        elif self.param_type == ParameterType.FLOAT:
            return self._validate_float(value)
        elif self.param_type == ParameterType.STRING:
            return str(value)
        elif self.param_type == ParameterType.BOOLEAN:
            return self._validate_boolean(value)
        elif self.param_type == ParameterType.CHOICE:
            return self._validate_choice(value)

        return self.default_value

    def _validate_boolean(self, value: Any) -> bool:
        """Validate boolean parameter value"""
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ("true", "1", "yes", "on")
        return bool(value)

    def _validate_choice(self, value: Any) -> Any:
        """Validate choice parameter value"""
        if value in self.choices:
            return value
        return self.default_value

    def _validate_float(self, value: Any) -> float:
        """Validate float parameter value"""
        try:
            val = float(value)
            if self.min_value is not None and val < self.min_value:
                val = self.min_value
            if self.max_value is not None and val > self.max_value:
                val = self.max_value
            return val
        except (ValueError, TypeError):
            return self.default_value

    def _validate_integer(self, value: Any) -> int:
        """Validate integer parameter value"""
        try:
            val = int(value)
            if self.min_value is not None and val < self.min_value:
                val = self.min_value
            if self.max_value is not None and val > self.max_value:
                val = self.max_value
            return val
        except (ValueError, TypeError):
            return self.default_value


class BaseModel(ABC):
    """Abstract base class for all AI models"""

    @property
    @abstractmethod
    def capabilities(self) -> ModelCapability:
        """
        Get model capabilities (default: both generate and edit)
        Override in subclasses for models with specific limitations
        """
        return ModelCapability.BOTH

    @property
    @abstractmethod
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""

    @property
    @abstractmethod
    def description(self) -> str:
        """Model description"""

    @property
    @abstractmethod
    def display_name(self) -> str:
        """Human-readable model name"""

    @property
    def file_encoding_strategy(self) -> Literal["base64", "url"] | None:
        """
        How file inputs are sent to Replicate (None = client default)

        Models whose runners validate inputs by URL extension need
        "base64" so the MIME type travels inside a data URI instead.
        """
        return None

    @property
    @abstractmethod
    def max_file_size_mb(self) -> int:
        """Maximum file size in MB for reference images"""

    @property
    @abstractmethod
    def max_reference_images(self) -> int:
        """Maximum number of reference images for generation"""

    @property
    def max_reference_images_edit(self) -> int:
        """Maximum number of reference images for editing (default: max - 1)"""
        return max(1, self.max_reference_images - 1)

    @property
    @abstractmethod
    def name(self) -> str:
        """Model name/identifier"""

    @property
    @abstractmethod
    def supported_mime_types(self) -> list[str]:
        """List of supported MIME types for reference images"""

    @abstractmethod
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
            **kwargs: Additional model-specific parameters
                (override user_settings)

        Returns:
            Dictionary of input parameters for the model API
        """

    @abstractmethod
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
            **kwargs: Additional model-specific parameters
                (override user_settings)

        Returns:
            Dictionary of input parameters for the model API
        """

    def build_parameters_dict(
        self, user_settings: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Build dictionary of all parameter values for API calls

        Args:
            user_settings: User's saved settings for this model

        Returns:
            Dictionary of parameter name -> value
        """
        params = {}
        for param_def in self.get_parameter_definitions():
            param_value = self.get_parameter_value(
                param_def.name, user_settings
            )
            params[param_def.name] = param_value
        return params

    def get_output_format_string(self, format_enum: OutputFormat) -> str:
        """
        Get string representation of output format for API calls

        Args:
            format_enum: OutputFormat enum value

        Returns:
            String representation for API calls
        """
        return format_enum.value

    def get_parameter_definitions(self) -> list[ParameterDefinition]:
        """
        Get list of configurable parameters for this model

        Returns:
            List of ParameterDefinition objects
        """
        return []

    def get_parameter_value(
        self,
        parameter_name: str,
        user_settings: dict[str, Any] | None = None,
    ) -> Any:
        """
        Get parameter value from user settings or default

        Args:
            parameter_name: Name of the parameter
            user_settings: User's saved settings for this model

        Returns:
            Parameter value (validated and converted)
        """
        param_def = self._get_parameter_definition(parameter_name)
        if not param_def:
            return None

        if user_settings and parameter_name in user_settings:
            return param_def.validate_value(user_settings[parameter_name])

        return param_def.default_value

    def is_mode_supported(self, mode: str) -> bool:
        """Check if a specific mode is supported"""
        if mode == "generate":
            return self.supports_generation()
        elif mode == "edit":
            return self.supports_editing()
        return False

    def supports_generation(self) -> bool:
        """Check if model supports image generation"""
        return self.capabilities in [
            ModelCapability.GENERATE,
            ModelCapability.BOTH,
        ]

    def supports_editing(self) -> bool:
        """Check if model supports image editing"""
        return self.capabilities in [ModelCapability.EDIT, ModelCapability.BOTH]

    def validate_file_size(self, size_bytes: int) -> bool:
        """
        Validate file size

        Args:
            size_bytes: File size in bytes

        Returns:
            True if size is valid, False otherwise
        """
        max_bytes = self.max_file_size_mb * 1024 * 1024
        return size_bytes <= max_bytes

    def validate_mime_type(self, mime_type: str) -> bool:
        """
        Validate MIME type

        Args:
            mime_type: MIME type to validate

        Returns:
            True if MIME type is supported, False otherwise
        """
        return mime_type in self.supported_mime_types

    def _get_parameter_definition(
        self, parameter_name: str
    ) -> ParameterDefinition | None:
        """Get parameter definition by name"""
        for param_def in self.get_parameter_definitions():
            if param_def.name == parameter_name:
                return param_def
        return None


_model_registry: dict[str, BaseModel] = {}


def register_model(model: BaseModel) -> None:
    """Register a model in the global registry"""
    _model_registry[model.name] = model


def get_model(name: str) -> BaseModel | None:
    """Get a model by name from the registry"""
    return _model_registry.get(name)


def get_all_models() -> dict[str, BaseModel]:
    """Get all registered models"""
    return _model_registry.copy()


def get_compatible_models(mode: str) -> dict[str, BaseModel]:
    """
    Get models compatible with a specific mode

    Args:
        mode: Operation mode ("generate" or "edit")

    Returns:
        Dictionary of compatible models
    """
    all_models = get_all_models()
    return {
        name: model
        for name, model in all_models.items()
        if model.is_mode_supported(mode)
    }


def get_models_for_context(has_image: bool = False) -> dict[str, BaseModel]:
    """
    Get models appropriate for the current context

    Args:
        has_image: Whether an image is currently open in GIMP

    Returns:
        Dictionary of model name -> model instance filtered by context
    """
    all_models = get_all_models()
    filtered_models = {}

    for name, model in all_models.items():
        if has_image:
            if model.supports_editing() or model.supports_generation():
                filtered_models[name] = model
        else:
            if model.supports_generation():
                filtered_models[name] = model

    return filtered_models


def get_model_names() -> list[str]:
    """Get list of all registered model names"""
    return list(_model_registry.keys())
