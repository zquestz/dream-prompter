import typing

from gi.repository import GObject
T = typing.TypeVar("T")

_namespace: str = "DBus"
_version: str = "1.0"

class Connection(GObject.GPointer): ...

class Error(GObject.GPointer): ...

class Message(GObject.GPointer): ...

class MessageIter(GObject.GPointer): ...

class PendingCall(GObject.GPointer): ...

class BusType(GObject.GEnum):
    SESSION = 0
    STARTER = 2
    SYSTEM = 1

