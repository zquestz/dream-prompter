import typing

from gi.repository import GObject
T = typing.TypeVar("T")

_namespace: str = "fontconfig"
_version: str = "2.0"

def init() -> None: ...

class CharSet(GObject.GPointer): ...

class Config(GObject.GPointer): ...

class Pattern(GObject.GPointer): ...

