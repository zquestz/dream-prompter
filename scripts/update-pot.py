#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Extract translatable strings from Dream Prompter plugin
This script creates the .pot template file for translations
"""

import os
import subprocess
import sys
from pathlib import Path


def discover_python_files() -> list[str]:
    """Automatically discover Python files in the plugin directory"""
    python_files = []

    for file_path in Path('.').glob('*.py'):
        python_files.append(str(file_path))

    models_dir = Path('models')
    if models_dir.exists():
        for file_path in models_dir.glob('*.py'):
            python_files.append(str(file_path))

    return sorted(python_files)


def extract_strings() -> bool:
    """Extract strings and create .pot file"""

    plugin_dir = Path(__file__).parent.parent
    os.chdir(plugin_dir)

    python_files = discover_python_files()

    if not python_files:
        print("No Python files found to extract strings from!")
        return False

    print(f"Extracting strings from {len(python_files)} Python files:")
    for f in python_files:
        print(f"  - {f}")

    pot_file = 'locale/dream-prompter.pot'

    os.makedirs('locale', exist_ok=True)

    cmd = [
        'xgettext',
        '--language=Python',
        '--keyword=_',
        '--keyword=N_',
        '--output=' + pot_file,
        '--from-code=UTF-8',
        '--copyright-holder=Josh Ellithorpe',
        '--package-name=Dream Prompter',
        '--package-version=1.1.0',
        '--msgid-bugs-address=quest@mac.com',
        '--add-comments=TRANSLATORS'
    ] + python_files

    try:
        _ = subprocess.run(cmd, check=True)
        print(f"Successfully created {pot_file}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error running xgettext: {e}")
        print("Please install gettext tools (xgettext)")
        return False


if __name__ == '__main__':
    if extract_strings():
        print("Translation template created successfully!")
    else:
        sys.exit(1)
