import typing

from gi.repository import GObject
T = typing.TypeVar("T")

_namespace: str = "cairo"
_version: str = "1.0"

def image_surface_create() -> None: ...

class Context(GObject.GBoxed): ...

class Device(GObject.GBoxed): ...

class FontFace(GObject.GBoxed): ...

class FontOptions(GObject.GBoxed): ...

class Matrix(GObject.GPointer): ...

class Path(GObject.GPointer): ...

class Pattern(GObject.GBoxed): ...

class Rectangle(GObject.GBoxed):
    """
    :Constructors:

    ::

        Rectangle()
    """
    x: float = ...
    y: float = ...
    width: float = ...
    height: float = ...

class RectangleInt(GObject.GBoxed):
    """
    :Constructors:

    ::

        RectangleInt()
    """
    x: int = ...
    y: int = ...
    width: int = ...
    height: int = ...

class Region(GObject.GBoxed): ...

class ScaledFont(GObject.GBoxed): ...

class Surface(GObject.GBoxed): ...

class Antialias(GObject.GEnum):
    BEST = 6
    DEFAULT = 0
    FAST = 4
    GOOD = 5
    GRAY = 2
    NONE = 1
    SUBPIXEL = 3

class Content(GObject.GEnum):
    ALPHA = 8192
    COLOR = 4096
    COLOR_ALPHA = 12288

class Extend(GObject.GEnum):
    NONE = 0
    PAD = 3
    REFLECT = 2
    REPEAT = 1

class FillRule(GObject.GEnum):
    EVEN_ODD = 1
    WINDING = 0

class Filter(GObject.GEnum):
    BEST = 2
    BILINEAR = 4
    FAST = 0
    GAUSSIAN = 5
    GOOD = 1
    NEAREST = 3

class FontSlant(GObject.GEnum):
    ITALIC = 1
    NORMAL = 0
    OBLIQUE = 2

class FontType(GObject.GEnum):
    FT = 1
    QUARTZ = 3
    TOY = 0
    USER = 4
    WIN32 = 2

class FontWeight(GObject.GEnum):
    BOLD = 1
    NORMAL = 0

class HintMetrics(GObject.GEnum):
    DEFAULT = 0
    OFF = 1
    ON = 2

class HintStyle(GObject.GEnum):
    DEFAULT = 0
    FULL = 4
    MEDIUM = 3
    NONE = 1
    SLIGHT = 2

class LineCap(GObject.GEnum):
    BUTT = 0
    ROUND = 1
    SQUARE = 2

class LineJoin(GObject.GEnum):
    BEVEL = 2
    MITER = 0
    ROUND = 1

class Operator(GObject.GEnum):
    ADD = 12
    ATOP = 5
    CLEAR = 0
    COLOR_BURN = 20
    COLOR_DODGE = 19
    DARKEN = 17
    DEST = 6
    DEST_ATOP = 10
    DEST_IN = 8
    DEST_OUT = 9
    DEST_OVER = 7
    DIFFERENCE = 23
    EXCLUSION = 24
    HARD_LIGHT = 21
    HSL_COLOR = 27
    HSL_HUE = 25
    HSL_LUMINOSITY = 28
    HSL_SATURATION = 26
    IN = 3
    LIGHTEN = 18
    MULTIPLY = 14
    OUT = 4
    OVER = 2
    OVERLAY = 16
    SATURATE = 13
    SCREEN = 15
    SOFT_LIGHT = 22
    SOURCE = 1
    XOR = 11

class PathDataType(GObject.GEnum):
    CLOSE_PATH = 3
    CURVE_TO = 2
    LINE_TO = 1
    MOVE_TO = 0

class RegionOverlap(GObject.GEnum):
    IN = 0
    OUT = 1
    PART = 2

class Status(GObject.GEnum):
    CLIP_NOT_REPRESENTABLE = 22
    DEVICE_ERROR = 35
    DEVICE_FINISHED = 37
    DEVICE_TYPE_MISMATCH = 34
    FILE_NOT_FOUND = 18
    FONT_TYPE_MISMATCH = 25
    INVALID_CLUSTERS = 29
    INVALID_CONTENT = 15
    INVALID_DASH = 19
    INVALID_DSC_COMMENT = 20
    INVALID_FORMAT = 16
    INVALID_INDEX = 21
    INVALID_MATRIX = 5
    INVALID_MESH_CONSTRUCTION = 36
    INVALID_PATH_DATA = 9
    INVALID_POP_GROUP = 3
    INVALID_RESTORE = 2
    INVALID_SIZE = 32
    INVALID_SLANT = 30
    INVALID_STATUS = 6
    INVALID_STRIDE = 24
    INVALID_STRING = 8
    INVALID_VISUAL = 17
    INVALID_WEIGHT = 31
    JBIG2_GLOBAL_MISSING = 38
    NEGATIVE_COUNT = 28
    NO_CURRENT_POINT = 4
    NO_MEMORY = 1
    NULL_POINTER = 7
    PATTERN_TYPE_MISMATCH = 14
    READ_ERROR = 10
    SUCCESS = 0
    SURFACE_FINISHED = 12
    SURFACE_TYPE_MISMATCH = 13
    TEMP_FILE_ERROR = 23
    USER_FONT_ERROR = 27
    USER_FONT_IMMUTABLE = 26
    USER_FONT_NOT_IMPLEMENTED = 33
    WRITE_ERROR = 11

class SubpixelOrder(GObject.GEnum):
    BGR = 2
    DEFAULT = 0
    RGB = 1
    VBGR = 4
    VRGB = 3

class TextClusterFlags(GObject.GEnum):
    BACKWARD = 1

