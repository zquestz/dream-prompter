import typing

from gi.repository import GObject
T = typing.TypeVar("T")

_namespace: str = "xft"
_version: str = "2.0"

def init() -> None: ...

class Color(GObject.GPointer): ...

class Draw(GObject.GPointer): ...

class Font(GObject.GPointer): ...

class GlyphSpec(GObject.GPointer): ...

