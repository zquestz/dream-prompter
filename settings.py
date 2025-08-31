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
        gimp_dir = os.path.join(os.environ.get('APPDATA', ''), 'GIMP', '3.0')
    elif system == "Darwin":
        home = os.path.expanduser("~")
        gimp_dir = os.path.join(home, 'Library', 'Application Support', 'GIMP', '3.0')
    else:
        gimp_dir = os.path.join(os.path.expanduser("~"), '.config', 'GIMP', '3.0')

    os.makedirs(gimp_dir, exist_ok=True)
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

        with open(get_config_file(), 'w') as f:
            json.dump(settings, f, indent=2)

        if platform.system() != "Windows":
            os.chmod(get_config_file(), 0o600)

    except Exception as e:
        print(f"Failed to store settings: {e}")

def load_settings():
    """Load settings from config file"""
    try:
        config_file = get_config_file()
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Failed to load settings: {e}")

    return {"api_key": "", "mode": "edit", "prompt": "", "api_key_visible": False}
