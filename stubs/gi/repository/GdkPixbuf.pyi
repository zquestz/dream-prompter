from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GModule
from gi.repository import GObject

PIXBUF_MAJOR: int = 2
PIXBUF_MICRO: int = 12
PIXBUF_MINOR: int = 42
PIXBUF_VERSION: str = "2.42.12"
_introspection_module = ...  # FIXME Constant
_lock = ...  # FIXME Constant
_namespace: str = "GdkPixbuf"
_overrides_module = ...  # FIXME Constant
_version: str = "2.0"

def pixbuf_error_quark() -> int: ...

class Pixbuf(GObject.Object, Gio.Icon, Gio.LoadableIcon):
    """
    :Constructors:

    ::

        Pixbuf(**properties)
        new(colorspace:GdkPixbuf.Colorspace, has_alpha:bool, bits_per_sample:int, width:int, height:int) -> GdkPixbuf.Pixbuf or None
        new_from_bytes(data:GLib.Bytes, colorspace:GdkPixbuf.Colorspace, has_alpha:bool, bits_per_sample:int, width:int, height:int, rowstride:int) -> GdkPixbuf.Pixbuf
        new_from_data(data:list, colorspace:GdkPixbuf.Colorspace, has_alpha:bool, bits_per_sample:int, width:int, height:int, rowstride:int, destroy_fn:GdkPixbuf.PixbufDestroyNotify=None, destroy_fn_data=None) -> GdkPixbuf.Pixbuf
        new_from_file(filename:str) -> GdkPixbuf.Pixbuf or None
        new_from_file_at_scale(filename:str, width:int, height:int, preserve_aspect_ratio:bool) -> GdkPixbuf.Pixbuf or None
        new_from_file_at_size(filename:str, width:int, height:int) -> GdkPixbuf.Pixbuf or None
        new_from_inline(data:list, copy_pixels:bool) -> GdkPixbuf.Pixbuf
        new_from_resource(resource_path:str) -> GdkPixbuf.Pixbuf or None
        new_from_resource_at_scale(resource_path:str, width:int, height:int, preserve_aspect_ratio:bool) -> GdkPixbuf.Pixbuf or None
        new_from_stream(stream:Gio.InputStream, cancellable:Gio.Cancellable=None) -> GdkPixbuf.Pixbuf or None
        new_from_stream_at_scale(stream:Gio.InputStream, width:int, height:int, preserve_aspect_ratio:bool, cancellable:Gio.Cancellable=None) -> GdkPixbuf.Pixbuf or None
        new_from_stream_finish(async_result:Gio.AsyncResult) -> GdkPixbuf.Pixbuf or None
        new_from_xpm_data(data:list) -> GdkPixbuf.Pixbuf or None

    Object GdkPixbuf

    Properties from GdkPixbuf:
      colorspace -> GdkColorspace: Colorspace
        The colorspace in which the samples are interpreted
      n-channels -> gint: Number of Channels
        The number of samples per pixel
      has-alpha -> gboolean: Has Alpha
        Whether the pixbuf has an alpha channel
      bits-per-sample -> gint: Bits per Sample
        The number of bits per sample
      width -> gint: Width
        The number of columns of the pixbuf
      height -> gint: Height
        The number of rows of the pixbuf
      rowstride -> gint: Rowstride
        The number of bytes between the start of a row and the start of the next row
      pixels -> gpointer: Pixels
        A pointer to the pixel data of the pixbuf
      pixel-bytes -> GBytes: Pixel Bytes
        Readonly pixel data

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        bits_per_sample: int
        colorspace: Colorspace
        has_alpha: bool
        height: int
        n_channels: int
        pixel_bytes: GLib.Bytes
        pixels: None
        rowstride: int
        width: int

    props: Props = ...
    def __init__(
        self,
        bits_per_sample: int = ...,
        colorspace: Colorspace = ...,
        has_alpha: bool = ...,
        height: int = ...,
        n_channels: int = ...,
        pixel_bytes: GLib.Bytes = ...,
        pixels: None = ...,
        rowstride: int = ...,
        width: int = ...,
    ): ...
    def add_alpha(
        self, substitute_color: bool, r: int, g: int, b: int
    ) -> Optional[Pixbuf]: ...
    def apply_embedded_orientation(self) -> Optional[Pixbuf]: ...
    @staticmethod
    def calculate_rowstride(
        colorspace: Colorspace,
        has_alpha: bool,
        bits_per_sample: int,
        width: int,
        height: int,
    ) -> int: ...
    def composite(
        self,
        dest: Pixbuf,
        dest_x: int,
        dest_y: int,
        dest_width: int,
        dest_height: int,
        offset_x: float,
        offset_y: float,
        scale_x: float,
        scale_y: float,
        interp_type: InterpType,
        overall_alpha: int,
    ) -> None: ...
    def composite_color(
        self,
        dest: Pixbuf,
        dest_x: int,
        dest_y: int,
        dest_width: int,
        dest_height: int,
        offset_x: float,
        offset_y: float,
        scale_x: float,
        scale_y: float,
        interp_type: InterpType,
        overall_alpha: int,
        check_x: int,
        check_y: int,
        check_size: int,
        color1: int,
        color2: int,
    ) -> None: ...
    def composite_color_simple(
        self,
        dest_width: int,
        dest_height: int,
        interp_type: InterpType,
        overall_alpha: int,
        check_size: int,
        color1: int,
        color2: int,
    ) -> Optional[Pixbuf]: ...
    def copy(self) -> Optional[Pixbuf]: ...
    def copy_area(
        self,
        src_x: int,
        src_y: int,
        width: int,
        height: int,
        dest_pixbuf: Pixbuf,
        dest_x: int,
        dest_y: int,
    ) -> None: ...
    def copy_options(self, dest_pixbuf: Pixbuf) -> bool: ...
    def fill(self, pixel: int) -> None: ...
    def flip(self, horizontal: bool) -> Optional[Pixbuf]: ...
    def get_bits_per_sample(self) -> int: ...
    def get_byte_length(self) -> int: ...
    def get_colorspace(self) -> Colorspace: ...
    @staticmethod
    def get_file_info(filename: str) -> Tuple[Optional[PixbufFormat], int, int]: ...
    @staticmethod
    def get_file_info_async(
        filename: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def get_file_info_finish(
        async_result: Gio.AsyncResult,
    ) -> Tuple[Optional[PixbufFormat], int, int]: ...
    @staticmethod
    def get_formats() -> list[PixbufFormat]: ...
    def get_has_alpha(self) -> bool: ...
    def get_height(self) -> int: ...
    def get_n_channels(self) -> int: ...
    def get_option(self, key: str) -> Optional[str]: ...
    def get_options(self) -> dict[str, str]: ...
    def get_pixels(self) -> bytes: ...
    def get_rowstride(self) -> int: ...
    def get_width(self) -> int: ...
    @staticmethod
    def init_modules(path: str) -> bool: ...
    @classmethod
    def new(
        cls,
        colorspace: Colorspace,
        has_alpha: bool,
        bits_per_sample: int,
        width: int,
        height: int,
    ) -> Optional[Pixbuf]: ...
    @classmethod
    def new_from_bytes(
        cls,
        data: GLib.Bytes,
        colorspace: Colorspace,
        has_alpha: bool,
        bits_per_sample: int,
        width: int,
        height: int,
        rowstride: int,
    ) -> Pixbuf: ...
    # override
    @classmethod
    def new_from_data(
        cls,
        data: GLib.Bytes,
        colorspace: Colorspace,
        has_alpha: bool,
        bits_per_sample: int,
        width: int,
        height: int,
        rowstride: int,
        destroy_fn: Any,
        *destroy_fn_data: Any,
    ) -> Pixbuf: ...
    @classmethod
    def new_from_file(cls, filename: str) -> Optional[Pixbuf]: ...
    @classmethod
    def new_from_file_at_scale(
        cls, filename: str, width: int, height: int, preserve_aspect_ratio: bool
    ) -> Optional[Pixbuf]: ...
    @classmethod
    def new_from_file_at_size(
        cls, filename: str, width: int, height: int
    ) -> Optional[Pixbuf]: ...
    @classmethod
    def new_from_inline(cls, data: Sequence[int], copy_pixels: bool) -> Pixbuf: ...
    @classmethod
    def new_from_resource(cls, resource_path: str) -> Optional[Pixbuf]: ...
    @classmethod
    def new_from_resource_at_scale(
        cls, resource_path: str, width: int, height: int, preserve_aspect_ratio: bool
    ) -> Optional[Pixbuf]: ...
    @classmethod
    def new_from_stream(
        cls, stream: Gio.InputStream, cancellable: Optional[Gio.Cancellable] = None
    ) -> Optional[Pixbuf]: ...
    @staticmethod
    def new_from_stream_async(
        stream: Gio.InputStream,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_from_stream_at_scale(
        cls,
        stream: Gio.InputStream,
        width: int,
        height: int,
        preserve_aspect_ratio: bool,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Optional[Pixbuf]: ...
    @staticmethod
    def new_from_stream_at_scale_async(
        stream: Gio.InputStream,
        width: int,
        height: int,
        preserve_aspect_ratio: bool,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_from_stream_finish(
        cls, async_result: Gio.AsyncResult
    ) -> Optional[Pixbuf]: ...
    @classmethod
    def new_from_xpm_data(cls, data: Sequence[str]) -> Optional[Pixbuf]: ...
    def new_subpixbuf(
        self, src_x: int, src_y: int, width: int, height: int
    ) -> Pixbuf: ...
    def read_pixel_bytes(self) -> GLib.Bytes: ...
    def read_pixels(self) -> int: ...
    def remove_option(self, key: str) -> bool: ...
    def rotate_simple(self, angle: PixbufRotation) -> Optional[Pixbuf]: ...
    def saturate_and_pixelate(
        self, dest: Pixbuf, saturation: float, pixelate: bool
    ) -> None: ...
    def save_to_bufferv(
        self,
        type: str,
        option_keys: Optional[Sequence[str]] = None,
        option_values: Optional[Sequence[str]] = None,
    ) -> Tuple[bool, bytes]: ...
    def save_to_callbackv(
        self,
        save_func: Callable[..., Tuple[bool, GLib.Error]],
        type: str,
        option_keys: Optional[Sequence[str]] = None,
        option_values: Optional[Sequence[str]] = None,
        *user_data: Any,
    ) -> bool: ...
    @staticmethod
    def save_to_stream_finish(async_result: Gio.AsyncResult) -> bool: ...
    def save_to_streamv(
        self,
        stream: Gio.OutputStream,
        type: str,
        option_keys: Optional[Sequence[str]] = None,
        option_values: Optional[Sequence[str]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def save_to_streamv_async(
        self,
        stream: Gio.OutputStream,
        type: str,
        option_keys: Optional[Sequence[str]] = None,
        option_values: Optional[Sequence[str]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def savev(
        self,
        filename: str,
        type: str,
        option_keys: Optional[Sequence[str]] = None,
        option_values: Optional[Sequence[str]] = None,
    ) -> bool: ...
    def scale(
        self,
        dest: Pixbuf,
        dest_x: int,
        dest_y: int,
        dest_width: int,
        dest_height: int,
        offset_x: float,
        offset_y: float,
        scale_x: float,
        scale_y: float,
        interp_type: InterpType,
    ) -> None: ...
    def scale_simple(
        self, dest_width: int, dest_height: int, interp_type: InterpType
    ) -> Optional[Pixbuf]: ...
    def set_option(self, key: str, value: str) -> bool: ...

class PixbufAnimation(GObject.Object):
    """
    :Constructors:

    ::

        PixbufAnimation(**properties)
        new_from_file(filename:str) -> GdkPixbuf.PixbufAnimation or None
        new_from_resource(resource_path:str) -> GdkPixbuf.PixbufAnimation or None
        new_from_stream(stream:Gio.InputStream, cancellable:Gio.Cancellable=None) -> GdkPixbuf.PixbufAnimation or None
        new_from_stream_finish(async_result:Gio.AsyncResult) -> GdkPixbuf.PixbufAnimation or None

    Object GdkPixbufAnimation

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def do_get_iter(
        self, start_time: Optional[GLib.TimeVal] = None
    ) -> PixbufAnimationIter: ...
    def do_get_size(self, width: int, height: int) -> None: ...
    def do_get_static_image(self) -> Pixbuf: ...
    def do_is_static_image(self) -> bool: ...
    def get_height(self) -> int: ...
    def get_iter(
        self, start_time: Optional[GLib.TimeVal] = None
    ) -> PixbufAnimationIter: ...
    def get_static_image(self) -> Pixbuf: ...
    def get_width(self) -> int: ...
    def is_static_image(self) -> bool: ...
    @classmethod
    def new_from_file(cls, filename: str) -> Optional[PixbufAnimation]: ...
    @classmethod
    def new_from_resource(cls, resource_path: str) -> Optional[PixbufAnimation]: ...
    @classmethod
    def new_from_stream(
        cls, stream: Gio.InputStream, cancellable: Optional[Gio.Cancellable] = None
    ) -> Optional[PixbufAnimation]: ...
    @staticmethod
    def new_from_stream_async(
        stream: Gio.InputStream,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_from_stream_finish(
        cls, async_result: Gio.AsyncResult
    ) -> Optional[PixbufAnimation]: ...

class PixbufAnimationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PixbufAnimationClass()
    """

    parent_class: GObject.ObjectClass = ...
    is_static_image: Callable[[PixbufAnimation], bool] = ...
    get_static_image: Callable[[PixbufAnimation], Pixbuf] = ...
    get_size: Callable[[PixbufAnimation, int, int], None] = ...
    get_iter: Callable[
        [PixbufAnimation, Optional[GLib.TimeVal]], PixbufAnimationIter
    ] = ...

class PixbufAnimationIter(GObject.Object):
    """
    :Constructors:

    ::

        PixbufAnimationIter(**properties)

    Object GdkPixbufAnimationIter

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def advance(self, current_time: Optional[GLib.TimeVal] = None) -> bool: ...
    def do_advance(self, current_time: Optional[GLib.TimeVal] = None) -> bool: ...
    def do_get_delay_time(self) -> int: ...
    def do_get_pixbuf(self) -> Pixbuf: ...
    def do_on_currently_loading_frame(self) -> bool: ...
    def get_delay_time(self) -> int: ...
    def get_pixbuf(self) -> Pixbuf: ...
    def on_currently_loading_frame(self) -> bool: ...

class PixbufAnimationIterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PixbufAnimationIterClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_delay_time: Callable[[PixbufAnimationIter], int] = ...
    get_pixbuf: Callable[[PixbufAnimationIter], Pixbuf] = ...
    on_currently_loading_frame: Callable[[PixbufAnimationIter], bool] = ...
    advance: Callable[[PixbufAnimationIter, Optional[GLib.TimeVal]], bool] = ...

class PixbufFormat(GObject.GBoxed):
    """
    :Constructors:

    ::

        PixbufFormat()
    """

    name: str = ...
    signature: PixbufModulePattern = ...
    domain: str = ...
    description: str = ...
    mime_types: list[str] = ...
    extensions: list[str] = ...
    flags: int = ...
    disabled: bool = ...
    license: str = ...
    def copy(self) -> Optional[PixbufFormat]: ...
    def free(self) -> None: ...
    def get_description(self) -> Optional[str]: ...
    def get_extensions(self) -> Optional[list[str]]: ...
    def get_license(self) -> Optional[str]: ...
    def get_mime_types(self) -> Optional[list[str]]: ...
    def get_name(self) -> Optional[str]: ...
    def is_disabled(self) -> bool: ...
    def is_save_option_supported(self, option_key: str) -> bool: ...
    def is_scalable(self) -> bool: ...
    def is_writable(self) -> bool: ...
    def set_disabled(self, disabled: bool) -> None: ...

class PixbufLoader(GObject.Object):
    """
    :Constructors:

    ::

        PixbufLoader(**properties)
        new() -> GdkPixbuf.PixbufLoader
        new_with_mime_type(mime_type:str) -> GdkPixbuf.PixbufLoader
        new_with_type(image_type:str) -> GdkPixbuf.PixbufLoader

    Object GdkPixbufLoader

    Signals from GdkPixbufLoader:
      size-prepared (gint, gint)
      area-prepared ()
      area-updated (gint, gint, gint, gint)
      closed ()

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: None = ...
    def close(self) -> bool: ...
    def do_area_prepared(self) -> None: ...
    def do_area_updated(self, x: int, y: int, width: int, height: int) -> None: ...
    def do_closed(self) -> None: ...
    def do_size_prepared(self, width: int, height: int) -> None: ...
    def get_animation(self) -> Optional[PixbufAnimation]: ...
    def get_format(self) -> Optional[PixbufFormat]: ...
    def get_pixbuf(self) -> Optional[Pixbuf]: ...
    @classmethod
    def new(cls) -> PixbufLoader: ...
    @classmethod
    def new_with_mime_type(cls, mime_type: str) -> PixbufLoader: ...
    @classmethod
    def new_with_type(cls, image_type: str) -> PixbufLoader: ...
    def set_size(self, width: int, height: int) -> None: ...
    def write(self, buf: Sequence[int]) -> bool: ...
    def write_bytes(self, buffer: GLib.Bytes) -> bool: ...

class PixbufLoaderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PixbufLoaderClass()
    """

    parent_class: GObject.ObjectClass = ...
    size_prepared: Callable[[PixbufLoader, int, int], None] = ...
    area_prepared: Callable[[PixbufLoader], None] = ...
    area_updated: Callable[[PixbufLoader, int, int, int, int], None] = ...
    closed: Callable[[PixbufLoader], None] = ...

class PixbufModule(GObject.GPointer):
    """
    :Constructors:

    ::

        PixbufModule()
    """

    module_name: str = ...
    module_path: str = ...
    module: GModule.Module = ...
    info: PixbufFormat = ...
    load: Callable[[None], Pixbuf] = ...
    load_xpm_data: Callable[[Sequence[str]], Pixbuf] = ...
    begin_load: None = ...
    stop_load: Callable[[None], bool] = ...
    load_increment: Callable[[None, Sequence[int]], bool] = ...
    load_animation: Callable[[None], PixbufAnimation] = ...
    save: Callable[
        [None, Pixbuf, Optional[Sequence[str]], Optional[Sequence[str]]], bool
    ] = ...
    save_to_callback: None = ...
    is_save_option_supported: Callable[[str], bool] = ...
    _reserved1: None = ...
    _reserved2: None = ...
    _reserved3: None = ...
    _reserved4: None = ...

class PixbufModulePattern(GObject.GPointer):
    """
    :Constructors:

    ::

        PixbufModulePattern()
    """

    prefix: str = ...
    mask: str = ...
    relevance: int = ...

class PixbufNonAnim(PixbufAnimation):
    """
    :Constructors:

    ::

        PixbufNonAnim(**properties)
        new(pixbuf:GdkPixbuf.Pixbuf) -> GdkPixbuf.PixbufAnimation

    Object GdkPixbufNonAnim

    Signals from GObject:
      notify (GParam)
    """

    @classmethod
    def new(cls, pixbuf: Pixbuf) -> PixbufNonAnim: ...

class PixbufSimpleAnim(PixbufAnimation):
    """
    :Constructors:

    ::

        PixbufSimpleAnim(**properties)
        new(width:int, height:int, rate:float) -> GdkPixbuf.PixbufSimpleAnim

    Object GdkPixbufSimpleAnim

    Properties from GdkPixbufSimpleAnim:
      loop -> gboolean: Loop
        Whether the animation should loop when it reaches the end

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        loop: bool

    props: Props = ...
    def __init__(self, loop: bool = ...): ...
    def add_frame(self, pixbuf: Pixbuf) -> None: ...
    def get_loop(self) -> bool: ...
    @classmethod
    def new(cls, width: int, height: int, rate: float) -> PixbufSimpleAnim: ...
    def set_loop(self, loop: bool) -> None: ...

class PixbufSimpleAnimClass(GObject.GPointer): ...
class PixbufSimpleAnimIter(PixbufAnimationIter): ...

class PixbufFormatFlags(GObject.GFlags):
    SCALABLE = 2
    THREADSAFE = 4
    WRITABLE = 1

class Colorspace(GObject.GEnum):
    RGB = 0

class InterpType(GObject.GEnum):
    BILINEAR = 2
    HYPER = 3
    NEAREST = 0
    TILES = 1

class PixbufAlphaMode(GObject.GEnum):
    BILEVEL = 0
    FULL = 1

class PixbufError(GObject.GEnum):
    BAD_OPTION = 2
    CORRUPT_IMAGE = 0
    FAILED = 5
    INCOMPLETE_ANIMATION = 6
    INSUFFICIENT_MEMORY = 1
    UNKNOWN_TYPE = 3
    UNSUPPORTED_OPERATION = 4
    @staticmethod
    def quark() -> int: ...

class PixbufRotation(GObject.GEnum):
    CLOCKWISE = 270
    COUNTERCLOCKWISE = 90
    NONE = 0
    UPSIDEDOWN = 180
