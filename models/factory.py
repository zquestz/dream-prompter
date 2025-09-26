#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Model factory for Dream Prompter plugin
Provides easy access to model instances and management
"""

from typing import Optional, Dict
from . import BaseModel, get_model, get_all_models

# Import models to register them
from . import nano_banana  # noqa: F401
from . import seedream4  # noqa: F401
from . import qwen_image_edit_plus  # noqa: F401


class ModelFactory:
    """Factory class for creating and managing model instances"""

    def __init__(self):
        """Initialize the model factory"""
        self._default_model = "google/nano-banana"

    def get_available_models(self) -> Dict[str, BaseModel]:
        """
        Get all available model instances

        Returns:
            Dictionary of model name -> model instance
        """
        return get_all_models()

    def get_compatible_models(self, mode: str) -> Dict[str, BaseModel]:
        """
        Get models compatible with a specific mode

        Args:
            mode: Operation mode ("generate" or "edit")

        Returns:
            Dictionary of compatible models
        """
        all_models = self.get_available_models()
        return {name: model for name, model in all_models.items()
                if model.is_mode_supported(mode)}

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
            raise RuntimeError(
                f"Default model '{self._default_model}' not found"
            )
        return model

    def get_models_for_context(self, has_image: bool = False) -> Dict[str, BaseModel]:
        """
        Get models appropriate for the current context

        Args:
            has_image: Whether an image is currently open in GIMP

        Returns:
            Dictionary of model name -> model instance filtered by context
        """
        all_models = self.get_available_models()
        filtered_models = {}

        for name, model in all_models.items():
            if has_image:
                if model.supports_editing() or model.supports_generation():
                    filtered_models[name] = model
            else:
                if model.supports_generation():
                    filtered_models[name] = model

        return filtered_models

    def get_model_by_name(self, name: str) -> Optional[BaseModel]:
        """
        Get a model instance by name

        Args:
            name: Model name (e.g., 'google/nano-banana')

        Returns:
            Model instance or None if not found
        """
        return get_model(name)


model_factory = ModelFactory()


def get_compatible_models(mode: str) -> Dict[str, BaseModel]:
    """Convenience function to get compatible models"""
    return model_factory.get_compatible_models(mode)


def get_default_model() -> BaseModel:
    """Convenience function to get the default model"""
    return model_factory.get_default_model()


def get_models_for_context(has_image: bool = False) -> Dict[str, BaseModel]:
    """Convenience function to get models for context"""
    return model_factory.get_models_for_context(has_image)


def get_model_by_name(name: str) -> Optional[BaseModel]:
    """Convenience function to get a model by name"""
    return model_factory.get_model_by_name(name)
