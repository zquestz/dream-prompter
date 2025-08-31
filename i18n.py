#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Internationalization support for Dream Prompter plugin
"""

import gettext
import locale
import os

DOMAIN = "dream-prompter"

def setup_i18n():
    """Initialize internationalization support"""
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    locale_dir = os.path.join(plugin_dir, "locale")

    try:
        locale.setlocale(locale.LC_ALL, '')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'C.UTF-8')
        except locale.Error:
            locale.setlocale(locale.LC_ALL, 'C')

    try:
        translation = gettext.translation(DOMAIN, locale_dir, fallback=True)
        translation.install()
        return translation.gettext
    except (OSError, IOError) as e:
        print(f"Translation files not found: {e}")
        import builtins
        builtins.__dict__['_'] = lambda x: x
        return lambda x: x
    except Exception as e:
        print(f"Unexpected i18n error: {e}")
        import builtins
        builtins.__dict__['_'] = lambda x: x
        return lambda x: x

_ = setup_i18n()
