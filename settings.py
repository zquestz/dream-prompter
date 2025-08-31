#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Settings management for Dream Prompter plugin
"""

import json
import os
import platform

def get_config_file():
    """Get path to config file in GIMP's user directory"""
    system = platform.system()

    if system == "Windows":
        appdata = os.environ.get('APPDATA')
        if not appdata:
            appdata = os.path.expanduser("~\\AppData\\Roaming")
        gimp_dir = os.path.join(appdata, 'GIMP', '3.0')
    elif system == "Darwin":
        home = os.path.expanduser("~")
        gimp_dir = os.path.join(home, 'Library', 'Application Support', 'GIMP', '3.0')
    else:
        gimp_dir = os.path.join(os.path.expanduser("~"), '.config', 'GIMP', '3.0')

    try:
        os.makedirs(gimp_dir, exist_ok=True)
    except (OSError, PermissionError) as e:
        print(f"Warning: Could not create config directory {gimp_dir}: {e}")

    return os.path.join(gimp_dir, "dream-prompter-config.json")

def store_settings(api_key, mode, prompt, api_key_visible):
    """Store settings to config file"""
    try:
        settings = {
            "api_key": api_key,
            "mode": mode,
            "prompt": prompt,
            "api_key_visible": api_key_visible
        }

        config_file = get_config_file()

        with open(config_file, 'w') as f:
            json.dump(settings, f, indent=2)

        if platform.system() != "Windows":
            os.chmod(config_file, 0o600)

    except (OSError, PermissionError) as e:
        print(f"Failed to store settings: {e}")
    except (TypeError, ValueError) as e:
        print(f"Invalid data for JSON encoding: {e}")
    except Exception as e:
        print(f"Unexpected error storing settings: {e}")

def load_settings():
    """Load settings from config file"""
    try:
        config_file = get_config_file()
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return json.load(f)
    except (OSError, PermissionError) as e:
        print(f"Failed to read settings file: {e}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in settings file: {e}")
    except Exception as e:
        print(f"Unexpected error loading settings: {e}")

    return {
      "api_key": "",
      "mode": "edit",
      "prompt": "",
      "api_key_visible": False
    }
