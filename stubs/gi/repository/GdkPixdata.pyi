import typing

from gi.repository import GLib
from gi.repository import GObject
from gi.repository import GdkPixbuf
T = typing.TypeVar("T")

PIXBUF_MAGIC_NUMBER: int = 1197763408
PIXDATA_HEADER_LENGTH: int = 24
_namespace: str = "GdkPixdata"
_version: str = "2.0"

def pixbuf_from_pixdata(pixdata: Pixdata, copy_pixels: bool) -> GdkPixbuf.Pixbuf: ...

class Pixdata(GObject.GPointer):
    """
    :Constructors:

    ::

        Pixdata()
    """
    magic: int = ...
    length: int = ...
    pixdata_type: int = ...
    rowstride: int = ...
    width: int = ...
    height: int = ...
    pixel_data: bytes = ...
    def deserialize(self, stream: typing.Sequence[int]) -> bool: ...
    def serialize(self) -> bytes: ...
    def to_csource(self, name: str, dump_type: PixdataDumpType) -> GLib.String: ...
    

class PixdataDumpType(GObject.GFlags):
    CONST = 1024
    CTYPES = 256
    GTYPES = 0
    MACROS = 2
    PIXDATA_STREAM = 0
    PIXDATA_STRUCT = 1
    RLE_DECODER = 65536
    STATIC = 512

class PixdataType(GObject.GFlags):
    COLOR_TYPE_MASK = 255
    COLOR_TYPE_RGB = 1
    COLOR_TYPE_RGBA = 2
    ENCODING_MASK = 251658240
    ENCODING_RAW = 16777216
    ENCODING_RLE = 33554432
    SAMPLE_WIDTH_8 = 65536
    SAMPLE_WIDTH_MASK = 983040

