#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GIMP integration functions for Dream Prompter plugin
Handles all GIMP-specific operations like creating images and layers
"""

import os
import tempfile
import textwrap

from gi.repository import Gimp, Gio

MAX_LAYER_NAME_LENGTH = 64

def create_new_image(pixbuf, prompt):
    """
    Create a new GIMP image in a new tab

    Args:
        pixbuf (GdkPixbuf.Pixbuf): Pixbuf to load into the new image
        prompt (str): Prompt text for layer naming

    Returns:
        Gimp.Image: The created image, or None if failed
    """

    if not pixbuf:
        print("No pixbuf provided for new image")
        return None

    try:
        width = pixbuf.get_width()
        height = pixbuf.get_height()
        image = Gimp.Image.new(width, height, Gimp.ImageBaseType.RGB)
        layer_name = textwrap.shorten(f"Dream - {prompt}", width=MAX_LAYER_NAME_LENGTH, placeholder="...")
        layer = Gimp.Layer.new_from_pixbuf(image, layer_name, pixbuf, 100, Gimp.LayerMode.NORMAL, 0, 1)

        image.insert_layer(layer, None, 0)
        Gimp.Display.new(image)

        return image

    except Exception as e:
        print(f"Error creating new image: {e}")
        return None

def create_edit_layer(image, drawable, pixbuf, prompt):
    """
    Create a new layer on existing image for AI edits

    Args:
        image (Gimp.Image): The existing image to add layer to
        drawable (Gimp.Drawable): Current selected drawable for positioning
        pixbuf (GdkPixbuf.Pixbuf): Pixbuf for the layer
        prompt (str): Prompt text for layer naming

    Returns:
        Gimp.Layer: The created layer, or None if failed
    """
    try:
        if not image:
            print("No image provided for edit layer")
            return None

        if not pixbuf:
            print("No pixbuf provided for edit layer")
            return None

        layer_name = textwrap.shorten(f"Edit - {prompt}", width=MAX_LAYER_NAME_LENGTH, placeholder="...")
        new_layer = Gimp.Layer.new_from_pixbuf(image, layer_name, pixbuf, 100, Gimp.LayerMode.NORMAL, 0, 1)

        if drawable:
            parent = drawable.get_parent()
            position = image.get_item_position(drawable)
            image.insert_layer(new_layer, parent, position)
        else:
            image.insert_layer(new_layer, None, 0)

        image.set_selected_layers([new_layer])

        return new_layer

    except Exception as e:
        print(f"Error creating edit layer: {e}")
        return None

def export_gimp_image_to_bytes(image):
    """
    Export a GIMP image to PNG bytes

    Args:
        image (Gimp.Image): GIMP image to export

    Returns:
        bytes: PNG image data, or None if failed
    """
    duplicate = None
    temp_path = None
    try:
        duplicate = image.duplicate()
        duplicate.flatten()

        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            temp_path = temp_file.name

        temp_gfile = Gio.File.new_for_path(temp_path)

        success = Gimp.file_save(Gimp.RunMode.NONINTERACTIVE, duplicate, temp_gfile, None)

        if not success:
            return None

        with open(temp_path, 'rb') as f:
            image_data = f.read()

        return image_data

    except Exception as e:
        print(f"Error exporting GIMP image: {e}")
        return None
    finally:
        # Always clean up resources
        if duplicate:
            duplicate.delete()
        if temp_path:
            try:
                os.remove(temp_path)
            except:
                pass
