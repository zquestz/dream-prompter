# Dream Prompter - GIMP Plugin Installation Guide

Dream Prompter is a GIMP plugin that brings Google's Nano Banana (Gemini 2.5 Flash Image) AI image editing and generation capabilities directly into GIMP.

## Features

- ✨ **AI-Powered Image Editing**: Transform existing images using natural language prompts
- 🎨 **AI Image Generation**: Create brand new images from scratch with text descriptions
- 🔄 **Consistent Multi-Turn Editing**: Make multiple edits while maintaining subject consistency
- 🖼️ **Image Merging**: Combine multiple images intelligently
- 🎯 **Dual Operation Modes**: Seamlessly switch between editing existing images and generating new ones
- 🏗️ **Native GIMP Integration**: Works within your GIMP workflow edits current layers or creates new ones
- 🌍 **Multi-Language Support**: Available in multiple languages with easy translation contribution

## Requirements

- GIMP 3.0.x
- Python 3.8+
- Google Gemini API key
- GTK 3.0

## Installation

### Method 1: Manual Installation (Current User)

1. **Locate your GIMP plugins directory:**
   - **Linux**: `~/.config/GIMP/3.0/plug-ins/`
   - **Windows**: `%APPDATA%\GIMP\3.0\plug-ins\`
   - **macOS**: `~/Library/Application Support/GIMP/3.0/plug-ins/`

2. **Create the plugin directory:**

   ```bash
   mkdir -p ~/.config/GIMP/3.0/plug-ins/dream-prompter/
   ```

3. **Copy plugin files:**

   ```bash
   cp *.py ~/.config/GIMP/3.0/plug-ins/dream-prompter/
   ```

4. **Build and copy translations:**

   ```bash
   # Build the translation files
   python3 scripts/build-translations.py

   # Copy the locale directory with translations
   cp -r locale ~/.config/GIMP/3.0/plug-ins/dream-prompter/
   ```

5. **Make the plugin executable:**

   ```bash
   chmod +x ~/.config/GIMP/3.0/plug-ins/dream-prompter/dream-prompter.py
   ```

### Method 2: Development Setup

For development or testing:

1. **Clone this repository:**

   ```bash
   git clone https://github.com/zquestz/dream-prompter.git
   cd dream-prompter
   ```

2. **Build translations:**

   ```bash
   python3 scripts/build-translations.py
   ```

3. **Create symlink to GIMP plugins directory:**
   ```bash
   ln -s $(pwd) ~/.config/GIMP/3.0/plug-ins/dream-prompter
   ```

### Method 3: System-wide Installation (All Users)

For system administrators who want to install the plugin for all users:

1. **Install to system plugins directory:**

   ```bash
   sudo mkdir -p /usr/lib/gimp/3.0/plug-ins/dream-prompter/
   sudo cp *.py /usr/lib/gimp/3.0/plug-ins/dream-prompter/
   sudo chmod +x /usr/lib/gimp/3.0/plug-ins/dream-prompter/dream-prompter.py
   ```

2. **Build and install translations:**

   ```bash
   # Build translations
   python3 scripts/build-translations.py

   # Copy locale directory
   sudo cp -r locale /usr/lib/gimp/3.0/plug-ins/dream-prompter/
   ```

3. **The plugin will now be available for all users on the system**

**Note**: System-wide installation requires administrator privileges and affects all GIMP users on the machine.

## Language Support

Dream Prompter supports multiple languages and automatically detects your system language.

### Available Languages

- **English** (default)
- **Spanish** - Complete translation
- **Other languages** - Ready for translation contributions

### Building Translations

If you're installing from source, you'll need to build the translation files:

```bash
# Build all available translations
# This creates .mo files in locale/[LANG]/LC_MESSAGES/ that GIMP can use
python3 scripts/build-translations.py
```

The plugin will automatically use your system language if a translation is available, otherwise it falls back to English.

## Getting a Google Gemini API Key

1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gemini API
4. Create credentials (API Key)
5. Secure your API key and note usage limits

## Usage

1. **Open/Create an image in GIMP**
2. **Launch the plugin:**
   - Go to **Filters** → **AI** → **Dream Prompter...**

3. **Configure the plugin:**
   - Enter your Google Gemini API key
   - Choose operation mode: Edit existing image or Generate new image
   - Write a descriptive prompt for your desired transformation or creation
   - (Optional) Select additional images to merge or reference

4. **Generate your AI edit:**
   - Click "Generate AI Edit"
   - Wait for processing to complete
   - The result will be added as a new layer

## Development

### Building Translations

For developers working on the plugin:

```bash
# Extract new translatable strings from code
python3 scripts/update-pot.py

# Update existing translation files with new strings
python3 scripts/update-translations.py

# Compile translations for distribution
python3 scripts/build-translations.py
```

## For Translators

Want to help translate Dream Prompter into your language? We'd love your contribution!

### Getting Started

1. **Check if your language needs translation:**

   ```bash
   # See what .po files exist
   ls locale/
   ```

2. **Create a new translation:**

   ```bash
   # Copy the template to create a new language file
   cp locale/dream-prompter.pot locale/[YOUR_LANG].po

   # For example, for French:
   cp locale/dream-prompter.pot locale/fr.po
   ```

3. **Edit your language file:**
   - Open `locale/[YOUR_LANG].po` in your favorite text editor
   - Or use a translation tool like Poedit, Lokalize, or Gtranslator
   - Translate the `msgstr ""` fields while keeping `msgid` unchanged

### Translation Guidelines

**UI Elements:**

- Keep button labels concise but clear
- Use your platform's standard terminology
- Be consistent throughout the translation

**Technical Terms:**

- "API key" - often kept as-is or adapted to local tech terminology
- "Prompt" - translate based on local AI/ML terminology usage
- "Layer" - use GIMP's existing translation for your language

**Example Prompts:**

- Adapt creative examples to be culturally appropriate
- Maintain the descriptive and inspiring nature
- Use natural, flowing language for your locale

**Formatting:**

- Keep HTML tags exactly as they are: `<b>Bold</b>`, `<a href="...">Link</a>`
- Preserve placeholder variables: `{url}`, `{count}`, `{mode}`
- Maintain line breaks and spacing in multi-line strings

### Testing Your Translation

1. **Build your translation:**

   ```bash
   python3 scripts/build-translations.py
   ```

2. **Test in GIMP:**
   - Install the plugin with your translation
   - Set your system language to your target language
   - Launch GIMP and test the plugin interface

3. **Check for:**
   - Text that overflows UI elements
   - Missing translations (English fallbacks)
   - Proper plural forms
   - Natural-sounding phrases in context

### Submitting Your Translation

1. **Fork this repository** on GitHub
2. **Add your `.po` file** to the `locale/` directory
3. **Test thoroughly** in GIMP
4. **Submit a pull request** with:
   - Your translation file (`locale/[LANG].po`)
   - Brief description of any cultural adaptations made
   - Screenshots if you needed to adjust UI layouts

### Translation Tools

**Recommended editors:**

- **Poedit** - User-friendly GUI with helpful features
- **Lokalize** - KDE's powerful translation tool
- **Gtranslator** - GNOME's translation editor
- **VS Code** - With gettext/po file extensions

**Priority Languages:**
We especially welcome translations for: French, German, Italian, Portuguese, Russian, Japanese, Korean, and Chinese.

## Troubleshooting

- **Permission denied**: Make sure the main `dream-prompter.py` file is executable (`chmod +x dream-prompter.py`)
- **Plugin loads but crashes**: Check GIMP's Error Console (`Windows` → `Dockable Dialogs` → `Error Console`) for specific error messages
- **Interface in wrong language**: Check your system locale settings, or ensure translation files are properly installed in the `locale/` directory
- **Missing translations**: Some text appears in English even with your language selected - this means those strings need translation contributions
