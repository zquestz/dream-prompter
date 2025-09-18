from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import Pango
from gi.repository import xlib

_lock = ...  # FIXME Constant
_namespace: str = "GdkX11"
_version: str = "4.0"

def x11_device_get_id(device: X11DeviceXI2) -> int: ...
def x11_device_manager_lookup(
    device_manager: X11DeviceManagerXI2, device_id: int
) -> Optional[X11DeviceXI2]: ...
def x11_free_compound_text(ctext: int) -> None: ...
def x11_free_text_list(list: str) -> None: ...
def x11_get_server_time(surface: X11Surface) -> int: ...
def x11_get_xatom_by_name_for_display(display: X11Display, atom_name: str) -> int: ...
def x11_get_xatom_name_for_display(display: X11Display, xatom: int) -> str: ...
def x11_lookup_xdisplay(xdisplay: xlib.Display) -> X11Display: ...
def x11_set_sm_client_id(sm_client_id: Optional[str] = None) -> None: ...

class X11AppLaunchContext(Gdk.AppLaunchContext):
    """
    :Constructors:

    ::

        X11AppLaunchContext(**properties)

    Object GdkX11AppLaunchContext

    Properties from GdkAppLaunchContext:
      display -> GdkDisplay: display

    Signals from GAppLaunchContext:
      launch-failed (gchararray)
      launch-started (GAppInfo, GVariant)
      launched (GAppInfo, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        display: Gdk.Display

    props: Props = ...
    def __init__(self, display: Gdk.Display = ...): ...

class X11AppLaunchContextClass(GObject.GPointer): ...

class X11DeviceManagerXI2(GObject.Object):
    """
    :Constructors:

    ::

        X11DeviceManagerXI2(**properties)

    Object GdkX11DeviceManagerXI2

    Properties from GdkX11DeviceManagerXI2:
      display -> GdkDisplay: display
      opcode -> gint: opcode
      major -> gint: major
      minor -> gint: minor

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        display: Gdk.Display
        major: int
        minor: int
        opcode: int

    props: Props = ...
    def __init__(
        self,
        display: Gdk.Display = ...,
        major: int = ...,
        minor: int = ...,
        opcode: int = ...,
    ): ...

class X11DeviceManagerXI2Class(GObject.GPointer): ...

class X11DeviceXI2(Gdk.Device):
    """
    :Constructors:

    ::

        X11DeviceXI2(**properties)

    Object GdkX11DeviceXI2

    Properties from GdkX11DeviceXI2:
      device-id -> gint: device-id

    Signals from GdkDevice:
      changed ()
      tool-changed (GdkDeviceTool)

    Properties from GdkDevice:
      display -> GdkDisplay: display
      name -> gchararray: name
      source -> GdkInputSource: source
      has-cursor -> gboolean: has-cursor
      n-axes -> guint: n-axes
      vendor-id -> gchararray: vendor-id
      product-id -> gchararray: product-id
      seat -> GdkSeat: seat
      num-touches -> guint: num-touches
      tool -> GdkDeviceTool: tool
      direction -> PangoDirection: direction
      has-bidi-layouts -> gboolean: has-bidi-layouts
      caps-lock-state -> gboolean: caps-lock-state
      num-lock-state -> gboolean: num-lock-state
      scroll-lock-state -> gboolean: scroll-lock-state
      modifier-state -> GdkModifierType: modifier-state

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        device_id: int
        caps_lock_state: bool
        direction: Pango.Direction
        display: Gdk.Display
        has_bidi_layouts: bool
        has_cursor: bool
        modifier_state: Gdk.ModifierType
        n_axes: int
        name: str
        num_lock_state: bool
        num_touches: int
        product_id: Optional[str]
        scroll_lock_state: bool
        seat: Gdk.Seat
        source: Gdk.InputSource
        tool: Gdk.DeviceTool
        vendor_id: Optional[str]

    props: Props = ...
    def __init__(
        self,
        device_id: int = ...,
        display: Gdk.Display = ...,
        has_cursor: bool = ...,
        name: str = ...,
        num_touches: int = ...,
        product_id: str = ...,
        seat: Gdk.Seat = ...,
        source: Gdk.InputSource = ...,
        vendor_id: str = ...,
    ): ...

class X11DeviceXI2Class(GObject.GPointer): ...

class X11Display(Gdk.Display):
    """
    :Constructors:

    ::

        X11Display(**properties)

    Object GdkX11Display

    Signals from GdkX11Display:
      xevent (gpointer) -> gboolean

    Signals from GdkDisplay:
      opened ()
      closed (gboolean)
      seat-added (GdkSeat)
      seat-removed (GdkSeat)
      setting-changed (gchararray)

    Properties from GdkDisplay:
      composited -> gboolean: composited
      rgba -> gboolean: rgba
      shadow-width -> gboolean: shadow-width
      input-shapes -> gboolean: input-shapes
      dmabuf-formats -> GdkDmabufFormats: dmabuf-formats

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        composited: bool
        dmabuf_formats: Gdk.DmabufFormats
        input_shapes: bool
        rgba: bool
        shadow_width: bool

    props: Props = ...
    def error_trap_pop(self) -> int: ...
    def error_trap_pop_ignored(self) -> None: ...
    def error_trap_push(self) -> None: ...
    def get_default_group(self) -> Gdk.Surface: ...
    def get_egl_display(self) -> None: ...
    def get_egl_version(self) -> Tuple[bool, int, int]: ...
    def get_glx_version(self) -> Tuple[bool, int, int]: ...
    def get_primary_monitor(self) -> Gdk.Monitor: ...
    def get_screen(self) -> X11Screen: ...
    def get_startup_notification_id(self) -> str: ...
    def get_user_time(self) -> int: ...
    def get_xcursor(self, cursor: Gdk.Cursor) -> int: ...
    def get_xdisplay(self) -> xlib.Display: ...
    def get_xrootwindow(self) -> int: ...
    def get_xscreen(self) -> xlib.Screen: ...
    def grab(self) -> None: ...
    @staticmethod
    def open(display_name: Optional[str] = None) -> Optional[Gdk.Display]: ...
    def set_cursor_theme(self, theme: Optional[str], size: int) -> None: ...
    @staticmethod
    def set_program_class(display: Gdk.Display, program_class: str) -> None: ...
    def set_startup_notification_id(self, startup_id: str) -> None: ...
    def set_surface_scale(self, scale: int) -> None: ...
    def string_to_compound_text(self, str: str) -> Tuple[int, str, int, bytes]: ...
    def text_property_to_text_list(
        self, encoding: str, format: int, text: int, length: int, list: str
    ) -> int: ...
    def ungrab(self) -> None: ...
    def utf8_to_compound_text(self, str: str) -> Tuple[bool, str, int, bytes]: ...

class X11DisplayClass(GObject.GPointer): ...

class X11Drag(Gdk.Drag):
    """
    :Constructors:

    ::

        X11Drag(**properties)

    Object GdkX11Drag

    Signals from GdkDrag:
      cancel (GdkDragCancelReason)
      drop-performed ()
      dnd-finished ()

    Properties from GdkDrag:
      content -> GdkContentProvider: content
      device -> GdkDevice: device
      display -> GdkDisplay: display
      formats -> GdkContentFormats: formats
      selected-action -> GdkDragAction: selected-action
      actions -> GdkDragAction: actions
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        actions: Gdk.DragAction
        content: Gdk.ContentProvider
        device: Gdk.Device
        display: Gdk.Display
        formats: Gdk.ContentFormats
        selected_action: Gdk.DragAction
        surface: Gdk.Surface

    props: Props = ...
    def __init__(
        self,
        actions: Gdk.DragAction = ...,
        content: Gdk.ContentProvider = ...,
        device: Gdk.Device = ...,
        formats: Gdk.ContentFormats = ...,
        selected_action: Gdk.DragAction = ...,
        surface: Gdk.Surface = ...,
    ): ...

class X11DragClass(GObject.GPointer): ...

class X11GLContext(Gdk.GLContext):
    """
    :Constructors:

    ::

        X11GLContext(**properties)

    Object GdkX11GLContext

    Properties from GdkGLContext:
      allowed-apis -> GdkGLAPI: allowed-apis
      api -> GdkGLAPI: api
      shared-context -> GdkGLContext: shared-context

    Properties from GdkDrawContext:
      display -> GdkDisplay: display
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        allowed_apis: Gdk.GLAPI
        api: Gdk.GLAPI
        shared_context: Optional[Gdk.GLContext]
        display: Optional[Gdk.Display]
        surface: Optional[Gdk.Surface]

    props: Props = ...
    def __init__(
        self,
        allowed_apis: Gdk.GLAPI = ...,
        shared_context: Gdk.GLContext = ...,
        display: Gdk.Display = ...,
        surface: Gdk.Surface = ...,
    ): ...

class X11GLContextClass(GObject.GPointer): ...

class X11Monitor(Gdk.Monitor):
    """
    :Constructors:

    ::

        X11Monitor(**properties)

    Object GdkX11Monitor

    Signals from GdkMonitor:
      invalidate ()

    Properties from GdkMonitor:
      description -> gchararray: description
      display -> GdkDisplay: display
      manufacturer -> gchararray: manufacturer
      model -> gchararray: model
      connector -> gchararray: connector
      scale-factor -> gint: scale-factor
      scale -> gdouble: scale
      geometry -> GdkRectangle: geometry
      width-mm -> gint: width-mm
      height-mm -> gint: height-mm
      refresh-rate -> gint: refresh-rate
      subpixel-layout -> GdkSubpixelLayout: subpixel-layout
      valid -> gboolean: valid

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connector: Optional[str]
        description: Optional[str]
        display: Gdk.Display
        geometry: Gdk.Rectangle
        height_mm: int
        manufacturer: Optional[str]
        model: Optional[str]
        refresh_rate: int
        scale: float
        scale_factor: int
        subpixel_layout: Gdk.SubpixelLayout
        valid: bool
        width_mm: int

    props: Props = ...
    def __init__(self, display: Gdk.Display = ...): ...
    def get_output(self) -> int: ...
    def get_workarea(self) -> Gdk.Rectangle: ...

class X11MonitorClass(GObject.GPointer): ...

class X11Screen(GObject.Object):
    """
    :Constructors:

    ::

        X11Screen(**properties)

    Object GdkX11Screen

    Signals from GdkX11Screen:
      window-manager-changed ()

    Signals from GObject:
      notify (GParam)
    """

    def get_current_desktop(self) -> int: ...
    def get_monitor_output(self, monitor_num: int) -> int: ...
    def get_number_of_desktops(self) -> int: ...
    def get_screen_number(self) -> int: ...
    def get_window_manager_name(self) -> str: ...
    def get_xscreen(self) -> xlib.Screen: ...
    def supports_net_wm_hint(self, property_name: str) -> bool: ...

class X11ScreenClass(GObject.GPointer): ...

class X11Surface(Gdk.Surface):
    """
    :Constructors:

    ::

        X11Surface(**properties)

    Object GdkX11Surface

    Signals from GdkSurface:
      layout (gint, gint)
      render (CairoRegion) -> gboolean
      event (gpointer) -> gboolean
      enter-monitor (GdkMonitor)
      leave-monitor (GdkMonitor)

    Properties from GdkSurface:
      cursor -> GdkCursor: cursor
      display -> GdkDisplay: display
      frame-clock -> GdkFrameClock: frame-clock
      mapped -> gboolean: mapped
      width -> gint: width
      height -> gint: height
      scale-factor -> gint: scale-factor
      scale -> gdouble: scale

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        cursor: Optional[Gdk.Cursor]
        display: Gdk.Display
        frame_clock: Gdk.FrameClock
        height: int
        mapped: bool
        scale: float
        scale_factor: int
        width: int

    props: Props = ...
    def __init__(
        self,
        cursor: Optional[Gdk.Cursor] = ...,
        display: Gdk.Display = ...,
        frame_clock: Gdk.FrameClock = ...,
    ): ...
    def get_desktop(self) -> int: ...
    def get_group(self) -> Optional[Gdk.Surface]: ...
    def get_xid(self) -> int: ...
    @staticmethod
    def lookup_for_display(display: X11Display, window: int) -> X11Surface: ...
    def move_to_current_desktop(self) -> None: ...
    def move_to_desktop(self, desktop: int) -> None: ...
    def set_frame_sync_enabled(self, frame_sync_enabled: bool) -> None: ...
    def set_group(self, leader: Gdk.Surface) -> None: ...
    def set_skip_pager_hint(self, skips_pager: bool) -> None: ...
    def set_skip_taskbar_hint(self, skips_taskbar: bool) -> None: ...
    def set_theme_variant(self, variant: str) -> None: ...
    def set_urgency_hint(self, urgent: bool) -> None: ...
    def set_user_time(self, timestamp: int) -> None: ...
    def set_utf8_property(self, name: str, value: Optional[str] = None) -> None: ...

class X11SurfaceClass(GObject.GPointer): ...

class X11DeviceType(GObject.GEnum):
    FLOATING = 2
    LOGICAL = 0
    PHYSICAL = 1
