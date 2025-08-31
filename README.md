# Dream Prompter - GIMP Plugin Installation Guide

Dream Prompter is a GIMP plugin that brings Google's Nano Banana (Gemini 2.5 Flash Image) AI image editing and generation capabilities directly into GIMP.

## Features

- ✨ **AI-Powered Image Editing**: Transform existing images using natural language prompts
- 🎨 **AI Image Generation**: Create brand new images from scratch with text descriptions
- 🔄 **Consistent Multi-Turn Editing**: Make multiple edits while maintaining subject consistency
- 🖼️ **Image Merging**: Combine multiple images intelligently
- 🎯 **Dual Operation Modes**: Seamlessly switch between editing existing images and generating new ones
- 🏗️ **Native GIMP Integration**: Works within your GIMP workflow edits current layers or creates new ones

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
   cp dream-prompter.py ~/.config/GIMP/3.0/plug-ins/dream-prompter/
   cp dream-prompter.css ~/.config/GIMP/3.0/plug-ins/dream-prompter/
   ```

4. **Make the plugin executable:**

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

2. **Create symlink to GIMP plugins directory:**
   ```bash
   ln -s $(pwd) ~/.config/GIMP/3.0/plug-ins/dream-prompter
   ```

### Method 3: System-wide Installation (All Users)

For system administrators who want to install the plugin for all users:

1. **Install to system plugins directory:**

   ```bash
   sudo mkdir -p /usr/lib/gimp/3.0/plug-ins/dream-prompter/
   sudo cp dream-prompter.py /usr/lib/gimp/3.0/plug-ins/dream-prompter/
   sudo cp dream-prompter.css /usr/lib/gimp/3.0/plug-ins/dream-prompter/
   sudo chmod +x /usr/lib/gimp/3.0/plug-ins/dream-prompter/dream-prompter.py
   ```

2. **The plugin will now be available for all users on the system**

**Note**: System-wide installation requires administrator privileges and affects all GIMP users on the machine.

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

## Example Prompts

### Image Editing Prompts

Transform existing images with these types of prompts:

- `"Change the background to a medieval castle"`
- `"Make this person wear a red dress instead"`
- `"Add snow falling in the scene"`
- `"Transform this into a painting style"`
- `"Replace the sky with a starry night"`
- `"Make the person look like a superhero"`
- `"Convert this to black and white with red highlights"`
- `"Add dramatic lighting from the left side"`

### Image Generation Prompts

Create brand new images with these types of prompts:

- `"A majestic dragon flying over a mountain range at sunset"`
- `"Portrait of a woman in Victorian dress, oil painting style"`
- `"Cyberpunk cityscape at night with neon lights reflecting on wet streets"`
- `"Peaceful forest clearing with sunbeams filtering through ancient trees"`
- `"Steampunk robot in a workshop surrounded by gears and steam"`
- `"Abstract composition with flowing colors in blue and gold"`
- `"Cozy library with floating books and magical glowing orbs"`
- `"Minimalist landscape with geometric mountains and a single moon"`

## Troubleshooting

- **Permission denied**: Make sure the `.py` file is executable (`chmod +x dream-prompter.py`)
- **Plugin loads but crashes**: Check GIMP's Error Console (`Windows` → `Dockable Dialogs` → `Error Console`) for specific error messages
