#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Model classes for Dream Prompter plugin
Defines interfaces and implementations for different AI models
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from enum import Enum

class OutputFormat(Enum):
    """Supported output formats"""
    PNG = "png"
    JPEG = "jpeg"
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

    @abstractmethod
    def build_generation_input(self, prompt: str, reference_images: Optional[List] = None, **kwargs) -> Dict[str, Any]:
        """
        Build input dictionary for image generation

        Args:
            prompt: Text prompt for generation
            reference_images: Optional list of reference image file objects
            **kwargs: Additional model-specific parameters

        Returns:
            Dictionary of input parameters for the model API
        """
        pass

    @abstractmethod
    def build_edit_input(self, prompt: str, main_image, reference_images: Optional[List] = None, **kwargs) -> Dict[str, Any]:
        """
        Build input dictionary for image editing

        Args:
            prompt: Text prompt for editing
            main_image: Main image to edit (file object or bytes)
            reference_images: Optional list of reference image file objects
            **kwargs: Additional model-specific parameters

        Returns:
            Dictionary of input parameters for the model API
        """
        pass

    def validate_reference_image_count(self, count: int, is_edit: bool = False) -> bool:
        """
        Validate reference image count

        Args:
            count: Number of reference images
            is_edit: Whether this is for editing (vs generation)

        Returns:
            True if count is valid, False otherwise
        """
        max_count = self.max_reference_images_edit if is_edit else self.max_reference_images
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
