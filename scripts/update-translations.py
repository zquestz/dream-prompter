#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Update existing translation files for Dream Prompter plugin
Merges new strings from .pot template into existing .po files
"""

import os
import subprocess
import sys
from pathlib import Path


def update_po_file(po_file: Path, pot_file: Path) -> bool:
    """Update a single .po file with new strings from .pot template"""

    print(f"Updating {po_file}...")

    try:
        cmd = [
            'msgmerge',
            '--update',
            '--backup=off',
            '--sort-output',
            str(po_file),
            str(pot_file)
        ]

        _ = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✓ Updated {po_file.name}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"✗ Error updating {po_file.name}: {e}")
        return False

    except FileNotFoundError:
        print("✗ msgmerge not found. Install gettext tools.")
        return False


def find_po_files() -> list[Path]:
    """Find all .po files directly in the locale directory"""

    locale_dir = Path('locale')
    if not locale_dir.exists():
        print("No locale directory found!")
        return []

    po_files = [f for f in locale_dir.iterdir() if f.is_file() and f.suffix == '.po']

    if not po_files:
        print("No .po files found in locale/ directory")
        return []

    return po_files


def update_all_translations() -> bool:
    """Update all existing .po files with new strings from .pot template"""

    plugin_dir = Path(__file__).parent.parent
    os.chdir(plugin_dir)

    pot_file = Path('locale/dream-prompter.pot')
    if not pot_file.exists():
        print("Translation template not found: locale/dream-prompter.pot")
        print("Run 'python3 scripts/update-pot.py' first")
        return False

    po_files = find_po_files()
    if not po_files:
        return False

    print(f"Found {len(po_files)} translation file(s) to update")

    success_count = 0

    for po_file in sorted(po_files):
        if update_po_file(po_file, pot_file):
            success_count += 1

    print(f"Update complete: {success_count}/{len(po_files)} files updated")
    return success_count == len(po_files)


if __name__ == '__main__':
    if update_all_translations():
        print("✓ All translations updated successfully!")
    else:
        print("✗ Some translations failed to update")
        sys.exit(1)
