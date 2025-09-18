import typing

from gi.repository import GObject
T = typing.TypeVar("T")

_namespace: str = "freetype2"
_version: str = "2.0"

def library_version() -> None: ...

class Bitmap(GObject.GPointer): ...

class Face(GObject.GPointer): ...

class Library(GObject.GPointer): ...

