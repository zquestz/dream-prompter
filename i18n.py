"""
Internationalization support for Dream Prompter plugin
"""

import gettext
import locale
import os
from collections.abc import Callable

DOMAIN = "dream-prompter"

GetTextFunc = Callable[[str], str]
NGetTextFunc = Callable[[str, str, int], str]


def _fallback_gettext(message: str) -> str:
    """Return the message untranslated"""
    return message


def _fallback_ngettext(singular: str, plural: str, n: int) -> str:
    """Select an untranslated form using English plural rules"""
    return singular if n == 1 else plural


def setup_i18n() -> tuple[GetTextFunc, NGetTextFunc]:
    """
    Initialize internationalization support

    Returns:
        Tuple of (gettext, ngettext) callables
    """
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    locale_dir = os.path.join(plugin_dir, "locale")

    try:
        locale.setlocale(locale.LC_ALL, "")
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, "C.UTF-8")
        except locale.Error:
            locale.setlocale(locale.LC_ALL, "C")

    try:
        translation = gettext.translation(DOMAIN, locale_dir, fallback=True)
        translation.install(names=["ngettext"])
        return translation.gettext, translation.ngettext
    except OSError as e:
        print(f"Translation files not found: {e}")
    except Exception as e:
        print(f"Unexpected i18n error: {e}")

    import builtins

    builtins.__dict__["_"] = _fallback_gettext
    builtins.__dict__["ngettext"] = _fallback_ngettext
    return _fallback_gettext, _fallback_ngettext


_, ngettext = setup_i18n()
