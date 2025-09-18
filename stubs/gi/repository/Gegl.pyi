import typing

from gi.repository import Babl
from gi.repository import GLib
from gi.repository import GObject
T = typing.TypeVar("T")

AUTO_ROWSTRIDE: int = 0
CH_BACK_CENTER: int = 256
CH_BACK_LEFT: int = 16
CH_BACK_RIGHT: int = 32
CH_FRONT_CENTER: int = 4
CH_FRONT_LEFT: int = 1
CH_FRONT_LEFT_OF_CENTER: int = 64
CH_FRONT_RIGHT: int = 2
CH_FRONT_RIGHT_OF_CENTER: int = 128
CH_LAYOUT_2POINT1: int = 0
CH_LAYOUT_2_1: int = 0
CH_LAYOUT_2_2: int = 0
CH_LAYOUT_3POINT1: int = 0
CH_LAYOUT_4POINT0: int = 0
CH_LAYOUT_4POINT1: int = 0
CH_LAYOUT_5POINT0: int = 0
CH_LAYOUT_5POINT0_BACK: int = 0
CH_LAYOUT_5POINT1: int = 0
CH_LAYOUT_5POINT1_BACK: int = 0
CH_LAYOUT_6POINT0: int = 0
CH_LAYOUT_6POINT0_FRONT: int = 0
CH_LAYOUT_6POINT1: int = 0
CH_LAYOUT_6POINT1_BACK: int = 0
CH_LAYOUT_6POINT1_FRONT: int = 0
CH_LAYOUT_7POINT0: int = 0
CH_LAYOUT_7POINT0_FRONT: int = 0
CH_LAYOUT_7POINT1: int = 0
CH_LAYOUT_7POINT1_WIDE: int = 0
CH_LAYOUT_7POINT1_WIDE_BACK: int = 0
CH_LAYOUT_HEXADECAGONAL: int = 0
CH_LAYOUT_HEXAGONAL: int = 0
CH_LAYOUT_NATIVE: int = -1
CH_LAYOUT_OCTAGONAL: int = 0
CH_LAYOUT_QUAD: int = 0
CH_LAYOUT_STEREO: int = 0
CH_LAYOUT_STEREO_DOWNMIX: int = 0
CH_LAYOUT_SURROUND: int = 0
CH_LOW_FREQUENCY: int = 8
CH_LOW_FREQUENCY_2: int = 0
CH_SIDE_LEFT: int = 512
CH_SIDE_RIGHT: int = 1024
CH_STEREO_LEFT: int = 536870912
CH_STEREO_RIGHT: int = 1073741824
CH_SURROUND_DIRECT_LEFT: int = 0
CH_SURROUND_DIRECT_RIGHT: int = 0
CH_TOP_BACK_CENTER: int = 65536
CH_TOP_BACK_LEFT: int = 32768
CH_TOP_BACK_RIGHT: int = 131072
CH_TOP_CENTER: int = 2048
CH_TOP_FRONT_CENTER: int = 8192
CH_TOP_FRONT_LEFT: int = 4096
CH_TOP_FRONT_RIGHT: int = 16384
CH_WIDE_LEFT: int = -2147483648
CH_WIDE_RIGHT: int = 0
FLOAT_EPSILON: float = 1e-05
LOOKUP_MAX_ENTRIES: int = 819200
MAJOR_VERSION: int = 0
MAX_AUDIO_CHANNELS: int = 8
MICRO_VERSION: int = 62
MINOR_VERSION: int = 4
PARAM_NO_VALIDATE: int = 64
_namespace: str = "Gegl"
_version: str = "0.4"

def babl_variant(format: Babl.Object, variant: BablVariant) -> Babl.Object: ...
def cl_disable() -> None: ...
def cl_init() -> bool: ...
def cl_is_accelerated() -> bool: ...
def config() -> Config: ...
def create_chain(ops: str, op_start: Node, op_end: Node, time: float, rel_dim: int, path_root: str) -> None: ...
def create_chain_argv(ops: str, op_start: Node, op_end: Node, time: float, rel_dim: int, path_root: str) -> None: ...
def exit() -> None: ...
def format(format_name: str) -> typing.Optional[typing.Any]: ...
def format_get_name(format: typing.Any) -> typing.Optional[str]: ...
def get_version() -> typing.Tuple[int, int, int]: ...
def graph_dump_outputs(node: Node) -> None: ...
def graph_dump_request(node: Node, roi: Rectangle) -> None: ...
def has_operation(operation_type: str) -> bool: ...
def init() -> list[str]: ...
def is_main_thread() -> bool: ...
def list_operations() -> list[str]: ...
def load_module_directory(path: str) -> None: ...
def parallel_distribute(max_n: int, func: typing.Callable[..., None], *user_data: typing.Any) -> None: ...
def parallel_distribute_area(area: Rectangle, thread_cost: float, split_strategy: SplitStrategy, func: typing.Callable[..., None], *user_data: typing.Any) -> None: ...
def parallel_distribute_range(size: int, thread_cost: float, func: typing.Callable[..., None], *user_data: typing.Any) -> None: ...
def param_spec_audio_fragment(name: str, nick: str, blurb: str, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_color(name: str, nick: str, blurb: str, default_color: Color, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_color_from_string(name: str, nick: str, blurb: str, default_color_string: str, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_color_get_default(self: GObject.ParamSpec) -> Color: ...
def param_spec_curve(name: str, nick: str, blurb: str, default_curve: Curve, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_double(name: str, nick: str, blurb: str, minimum: float, maximum: float, default_value: float, ui_minimum: float, ui_maximum: float, ui_gamma: float, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_enum(name: str, nick: str, blurb: str, enum_type: typing.Type[typing.Any], default_value: int, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_file_path(name: str, nick: str, blurb: str, no_validate: bool, null_ok: bool, default_value: str, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_format(name: str, nick: str, blurb: str, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_get_property_key(pspec: GObject.ParamSpec, key_name: str) -> str: ...
def param_spec_int(name: str, nick: str, blurb: str, minimum: int, maximum: int, default_value: int, ui_minimum: int, ui_maximum: int, ui_gamma: float, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_path(name: str, nick: str, blurb: str, default_path: Path, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_seed(name: str, nick: str, blurb: str, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_set_property_key(pspec: GObject.ParamSpec, key_name: str, value: str) -> None: ...
def param_spec_string(name: str, nick: str, blurb: str, no_validate: bool, null_ok: bool, default_value: str, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def param_spec_uri(name: str, nick: str, blurb: str, no_validate: bool, null_ok: bool, default_value: str, flags: GObject.ParamFlags) -> GObject.ParamSpec: ...
def rectangle_infinite_plane() -> Rectangle: ...
def reset_stats() -> None: ...
def serialize(start: Node, end: Node, basepath: str, serialize_flags: SerializeFlag) -> str: ...
def stats() -> Stats: ...

class AudioFragment(GObject.Object):
    """
    :Constructors:

    ::

        AudioFragment(**properties)
        new(sample_rate:int, channels:int, channel_layout:int, max_samples:int) -> Gegl.AudioFragment

    Object GeglAudioFragment

    Properties from GeglAudioFragment:
      string -> gchararray: String
        A String representation of the GeglAudioFragment

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        string: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    data: list[float] = ...
    priv: AudioFragmentPrivate = ...
    def __init__(self, string: str = ...) -> None: ...
    def get_channel_layout(self) -> int: ...
    def get_channels(self) -> int: ...
    def get_max_samples(self) -> int: ...
    def get_pos(self) -> int: ...
    def get_sample_count(self) -> int: ...
    def get_sample_rate(self) -> int: ...
    @classmethod
    def new(cls, sample_rate: int, channels: int, channel_layout: int, max_samples: int) -> AudioFragment: ...
    def set_channel_layout(self, channel_layout: int) -> None: ...
    def set_channels(self, channels: int) -> None: ...
    def set_max_samples(self, max_samples: int) -> None: ...
    def set_pos(self, pos: int) -> None: ...
    def set_sample_count(self, sample_count: int) -> None: ...
    def set_sample_rate(self, sample_rate: int) -> None: ...


class AudioFragmentClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioFragmentClass()
    """
    parent_class: GObject.ObjectClass = ...

class AudioFragmentPrivate(GObject.GPointer): ...

class Buffer(TileHandler):
    """
    :Constructors:

    ::

        Buffer(**properties)
        new(format_name:str, x:int, y:int, width:int, height:int) -> Gegl.Buffer
        new_for_backend(extent:Gegl.Rectangle, backend:Gegl.TileBackend) -> Gegl.Buffer

    Object GeglBuffer

    Signals from GeglBuffer:
      changed (GeglRectangle)

    Properties from GeglBuffer:
      x -> gint: x
        local origin's offset relative to source origin
      y -> gint: y
        local origin's offset relative to source origin
      width -> gint: width
        pixel width of buffer
      height -> gint: height
        pixel height of buffer
      shift-x -> gint: shift-x

      shift-y -> gint: shift-y

      abyss-x -> gint: abyss-x

      abyss-y -> gint: abyss-y

      abyss-width -> gint: abyss-width
        pixel width of abyss
      abyss-height -> gint: abyss-height
        pixel height of abyss
      tile-width -> gint: tile-width
        width of a tile
      tile-height -> gint: tile-height
        height of a tile
      format -> gpointer: format
        babl format
      px-size -> gint: pixel-size
        size of a single pixel in bytes.
      pixels -> gint: pixels
        total amount of pixels in image (width x height)
      path -> gchararray: Path
        URI to where the buffer is stored
      backend -> GeglTileBackend: backend
        A custom tile-backend instance to use
      initialized -> gboolean: initialized

    Properties from GeglTileHandler:
      source -> GObject: GeglBuffer
        The tilestore to be a facade for

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        abyss_height: int
        abyss_width: int
        abyss_x: int
        abyss_y: int
        backend: TileBackend
        format: None
        height: int
        initialized: bool
        path: str
        pixels: int
        px_size: int
        shift_x: int
        shift_y: int
        tile_height: int
        tile_width: int
        width: int
        x: int
        y: int
        source: GObject.Object
    props: Props = ...
    def __init__(self, abyss_height: int = ...,
                 abyss_width: int = ...,
                 abyss_x: int = ...,
                 abyss_y: int = ...,
                 backend: TileBackend = ...,
                 format: typing.Optional[None] = ...,
                 height: int = ...,
                 initialized: bool = ...,
                 path: str = ...,
                 shift_x: int = ...,
                 shift_y: int = ...,
                 tile_height: int = ...,
                 tile_width: int = ...,
                 width: int = ...,
                 x: int = ...,
                 y: int = ...,
                 source: GObject.Object = ...) -> None: ...
    def add_handler(self, handler: None) -> None: ...
    def clear(self, roi: Rectangle) -> None: ...
    def copy(self, src_rect: Rectangle, repeat_mode: AbyssPolicy, dst: Buffer, dst_rect: Rectangle) -> None: ...
    def create_sub_buffer(self, extent: Rectangle) -> Buffer: ...
    def dup(self) -> Buffer: ...
    def flush(self) -> None: ...
    def flush_ext(self, rect: Rectangle) -> None: ...
    def freeze_changed(self) -> None: ...
    def get(self, rect: Rectangle, scale: float, format_name: typing.Optional[str], repeat_mode: AbyssPolicy) -> bytes: ...
    def get_abyss(self) -> Rectangle: ...
    def get_extent(self) -> Rectangle: ...
    def linear_close(self, linear: None) -> None: ...
    @staticmethod
    def load(path: str) -> Buffer: ...
    @classmethod
    def new(cls, format_name: str, x: int, y: int, width: int, height: int) -> Buffer: ...
    @classmethod
    def new_for_backend(cls, extent: Rectangle, backend: TileBackend) -> Buffer: ...
    @staticmethod
    def open(path: str) -> Buffer: ...
    def remove_handler(self, handler: None) -> None: ...
    def sample_cleanup(self) -> None: ...
    def save(self, path: str, roi: Rectangle) -> None: ...
    def set(self, rect: Rectangle, format_name: str, src: typing.Sequence[int]) -> None: ...
    def set_abyss(self, abyss: Rectangle) -> bool: ...
    def set_color(self, rect: Rectangle, color: Color) -> None: ...
    def set_color_from_pixel(self, rect: Rectangle, pixel: None, pixel_format: Babl.Object) -> None: ...
    def set_extent(self, extent: Rectangle) -> bool: ...
    def set_pattern(self, rect: Rectangle, pattern: Buffer, x_offset: int, y_offset: int) -> None: ...
    def share_storage(self, buffer2: Buffer) -> bool: ...
    def signal_connect(self, detailed_signal: str, c_handler: typing.Callable[..., None], *data: typing.Any) -> int: ...
    @staticmethod
    def swap_create_file(suffix: typing.Optional[str] = None) -> typing.Optional[str]: ...
    @staticmethod
    def swap_has_file(path: str) -> bool: ...
    @staticmethod
    def swap_remove_file(path: str) -> None: ...
    def thaw_changed(self) -> None: ...


class BufferIterator(GObject.GPointer):
    """
    :Constructors:

    ::

        BufferIterator()
    """
    length: int = ...
    priv: BufferIteratorPriv = ...
    items: list[BufferIteratorItem] = ...

class BufferIteratorItem(GObject.GPointer):
    """
    :Constructors:

    ::

        BufferIteratorItem()
    """
    data: None = ...
    roi: Rectangle = ...

class BufferIteratorPriv(GObject.GPointer): ...

class BufferMatrix2(GObject.GPointer):
    """
    :Constructors:

    ::

        BufferMatrix2()
    """
    coeff: list[float] = ...
    def determinant(self) -> float: ...
    def is_identity(self) -> bool: ...
    def is_scale(self) -> bool: ...


class Color(GObject.Object):
    """
    :Constructors:

    ::

        Color(**properties)
        new(string:str) -> Gegl.Color

    Object GeglColor

    Properties from GeglColor:
      string -> gchararray: String
        A String representation of the GeglColor

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        string: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: ColorPrivate = ...
    def __init__(self, string: str = ...) -> None: ...
    def duplicate(self) -> Color: ...
    def get_bytes(self, format: Babl.Object) -> GLib.Bytes: ...
    def get_cmyk(self, space: typing.Optional[Babl.Object] = None) -> typing.Tuple[float, float, float, float, float]: ...
    def get_components(self, format: typing.Any) -> list[float]: ...
    def get_format(self) -> Babl.Object: ...
    def get_hsla(self, space: typing.Optional[Babl.Object] = None) -> typing.Tuple[float, float, float, float]: ...
    def get_hsva(self, space: typing.Optional[Babl.Object] = None) -> typing.Tuple[float, float, float, float]: ...
    def get_rgba(self) -> typing.Tuple[float, float, float, float]: ...
    def get_rgba_with_space(self, space: Babl.Object) -> typing.Tuple[float, float, float, float]: ...
    @classmethod
    def new(cls, string: str) -> Color: ...
    def set_bytes(self, format: Babl.Object, bytes: GLib.Bytes) -> None: ...
    def set_cmyk(self, cyan: float, magenta: float, yellow: float, key: float, alpha: float, space: typing.Optional[Babl.Object] = None) -> None: ...
    def set_components(self, format: typing.Any, components: typing.Sequence[float]) -> None: ...
    def set_hsla(self, hue: float, saturation: float, lightness: float, alpha: float, space: typing.Optional[Babl.Object] = None) -> None: ...
    def set_hsva(self, hue: float, saturation: float, value: float, alpha: float, space: typing.Optional[Babl.Object] = None) -> None: ...
    def set_rgba(self, red: float, green: float, blue: float, alpha: float) -> None: ...
    def set_rgba_with_space(self, red: float, green: float, blue: float, alpha: float, space: Babl.Object) -> None: ...


class ColorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorClass()
    """
    parent_class: GObject.ObjectClass = ...

class ColorPrivate(GObject.GPointer): ...

class Config(GObject.Object):
    """
    :Constructors:

    ::

        Config(**properties)

    Object GeglConfig

    Properties from GeglConfig:
      quality -> gdouble: Quality
        quality/speed trade off 1.0 = full quality, 0.0 = full speed
      tile-cache-size -> guint64: Tile Cache size
        size of tile cache in bytes
      chunk-size -> gint: Chunk size
        the number of pixels processed simultaneously by GEGL.
      swap -> gchararray: Swap
        where gegl stores it's swap files
      swap-compression -> gchararray: Swap compression
        compression algorithm used for data stored in the swap
      tile-width -> gint: Tile width
        default tile width for created buffers.
      tile-height -> gint: Tile height
        default tile height for created buffers.
      threads -> gint: Number of threads
        Number of concurrent evaluation threads
      use-opencl -> gboolean: Use OpenCL
        Try to use OpenCL
      queue-size -> gint: Queue size
        Maximum size of a file backend's writer thread queue (in bytes)
      application-license -> gchararray: Application license
        A list of additional licenses to allow for operations
      mipmap-rendering -> gboolean: mipmap rendering
        Enable code paths for mipmap preview rendering, uses approximations for 50% 25% etc zoom factors to reduce processing.

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        application_license: str
        chunk_size: int
        mipmap_rendering: bool
        quality: float
        queue_size: int
        swap: str
        swap_compression: str
        threads: int
        tile_cache_size: int
        tile_height: int
        tile_width: int
        use_opencl: bool
    props: Props = ...
    def __init__(self, application_license: str = ...,
                 chunk_size: int = ...,
                 mipmap_rendering: bool = ...,
                 quality: float = ...,
                 queue_size: int = ...,
                 swap: str = ...,
                 swap_compression: str = ...,
                 threads: int = ...,
                 tile_cache_size: int = ...,
                 tile_height: int = ...,
                 tile_width: int = ...,
                 use_opencl: bool = ...) -> None: ...

class Curve(GObject.Object):
    """
    :Constructors:

    ::

        Curve(**properties)
        new(y_min:float, y_max:float) -> Gegl.Curve
        new_default() -> Gegl.Curve

    Object GeglCurve

    Signals from GObject:
      notify (GParam)
    """
    parent_instance: GObject.Object = ...
    def add_point(self, x: float, y: float) -> int: ...
    def calc_value(self, x: float) -> float: ...
    def duplicate(self) -> Curve: ...
    def get_point(self, index: int) -> typing.Tuple[float, float]: ...
    def get_y_bounds(self) -> typing.Tuple[float, float]: ...
    @classmethod
    def new(cls, y_min: float, y_max: float) -> Curve: ...
    @classmethod
    def new_default(cls) -> Curve: ...
    def num_points(self) -> int: ...
    def set_point(self, index: int, x: float, y: float) -> None: ...


class CurveClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CurveClass()
    """
    parent_class: GObject.ObjectClass = ...

class Lookup(GObject.GPointer):
    """
    :Constructors:

    ::

        Lookup()
    """
    function: typing.Callable[[float, None], float] = ...
    data: None = ...
    shift: int = ...
    positive_min: int = ...
    positive_max: int = ...
    negative_min: int = ...
    negative_max: int = ...
    bitmask: list[int] = ...
    table: list[float] = ...

class Matrix3(GObject.GBoxed):
    """
    :Constructors:

    ::

        Matrix3()
        new() -> Gegl.Matrix3
    """
    coeff: list[float] = ...
    def copy(self) -> Matrix3: ...
    def copy_into(self, src: Matrix3) -> None: ...
    def determinant(self) -> float: ...
    def equal(self, matrix2: Matrix3) -> bool: ...
    def identity(self) -> None: ...
    def invert(self) -> None: ...
    def is_affine(self) -> bool: ...
    def is_identity(self) -> bool: ...
    def is_scale(self) -> bool: ...
    def is_translate(self) -> bool: ...
    def multiply(self, right: Matrix3, product: Matrix3) -> None: ...
    @classmethod
    def new(cls) -> Matrix3: ...
    def originate(self, x: float, y: float) -> None: ...
    def parse_string(self, string: str) -> None: ...
    def round_error(self) -> None: ...
    def to_string(self) -> str: ...
    def transform_point(self, x: float, y: float) -> None: ...


class Metadata(GObject.GInterface):
    """
    Interface GeglMetadata

    Signals from GObject:
      notify (GParam)
    """
    def get_resolution(self, unit: ResolutionUnit, x: float, y: float) -> bool: ...
    def iter_get_value(self, iter: MetadataIter, value: typing.Any) -> bool: ...
    def iter_init(self, iter: MetadataIter) -> None: ...
    def iter_lookup(self, iter: MetadataIter, key: str) -> bool: ...
    def iter_next(self, iter: MetadataIter) -> str: ...
    def iter_set_value(self, iter: MetadataIter, value: typing.Any) -> bool: ...
    def register_map(self, file_module: str, flags: int, map: typing.Sequence[MetadataMap]) -> None: ...
    def set_resolution(self, unit: ResolutionUnit, x: float, y: float) -> bool: ...
    def unregister_map(self) -> None: ...


class MetadataHash(MetadataStore, Metadata):
    """
    :Constructors:

    ::

        MetadataHash(**properties)
        new() -> Gegl.MetadataStore

    Object GeglMetadataHash

    Signals from GeglMetadataStore:
      changed (GParam)
      mapped (gchararray, gboolean)
      unmapped (gchararray, gchararray)
      generate-value (GParam, GValue) -> gboolean
      parse-value (GParam, GValue) -> gboolean

    Properties from GeglMetadataStore:
      resolution-unit -> GeglResolutionUnit: Resolution Unit
        Units for image resolution
      resolution-x -> gdouble: Resolution X
        X Resolution
      resolution-y -> gdouble: Resolution Y
        X Resolution
      file-module-name -> gchararray: File Module Name
        Name of currently active file module or NULL
      title -> gchararray: Title
        Short title or caption
      artist -> gchararray: Artist
        Name of image creator
      description -> gchararray: Description
        Description of image (possibly long)
      copyright -> gchararray: Copyright
        Copyright notice
      disclaimer -> gchararray: Disclaimer
        Legal disclaimer
      warning -> gchararray: Warning
        Warning of nature of content
      comment -> gchararray: Comment
        Miscellaneous comment
      software -> gchararray: Software
        Software used to create the image
      source -> gchararray: Source
        Device used to create the image
      timestamp -> GDateTime: Timestamp
        Image creation time

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        artist: str
        comment: str
        copyright: str
        description: str
        disclaimer: str
        file_module_name: str
        resolution_unit: ResolutionUnit
        resolution_x: float
        resolution_y: float
        software: str
        source: str
        timestamp: GLib.DateTime
        title: str
        warning: str
    props: Props = ...
    def __init__(self, artist: str = ...,
                 comment: str = ...,
                 copyright: str = ...,
                 description: str = ...,
                 disclaimer: str = ...,
                 resolution_unit: ResolutionUnit = ...,
                 resolution_x: float = ...,
                 resolution_y: float = ...,
                 software: str = ...,
                 source: str = ...,
                 timestamp: GLib.DateTime = ...,
                 title: str = ...,
                 warning: str = ...) -> None: ...
    @classmethod
    def new(cls) -> MetadataHash: ...


class MetadataHashClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MetadataHashClass()
    """
    parent_class: MetadataStoreClass = ...

class MetadataInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        MetadataInterface()
    """
    base_iface: GObject.TypeInterface = ...
    register_map: typing.Callable[[Metadata, str, int, typing.Sequence[MetadataMap]], None] = ...
    set_resolution: typing.Callable[[Metadata, ResolutionUnit, float, float], bool] = ...
    get_resolution: typing.Callable[[Metadata, ResolutionUnit, float, float], bool] = ...
    iter_lookup: typing.Callable[[Metadata, MetadataIter, str], bool] = ...
    iter_init: typing.Callable[[Metadata, MetadataIter], None] = ...
    iter_next: typing.Callable[[Metadata, MetadataIter], str] = ...
    iter_set_value: typing.Callable[[Metadata, MetadataIter, typing.Any], bool] = ...
    iter_get_value: typing.Callable[[Metadata, MetadataIter, typing.Any], bool] = ...

class MetadataIter(GObject.GPointer):
    """
    :Constructors:

    ::

        MetadataIter()
    """
    stamp: int = ...
    user_data: None = ...
    user_data2: None = ...
    user_data3: None = ...

class MetadataMap(GObject.GPointer):
    """
    :Constructors:

    ::

        MetadataMap()
    """
    local_name: str = ...
    name: str = ...
    transform: typing.Callable[[typing.Any, typing.Any], None] = ...

class MetadataStore(GObject.Object, Metadata):
    """
    :Constructors:

    ::

        MetadataStore(**properties)

    Object GeglMetadataStore

    Signals from GeglMetadataStore:
      changed (GParam)
      mapped (gchararray, gboolean)
      unmapped (gchararray, gchararray)
      generate-value (GParam, GValue) -> gboolean
      parse-value (GParam, GValue) -> gboolean

    Properties from GeglMetadataStore:
      resolution-unit -> GeglResolutionUnit: Resolution Unit
        Units for image resolution
      resolution-x -> gdouble: Resolution X
        X Resolution
      resolution-y -> gdouble: Resolution Y
        X Resolution
      file-module-name -> gchararray: File Module Name
        Name of currently active file module or NULL
      title -> gchararray: Title
        Short title or caption
      artist -> gchararray: Artist
        Name of image creator
      description -> gchararray: Description
        Description of image (possibly long)
      copyright -> gchararray: Copyright
        Copyright notice
      disclaimer -> gchararray: Disclaimer
        Legal disclaimer
      warning -> gchararray: Warning
        Warning of nature of content
      comment -> gchararray: Comment
        Miscellaneous comment
      software -> gchararray: Software
        Software used to create the image
      source -> gchararray: Source
        Device used to create the image
      timestamp -> GDateTime: Timestamp
        Image creation time

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        artist: str
        comment: str
        copyright: str
        description: str
        disclaimer: str
        file_module_name: str
        resolution_unit: ResolutionUnit
        resolution_x: float
        resolution_y: float
        software: str
        source: str
        timestamp: GLib.DateTime
        title: str
        warning: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, artist: str = ...,
                 comment: str = ...,
                 copyright: str = ...,
                 description: str = ...,
                 disclaimer: str = ...,
                 resolution_unit: ResolutionUnit = ...,
                 resolution_x: float = ...,
                 resolution_y: float = ...,
                 software: str = ...,
                 source: str = ...,
                 timestamp: GLib.DateTime = ...,
                 title: str = ...,
                 warning: str = ...) -> None: ...
    def declare(self, pspec: GObject.ParamSpec) -> None: ...
    def do__declare(self, pspec: GObject.ParamSpec, shadow: bool) -> None: ...
    def do__get_value(self, name: str) -> typing.Any: ...
    def do_has_value(self, name: str) -> bool: ...
    def do_register_hook(self, file_module_name: str, flags: int) -> None: ...
    def do_set_value(self, name: str, value: typing.Any) -> None: ...
    def get_artist(self) -> str: ...
    def get_comment(self) -> str: ...
    def get_copyright(self) -> str: ...
    def get_description(self) -> str: ...
    def get_disclaimer(self) -> str: ...
    def get_file_module_name(self) -> str: ...
    def get_resolution_unit(self) -> ResolutionUnit: ...
    def get_resolution_x(self) -> float: ...
    def get_resolution_y(self) -> float: ...
    def get_software(self) -> str: ...
    def get_source(self) -> str: ...
    def get_string(self, name: str) -> str: ...
    def get_timestamp(self) -> GLib.DateTime: ...
    def get_title(self) -> str: ...
    def get_value(self, name: str) -> typing.Any: ...
    def get_warning(self) -> str: ...
    def has_value(self, name: str) -> bool: ...
    def notify(self, pspec: GObject.ParamSpec, shadow: bool) -> None: ...
    def register(self, local_name: str, name: str, transform: typing.Callable[[typing.Any, typing.Any], None]) -> None: ...
    def set_artist(self, artist: str) -> None: ...
    def set_comment(self, comment: str) -> None: ...
    def set_copyright(self, copyright: str) -> None: ...
    def set_description(self, description: str) -> None: ...
    def set_disclaimer(self, disclaimer: str) -> None: ...
    def set_resolution_unit(self, unit: ResolutionUnit) -> None: ...
    def set_resolution_x(self, resolution_x: float) -> None: ...
    def set_resolution_y(self, resolution_y: float) -> None: ...
    def set_software(self, software: str) -> None: ...
    def set_source(self, source: str) -> None: ...
    def set_string(self, name: str, string: str) -> None: ...
    def set_timestamp(self, timestamp: GLib.DateTime) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_value(self, name: str, value: typing.Any) -> None: ...
    def set_warning(self, warning: str) -> None: ...
    def typeof_value(self, name: str) -> typing.Type[typing.Any]: ...


class MetadataStoreClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MetadataStoreClass()
    """
    parent_class: GObject.ObjectClass = ...
    _declare: None = ...
    pspec: None = ...
    set_value: typing.Callable[[MetadataStore, str, typing.Any], None] = ...
    _get_value: None = ...
    has_value: typing.Callable[[MetadataStore, str], bool] = ...
    register_hook: typing.Callable[[MetadataStore, str, int], None] = ...
    parse_value: None = ...
    generate_value: None = ...
    padding: list[None] = ...

class Node(GObject.Object):
    """
    :Constructors:

    ::

        Node(**properties)
        new() -> Gegl.Node
        new_from_file(path:str) -> Gegl.Node
        new_from_serialized(chaindata:str, path_root:str) -> Gegl.Node
        new_from_xml(xmldata:str, path_root:str) -> Gegl.Node

    Object GeglNode

    Signals from GeglNode:
      invalidated (GeglRectangle)
      computed (GeglRectangle)
      progress (gdouble)

    Properties from GeglNode:
      operation -> gchararray: Operation Type
        The type of associated GeglOperation
      gegl-operation -> GeglOperation: Operation Object
        The associated GeglOperation instance
      name -> gchararray: Name
        The name of the node
      dont-cache -> gboolean: Do not cache
        Do not cache the result of this operation, the property is inherited by children created from a node. (Deprecated for "cache-policy".)
      cache-policy -> GeglCachePolicy: Cache Policy
        Cache policy for this node, the property is inherited by children created from a node.
      use-opencl -> gboolean: Use OpenCL
        Use the OpenCL version of this operation if available, this property is inherited by children created from a node.
      passthrough -> gboolean: Passthrough
        Act as a nop, passing input unmodifed through to ouput.

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        cache_policy: CachePolicy
        dont_cache: bool
        gegl_operation: typing.Optional[Operation]
        name: str
        operation: str
        passthrough: bool
        use_opencl: bool
    props: Props = ...
    def __init__(self, cache_policy: CachePolicy = ...,
                 dont_cache: bool = ...,
                 gegl_operation: Operation = ...,
                 name: str = ...,
                 operation: str = ...,
                 passthrough: bool = ...,
                 use_opencl: bool = ...) -> None: ...
    def add_child(self, child: Node) -> Node: ...
    def blit_buffer(self, buffer: typing.Optional[Buffer], roi: typing.Optional[Rectangle], level: int, abyss_policy: AbyssPolicy) -> None: ...
    def connect(self, a_pad_name: str, b: Node, b_pad_name: str) -> bool: ...
    def connect_from(self, input_pad_name: str, source: Node, output_pad_name: str) -> bool: ...
    def connect_to(self, output_pad_name: str, sink: Node, input_pad_name: str) -> bool: ...
    def create_child(self, operation: str) -> Node: ...
    def detect(self, x: int, y: int) -> Node: ...
    def disconnect(self, input_pad: str) -> bool: ...
    def find_property(self, property_name: str) -> GObject.ParamSpec: ...
    def get_bounding_box(self) -> Rectangle: ...
    def get_children(self) -> list[Node]: ...
    def get_consumers(self, output_pad: str) -> typing.Tuple[int, list[Node], list[str]]: ...
    def get_gegl_operation(self) -> typing.Optional[Operation]: ...
    def get_input_proxy(self, pad_name: str) -> Node: ...
    def get_operation(self) -> str: ...
    def get_output_proxy(self, pad_name: str) -> Node: ...
    def get_pad_description(self, pad_name: str) -> str: ...
    def get_pad_label(self, pad_name: str) -> str: ...
    def get_parent(self) -> Node: ...
    def get_passthrough(self) -> bool: ...
    def get_producer(self, input_pad_name: str, output_pad_name: typing.Optional[str] = None) -> Node: ...
    def get_property(self, property_name: str) -> typing.Any: ...
    def has_pad(self, pad_name: str) -> bool: ...
    def is_graph(self) -> bool: ...
    def link(self, sink: Node) -> None: ...
    def list_input_pads(self) -> list[str]: ...
    def list_output_pads(self) -> list[str]: ...
    @classmethod
    def new(cls) -> Node: ...
    @classmethod
    def new_from_file(cls, path: str) -> Node: ...
    @classmethod
    def new_from_serialized(cls, chaindata: str, path_root: str) -> Node: ...
    @classmethod
    def new_from_xml(cls, xmldata: str, path_root: str) -> Node: ...
    def new_processor(self, rectangle: Rectangle) -> Processor: ...
    def process(self) -> None: ...
    def progress(self, progress: float, message: str) -> None: ...
    def remove_child(self, child: Node) -> Node: ...
    def set_enum_as_string(self, key: str, value: str) -> None: ...
    def set_passthrough(self, passthrough: bool) -> None: ...
    def set_property(self, property_name: str, value: typing.Any) -> None: ...
    def set_time(self, time: float) -> None: ...
    def to_xml(self, path_root: str) -> str: ...
    def to_xml_full(self, tail: typing.Optional[Node], path_root: str) -> str: ...


class Operation(GObject.Object):
    """
    :Constructors:

    ::

        Operation(**properties)

    Object GeglOperation

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def find_property(operation_type: str, property_name: str) -> GObject.ParamSpec: ...
    @staticmethod
    def get_key(operation_type: str, key_name: str) -> str: ...
    @staticmethod
    def get_op_version(op_name: str) -> str: ...
    @staticmethod
    def get_property_key(operation_type: str, property_name: str, property_key_name: str) -> str: ...
    @staticmethod
    def list_keys(operation_type: str) -> list[str]: ...
    @staticmethod
    def list_properties(operation_type: str) -> list[GObject.ParamSpec]: ...
    @staticmethod
    def list_property_keys(operation_type: str, property_name: str) -> list[str]: ...


class OperationContext(GObject.GPointer): ...

class ParamAudioFragment(GObject.ParamSpec): ...

class ParamColor(GObject.ParamSpec): ...

class ParamCurve(GObject.ParamSpec): ...

class ParamDouble(GObject.ParamSpecDouble): ...

class ParamEnum(GObject.ParamSpecEnum): ...

class ParamFilePath(GObject.ParamSpecString): ...

class ParamFormat(GObject.ParamSpecPointer): ...

class ParamInt(GObject.ParamSpecInt): ...

class ParamPath(GObject.ParamSpec): ...

class ParamSeed(GObject.ParamSpecUInt): ...

class ParamSpecDouble(GObject.GPointer):
    """
    :Constructors:

    ::

        ParamSpecDouble()
    """
    parent_instance: GObject.ParamSpecDouble = ...
    ui_minimum: float = ...
    ui_maximum: float = ...
    ui_gamma: float = ...
    ui_step_small: float = ...
    ui_step_big: float = ...
    ui_digits: int = ...
    def set_digits(self, digits: int) -> None: ...
    def set_steps(self, small_step: float, big_step: float) -> None: ...


class ParamSpecEnum(GObject.GPointer):
    """
    :Constructors:

    ::

        ParamSpecEnum()
    """
    parent_instance: GObject.ParamSpecEnum = ...
    excluded_values: list[None] = ...
    def exclude_value(self, value: int) -> None: ...


class ParamSpecFilePath(GObject.GPointer):
    """
    :Constructors:

    ::

        ParamSpecFilePath()
    """
    parent_instance: GObject.ParamSpecString = ...
    no_validate: int = ...
    null_ok: int = ...

class ParamSpecFormat(GObject.GPointer):
    """
    :Constructors:

    ::

        ParamSpecFormat()
    """
    parent_instance: GObject.ParamSpecPointer = ...

class ParamSpecInt(GObject.GPointer):
    """
    :Constructors:

    ::

        ParamSpecInt()
    """
    parent_instance: GObject.ParamSpecInt = ...
    ui_minimum: int = ...
    ui_maximum: int = ...
    ui_gamma: float = ...
    ui_step_small: int = ...
    ui_step_big: int = ...
    def set_steps(self, small_step: int, big_step: int) -> None: ...


class ParamSpecSeed(GObject.GPointer):
    """
    :Constructors:

    ::

        ParamSpecSeed()
    """
    parent_instance: GObject.ParamSpecUInt = ...
    ui_minimum: int = ...
    ui_maximum: int = ...

class ParamSpecString(GObject.GPointer):
    """
    :Constructors:

    ::

        ParamSpecString()
    """
    parent_instance: GObject.ParamSpecString = ...
    no_validate: int = ...
    null_ok: int = ...

class ParamSpecUri(GObject.GPointer):
    """
    :Constructors:

    ::

        ParamSpecUri()
    """
    parent_instance: GObject.ParamSpecString = ...
    no_validate: int = ...
    null_ok: int = ...

class ParamString(GObject.ParamSpecString): ...

class ParamUri(GObject.ParamSpecString): ...

class Path(GObject.Object):
    """
    :Constructors:

    ::

        Path(**properties)
        new() -> Gegl.Path
        new_from_string(instructions:str) -> Gegl.Path

    Object GeglPath

    Signals from GeglPath:
      changed (gpointer)

    Signals from GObject:
      notify (GParam)
    """
    parent_instance: GObject.Object = ...
    @staticmethod
    def add_type(type: int, items: int, description: str) -> None: ...
    def calc(self, pos: float) -> typing.Tuple[bool, float, float]: ...
    def calc_y_for_x(self, x: float) -> typing.Tuple[int, float]: ...
    def clear(self) -> None: ...
    def closest_point(self, x: float, y: float) -> typing.Tuple[float, float, float, int]: ...
    def dirty(self) -> None: ...
    def foreach(self, each_item: typing.Callable[..., None], *user_data: typing.Any) -> None: ...
    def foreach_flat(self, each_item: typing.Callable[..., None], *user_data: typing.Any) -> None: ...
    def freeze(self) -> None: ...
    def get_bounds(self) -> typing.Tuple[float, float, float, float]: ...
    def get_length(self) -> float: ...
    def get_matrix(self) -> Matrix3: ...
    def get_n_nodes(self) -> int: ...
    def get_node(self, index: int) -> typing.Tuple[bool, PathItem]: ...
    def insert_node(self, pos: int, node: PathItem) -> None: ...
    def is_empty(self) -> bool: ...
    @classmethod
    def new(cls) -> Path: ...
    @classmethod
    def new_from_string(cls, instructions: str) -> Path: ...
    def parse_string(self, instructions: str) -> None: ...
    def remove_node(self, pos: int) -> None: ...
    def replace_node(self, pos: int, node: PathItem) -> None: ...
    def set_matrix(self, matrix: Matrix3) -> None: ...
    def thaw(self) -> None: ...
    def to_string(self) -> str: ...


class PathClass(GObject.GPointer): ...

class PathItem(GObject.GPointer):
    """
    :Constructors:

    ::

        PathItem()
    """
    type: int = ...
    point: list[PathPoint] = ...

class PathList(GObject.GPointer):
    """
    :Constructors:

    ::

        PathList()
    """
    next: None = ...
    d: PathItem = ...

class PathPoint(GObject.GPointer):
    """
    :Constructors:

    ::

        PathPoint()
    """
    x: float = ...
    y: float = ...

class Processor(GObject.Object):
    """
    :Constructors:

    ::

        Processor(**properties)

    Object GeglProcessor

    Properties from GeglProcessor:
      node -> GeglNode: GeglNode
        The GeglNode to process (will saturate the provider's cache if the provided node is a sink node)
      chunksize -> gint: chunksize
        Size of chunks being rendered (larger chunks need more memory to do the processing).
      progress -> gdouble: progress
        query progress; 0.0 is not started, 1.0 is done.
      rectangle -> gpointer: rectangle
        The rectangle of the region to process.

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        chunksize: int
        progress: float
        rectangle: None
        node: Node
    props: Props = ...
    def __init__(self, chunksize: int = ...,
                 node: Node = ...,
                 progress: float = ...,
                 rectangle: None = ...) -> None: ...
    def get_buffer(self) -> Buffer: ...
    def set_level(self, level: int) -> None: ...
    def set_rectangle(self, rectangle: Rectangle) -> None: ...
    def set_scale(self, scale: float) -> None: ...
    def work(self) -> typing.Tuple[bool, float]: ...


class Random(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gegl.Random
        new_with_seed(seed:int) -> Gegl.Random
    """
    def duplicate(self) -> Random: ...
    def float(self, x: int, y: int, z: int, n: int) -> float: ...
    def float_range(self, x: int, y: int, z: int, n: int, min: float, max: float) -> float: ...
    def free(self) -> None: ...
    def int(self, x: int, y: int, z: int, n: int) -> int: ...
    def int_range(self, x: int, y: int, z: int, n: int, min: int, max: int) -> int: ...
    @classmethod
    def new(cls) -> Random: ...
    @classmethod
    def new_with_seed(cls, seed: int) -> Random: ...
    def set_seed(self, seed: int) -> None: ...


class Rectangle(GObject.GBoxed):
    """
    :Constructors:

    ::

        Rectangle()
        new(x:int, y:int, width:int, height:int) -> Gegl.Rectangle
    """
    x: int = ...
    y: int = ...
    width: int = ...
    height: int = ...
    def align(self, rectangle: Rectangle, tile: Rectangle, alignment: RectangleAlignment) -> bool: ...
    def align_to_buffer(self, rectangle: Rectangle, buffer: Buffer, alignment: RectangleAlignment) -> bool: ...
    def bounding_box(self, source1: Rectangle, source2: Rectangle) -> None: ...
    def contains(self, child: Rectangle) -> bool: ...
    def copy(self, source: Rectangle) -> None: ...
    def dump(self) -> None: ...
    def dup(self) -> Rectangle: ...
    def equal(self, rectangle2: Rectangle) -> bool: ...
    def equal_coords(self, x: int, y: int, width: int, height: int) -> bool: ...
    @staticmethod
    def infinite_plane() -> Rectangle: ...
    def intersect(self, src1: Rectangle, src2: Rectangle) -> bool: ...
    def is_empty(self) -> bool: ...
    def is_infinite_plane(self) -> bool: ...
    @classmethod
    def new(cls, x: int, y: int, width: int, height: int) -> Rectangle: ...
    def set(self, x: int, y: int, width: int, height: int) -> None: ...
    def subtract(self, minuend: Rectangle, subtrahend: Rectangle) -> int: ...
    def subtract_bounding_box(self, minuend: Rectangle, subtrahend: Rectangle) -> bool: ...
    def xor(self, source1: Rectangle, source2: Rectangle) -> int: ...


class Sampler(GObject.GPointer):
    def get(self, x: float, y: float, scale: BufferMatrix2, output: None, repeat_mode: AbyssPolicy) -> None: ...
    def get_context_rect(self) -> Rectangle: ...


class Stats(GObject.Object):
    """
    :Constructors:

    ::

        Stats(**properties)

    Object GeglStats

    Properties from GeglStats:
      tile-cache-total -> guint64: Tile Cache total size
        Total size of tile cache in bytes
      tile-cache-total-max -> guint64: Tile Cache maximal total size
        Maximal total size of tile cache throughout the session in bytes
      tile-cache-total-uncompressed -> guint64: Tile Cache total uncompressed size
        Total size of tile cache if no compression was employed in bytes
      tile-cache-hits -> gint: Tile Cache hits
        Number of tile cache hits
      tile-cache-misses -> gint: Tile Cache misses
        Number of tile cache misses
      swap-total -> guint64: Swap total size
        Total size of the data in the swap
      swap-total-uncompressed -> guint64: Swap total uncompressed size
        Total size of if the data in the swap if no compression was employed in bytes
      swap-file-size -> guint64: Swap file size
        Size of the swap file
      swap-busy -> gboolean: Swap busy
        Whether there is work queued for the swap
      swap-queued-total -> guint64: Swap total queued size
        Total size of the data queued for writing to the swap
      swap-queue-full -> gboolean: Swap queue full
        Whether the swap queue is full
      swap-queue-stalls -> gint: Swap queue stall count
        Number of times writing to the swap has been stalled, due to a full queue
      swap-reading -> gboolean: Swap reading
        Whether data is being read from the swap
      swap-read-total -> guint64: Swap read total
        Total amount of data read from the swap
      swap-writing -> gboolean: Swap writing
        Whether data is being written to the swap
      swap-write-total -> guint64: Swap write total
        Total amount of data written to the swap
      zoom-total -> guint64: Zoom total
        Total size of data processed by the zoom tile handler
      tile-alloc-total -> guint64: Tile allocator total
        Total size of tile-allocator memory
      scratch-total -> guint64: Scratch total
        Total size of scratch memory
      assigned-threads -> gint: Assigned threads
        Number of assigned worker threads
      active-threads -> gint: Active threads
        Number of active worker threads

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        active_threads: int
        assigned_threads: int
        scratch_total: int
        swap_busy: bool
        swap_file_size: int
        swap_queue_full: bool
        swap_queue_stalls: int
        swap_queued_total: int
        swap_read_total: int
        swap_reading: bool
        swap_total: int
        swap_total_uncompressed: int
        swap_write_total: int
        swap_writing: bool
        tile_alloc_total: int
        tile_cache_hits: int
        tile_cache_misses: int
        tile_cache_total: int
        tile_cache_total_max: int
        tile_cache_total_uncompressed: int
        zoom_total: int
    props: Props = ...

class Tile(GObject.GPointer): ...

class TileBackend(TileSource):
    """
    :Constructors:

    ::

        TileBackend(**properties)

    Object GeglTileBackend

    Properties from GeglTileBackend:
      tile-width -> gint: tile-width
        Tile width in pixels
      tile-height -> gint: tile-height
        Tile height in pixels
      px-size -> gint: px-size
        Size of a single pixel in bytes
      tile-size -> gint: tile-size
        Size of the tiles linear buffer in bytes
      format -> gpointer: format
        babl format
      flush-on-destroy -> gboolean: flush-on-destroy
        Cache tiles will be flushed before the backend is destroyed

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        flush_on_destroy: bool
        format: None
        px_size: int
        tile_height: int
        tile_size: int
        tile_width: int
    props: Props = ...
    parent_instance: TileSource = ...
    priv: TileBackendPrivate = ...
    def __init__(self, flush_on_destroy: bool = ...,
                 format: None = ...,
                 tile_height: int = ...,
                 tile_width: int = ...) -> None: ...
    def command(self, command: TileCommand, x: int, y: int, z: int, data: None) -> None: ...
    def get_flush_on_destroy(self) -> bool: ...
    def get_tile_height(self) -> int: ...
    def get_tile_size(self) -> int: ...
    def get_tile_width(self) -> int: ...
    def peek_storage(self) -> TileSource: ...
    def set_extent(self, rectangle: Rectangle) -> None: ...
    def set_flush_on_destroy(self, flush_on_destroy: bool) -> None: ...
    @staticmethod
    def unlink_swap(path: str) -> None: ...


class TileBackendClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TileBackendClass()
    """
    parent_class: TileSourceClass = ...
    padding: list[None] = ...

class TileBackendPrivate(GObject.GPointer): ...

class TileCopyParams(GObject.GPointer):
    """
    :Constructors:

    ::

        TileCopyParams()
    """
    dst_buffer: Buffer = ...
    dst_x: int = ...
    dst_y: int = ...
    dst_z: int = ...

class TileHandler(TileSource):
    """
    :Constructors:

    ::

        TileHandler(**properties)

    Object GeglTileHandler

    Properties from GeglTileHandler:
      source -> GObject: GeglBuffer
        The tilestore to be a facade for

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        source: GObject.Object
    props: Props = ...
    parent_instance: TileSource = ...
    source: TileSource = ...
    priv: TileHandlerPrivate = ...
    def __init__(self, source: GObject.Object = ...) -> None: ...
    def damage_rect(self, rect: Rectangle) -> None: ...
    def damage_tile(self, x: int, y: int, z: int, damage: int) -> None: ...
    def lock(self) -> None: ...
    def set_source(self, source: TileSource) -> None: ...
    def unlock(self) -> None: ...


class TileHandlerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TileHandlerClass()
    """
    parent_class: TileSourceClass = ...

class TileHandlerPrivate(GObject.GPointer): ...

class TileSource(GObject.Object):
    """
    :Constructors:

    ::

        TileSource(**properties)

    Object GeglTileSource

    Signals from GObject:
      notify (GParam)
    """
    parent_instance: GObject.Object = ...
    command: typing.Callable[[TileSource, TileCommand, int, int, int, None], None] = ...
    padding: list[None] = ...

class TileSourceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TileSourceClass()
    """
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class AccessMode(GObject.GFlags):
    READ = 1
    READWRITE = 3
    WRITE = 2

class BlitFlags(GObject.GFlags):
    CACHE = 1
    DEFAULT = 0
    DIRTY = 2

class PadType(GObject.GFlags):
    INPUT = 512
    OUTPUT = 256

class SerializeFlag(GObject.GFlags):
    BAKE_ANIM = 8
    INDENT = 4
    TRIM_DEFAULTS = 1
    VERSION = 2

class AbyssPolicy(GObject.GEnum):
    BLACK = 3
    CLAMP = 1
    LOOP = 2
    NONE = 0
    WHITE = 4

class BablVariant(GObject.GEnum):
    ADD_ALPHA = 8
    FLOAT = 0
    LINEAR = 1
    LINEAR_PREMULTIPLIED = 4
    LINEAR_PREMULTIPLIED_IF_ALPHA = 6
    NON_LINEAR = 2
    PERCEPTUAL = 3
    PERCEPTUAL_PREMULTIPLIED = 5
    PERCEPTUAL_PREMULTIPLIED_IF_ALPHA = 7

class CachePolicy(GObject.GEnum):
    ALWAYS = 2
    AUTO = 0
    NEVER = 1

class DistanceMetric(GObject.GEnum):
    CHEBYSHEV = 2
    EUCLIDEAN = 0
    MANHATTAN = 1

class DitherMethod(GObject.GEnum):
    ADD = 5
    ADD_COVARIANT = 6
    BAYER = 2
    BLUE_NOISE = 9
    BLUE_NOISE_COVARIANT = 10
    FLOYD_STEINBERG = 1
    NONE = 0
    RANDOM = 3
    RANDOM_COVARIANT = 4
    XOR = 7
    XOR_COVARIANT = 8

class MapFlags(GObject.GEnum):
    MAP_EXCLUDE_UNMAPPED = 1

class Orientation(GObject.GEnum):
    HORIZONTAL = 0
    VERTICAL = 1

class RectangleAlignment(GObject.GEnum):
    NEAREST = 2
    SUBSET = 0
    SUPERSET = 1

class ResolutionUnit(GObject.GEnum):
    DPI = 1
    DPM = 2
    NONE = 0

class SamplerType(GObject.GEnum):
    CUBIC = 2
    LINEAR = 1
    LOHALO = 4
    NEAREST = 0
    NOHALO = 3

class SplitStrategy(GObject.GEnum):
    AUTO = 0
    HORIZONTAL = 1
    VERTICAL = 2

class TileCommand(GObject.GEnum):
    EGL_TILE_COPY = 9
    EGL_TILE_EXIST = 4
    EGL_TILE_FLUSH = 6
    EGL_TILE_GET = 2
    EGL_TILE_IDLE = 0
    EGL_TILE_IS_CACHED = 3
    EGL_TILE_LAST_COMMAND = 10
    EGL_TILE_REFETCH = 7
    EGL_TILE_REINIT = 8
    EGL_TILE_SET = 1
    EGL_TILE_VOID = 5
    GEGL_TILE_LAST_0_4_8_COMMAND = 9
