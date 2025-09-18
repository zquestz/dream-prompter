#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GIMP integration functions for Dream Prompter plugin
Handles all GIMP-specific operations like creating images and layers
"""

import os
import tempfile
import textwrap

from gi.repository import GdkPixbuf, Gimp, Gio

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

        if not pixbuf.get_has_alpha():
            pixbuf = pixbuf.add_alpha(False, 0, 0, 0)

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

        selection_bounds = get_selection_bounds(image)
        offset_x = 0
        offset_y = 0

        if selection_bounds:
            x, y, width, height = selection_bounds
            pixbuf = pixbuf.scale_simple(width, height, GdkPixbuf.InterpType.BILINEAR)
            offset_x = x
            offset_y = y

        if not pixbuf.get_has_alpha():
            pixbuf = pixbuf.add_alpha(False, 0, 0, 0)

        new_layer = Gimp.Layer.new_from_pixbuf(image, layer_name, pixbuf, 100, Gimp.LayerMode.NORMAL, 0, 1)

        if offset_x != 0 or offset_y != 0:
            new_layer.set_offsets(offset_x, offset_y)

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

def get_selection_bounds(image):
    """
    Get the bounds of the current selection

    Args:
        image (Gimp.Image): GIMP image

    Returns:
        tuple: (x, y, width, height) of selection, or None if no selection
    """
    if not image:
        return None

    try:
        selection = image.get_selection()
        if selection:
            success, has_selection, x1, y1, x2, y2 = selection.bounds(image)

            if success and has_selection:
                width = x2 - x1
                height = y2 - y1
                return (x1, y1, width, height)
        return None

    except Exception as e:
        print(f"Error getting selection bounds: {e}")
        return None

def has_active_selection(image):
    """
    Check if image has an active selection (not full image)

    Args:
        image (Gimp.Image): GIMP image to check

    Returns:
        bool: True if there's an active selection that's not the full image
    """
    if not image:
        return False

    try:
        bounds = get_selection_bounds(image)

        if not bounds:
            return False

        x, y, width, height = bounds

        img_width = image.get_width()
        img_height = image.get_height()

        if x == 0 and y == 0 and width == img_width and height == img_height:
            return False

        return True

    except Exception as e:
        print(f"Error checking selection: {e}")
        return False

def export_current_region_to_bytes(image):
    """
    Export the current region to PNG bytes (selection if active, otherwise full image)
    """
    if not has_active_selection(image):
        return export_gimp_image_to_bytes(image)

    duplicate = None
    temp_path = None
    try:
        bounds = get_selection_bounds(image)
        if not bounds:
            return export_gimp_image_to_bytes(image)

        x, y, width, height = bounds
        duplicate = image.duplicate()

        success = duplicate.crop(width, height, x, y)
        if not success:
            return None

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
        print(f"Error exporting current region: {e}")
        return None
    finally:
        if duplicate:
            duplicate.delete()
        if temp_path:
            try:
                os.remove(temp_path)
            except:
                pass
