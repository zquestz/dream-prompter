#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GIMP integration functions for Dream Prompter plugin
Handles all GIMP-specific operations like creating images and layers
"""

import os
import tempfile

from gi.repository import GdkPixbuf, Gimp, Gio

from i18n import _

MAX_LAYER_NAME_LENGTH = 64


def create_edit_layer(image, drawable, pixbuf, layer_name):
    """
    Create a new layer on existing image for AI edits

    Args:
        image (Gimp.Image): The existing image to add layer to
        drawable (Gimp.Drawable): Current selected drawable for positioning
        pixbuf (GdkPixbuf.Pixbuf): Pixbuf for the layer
        layer_name (str): Layer name for the new layer

    Returns:
        Gimp.Layer: The created layer, or None if failed
    """
    if not image:
        print("No image provided for edit layer")
        return None

    if not pixbuf:
        print("No pixbuf provided for edit layer")
        return None

    try:
        selection_bounds = get_selection_bounds(image)
        offset_x = 0
        offset_y = 0

        if selection_bounds:
            x, y, width, height = selection_bounds
            pixbuf = pixbuf.scale_simple(width, height, GdkPixbuf.InterpType.BILINEAR)
            offset_x = x
            offset_y = y
        else:
            img_width = image.get_width()
            img_height = image.get_height()
            pixbuf_width = pixbuf.get_width()
            pixbuf_height = pixbuf.get_height()

            if pixbuf_width != img_width or pixbuf_height != img_height:
                interp_type = GdkPixbuf.InterpType.BILINEAR
                pixbuf = pixbuf.scale_simple(img_width, img_height, interp_type)

        if not pixbuf.get_has_alpha():
            pixbuf = pixbuf.add_alpha(False, 0, 0, 0)

        new_layer = Gimp.Layer.new_from_pixbuf(
            image,
            _truncate_layer_name(layer_name),
            pixbuf,
            100,
            Gimp.LayerMode.NORMAL,
            0,
            1
        )

        if offset_x != 0 or offset_y != 0:
            new_layer.set_offsets(offset_x, offset_y)

        if drawable:
            parent = drawable.get_parent()
            position = image.get_item_position(drawable)
            image.insert_layer(new_layer, parent, position)
        else:
            image.insert_layer(new_layer, None, 0)

        image.set_selected_layers([new_layer])
        Gimp.displays_flush()

        print(f"Created edit layer: {layer_name}")
        return new_layer

    except Exception as e:
        print(f"Error creating edit layer: {e}")
        return None

    return None


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
        layer_name = f"Dream - {prompt}" if prompt else _("AI Generated")

        if not pixbuf.get_has_alpha():
            pixbuf = pixbuf.add_alpha(False, 0, 0, 0)

        layer = Gimp.Layer.new_from_pixbuf(
            image,
            _truncate_layer_name(layer_name),
            pixbuf,
            100,
            Gimp.LayerMode.NORMAL,
            0,
            1
        )

        image.insert_layer(layer, None, 0)
        display = Gimp.Display.new(image)

        if display:
            Gimp.displays_flush()

        print(f"Created new image with layer: {layer_name}")
        return image

    except Exception as e:
        print(f"Error creating new image: {e}")
        return None


def export_current_region_to_bytes(image):
    """
    Export the current region to PNG bytes (selection if active, otherwise full image)

    Args:
        image (Gimp.Image): GIMP image to export

    Returns:
        bytes: PNG image data, or None if failed
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
            print("Failed to crop image to selection")
            return None

        duplicate.flatten()

        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            temp_path = temp_file.name

        temp_gfile = Gio.File.new_for_path(temp_path)

        success = Gimp.file_save(
            Gimp.RunMode.NONINTERACTIVE,
            duplicate,
            temp_gfile,
            None
        )

        if not success:
            print("Failed to save region to temporary file")
            return None

        with open(temp_path, 'rb') as f:
            image_data = f.read()

        print(f"Exported current region to {len(image_data)} bytes")
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
            except Exception:
                pass


def export_gimp_image_to_bytes(image):
    """
    Export a GIMP image to PNG bytes

    Args:
        image (Gimp.Image): GIMP image to export

    Returns:
        bytes: PNG image data, or None if failed
    """
    if not image:
        print("No image provided for export")
        return None

    duplicate = None
    temp_path = None

    try:
        duplicate = image.duplicate()
        duplicate.flatten()

        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            temp_path = temp_file.name

        temp_gfile = Gio.File.new_for_path(temp_path)

        success = Gimp.file_save(
            Gimp.RunMode.NONINTERACTIVE,
            duplicate,
            temp_gfile,
            None
        )

        if not success:
            print("Failed to save image to temporary file")
            return None

        with open(temp_path, 'rb') as f:
            image_data = f.read()

        print(f"Exported GIMP image to {len(image_data)} bytes")
        return image_data

    except Exception as e:
        print(f"Error exporting GIMP image: {e}")
        return None
    finally:
        if duplicate:
            duplicate.delete()
        if temp_path:
            try:
                os.remove(temp_path)
            except Exception:
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


def _truncate_layer_name(name):
    """
    Truncate layer name to fit GIMP's limitations

    Args:
        name (str): Original layer name

    Returns:
        str: Truncated layer name
    """
    if not name:
        return _("AI Layer")

    if len(name) <= MAX_LAYER_NAME_LENGTH:
        return name

    return name[:MAX_LAYER_NAME_LENGTH-3] + "..."
