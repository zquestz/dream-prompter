# Translation Scripts

This directory contains scripts for managing translations for the Dream Prompter GIMP plugin.

## Scripts Overview

### `update-pot.py`

Extracts translatable strings from Python source files and creates/updates the translation template.

**Usage:**

```bash
python3 scripts/update-pot.py
```

**What it does:**

- Automatically discovers all Python files in the project
- Extracts strings marked with `_()` function calls
- Creates `locale/dream-prompter.pot` template file
- Lists all files being processed

### `update-translations.py`

Updates existing translation files with new strings from the template.

**Usage:**

```bash
python3 scripts/update-translations.py
```

**What it does:**

- Merges new strings from `.pot` template into existing `.po` files
- Preserves existing translations
- Marks new strings as "untranslated"
- Updates all `.po` files found in `locale/` directory

### `build-translations.py`

Compiles translation files into binary format for use by the plugin.

**Usage:**

```bash
# Compile all translations
python3 scripts/build-translations.py

# Show setup instructions for new languages
python3 scripts/build-translations.py --init

# Show help
python3 scripts/build-translations.py --help
```

**What it does:**

- Compiles `.po` files to `.mo` binary files
- Creates proper directory structure (`locale/LANG/LC_MESSAGES/`)
- Shows compilation status and warnings
- Places files where GIMP can find them

## Translation Workflow

### 1. Extract Strings

First, extract all translatable strings from the source code:

```bash
python3 scripts/update-pot.py
```

### 2. Create New Language

To add a new language (e.g., Spanish):

```bash
cp locale/dream-prompter.pot locale/es.po
```

Edit `locale/es.po` with your translations using a text editor or translation tool like Poedit.

### 3. Update Existing Translations

When source code changes, update existing translations:

```bash
python3 scripts/update-translations.py
```

### 4. Compile Translations

Convert translations to binary format:

```bash
python3 scripts/build-translations.py
```

## Requirements

These scripts require the **gettext** tools to be installed:

**Ubuntu/Debian:**

```bash
sudo apt install gettext
```

**macOS:**

```bash
brew install gettext
```

**Arch:**

```bash
sudo pacman -S gettext
```

**Other systems:** Install the `gettext` package through your package manager.

## File Structure

After running the scripts, your translation files will be organized like this:

```
locale/
├── dream-prompter.pot          # Translation template
├── es.po                       # Spanish translations (source)
├── fr.po                       # French translations (source)
├── es/
│   └── LC_MESSAGES/
│       └── dream-prompter.mo   # Spanish compiled translations
└── fr/
    └── LC_MESSAGES/
        └── dream-prompter.mo   # French compiled translations
```

## Common Language Codes

- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ja` - Japanese
- `zh` - Chinese
- `ru` - Russian
- `ar` - Arabic
- `hi` - Hindi

## Troubleshooting

**Error: "msgfmt not found"**

- Install gettext tools (see Requirements section above)

**Error: "No .po files found"**

- Create translation files first using the workflow above
- Make sure `.po` files are in the `locale/` directory

**Error: "No template found"**

- Run `python3 scripts/update-pot.py` first to create the template

## Contributing Translations

To contribute a new language translation:

1. Follow the workflow above to create a new `.po` file
2. Translate all strings in the file
3. Test the translation by compiling and using the plugin
4. Submit the `.po` file in a pull request

Translations help make Dream Prompter accessible to users worldwide!
