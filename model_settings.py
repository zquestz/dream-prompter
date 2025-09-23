#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Model settings utility functions for Dream Prompter plugin
Provides easy access to model parameter management
"""

from typing import Dict, Any, List, Optional, Tuple, cast
from models import BaseModel, ParameterDefinition, ParameterType
from models.factory import get_model_by_name, get_all_models
from settings import get_model_settings, store_model_settings, get_model_parameter, set_model_parameter
from i18n import _

class ModelParameterManager:
    """Manager class for model parameters and settings"""

    def __init__(self, model_name: str):
        """
        Initialize parameter manager for a specific model

        Args:
            model_name: Name of the model (e.g., 'google/nano-banana')
        """
        self.model_name = model_name
        model = get_model_by_name(model_name)
        if not model:
            raise ValueError(f"Model '{model_name}' not found")
        self.model = cast(BaseModel, model)

    def get_parameter_definitions(self) -> List[ParameterDefinition]:
        """Get all parameter definitions for this model"""
        return self.model.get_parameter_definitions()

    def get_parameter_value(self, parameter_name: str, default_override: Any = None) -> Any:
        """
        Get current value for a parameter

        Args:
            parameter_name: Name of the parameter
            default_override: Override default if parameter not set

        Returns:
            Current parameter value
        """
        user_settings = get_model_settings(self.model_name)
        param_def = self._get_parameter_definition(parameter_name)

        if not param_def:
            return default_override

        if parameter_name in user_settings:
            return param_def.validate_value(user_settings[parameter_name])

        return default_override if default_override is not None else param_def.default_value

    def set_parameter_value(self, parameter_name: str, value: Any) -> bool:
        """
        Set value for a parameter

        Args:
            parameter_name: Name of the parameter
            value: Value to set

        Returns:
            True if successful, False if parameter not found
        """
        param_def = self._get_parameter_definition(parameter_name)
        if not param_def:
            return False

        validated_value = param_def.validate_value(value)
        set_model_parameter(self.model_name, parameter_name, validated_value)
        return True

    def get_all_parameter_values(self) -> Dict[str, Any]:
        """Get current values for all parameters"""
        values = {}
        for param_def in self.get_parameter_definitions():
            values[param_def.name] = self.get_parameter_value(param_def.name)
        return values

    def set_multiple_parameters(self, parameters: Dict[str, Any]) -> Dict[str, bool]:
        """
        Set multiple parameters at once

        Args:
            parameters: Dictionary of parameter_name -> value

        Returns:
            Dictionary of parameter_name -> success_boolean
        """
        results = {}
        for param_name, value in parameters.items():
            results[param_name] = self.set_parameter_value(param_name, value)
        return results

    def reset_parameter_to_default(self, parameter_name: str) -> bool:
        """
        Reset a parameter to its default value

        Args:
            parameter_name: Name of the parameter

        Returns:
            True if successful, False if parameter not found
        """
        param_def = self._get_parameter_definition(parameter_name)
        if not param_def:
            return False

        return self.set_parameter_value(parameter_name, param_def.default_value)

    def reset_all_parameters(self) -> None:
        """Reset all parameters to their default values"""
        for param_def in self.get_parameter_definitions():
            self.reset_parameter_to_default(param_def.name)

    def get_parameter_info(self, parameter_name: str) -> Optional[Dict[str, Any]]:
        """
        Get complete information about a parameter

        Args:
            parameter_name: Name of the parameter

        Returns:
            Dictionary with parameter information or None
        """
        param_def = self._get_parameter_definition(parameter_name)
        if not param_def:
            return None

        return {
            'name': param_def.name,
            'type': param_def.type.value,
            'label': param_def.label,
            'description': param_def.description,
            'default_value': param_def.default_value,
            'current_value': self.get_parameter_value(parameter_name),
            'choices': param_def.choices,
            'min_value': param_def.min_value,
            'max_value': param_def.max_value,
            'step': param_def.step
        }

    def get_all_parameters_info(self) -> List[Dict[str, Any]]:
        """Get complete information for all parameters"""
        info_list = []
        for param_def in self.get_parameter_definitions():
            info = self.get_parameter_info(param_def.name)
            if info:
                info_list.append(info)
        return info_list

    def _get_parameter_definition(self, parameter_name: str) -> Optional[ParameterDefinition]:
        """Get parameter definition by name"""
        for param_def in self.get_parameter_definitions():
            if param_def.name == parameter_name:
                return param_def
        return None

def get_model_parameter_manager(model_name: str) -> Optional[ModelParameterManager]:
    """
    Get parameter manager for a model

    Args:
        model_name: Name of the model

    Returns:
        ModelParameterManager instance or None if model not found
    """
    try:
        return ModelParameterManager(model_name)
    except ValueError:
        return None

def get_all_model_parameters() -> Dict[str, List[Dict[str, Any]]]:
    """
    Get parameter information for all available models

    Returns:
        Dictionary of model_name -> list of parameter info
    """
    all_params = {}
    all_models = get_all_models()

    for model_name, model in all_models.items():
        try:
            manager = ModelParameterManager(model_name)
            all_params[model_name] = manager.get_all_parameters_info()
        except Exception as e:
            print(f"Error getting parameters for {model_name}: {e}")
            all_params[model_name] = []

    return all_params

def validate_parameter_value(model_name: str, parameter_name: str, value: Any) -> Tuple[bool, Any, str]:
    """
    Validate a parameter value for a specific model

    Args:
        model_name: Name of the model
        parameter_name: Name of the parameter
        value: Value to validate

    Returns:
        Tuple of (is_valid, validated_value, error_message)
    """
    try:
        manager = ModelParameterManager(model_name)
        param_def = manager._get_parameter_definition(parameter_name)

        if not param_def:
            return False, None, f"Parameter '{parameter_name}' not found"

        validated_value = param_def.validate_value(value)
        return True, validated_value, ""

    except Exception as e:
        return False, None, str(e)

def get_parameter_display_value(param_info: Dict[str, Any]) -> str:
    """
    Get a human-readable display value for a parameter

    Args:
        param_info: Parameter information dictionary

    Returns:
        String representation of the current value
    """
    current_value = param_info.get('current_value')
    param_type = param_info.get('type')

    if current_value is None:
        return _("Not set")

    if param_type == ParameterType.BOOLEAN.value:
        return _("Yes") if current_value else _("No")
    elif param_type == ParameterType.CHOICE.value:
        return str(current_value)
    elif param_type == ParameterType.FLOAT.value:
        return f"{current_value:.2f}"
    else:
        return str(current_value)

def export_model_settings(model_name: str) -> Dict[str, Any]:
    """
    Export all settings for a model

    Args:
        model_name: Name of the model

    Returns:
        Dictionary of all parameter values
    """
    try:
        manager = ModelParameterManager(model_name)
        return manager.get_all_parameter_values()
    except Exception as e:
        print(f"Error exporting settings for {model_name}: {e}")
        return {}

def import_model_settings(model_name: str, settings: Dict[str, Any]) -> Dict[str, bool]:
    """
    Import settings for a model

    Args:
        model_name: Name of the model
        settings: Dictionary of parameter values

    Returns:
        Dictionary of parameter_name -> import_success
    """
    try:
        manager = ModelParameterManager(model_name)
        return manager.set_multiple_parameters(settings)
    except Exception as e:
        print(f"Error importing settings for {model_name}: {e}")
        return {key: False for key in settings.keys()}
