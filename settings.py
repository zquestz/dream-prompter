#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Settings management for Dream Prompter plugin
"""

import json
import os
import platform
from typing import cast, Dict, Union, Literal

ModeKey = Literal["edit", "generate"]
SettingsDict = Dict[str, Union[str, bool]]

CONFIG_FILE_NAME = "dream-prompter-config.json"
GIMP_VERSION = "3.0"
FILE_PERMISSIONS = 0o600

DEFAULT_MODE = "edit"
DEFAULT_API_KEY_VISIBLE = False

def get_default_model_name() -> str:
    """Get default model name from factory"""
    try:
        from models.factory import model_factory
        return model_factory._default_model
    except ImportError:
        return "google/nano-banana"  # Fallback

DEFAULT_SETTINGS: SettingsDict = {
    "api_key": "",
    "mode": DEFAULT_MODE,
    "prompt": "",
    "api_key_visible": DEFAULT_API_KEY_VISIBLE,
    "model": ""
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

def load_settings() -> SettingsDict:
    """Load settings from config file"""
    try:
        config_file = get_config_file()
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
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

def store_settings(api_key: str, mode: str, prompt: str, api_key_visible: bool, model: str = "") -> None:
    """Store settings to config file"""
    if mode not in ("edit", "generate"):
        raise ValueError(f"Invalid mode: {mode}. Must be 'edit' or 'generate'")

    try:
        if not model:
            model = get_default_model_name()

        settings = {
            "api_key": api_key,
            "mode": mode,
            "prompt": prompt,
            "api_key_visible": api_key_visible,
            "model": model
        }

        config_file = get_config_file()

        with open(config_file, 'w', encoding='utf-8') as f:
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
    return os.path.join(os.path.expanduser("~"), '.config', 'GIMP', GIMP_VERSION)

def _get_macos_config_dir() -> str:
    """Get macOS config directory"""
    home = os.path.expanduser("~")
    return os.path.join(home, 'Library', 'Application Support', 'GIMP', GIMP_VERSION)

def _get_windows_config_dir() -> str:
    """Get Windows config directory"""
    appdata = os.environ.get('APPDATA')
    if not appdata:
        appdata = os.path.expanduser("~\\AppData\\Roaming")
    return os.path.join(appdata, 'GIMP', GIMP_VERSION)
