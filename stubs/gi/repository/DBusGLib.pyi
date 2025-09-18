import typing

from gi.repository import GObject
T = typing.TypeVar("T")

_namespace: str = "DBusGLib"
_version: str = "1.0"

class Connection(GObject.GPointer): ...

class MethodInvocation(GObject.GPointer): ...

class Proxy(GObject.Object): ...

class ProxyClass(GObject.GPointer): ...

