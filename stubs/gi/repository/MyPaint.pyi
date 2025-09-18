import typing

from gi.repository import GObject
T = typing.TypeVar("T")

_namespace: str = "MyPaint"
_version: str = "1.6"

def brush_input_from_cname(cname: str) -> BrushInput: ...
def brush_input_info(id: BrushInput) -> BrushInputInfo: ...
def brush_setting_from_cname(cname: str) -> BrushSetting: ...
def brush_setting_info(id: BrushSetting) -> BrushSettingInfo: ...

class Brush(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> MyPaint.Brush
        new_with_buckets(num_smudge_buckets:int) -> MyPaint.Brush
    """
    def from_defaults(self) -> None: ...
    def from_string(self, string: str) -> bool: ...
    def get_base_value(self, id: BrushSetting) -> float: ...
    def get_inputs_used_n(self, id: BrushSetting) -> int: ...
    def get_mapping_n(self, id: BrushSetting, input: BrushInput) -> int: ...
    def get_mapping_point(self, id: BrushSetting, input: BrushInput, index: int) -> typing.Tuple[float, float]: ...
    def get_state(self, i: BrushState) -> float: ...
    def get_total_stroke_painting_time(self) -> float: ...
    @staticmethod
    def input_from_cname(cname: str) -> BrushInput: ...
    def is_constant(self, id: BrushSetting) -> bool: ...
    @classmethod
    def new(cls) -> Brush: ...
    def new_stroke(self) -> None: ...
    @classmethod
    def new_with_buckets(cls, num_smudge_buckets: int) -> Brush: ...
    def reset(self) -> None: ...
    def set_base_value(self, id: BrushSetting, value: float) -> None: ...
    def set_mapping_n(self, id: BrushSetting, input: BrushInput, n: int) -> None: ...
    def set_mapping_point(self, id: BrushSetting, input: BrushInput, index: int, x: float, y: float) -> None: ...
    def set_print_inputs(self, enabled: bool) -> None: ...
    def set_state(self, i: BrushState, value: float) -> None: ...
    @staticmethod
    def setting_from_cname(cname: str) -> BrushSetting: ...
    def stroke_to(self, surface: Surface, x: float, y: float, pressure: float, xtilt: float, ytilt: float, dtime: float) -> int: ...
    

class BrushInputInfo(GObject.GPointer):
    """
    :Constructors:

    ::

        BrushInputInfo()
    """
    cname: str = ...
    hard_min: float = ...
    soft_min: float = ...
    normal: float = ...
    soft_max: float = ...
    hard_max: float = ...
    name: str = ...
    tooltip: str = ...
    def get_name(self) -> str: ...
    def get_tooltip(self) -> str: ...
    

class BrushSettingInfo(GObject.GPointer):
    """
    :Constructors:

    ::

        BrushSettingInfo()
    """
    cname: str = ...
    name: str = ...
    constant: bool = ...
    min: float = ...
    def_: float = ...
    max: float = ...
    tooltip: str = ...
    def get_name(self) -> str: ...
    def get_tooltip(self) -> str: ...
    

class FixedTiledSurface(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(width:int, height:int) -> MyPaint.FixedTiledSurface
    """
    def get_height(self) -> int: ...
    def get_width(self) -> int: ...
    def interface(self) -> Surface: ...
    @classmethod
    def new(cls, width: int, height: int) -> FixedTiledSurface: ...
    

class Rectangle(GObject.GBoxed):
    """
    :Constructors:

    ::

        Rectangle()
    """
    x: int = ...
    y: int = ...
    width: int = ...
    height: int = ...
    def copy(self) -> Rectangle: ...
    def expand_to_include_point(self, x: int, y: int) -> None: ...
    def expand_to_include_rect(self, other: Rectangle) -> None: ...
    

class Rectangles(GObject.GPointer):
    """
    :Constructors:

    ::

        Rectangles()
    """
    num_rectangles: int = ...
    rectangles: Rectangle = ...

class Surface(GObject.GBoxed):
    """
    :Constructors:

    ::

        Surface()
    """
    draw_dab: typing.Callable[[Surface, float, float, float, float, float, float, float, float, float, float, float, float, float], int] = ...
    get_color: typing.Callable[[Surface, float, float, float, float, float, float, float], None] = ...
    begin_atomic: typing.Callable[[Surface], None] = ...
    end_atomic: typing.Callable[[Surface, Rectangle], None] = ...
    destroy: typing.Callable[[Surface], None] = ...
    save_png: typing.Callable[[Surface, str, int, int, int, int], None] = ...
    refcount: int = ...
    def begin_atomic(self) -> None: ...
    def draw_dab(self, x: float, y: float, radius: float, color_r: float, color_g: float, color_b: float, opaque: float, hardness: float, alpha_eraser: float, aspect_ratio: float, angle: float, lock_alpha: float, colorize: float) -> int: ...
    def end_atomic(self) -> Rectangle: ...
    def get_alpha(self, x: float, y: float, radius: float) -> float: ...
    def get_color(self, x: float, y: float, radius: float, color_r: float, color_g: float, color_b: float, color_a: float) -> None: ...
    def save_png(self, path: str, x: int, y: int, width: int, height: int) -> None: ...
    

class TileRequest(GObject.GPointer):
    """
    :Constructors:

    ::

        TileRequest()
    """
    tx: int = ...
    ty: int = ...
    readonly: bool = ...
    buffer: int = ...
    context: None = ...
    thread_id: int = ...
    mipmap_level: int = ...
    def init(self, level: int, tx: int, ty: int, readonly: bool) -> None: ...
    

class TiledSurface(GObject.GPointer):
    """
    :Constructors:

    ::

        TiledSurface()
    """
    parent: Surface = ...
    tile_request_start: typing.Callable[[TiledSurface, TileRequest], None] = ...
    tile_request_end: typing.Callable[[TiledSurface, TileRequest], None] = ...
    surface_do_symmetry: bool = ...
    surface_center_x: float = ...
    operation_queue: None = ...
    dirty_bbox: Rectangle = ...
    threadsafe_tile_requests: bool = ...
    tile_size: int = ...
    def get_alpha(self, x: float, y: float, radius: float) -> float: ...
    def set_symmetry_state(self, active: bool, center_x: float) -> None: ...
    def tile_request_end(self, request: TileRequest) -> None: ...
    def tile_request_start(self, request: TileRequest) -> None: ...
    

class BrushInput(GObject.GEnum):
    INPUTS_COUNT = 18
    INPUT_ATTACK_ANGLE = 10
    INPUT_BARREL_ROTATION = 16
    INPUT_BRUSH_RADIUS = 17
    INPUT_CUSTOM = 8
    INPUT_DIRECTION = 5
    INPUT_DIRECTION_ANGLE = 9
    INPUT_GRIDMAP_X = 13
    INPUT_GRIDMAP_Y = 14
    INPUT_PRESSURE = 0
    INPUT_RANDOM = 3
    INPUT_SPEED1 = 1
    INPUT_SPEED2 = 2
    INPUT_STROKE = 4
    INPUT_TILT_ASCENSION = 7
    INPUT_TILT_DECLINATION = 6
    INPUT_TILT_DECLINATIONX = 11
    INPUT_TILT_DECLINATIONY = 12
    INPUT_VIEWZOOM = 15

class BrushSetting(GObject.GEnum):
    SETTINGS_COUNT = 64
    SETTING_ANTI_ALIASING = 5
    SETTING_CHANGE_COLOR_H = 24
    SETTING_CHANGE_COLOR_HSL_S = 26
    SETTING_CHANGE_COLOR_HSV_S = 28
    SETTING_CHANGE_COLOR_L = 25
    SETTING_CHANGE_COLOR_V = 27
    SETTING_COLORIZE = 42
    SETTING_COLOR_H = 20
    SETTING_COLOR_S = 21
    SETTING_COLOR_V = 22
    SETTING_CUSTOM_INPUT = 36
    SETTING_CUSTOM_INPUT_SLOWNESS = 37
    SETTING_DABS_PER_ACTUAL_RADIUS = 7
    SETTING_DABS_PER_BASIC_RADIUS = 6
    SETTING_DABS_PER_SECOND = 8
    SETTING_DIRECTION_FILTER = 40
    SETTING_ELLIPTICAL_DAB_ANGLE = 39
    SETTING_ELLIPTICAL_DAB_RATIO = 38
    SETTING_ERASER = 32
    SETTING_GRIDMAP_SCALE = 45
    SETTING_GRIDMAP_SCALE_X = 46
    SETTING_GRIDMAP_SCALE_Y = 47
    SETTING_HARDNESS = 4
    SETTING_LOCK_ALPHA = 41
    SETTING_OFFSET_ANGLE = 53
    SETTING_OFFSET_ANGLE_2 = 56
    SETTING_OFFSET_ANGLE_2_ASC = 57
    SETTING_OFFSET_ANGLE_2_VIEW = 58
    SETTING_OFFSET_ANGLE_ADJ = 59
    SETTING_OFFSET_ANGLE_ASC = 54
    SETTING_OFFSET_ANGLE_VIEW = 55
    SETTING_OFFSET_BY_RANDOM = 14
    SETTING_OFFSET_BY_SPEED = 15
    SETTING_OFFSET_BY_SPEED_SLOWNESS = 16
    SETTING_OFFSET_MULTIPLIER = 60
    SETTING_OFFSET_X = 52
    SETTING_OFFSET_Y = 51
    SETTING_OPAQUE = 0
    SETTING_OPAQUE_LINEARIZE = 2
    SETTING_OPAQUE_MULTIPLY = 1
    SETTING_PAINT_MODE = 63
    SETTING_POSTERIZE = 61
    SETTING_POSTERIZE_NUM = 62
    SETTING_PRESSURE_GAIN_LOG = 44
    SETTING_RADIUS_BY_RANDOM = 9
    SETTING_RADIUS_LOGARITHMIC = 3
    SETTING_RESTORE_COLOR = 23
    SETTING_SLOW_TRACKING = 17
    SETTING_SLOW_TRACKING_PER_DAB = 18
    SETTING_SMUDGE = 29
    SETTING_SMUDGE_BUCKET = 49
    SETTING_SMUDGE_LENGTH = 30
    SETTING_SMUDGE_LENGTH_LOG = 48
    SETTING_SMUDGE_RADIUS_LOG = 31
    SETTING_SMUDGE_TRANSPARENCY = 50
    SETTING_SNAP_TO_PIXEL = 43
    SETTING_SPEED1_GAMMA = 12
    SETTING_SPEED1_SLOWNESS = 10
    SETTING_SPEED2_GAMMA = 13
    SETTING_SPEED2_SLOWNESS = 11
    SETTING_STROKE_DURATION_LOGARITHMIC = 34
    SETTING_STROKE_HOLDTIME = 35
    SETTING_STROKE_THRESHOLD = 33
    SETTING_TRACKING_NOISE = 19

class BrushState(GObject.GEnum):
    STATES_COUNT = 44
    STATE_ACTUAL_ELLIPTICAL_DAB_ANGLE = 25
    STATE_ACTUAL_ELLIPTICAL_DAB_RATIO = 24
    STATE_ACTUAL_RADIUS = 4
    STATE_ACTUAL_X = 14
    STATE_ACTUAL_Y = 15
    STATE_ASCENSION = 29
    STATE_ATTACK_ANGLE = 34
    STATE_BARREL_ROTATION = 43
    STATE_CUSTOM_INPUT = 22
    STATE_DABS_PER_ACTUAL_RADIUS = 41
    STATE_DABS_PER_BASIC_RADIUS = 40
    STATE_DABS_PER_SECOND = 42
    STATE_DECLINATION = 28
    STATE_DECLINATIONX = 38
    STATE_DECLINATIONY = 39
    STATE_DIRECTION_ANGLE_DX = 32
    STATE_DIRECTION_ANGLE_DY = 33
    STATE_DIRECTION_DX = 26
    STATE_DIRECTION_DY = 27
    STATE_FLIP = 35
    STATE_GRIDMAP_X = 36
    STATE_GRIDMAP_Y = 37
    STATE_LAST_GETCOLOR_A = 12
    STATE_LAST_GETCOLOR_B = 11
    STATE_LAST_GETCOLOR_G = 10
    STATE_LAST_GETCOLOR_R = 9
    STATE_LAST_GETCOLOR_RECENTNESS = 13
    STATE_NORM_DX_SLOW = 16
    STATE_NORM_DY_SLOW = 17
    STATE_NORM_SPEED1_SLOW = 18
    STATE_NORM_SPEED2_SLOW = 19
    STATE_PARTIAL_DABS = 3
    STATE_PRESSURE = 2
    STATE_RNG_SEED = 23
    STATE_SMUDGE_A = 8
    STATE_SMUDGE_BA = 7
    STATE_SMUDGE_GA = 6
    STATE_SMUDGE_RA = 5
    STATE_STROKE = 20
    STATE_STROKE_STARTED = 21
    STATE_VIEWROTATION = 31
    STATE_VIEWZOOM = 30
    STATE_X = 0
    STATE_Y = 1

