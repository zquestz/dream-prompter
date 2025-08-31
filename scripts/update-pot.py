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

def extract_strings():
    """Extract strings and create .pot file"""

    plugin_dir = Path(__file__).parent.parent
    os.chdir(plugin_dir)

    python_files = [
        'api.py',
        'dialog.py',
        'dialog_events.py',
        'dialog_gtk.py',
        'dialog_threads.py',
        'dream-prompter.py',
        'gimp_integration.py',
        'i18n.py',
        'settings.py'
    ]

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
        '--package-version=1.0.0',
        '--msgid-bugs-address=quest@mac.com',
        '--add-comments=TRANSLATORS'
    ] + python_files

    try:
        subprocess.run(cmd, check=True)
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
