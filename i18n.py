#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Internationalization support for Dream Prompter plugin
"""

import os
import gettext
import locale

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
    except Exception:
        import builtins
        builtins.__dict__['_'] = lambda x: x
        return lambda x: x

def get_language_code():
    """Get the current language code"""
    try:
        lang = locale.getdefaultlocale()[0]
        if lang:
            return lang.split('_')[0]
        pass
    except Exception:
        return 'en'

# Initialize i18n and make _ function globally available
_ = setup_i18n()
