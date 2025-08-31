#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dream Prompter - Nano Banana GIMP Plugin
A GIMP plugin for AI-powered image editing and generation using Google's Nano Banana (Gemini 2.5 Flash Image)
"""

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gimp', '3.0')
gi.require_version('GimpUi', '3.0')
gi.require_version('GLib', '2.0')

from gi.repository import Gimp, GimpUi, GObject, Gtk, GLib
import sys
import os

# Plugin metadata
PLUGIN_NAME = "dream-prompter"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "AI-powered image editing and creation with Nano Banana"

class DreamPrompterDialog(GimpUi.Dialog):
    """Main dialog window for the Dream Prompter plugin"""

    def __init__(self, procedure, image, drawable):
        super().__init__(
            title="Dream Prompter - Nano Banana AI Image Creator and Editor",
            role="dream-prompter-dialog",
            use_header_bar=True
        )

        self.procedure = procedure
        self.image = image
        self.drawable = drawable

        # Set dialog properties
        self.set_default_size(600, 600)
        self.set_resizable(True)

        # Build the interface
        self._build_interface()

        # Connect signals
        self._connect_signals()

        # Set initial state based on whether we have an image/drawable
        self._set_initial_mode()

    def _build_interface(self):
        """Build the main plugin interface"""
        # Create main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        main_box.set_margin_top(12)
        main_box.set_margin_bottom(12)
        main_box.set_margin_start(12)
        main_box.set_margin_end(12)

        # API Key section (required for everything)
        api_key_section = self._create_api_key_section()
        main_box.pack_start(api_key_section, False, False, 0)

        # Mode selection section
        mode_section = self._create_mode_section()
        main_box.pack_start(mode_section, False, False, 0)

        # Prompt section
        prompt_section = self._create_prompt_section()
        main_box.pack_start(prompt_section, True, True, 0)

        # Additional images section
        images_section = self._create_additional_images_section()
        main_box.pack_start(images_section, False, False, 0)

        # Action buttons section
        buttons_section = self._create_buttons_section()
        main_box.pack_start(buttons_section, False, False, 0)

        # Status section
        status_section = self._create_status_section()
        main_box.pack_start(status_section, False, False, 0)

        # Add main container to dialog
        self.get_content_area().add(main_box)

    def _create_mode_section(self):
        """Create mode selection section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Section title
        title_label = Gtk.Label()
        title_label.set_markup("<b>Operation Mode</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        # Radio buttons container
        radio_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)

        # Edit mode radio
        self.edit_mode_radio = Gtk.RadioButton.new_with_label(None, "Edit existing image")
        radio_box.pack_start(self.edit_mode_radio, False, False, 0)

        # Generate mode radio
        self.generate_mode_radio = Gtk.RadioButton.new_with_label_from_widget(
            self.edit_mode_radio, "Generate new image"
        )
        radio_box.pack_start(self.generate_mode_radio, False, False, 0)

        section_box.pack_start(radio_box, False, False, 0)

        # Mode description
        self.mode_description = Gtk.Label()
        self.mode_description.set_halign(Gtk.Align.START)
        self.mode_description.get_style_context().add_class("dim-label")
        section_box.pack_start(self.mode_description, False, False, 0)

        return section_box

    def _set_initial_mode(self):
        """Set initial mode based on available image/drawable"""
        if not self.image or not self.drawable:
            # No image open - default to Generate mode, disable Edit
            self.generate_mode_radio.set_active(True)
            self.edit_mode_radio.set_sensitive(False)
            self.mode_description.set_text("No image open - only generation mode available")
        else:
            # Image open - default to Edit mode, both options available
            self.edit_mode_radio.set_active(True)
            self.edit_mode_radio.set_sensitive(True)
            self.generate_mode_radio.set_sensitive(True)
            self.mode_description.set_text("Edit the current layer using AI")

        # Update UI based on initial mode
        self._on_mode_changed(None)

    def _on_mode_changed(self, radio_button):
        """Handle mode selection changes"""
        if self.edit_mode_radio.get_active():
            # Edit mode
            if self.drawable:
                self.mode_description.set_text("Edit the current layer using AI")
            else:
                self.mode_description.set_text("No layer available to edit")
            self.generate_btn.set_label("Generate AI Edit")
            self.images_help_label.set_markup('<small>Select additional images to merge or reference in your AI edit</small>')
        else:
            # Generate mode
            if self.image:
                self.mode_description.set_text("Create a new image and add it as a layer to the current project")
            else:
                self.mode_description.set_text("Create a new image in a new GIMP project")
            self.generate_btn.set_label("Generate New Image")
            self.images_help_label.set_markup('<small>Select reference images to influence the style or composition of your new image</small>')

        # Update prompt examples
        self._update_prompt_examples()

        # Update button state
        self._update_generate_button_state()

    def _update_generate_button_state(self):
        """Update generate button sensitivity based on input state"""
        # Get current values
        text = self.prompt_buffer.get_text(
            self.prompt_buffer.get_start_iter(),
            self.prompt_buffer.get_end_iter(),
            False
        ).strip()

        # Just check if there's any text (no more placeholder checking needed)
        has_text = bool(text)
        has_api_key = bool(self.api_key_entry.get_text().strip())

        # In edit mode, also need a drawable
        if self.edit_mode_radio.get_active():
            has_drawable = self.drawable is not None
            self.generate_btn.set_sensitive(has_text and has_api_key and has_drawable)
        else:
            # Generate mode doesn't need a drawable
            self.generate_btn.set_sensitive(has_text and has_api_key)


    def _create_api_key_section(self):
        """Create API key input section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Section title
        title_label = Gtk.Label()
        title_label.set_markup("<b>Google Gemini API Key</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        # API key input container
        key_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        # API key entry
        self.api_key_entry = Gtk.Entry()
        self.api_key_entry.set_placeholder_text("Enter your Google Gemini API key...")
        self.api_key_entry.set_visibility(False)  # Hide the text for security
        self.api_key_entry.set_input_purpose(Gtk.InputPurpose.PASSWORD)
        key_container.pack_start(self.api_key_entry, True, True, 0)

        # Show/hide toggle button
        self.toggle_visibility_btn = Gtk.ToggleButton()
        self.toggle_visibility_btn.set_image(Gtk.Image.new_from_icon_name("view-conceal-symbolic", Gtk.IconSize.BUTTON))
        self.toggle_visibility_btn.set_tooltip_text("Show/Hide API key")
        key_container.pack_start(self.toggle_visibility_btn, False, False, 0)

        section_box.pack_start(key_container, False, False, 0)

        # Help text
        help_label = Gtk.Label()
        help_label.set_markup('<small>Get your API key from <a href="https://console.cloud.google.com/">Google Cloud Console</a></small>')
        help_label.set_halign(Gtk.Align.START)
        help_label.set_line_wrap(True)
        section_box.pack_start(help_label, False, False, 0)

        return section_box

    def _create_prompt_section(self):
        """Create prompt input section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Section title
        title_label = Gtk.Label()
        title_label.set_markup("<b>AI Prompt</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        # Prompt text view with scroll
        scroll_window = Gtk.ScrolledWindow()
        scroll_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll_window.set_min_content_height(120)

        self.prompt_textview = Gtk.TextView()
        self.prompt_textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.prompt_buffer = self.prompt_textview.get_buffer()

        scroll_window.add(self.prompt_textview)
        section_box.pack_start(scroll_window, True, True, 0)

        # Prompt examples
        self.examples_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
        self._update_prompt_examples()
        section_box.pack_start(self.examples_box, False, False, 0)

        return section_box

    def _update_prompt_examples(self):
        """Update prompt examples based on current mode"""
        # Clear existing examples
        for child in self.examples_box.get_children():
            self.examples_box.remove(child)

        examples_label = Gtk.Label()
        examples_label.set_markup('<small><b>Example prompts:</b></small>')
        examples_label.set_halign(Gtk.Align.START)
        self.examples_box.pack_start(examples_label, False, False, 0)

        if self.edit_mode_radio.get_active():
            # Edit mode examples
            example_texts = [
                "• Change the background to a medieval castle",
                "• Make this person wear a red dress instead",
                "• Add snow falling in the scene",
                "• Transform this into a painting style"
            ]
        else:
            # Generate mode examples
            example_texts = [
                "• A majestic dragon flying over a mountain range",
                "• Portrait of a woman in Victorian dress",
                "• Cyberpunk cityscape at night with neon lights",
                "• Peaceful forest clearing with sunbeams"
            ]

        for example in example_texts:
            example_label = Gtk.Label()
            example_label.set_markup(f'<small><i>{example}</i></small>')
            example_label.set_halign(Gtk.Align.START)
            self.examples_box.pack_start(example_label, False, False, 0)

        self.examples_box.show_all()

    def _create_additional_images_section(self):
        """Create additional images selection section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Section title
        title_label = Gtk.Label()
        title_label.set_markup("<b>Additional Images (Optional)</b>")
        title_label.set_halign(Gtk.Align.START)
        section_box.pack_start(title_label, False, False, 0)

        # File selection container
        files_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        # File chooser button
        self.file_chooser_btn = Gtk.Button()
        self.file_chooser_btn.set_label("Select Images...")
        self.file_chooser_btn.set_image(Gtk.Image.new_from_icon_name("document-open-symbolic", Gtk.IconSize.BUTTON))
        files_container.pack_start(self.file_chooser_btn, False, False, 0)

        # Selected files info
        self.files_info_label = Gtk.Label()
        self.files_info_label.set_text("No additional images selected")
        self.files_info_label.set_halign(Gtk.Align.START)
        self.files_info_label.get_style_context().add_class("dim-label")
        files_container.pack_start(self.files_info_label, True, True, 0)

        # Clear files button
        self.clear_files_btn = Gtk.Button()
        self.clear_files_btn.set_image(Gtk.Image.new_from_icon_name("edit-clear-symbolic", Gtk.IconSize.BUTTON))
        self.clear_files_btn.set_tooltip_text("Clear selected files")
        self.clear_files_btn.set_sensitive(False)
        files_container.pack_start(self.clear_files_btn, False, False, 0)

        section_box.pack_start(files_container, False, False, 0)

        # Selected files list
        self.files_listbox = Gtk.ListBox()
        self.files_listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.files_listbox.get_style_context().add_class("content")
        self.files_listbox.set_visible(False)
        section_box.pack_start(self.files_listbox, False, False, 0)

        # Help text
        self.images_help_label = Gtk.Label()
        self.images_help_label.set_markup('<small>Select additional images to merge or reference in your AI edit</small>')
        self.images_help_label.set_halign(Gtk.Align.START)
        self.images_help_label.set_line_wrap(True)
        section_box.pack_start(self.images_help_label, False, False, 0)

        # Store selected files
        self.selected_files = []

        return section_box

    def _create_buttons_section(self):
        """Create action buttons section"""
        buttons_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        buttons_box.set_halign(Gtk.Align.CENTER)

        # Cancel button
        self.cancel_btn = Gtk.Button()
        self.cancel_btn.set_label("Cancel")
        self.cancel_btn.set_size_request(100, -1)
        buttons_box.pack_start(self.cancel_btn, False, False, 0)

        # Generate/Edit button (text changes based on mode)
        self.generate_btn = Gtk.Button()
        self.generate_btn.set_label("Generate AI Edit")
        self.generate_btn.set_image(Gtk.Image.new_from_icon_name("applications-graphics-symbolic", Gtk.IconSize.BUTTON))
        self.generate_btn.get_style_context().add_class("suggested-action")
        self.generate_btn.set_size_request(150, -1)
        buttons_box.pack_start(self.generate_btn, False, False, 0)

        return buttons_box

    def _create_status_section(self):
        """Create status display section"""
        section_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Status bar
        self.status_label = Gtk.Label()
        self.status_label.set_text("Ready")
        self.status_label.set_halign(Gtk.Align.START)
        self.status_label.get_style_context().add_class("dim-label")
        section_box.pack_start(self.status_label, False, False, 0)

        # Progress bar (hidden by default)
        self.progress_bar = Gtk.ProgressBar()
        self.progress_bar.set_show_text(True)
        self.progress_bar.set_visible(False)
        section_box.pack_start(self.progress_bar, False, False, 0)

        return section_box

    def _connect_signals(self):
        """Connect UI signals to handlers"""
        # Mode selection
        self.edit_mode_radio.connect("toggled", self._on_mode_changed)
        self.generate_mode_radio.connect("toggled", self._on_mode_changed)

        # API key visibility toggle
        self.toggle_visibility_btn.connect("toggled", self._on_toggle_visibility)

        # File chooser
        self.file_chooser_btn.connect("clicked", self._on_select_files)
        self.clear_files_btn.connect("clicked", self._on_clear_files)

        # Action buttons
        self.cancel_btn.connect("clicked", self._on_cancel)
        self.generate_btn.connect("clicked", self._on_generate)

        # Text changes
        self.prompt_buffer.connect("changed", self._on_prompt_changed)
        self.api_key_entry.connect("changed", self._on_api_key_changed)

    def _on_toggle_visibility(self, button):
        """Toggle API key visibility"""
        if button.get_active():
            self.api_key_entry.set_visibility(True)
            button.set_image(Gtk.Image.new_from_icon_name("view-reveal-symbolic", Gtk.IconSize.BUTTON))
            button.set_tooltip_text("Hide API key")
        else:
            self.api_key_entry.set_visibility(False)
            button.set_image(Gtk.Image.new_from_icon_name("view-conceal-symbolic", Gtk.IconSize.BUTTON))
            button.set_tooltip_text("Show API key")

    def _on_select_files(self, button):
        """Handle file selection"""
        dialog = Gtk.FileChooserDialog(
            title="Select Additional Images",
            parent=self,
            action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            "Cancel", Gtk.ResponseType.CANCEL,
            "Select", Gtk.ResponseType.OK
        )

        # Set up file filters
        filter_images = Gtk.FileFilter()
        filter_images.set_name("Image files")
        filter_images.add_mime_type("image/jpeg")
        filter_images.add_mime_type("image/png")
        filter_images.add_mime_type("image/gif")
        filter_images.add_mime_type("image/bmp")
        filter_images.add_mime_type("image/tiff")
        dialog.add_filter(filter_images)

        dialog.set_select_multiple(True)

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            files = dialog.get_filenames()
            self.selected_files.extend(files)
            self._update_files_display()

        dialog.destroy()

    def _on_clear_files(self, button):
        """Clear selected files"""
        self.selected_files.clear()
        self._update_files_display()

    def _update_files_display(self):
        """Update the files display"""
        if not self.selected_files:
            self.files_info_label.set_text("No additional images selected")
            self.files_listbox.set_visible(False)
            self.clear_files_btn.set_sensitive(False)
        else:
            count = len(self.selected_files)
            self.files_info_label.set_text(f"{count} image{'s' if count != 1 else ''} selected")
            self.clear_files_btn.set_sensitive(True)

            # Clear existing list items
            for child in self.files_listbox.get_children():
                self.files_listbox.remove(child)

            # Add file items
            for file_path in self.selected_files:
                filename = os.path.basename(file_path)
                row = Gtk.ListBoxRow()

                file_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
                file_box.set_margin_top(3)
                file_box.set_margin_bottom(3)
                file_box.set_margin_start(6)
                file_box.set_margin_end(6)

                # File icon
                icon = Gtk.Image.new_from_icon_name("image-x-generic-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
                file_box.pack_start(icon, False, False, 0)

                # File name
                label = Gtk.Label()
                label.set_text(filename)
                label.set_halign(Gtk.Align.START)
                label.set_ellipsize(3)  # Pango.EllipsizeMode.END
                file_box.pack_start(label, True, True, 0)

                # Remove button
                remove_btn = Gtk.Button()
                remove_btn.set_image(Gtk.Image.new_from_icon_name("edit-delete-symbolic", Gtk.IconSize.SMALL_TOOLBAR))
                remove_btn.set_relief(Gtk.ReliefStyle.NONE)
                remove_btn.connect("clicked", self._on_remove_file, file_path)
                file_box.pack_start(remove_btn, False, False, 0)

                row.add(file_box)
                self.files_listbox.add(row)

            self.files_listbox.set_visible(True)
            self.files_listbox.show_all()

    def _on_remove_file(self, button, file_path):
        """Remove a specific file from selection"""
        if file_path in self.selected_files:
            self.selected_files.remove(file_path)
            self._update_files_display()

    def _on_prompt_changed(self, buffer):
        """Handle prompt text changes"""
        self._update_generate_button_state()

    def _on_api_key_changed(self, entry):
        """Handle API key changes"""
        self._update_generate_button_state()

    def _on_cancel(self, button):
        """Handle cancel button"""
        self.response(Gtk.ResponseType.CANCEL)

    def _on_generate(self, button):
        """Handle generate button - this is where we'll integrate the API later"""
        # Get the current values
        api_key = self.api_key_entry.get_text().strip()
        prompt_text = self.prompt_buffer.get_text(
            self.prompt_buffer.get_start_iter(),
            self.prompt_buffer.get_end_iter(),
            False
        ).strip()

        if not api_key:
            self._show_error("Please enter your Google Gemini API key")
            return

        if not prompt_text:
            self._show_error("Please enter a prompt")
            return

        # Check mode-specific requirements
        if self.edit_mode_radio.get_active() and not self.drawable:
            self._show_error("Edit mode requires a selected layer")
            return

        # Show processing
        mode = "Edit" if self.edit_mode_radio.get_active() else "Generate"
        self._set_status(f"Processing {mode.lower()} request...")
        self.progress_bar.set_visible(True)
        self.progress_bar.pulse()

        # TODO: Replace this simulation with actual Gemini API call
        # - Send image + prompt to Google Gemini API
        # - Handle response and create new layer with result
        # - Maintain consistency for multi-turn editing
        print(f"Mode: {mode}")
        print(f"API Key: {'*' * len(api_key)}")
        print(f"Prompt: {prompt_text}")
        print(f"Additional files: {self.selected_files}")
        print(f"Current image: {self.image}")
        print(f"Current drawable: {self.drawable}")

        GLib.timeout_add_seconds(2, self._finish_processing)

    def _finish_processing(self):
        """Finish the processing simulation"""
        mode = "edit" if self.edit_mode_radio.get_active() else "generation"
        self._set_status(f"Ready for API integration! (Last: {mode} mode)")
        self.progress_bar.set_visible(False)
        return False  # Don't repeat the timeout

    def _show_error(self, message):
        """Show error message"""
        dialog = Gtk.MessageDialog(
            parent=self,
            flags=Gtk.DialogFlags.MODAL,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=message
        )
        dialog.run()
        dialog.destroy()

    def _set_status(self, message):
        """Update status message"""
        self.status_label.set_text(message)


class DreamPrompter(Gimp.PlugIn):
    """Main plugin class"""

    ## Parameters ##
    __gproperties__ = {
        "dummy": (str,
                  "Dummy property",
                  "Dummy property to avoid errors",
                  "",
                  GObject.ParamFlags.READWRITE),
    }

    ## GimpPlugIn virtual methods ##
    def do_query_procedures(self):
        """Register the plugin procedure"""
        return ['dream-prompter']

    def do_create_procedure(self, name):
        """Create the plugin procedure"""
        if name == 'dream-prompter':
            procedure = Gimp.ImageProcedure.new(
                self,
                name,
                Gimp.PDBProcType.PLUGIN,
                self.run_dream_prompter,
                None
            )
            procedure.set_image_types("*")
            procedure.set_sensitivity_mask(Gimp.ProcedureSensitivityMask.ALWAYS)
            procedure.set_documentation(
                "AI-powered image editing and generation with Nano Banana",
                "Transform existing images or generate new images using Google's Gemini 2.5 Flash Image model (Nano Banana) "
                "with natural language prompts. Supports consistent multi-turn editing and "
                "image merging capabilities.",
                name
            )
            procedure.set_menu_label("Dream Prompter...")
            procedure.set_attribution("Josh Ellithorpe", "Josh Ellithorpe", "2025")
            procedure.add_menu_path("<Image>/Filters/AI")

            return procedure
        return None

    def run_dream_prompter(self, procedure, run_mode, image, drawables, config, run_data):
        """Run the Dream Prompter plugin"""
        if run_mode == Gimp.RunMode.INTERACTIVE:
            # Initialize GTK if needed
            GimpUi.init("dream-prompter")

            # Get the active drawable (may be None)
            drawable = drawables[0] if drawables else None

            # Show the dialog (works with or without drawable/image)
            dialog = DreamPrompterDialog(procedure, image, drawable)
            dialog.show_all()

            response = dialog.run()
            dialog.destroy()

            if response == Gtk.ResponseType.OK:
                return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())
            else:
                return procedure.new_return_values(Gimp.PDBStatusType.CANCEL, GLib.Error())

        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


# Register the plugin
Gimp.main(DreamPrompter.__gtype__, sys.argv)
