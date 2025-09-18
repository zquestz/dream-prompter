#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Build translation files for Dream Prompter plugin
Compiles .po files to .mo files
"""

import os
import subprocess
import sys
from pathlib import Path

def compile_translations() -> bool:
    """Compile all .po files to .mo files"""

    plugin_dir = Path(__file__).parent.parent
    os.chdir(plugin_dir)

    locale_dir = Path('locale')
    if not locale_dir.exists():
        print("No locale directory found!")
        return False

    po_files = [f for f in locale_dir.iterdir() if f.is_file() and f.suffix == '.po']

    if not po_files:
        print("No .po files found in locale/ directory")
        return False

    success_count = 0

    for po_file in sorted(po_files):
        lang_code = po_file.stem

        target_dir = locale_dir / lang_code / 'LC_MESSAGES'
        target_dir.mkdir(parents=True, exist_ok=True)
        mo_file = target_dir / 'dream-prompter.mo'

        print(f"Compiling {po_file} -> {mo_file}")

        try:
            cmd = ['msgfmt', '-o', str(mo_file), str(po_file)]
            _ = subprocess.run(cmd, check=True, capture_output=True)
            success_count += 1
            print(f"✓ Successfully compiled {lang_code}")

        except subprocess.CalledProcessError as e:
            print(f"✗ Error compiling {lang_code}: {e}")

        except FileNotFoundError:
            print("✗ msgfmt not found. Please install gettext tools.")
            return False

    print(f"\nCompilation complete: {success_count}/{len(po_files)} files compiled successfully")
    return success_count > 0

def create_template_files() -> bool:
    """Create template .po files from .pot for manual language setup"""

    pot_file = Path('locale/dream-prompter.pot')
    if not pot_file.exists():
        print("No template found: locale/dream-prompter.pot")
        print("Run 'python3 scripts/update-pot.py' first")
        return False

    print("To create a new language translation:")
    print("  cp locale/dream-prompter.pot locale/[LANG].po")
    print("  # Edit locale/[LANG].po with your translations")
    print("  python3 scripts/build-translations.py")
    return True

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--init':
        _ = create_template_files()
    else:
        if compile_translations():
            print("Translation files built successfully!")
        else:
            print("Failed to build translation files.")
            sys.exit(1)
