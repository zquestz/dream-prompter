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
from typing import List


def compile_translations() -> bool:
    """Compile all .po files to .mo files"""

    plugin_dir = Path(__file__).parent.parent
    os.chdir(plugin_dir)

    locale_dir = Path('locale')
    if not locale_dir.exists():
        print("No locale directory found!")
        print("Run 'python3 scripts/update-pot.py' first to create "
              "translations")
        return False

    po_files = get_po_files(locale_dir)

    if not po_files:
        print("No .po files found in locale/ directory")
        print("Create .po files from template or run translation scripts")
        return False

    print(f"Found {len(po_files)} translation files to compile")
    success_count = 0

    for po_file in sorted(po_files):
        lang_code = po_file.stem

        target_dir = locale_dir / lang_code / 'LC_MESSAGES'
        target_dir.mkdir(parents=True, exist_ok=True)
        mo_file = target_dir / 'dream-prompter.mo'

        print(f"Compiling {po_file.name} -> {mo_file.relative_to(locale_dir)}")

        try:
            cmd = ['msgfmt', '-o', str(mo_file), str(po_file)]
            result = subprocess.run(
                cmd, check=True, capture_output=True, text=True
            )

            if result.stderr:
                print(f"Warnings for {lang_code}: {result.stderr.strip()}")
            success_count += 1
            print(f"✓ Successfully compiled {lang_code}")

        except subprocess.CalledProcessError as e:
            print(f"✗ Error compiling {lang_code}:")
            if e.stderr:
                print(f"  {e.stderr.decode().strip()}")
            else:
                print(f"  {e}")

        except FileNotFoundError:
            print("✗ msgfmt not found. Please install gettext tools.")
            return False

    files_compiled = (
        f"{success_count}/{len(po_files)} files compiled successfully"
    )
    print(f"\nCompilation complete: {files_compiled}")
    return success_count > 0


def create_template_files() -> bool:
    """Create template .po files from .pot for manual language setup"""

    plugin_dir = Path(__file__).parent.parent
    os.chdir(plugin_dir)

    pot_file = Path('locale/dream-prompter.pot')
    if not pot_file.exists():
        print("No template found: locale/dream-prompter.pot")
        print("Run 'python3 scripts/update-pot.py' first")
        return False

    print("Translation Setup Instructions:")
    print("1. Copy template: cp locale/dream-prompter.pot locale/[LANG].po")
    print("   Example: cp locale/dream-prompter.pot locale/es.po")
    print("2. Edit locale/[LANG].po with your translations")
    print("3. Compile: python3 scripts/build-translations.py")
    return True


def get_po_files(locale_dir: Path) -> List[Path]:
    """Get list of .po files in the locale directory"""
    return [
        f for f in locale_dir.iterdir()
        if f.is_file() and f.suffix == '.po'
    ]


def print_usage() -> None:
    """Print usage information"""
    print("Dream Prompter Translation Builder")
    print("")
    print("Usage:")
    print("  python3 scripts/build-translations.py        "
          "# Compile translations")
    print("  python3 scripts/build-translations.py --init "
          "# Show setup instructions")
    print("  python3 scripts/build-translations.py --help "
          "# Show help")
    print("")
    print("This script compiles .po translation files to .mo binary files")
    print("that can be used by the Dream Prompter plugin.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == '--init':
            _ = create_template_files()
        elif sys.argv[1] in ['--help', '-h']:
            print_usage()
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print_usage()
            sys.exit(1)
    else:
        if compile_translations():
            print("Translation files built successfully!")
        else:
            print("Failed to build translation files.")
            sys.exit(1)
