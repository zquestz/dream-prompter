#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Model factory for Dream Prompter plugin
Provides easy access to model instances and management
"""

from typing import Optional, List, Dict, Any
from . import BaseModel, get_model, get_all_models, get_model_names

class ModelFactory:
    """Factory class for creating and managing model instances"""

    def __init__(self):
        """Initialize the model factory"""
        self._default_model = "google/nano-banana"
        self._initialize_models()

    def _initialize_models(self) -> None:
        """Initialize all available models"""
        from . import nano_banana
        from . import seedream4

    def create_model_info_dict(self, model_name: str) -> Optional[Dict[str, Any]]:
        """
        Create a dictionary with model information for UI/display purposes

        Args:
            model_name: Name of the model

        Returns:
            Dictionary with model info or None if model not found
        """
        model = self.get_model_by_name(model_name)
        if not model:
            return None

        return {
            'name': model.name,
            'display_name': model.display_name,
            'description': model.description,
            'max_reference_images': model.max_reference_images,
            'max_reference_images_edit': model.max_reference_images_edit,
            'max_file_size_mb': model.max_file_size_mb,
            'supported_mime_types': model.supported_mime_types,
            'default_output_format': model.default_output_format.value,
        }

    def get_available_model_names(self) -> List[str]:
        """
        Get list of all available model names

        Returns:
            List of model names
        """
        return get_model_names()

    def get_available_models(self) -> Dict[str, BaseModel]:
        """
        Get all available model instances

        Returns:
            Dictionary of model name -> model instance
        """
        return get_all_models()

    def get_default_model(self) -> BaseModel:
        """
        Get the default model instance

        Returns:
            Default model instance

        Raises:
            RuntimeError: If default model is not available
        """
        model = get_model(self._default_model)
        if not model:
            raise RuntimeError(f"Default model '{self._default_model}' not found")
        return model

    def get_model_by_name(self, name: str) -> Optional[BaseModel]:
        """
        Get a model instance by name

        Args:
            name: Model name (e.g., 'google/nano-banana')

        Returns:
            Model instance or None if not found
        """
        return get_model(name)

    def get_model_limits(self, model_name: str, operation_type: str) -> Optional[Dict[str, Any]]:
        """
        Get model limits for a specific operation

        Args:
            model_name: Name of the model
            operation_type: Type of operation ('generate' or 'edit')

        Returns:
            Dictionary with limits or None if model not found
        """
        model = self.get_model_by_name(model_name)
        if not model:
            return None

        is_edit = operation_type.lower() == 'edit'
        max_ref_images = model.max_reference_images_edit if is_edit else model.max_reference_images

        return {
            'max_reference_images': max_ref_images,
            'max_file_size_mb': model.max_file_size_mb,
            'supported_mime_types': model.supported_mime_types,
            'default_output_format': model.default_output_format.value
        }

    def set_default_model(self, model_name: str) -> bool:
        """
        Set the default model

        Args:
            model_name: Name of the model to set as default

        Returns:
            True if successful, False if model not found
        """
        if self.get_model_by_name(model_name):
            self._default_model = model_name
            return True
        return False

    def validate_model_compatibility(self, model_name: str, operation_type: str) -> bool:
        """
        Validate if a model supports a specific operation type

        Args:
            model_name: Name of the model
            operation_type: Type of operation ('generate' or 'edit')

        Returns:
            True if model supports the operation, False otherwise
        """
        model = self.get_model_by_name(model_name)
        if not model:
            return False

        return operation_type.lower() in ['generate', 'edit']

model_factory = ModelFactory()

def get_default_model() -> BaseModel:
    """Convenience function to get the default model"""
    return model_factory.get_default_model()

def get_model_by_name(name: str) -> Optional[BaseModel]:
    """Convenience function to get a model by name"""
    return model_factory.get_model_by_name(name)

def get_model_limits(model_name: str, operation_type: str) -> Optional[Dict[str, Any]]:
    """Convenience function to get model limits"""
    return model_factory.get_model_limits(model_name, operation_type)
