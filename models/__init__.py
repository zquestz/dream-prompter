#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Model classes for Dream Prompter plugin
Defines interfaces and implementations for different AI models
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from enum import Enum


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

    def __init__(self, name: str, param_type: ParameterType, default_value: Any,
                 label: Optional[str] = None, description: Optional[str] = None,
                 choices: Optional[List[Any]] = None, min_value: Any = None,
                 max_value: Any = None, step: Any = None):
        self.name = name
        self.type = param_type
        self.default_value = default_value
        self.label = label or name
        self.description = description or ""
        self.choices = choices or []
        self.min_value = min_value
        self.max_value = max_value
        self.step = step

    def validate_value(self, value: Any) -> Any:
        """Validate and convert a value for this parameter"""
        if value is None:
            return self.default_value

        if self.type == ParameterType.INTEGER:
            try:
                val = int(value)
                if self.min_value is not None and val < self.min_value:
                    val = self.min_value
                if self.max_value is not None and val > self.max_value:
                    val = self.max_value
                return val
            except (ValueError, TypeError):
                return self.default_value

        elif self.type == ParameterType.FLOAT:
            try:
                val = float(value)
                if self.min_value is not None and val < self.min_value:
                    val = self.min_value
                if self.max_value is not None and val > self.max_value:
                    val = self.max_value
                return val
            except (ValueError, TypeError):
                return self.default_value

        elif self.type == ParameterType.STRING:
            return str(value)

        elif self.type == ParameterType.BOOLEAN:
            if isinstance(value, bool):
                return value
            if isinstance(value, str):
                return value.lower() in ('true', '1', 'yes', 'on')
            return bool(value)

        elif self.type == ParameterType.CHOICE:
            if value in self.choices:
                return value
            return self.default_value

        return self.default_value


class OutputFormat(Enum):
    """Supported output formats"""
    PNG = "png"
    JPEG = "jpg"
    WEBP = "webp"


class BaseModel(ABC):
    """Abstract base class for all AI models"""

    @property
    @abstractmethod
    def name(self) -> str:
        """Model name/identifier"""
        pass

    @property
    @abstractmethod
    def display_name(self) -> str:
        """Human-readable model name"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Model description"""
        pass

    @property
    @abstractmethod
    def max_reference_images(self) -> int:
        """Maximum number of reference images for generation"""
        pass

    @property
    def max_reference_images_edit(self) -> int:
        """Maximum number of reference images for editing (default: max - 1)"""
        return max(1, self.max_reference_images - 1)

    @property
    @abstractmethod
    def max_file_size_mb(self) -> int:
        """Maximum file size in MB for reference images"""
        pass

    @property
    @abstractmethod
    def supported_mime_types(self) -> List[str]:
        """List of supported MIME types for reference images"""
        pass

    @property
    @abstractmethod
    def default_output_format(self) -> OutputFormat:
        """Default output format for generated images"""
        pass

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """
        Get list of configurable parameters for this model

        Returns:
            List of ParameterDefinition objects
        """
        return []

    def get_parameter_value(self, parameter_name: str,
                            user_settings: Optional[Dict[str, Any]] = None) -> Any:
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

    def _get_parameter_definition(self, parameter_name: str
                                  ) -> Optional[ParameterDefinition]:
        """Get parameter definition by name"""
        for param_def in self.get_parameter_definitions():
            if param_def.name == parameter_name:
                return param_def
        return None

    def build_parameters_dict(self,
                              user_settings: Optional[Dict[str, Any]] = None
                              ) -> Dict[str, Any]:
        """
        Build dictionary of all parameter values for API calls

        Args:
            user_settings: User's saved settings for this model

        Returns:
            Dictionary of parameter name -> value
        """
        params = {}
        for param_def in self.get_parameter_definitions():
            param_value = self.get_parameter_value(param_def.name, user_settings)
            params[param_def.name] = param_value
        return params

    @abstractmethod
    def build_generation_input(self, prompt: str,
                               reference_images: Optional[List] = None,
                               user_settings: Optional[Dict[str, Any]] = None,
                               **kwargs) -> Dict[str, Any]:
        """
        Build input dictionary for image generation

        Args:
            prompt: Text prompt for generation
            reference_images: Optional list of reference image file objects
            user_settings: User's saved settings for this model
            **kwargs: Additional model-specific parameters (override user_settings)

        Returns:
            Dictionary of input parameters for the model API
        """
        pass

    @abstractmethod
    def build_edit_input(self, prompt: str, main_image,
                         reference_images: Optional[List] = None,
                         user_settings: Optional[Dict[str, Any]] = None,
                         **kwargs) -> Dict[str, Any]:
        """
        Build input dictionary for image editing

        Args:
            prompt: Text prompt for editing
            main_image: Main image to edit (file object or bytes)
            reference_images: Optional list of reference image file objects
            user_settings: User's saved settings for this model
            **kwargs: Additional model-specific parameters (override user_settings)

        Returns:
            Dictionary of input parameters for the model API
        """
        pass

    def validate_reference_image_count(self, count: int,
                                       is_edit: bool = False) -> bool:
        """
        Validate reference image count

        Args:
            count: Number of reference images
            is_edit: Whether this is for editing (vs generation)

        Returns:
            True if count is valid, False otherwise
        """
        if is_edit:
            max_count = self.max_reference_images_edit
        else:
            max_count = self.max_reference_images
        return 0 <= count <= max_count

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

    def get_output_format_string(self, format_enum: OutputFormat) -> str:
        """
        Get string representation of output format for API calls

        Args:
            format_enum: OutputFormat enum value

        Returns:
            String representation for API calls
        """
        return format_enum.value


_model_registry: Dict[str, BaseModel] = {}


def register_model(model: BaseModel) -> None:
    """Register a model in the global registry"""
    _model_registry[model.name] = model


def get_model(name: str) -> Optional[BaseModel]:
    """Get a model by name from the registry"""
    return _model_registry.get(name)


def get_all_models() -> Dict[str, BaseModel]:
    """Get all registered models"""
    return _model_registry.copy()


def get_model_names() -> List[str]:
    """Get list of all registered model names"""
    return list(_model_registry.keys())
