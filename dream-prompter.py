#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dream Prompter - Nano Banana GIMP Plugin
A GIMP plugin for AI-powered image creation/editing using Google's Nano Banana (Gemini 2.5 Flash Image)
"""

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gimp', '3.0')
gi.require_version('GimpUi', '3.0')
gi.require_version('GLib', '2.0')
import sys

from i18n import _, DOMAIN

from dialog import DreamPrompterDialog
from gi.repository import Gimp, GimpUi, Gtk, GLib

# Plugin metadata
PLUGIN_NAME = "dream-prompter"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "AI-powered image creation/editing with Nano Banana"

class DreamPrompter(Gimp.PlugIn):
    """Main plugin class"""

    def do_set_i18n(self, procname):
        """Enable localization"""
        return DOMAIN

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
                _("AI-powered image creation/editing with Nano Banana"),
                _("Transform existing images or generate new images using Google's Gemini 2.5 Flash Image model (Nano Banana) "
                  "with natural language prompts. Supports consistent multi-turn editing and image merging capabilities."),
                name
            )
            procedure.set_menu_label(_("Dream Prompter..."))
            procedure.set_attribution("Josh Ellithorpe", "Josh Ellithorpe", "2025")
            procedure.add_menu_path("<Image>/Filters/AI")

            return procedure
        return None

    def run_dream_prompter(self, procedure, run_mode, image, drawables, config, run_data):
        """Run the Dream Prompter plugin"""
        if run_mode == Gimp.RunMode.INTERACTIVE:
            GimpUi.init("dream-prompter")

            drawable = drawables[0] if drawables else None

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
