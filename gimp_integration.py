#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GIMP integration functions for Dream Prompter plugin
Handles all GIMP-specific operations like creating images and layers
"""

from gi.repository import Gimp

def create_new_image(image_data=None, width=400, height=400):
    """
    Create a new GIMP image in a new tab

    Args:
        image_data (GdkPixbuf.Pixbuf): Optional pixbuf to load
        width (int): Width for new image if no data provided
        height (int): Height for new image if no data provided

    Returns:
        Gimp.Image: The created image, or None if failed
    """
    try:
        if image_data:
            width = image_data.get_width()
            height = image_data.get_height()
            image = Gimp.Image.new(width, height, Gimp.ImageBaseType.RGB)
            layer = Gimp.Layer.new_from_pixbuf(image, "Generated", image_data, 100, Gimp.LayerMode.NORMAL, 0, 1)

        else:
            image = Gimp.Image.new(width, height, Gimp.ImageBaseType.RGB)
            layer = Gimp.Layer.new(image, "Generated", width, height,
                                   Gimp.ImageType.RGB_IMAGE, 100, Gimp.LayerMode.NORMAL)

        image.insert_layer(layer, None, 0)
        Gimp.Display.new(image)

        return image

    except Exception as e:
        print(f"Error creating new image: {e}")
        return None

def create_edit_layer(image, drawable=None, image_data=None):
    """
    Create a new layer on existing image for AI edits

    Args:
        image (Gimp.Image): The existing image to add layer to
        drawable (Gimp.Drawable): Current selected drawable for positioning
        image_data (GdkPixbuf.Pixbuf): Optional pixbuf for the layer

    Returns:
        Gimp.Layer: The created layer, or None if failed
    """
    try:
        if not image:
            print("No image provided for edit layer")
            return None

        if image_data:
            new_layer = Gimp.Layer.new_from_pixbuf(image, "AI Edit", image_data, 100, Gimp.LayerMode.NORMAL, 0, 1)
        else:
            width = image.get_width()
            height = image.get_height()
            new_layer = Gimp.Layer.new(image, "AI Edit", width, height,
                                       Gimp.ImageType.RGB_IMAGE, 100, Gimp.LayerMode.NORMAL)

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
