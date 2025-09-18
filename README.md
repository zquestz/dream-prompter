# Dream Prompter - GIMP Plugin

Dream Prompter brings Google's Nano Banana (Gemini 2.5 Flash Image Preview) AI capabilities directly into GIMP for intelligent image generation and editing.

![Dream Prompter](screenshots/dream-prompter.png)

## Features

- 🎨 **AI Image Generation**: Create new images from text descriptions
- ✨ **AI Image Editing**: Transform existing images with natural language prompts
- 🖼️ **Reference Images**: Use up to 3 reference images for generation, 2 for editing
- 🔄 **Smart Layer Management**: Automatically creates properly named layers
- 🎯 **Dual Operation Modes**: Seamlessly switch between editing and generation
- 🌍 **Multi-Language Support**: Setup to support multiple languages via i18n
- 🔒 **Safe File Handling**: Validates image formats and file sizes
- 🏗️ **Native GIMP Integration**: Works seamlessly within your GIMP workflow

## Installation

### Prerequisites

- **GIMP 3.0.x**
- **Python 3.8+**
- **Google Gemini API key** (paid account required)

Install the required Python library:

```bash
pip install google-genai
```

### Quick Install

1. **Download the latest release** from [GitHub Releases](https://github.com/zquestz/dream-prompter/releases)

2. **Extract the release**

   This will create a folder named `dream-prompter-{version}` (e.g., `dream-prompter-1.0.0`)

3. **Move to your GIMP plugins folder with the correct name:**

   Rename and move the extracted folder to exactly `dream-prompter` in your GIMP plugins directory:
   - **Linux**: `~/.config/GIMP/3.0/plug-ins/dream-prompter/`
   - **Windows**: `%APPDATA%\GIMP\3.0\plug-ins\dream-prompter\`
   - **macOS**: `~/Library/Application Support/GIMP/3.0/plug-ins/dream-prompter/`

   Example for Linux:

   ```bash
   # Extract creates dream-prompter-1.0.0/
   unzip dream-prompter-1.0.0.zip
   # Move to correct location with correct name
   mv dream-prompter-1.0.0 ~/.config/GIMP/3.0/plug-ins/dream-prompter
   ```

4. **Make executable** (Linux/macOS only):

   ```bash
   chmod +x ~/.config/GIMP/3.0/plug-ins/dream-prompter/dream-prompter.py
   ```

5. **Restart GIMP**

**Building translations (optional):** If you need languages other than English, run `python3 scripts/build-translations.py` in the plugin directory after installation.

### Arch Linux Installation

To install Dream Prompter on Arch Linux, you can install it from the AUR.

```bash
yay -S dream-prompter
```

### Advanced Installation

#### Manual Installation from Source

1. **Find your GIMP plugins directory** (paths listed above)

2. **Create plugin directory:**

   ```bash
   mkdir -p ~/.config/GIMP/3.0/plug-ins/dream-prompter/
   ```

3. **Copy all Python files:**

   ```bash
   cp *.py ~/.config/GIMP/3.0/plug-ins/dream-prompter/
   ```

4. **Build and install translations (Optional):**

   ```bash
   python3 scripts/build-translations.py
   cp -r locale ~/.config/GIMP/3.0/plug-ins/dream-prompter/
   ```

5. **Make executable:**
   ```bash
   chmod +x ~/.config/GIMP/3.0/plug-ins/dream-prompter/dream-prompter.py
   ```

#### Development Setup

```bash
git clone https://github.com/zquestz/dream-prompter.git
cd dream-prompter
pip install google-genai
python3 scripts/build-translations.py # optional, defaults to English
ln -s $(pwd) ~/.config/GIMP/3.0/plug-ins/dream-prompter
```

### Python Dependencies Note

**Important**: Use the same Python that GIMP uses. If `pip install google-genai` doesn't work:

```bash
# System-wide installation
sudo pip install google-genai

# User installation (recommended)
pip install --user google-genai

# Ensure Python 3
pip3 install google-genai
```

#### macOS Instructions

If you get the **"google-genai not installed"** error on macOS:

1. **Locate GIMP's Python** by opening the Python Console: `Filters → Development → Python-Fu`
2. **Run this command** in the console:

   ```python
   import sys; print(sys.executable)
   ```

   You should see something like:

   ```
   /Applications/GIMP.app/Contents/MacOS/python3
   ```

3. **Install google-genai using GIMP's Python** from Terminal:

   ```bash
   # Change to GIMP's Python directory
   cd /Applications/GIMP.app/Contents/MacOS

   # Ensure pip is installed
   ./python3 -m ensurepip

   # Install google-genai
   ./python3 -m pip install google-genai
   ```

## Getting Your API Key

**Important**: The Gemini 2.5 Flash Image Preview model (Nano Banana) requires a **paid Google Cloud account** with billing enabled. Free tier accounts cannot access the image generation capabilities.

1. **Visit [Google AI Studio](https://aistudio.google.com/)**
2. **Create or select a project**
3. **Enable billing** for your Google Cloud account
4. **Generate an API key**
5. **Keep your key secure and monitor usage/costs**

### API Specifications

- **Model**: `gemini-2.5-flash-image-preview` (Nano Banana)
- **Billing**: **Paid account required** - image generation is not available on free tier
- **Image Limits**:
  - Generation mode: Up to 3 reference images
  - Edit mode: Up to 2 reference images (current image + 2 = 3 total)
- **File Size**: Maximum 7MB per image
- **Formats**: PNG, JPEG, WebP only

### Cost Considerations

- Each image generation/edit counts toward your API usage
- Monitor your usage at [Google AI Studio](https://aistudio.google.com/) to avoid unexpected charges
- Consider setting up billing alerts in Google Cloud Console

## Usage

### Basic Workflow

1. **Open an image in GIMP** (for editing) or create a new document (for generation)
2. **Launch Dream Prompter**: `Filters → AI → Dream Prompter...`
3. **Enter your API key** (saved automatically for future use)
4. **Select mode**:
   - **Edit Mode**: Transform the current layer
   - **Generate Mode**: Create a new image
5. **Write your prompt**: Be descriptive and specific
6. **Add reference images** (optional): Click "Select Images..." to add references
7. **Generate**: Click the generate button and watch the progress
8. **Result**: New layer appears with a descriptive name

### Example Prompts

**For Generation:**

- "A majestic dragon flying over snow-capped mountains at sunset"
- "Portrait of a woman in Victorian dress, oil painting style"
- "Cyberpunk cityscape with neon reflections on wet streets"

**For Editing:**

- "Change the background to a peaceful forest clearing"
- "Make this person wear a red Victorian dress"
- "Transform this into a watercolor painting style"
- "Add falling snow to this winter scene"

### Tips for Best Results

- **Be specific**: "Red sports car" vs "bright red Ferrari 488 GTB"
- **Include style**: "photorealistic", "oil painting", "digital art"
- **Describe lighting**: "golden hour", "dramatic shadows", "soft natural light"
- **Use reference images** to guide style and composition
- **Keep files under 7MB** for reference images

## Language Support

### Available Languages

Dream Prompter is fully translated and available in:

- **🇺🇸 English** (default)
- **🇪🇸 Spanish** (complete)
- **🇫🇷 French** (complete)
- **🇵🇹 Portuguese** (complete)
- **🇷🇺 Russian** (complete)
- **🇯🇵 Japanese** (complete)
- **🇮🇳 Hindi** (complete)
- **🇧🇩 Bengali** (complete)
- **🇨🇳 Chinese (Simplified)** (complete)
- **🇹🇼 Chinese (Traditional)** (complete)
- **🇰🇷 Korean** (complete)

The plugin automatically detects your system language and uses the appropriate translation. If your language isn't available, it defaults to English.

### For Developers

```bash
# Extract new translatable strings
python3 scripts/update-pot.py

# Update existing translations
python3 scripts/update-translations.py

# Build compiled translations
python3 scripts/build-translations.py
```

## Architecture

The plugin is organized into focused modules:

- **`dream-prompter.py`** - Main GIMP plugin entry point
- **`dialog_gtk.py`** - GTK user interface components
- **`dialog_events.py`** - Event handling and user interactions
- **`dialog_threads.py`** - Background processing and threading
- **`api.py`** - Google Gemini API integration
- **`integrator.py`** - GIMP-specific operations
- **`settings.py`** - Configuration persistence
- **`i18n.py`** - Internationalization support

## Troubleshooting

### Common Issues

**"google-genai not installed" warning**

- Install with: `pip install google-genai`
- Ensure you're using GIMP's Python environment

**Plugin doesn't appear in menu**

- Check file permissions: `chmod +x dream-prompter.py`
- Restart GIMP after installation
- Verify files are in correct plugins directory

**API errors**

- Verify your API key is correct
- **Ensure billing is enabled** - free accounts cannot access image generation
- Check your quota at [Google AI Studio](https://aistudio.google.com/)
- Monitor costs to avoid unexpected charges

**Image processing issues**

- Reference images must be under 7MB
- Only PNG, JPEG, WebP formats supported
- Maximum 3 images for generation, 2 for editing

**Interface problems**

- Check GIMP's Error Console: `Windows → Dockable Dialogs → Error Console`
- Ensure translations are built: `python3 scripts/build-translations.py`
- Report UI issues with screenshots

### Getting Help

1. **Check the Error Console** in GIMP for specific error messages
2. **Verify all requirements** are installed correctly
3. **Test with simple prompts** first
4. **Check file permissions** on the plugin directory
5. **Review API quotas** if getting timeout errors

## Contributing

### For Translators

We welcome translations! Here's how to contribute:

1. **Copy the template**: `cp locale/dream-prompter.pot locale/[YOUR_LANG].po`
2. **Translate the strings** using Poedit, Lokalize, or any text editor
3. **Test your translation**: Build with `python3 scripts/build-translations.py`
4. **Submit a pull request** with your `.po` file

**Translation Guidelines:**

- Keep UI text concise but clear
- Use GIMP's existing terminology for your language
- Preserve HTML tags and placeholders like `{count}`, `{url}`
- Test that text fits in the interface

### For Developers

1. **Fork the repository**
2. **Create a feature branch**
3. **Follow the existing code style**
4. **Update translations** if adding new strings
5. **Submit a pull request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

Built with Google's Gemini 2.5 Flash Image Preview (Nano Banana) API.
