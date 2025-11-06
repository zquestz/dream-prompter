#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Settings management for Dream Prompter plugin
"""

import json
import os
import platform
from typing import cast, Dict, Union, Literal, Any, Optional

try:
    from models.factory import model_factory
except ImportError:
    model_factory = None

ModeKey = Literal["edit", "generate"]
SettingsDict = Dict[str, Union[str, bool, Dict[str, Any]]]
ModelSettingsDict = Dict[str, Any]

CONFIG_FILE_NAME = "dream-prompter-config.json"
GIMP_VERSION = "3.0"
FILE_PERMISSIONS = 0o600

DEFAULT_MODE = "edit"
DEFAULT_API_KEY_VISIBLE = False

DEFAULT_SETTINGS: SettingsDict = {
    "api_key": "",
    "mode": DEFAULT_MODE,
    "prompt": "",
    "api_key_visible": DEFAULT_API_KEY_VISIBLE,
    "model": "",
    "model_settings": {},
}


def get_config_file() -> str:
    """Get path to config file in GIMP's user directory"""
    system = platform.system()

    if system == "Windows":
        gimp_dir = _get_windows_config_dir()
    elif system == "Darwin":
        gimp_dir = _get_macos_config_dir()
    else:
        gimp_dir = _get_linux_config_dir()

    try:
        os.makedirs(gimp_dir, exist_ok=True)
    except (OSError, PermissionError) as e:
        print(f"Warning: Could not create config directory {gimp_dir}: {e}")

    return os.path.join(gimp_dir, CONFIG_FILE_NAME)


def get_default_model_name() -> str:
    """Get default model name from factory"""
    if model_factory:
        return model_factory._default_model
    return "google/nano-banana"


def get_model_parameter(
    model_name: str, parameter: str, default_value: Any = None
) -> Any:
    """
    Get a specific parameter value for a model

    Args:
        model_name: Name of the model
        parameter: Parameter name
        default_value: Default value if parameter not found

    Returns:
        Parameter value or default_value
    """
    model_settings = get_model_settings(model_name)
    return model_settings.get(parameter, default_value)


def get_model_settings(model_name: str) -> ModelSettingsDict:
    """
    Get settings for a specific model

    Args:
        model_name: Name of the model (e.g., 'google/nano-banana')

    Returns:
        Dictionary of model-specific settings
    """
    try:
        settings = load_settings()
        model_settings = settings.get("model_settings", {})
        if isinstance(model_settings, dict):
            return model_settings.get(model_name, {})
        return {}
    except Exception as e:
        print(f"Error loading model settings for {model_name}: {e}")
        return {}


def load_settings() -> SettingsDict:
    """Load settings from config file"""
    try:
        config_file = get_config_file()
        if os.path.exists(config_file):
            with open(config_file, "r", encoding="utf-8") as f:
                loaded_settings = cast(SettingsDict, json.load(f))
                for key, default_value in DEFAULT_SETTINGS.items():
                    if key not in loaded_settings:
                        loaded_settings[key] = default_value

                if not loaded_settings.get("model"):
                    loaded_settings["model"] = get_default_model_name()

                return loaded_settings
    except (OSError, PermissionError) as e:
        print(f"Failed to read settings file: {e}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in settings file: {e}")
    except Exception as e:
        print(f"Unexpected error loading settings: {e}")

    return DEFAULT_SETTINGS.copy()


def set_model_parameter(model_name: str, parameter: str, value: Any) -> None:
    """
    Set a specific parameter value for a model

    Args:
        model_name: Name of the model
        parameter: Parameter name
        value: Parameter value
    """
    model_settings = get_model_settings(model_name)
    model_settings[parameter] = value
    store_model_settings(model_name, model_settings)


def store_model_settings(
    model_name: str, model_settings: ModelSettingsDict
) -> None:
    """
    Store settings for a specific model

    Args:
        model_name: Name of the model (e.g., 'google/nano-banana')
        model_settings: Dictionary of model-specific settings
    """
    try:
        current_settings = load_settings()
        all_model_settings = current_settings.get("model_settings", {})

        if isinstance(all_model_settings, dict):
            all_model_settings[model_name] = model_settings

        store_settings(
            api_key=str(current_settings.get("api_key", "")),
            mode=str(current_settings.get("mode", DEFAULT_MODE)),
            prompt=str(current_settings.get("prompt", "")),
            api_key_visible=bool(
                current_settings.get("api_key_visible", DEFAULT_API_KEY_VISIBLE)
            ),
            model=str(current_settings.get("model", "")),
            model_settings=(
                all_model_settings
                if isinstance(all_model_settings, dict)
                else None
            ),
        )
    except Exception as e:
        print(f"Error storing model settings for {model_name}: {e}")


def store_settings(
    api_key: str,
    mode: str,
    prompt: str,
    api_key_visible: bool,
    model: str = "",
    model_settings: Optional[Dict[str, Dict[str, Any]]] = None,
) -> None:
    """Store settings to config file"""
    if mode not in ("edit", "generate"):
        raise ValueError(f"Invalid mode: {mode}. Must be 'edit' or 'generate'")

    try:
        if not model:
            model = get_default_model_name()

        existing_settings = load_settings()
        existing_model_settings = existing_settings.get("model_settings", {})

        if model_settings:
            if isinstance(existing_model_settings, dict):
                existing_model_settings.update(model_settings)

        settings = {
            "api_key": api_key,
            "mode": mode,
            "prompt": prompt,
            "api_key_visible": api_key_visible,
            "model": model,
            "model_settings": existing_model_settings,
        }

        config_file = get_config_file()

        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2)

        if platform.system() != "Windows":
            os.chmod(config_file, FILE_PERMISSIONS)

    except (OSError, PermissionError) as e:
        print(f"Failed to store settings: {e}")
    except (TypeError, ValueError) as e:
        print(f"Invalid data for JSON encoding: {e}")
    except Exception as e:
        print(f"Unexpected error storing settings: {e}")


def _get_linux_config_dir() -> str:
    """Get Linux config directory"""
    return os.path.join(
        os.path.expanduser("~"), ".config", "GIMP", GIMP_VERSION
    )


def _get_macos_config_dir() -> str:
    """Get macOS config directory"""
    home = os.path.expanduser("~")
    return os.path.join(
        home, "Library", "Application Support", "GIMP", GIMP_VERSION
    )


def _get_windows_config_dir() -> str:
    """Get Windows config directory"""
    appdata = os.environ.get("APPDATA")
    if not appdata:
        appdata = os.path.expanduser("~\\AppData\\Roaming")
    return os.path.join(appdata, "GIMP", GIMP_VERSION)
