import typing

from gi.repository import GObject
T = typing.TypeVar("T")

_namespace: str = "xfixes"
_version: str = "4.0"

class XserverRegion(GObject.GPointer): ...

