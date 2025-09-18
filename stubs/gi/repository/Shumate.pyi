import typing

from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk

T = typing.TypeVar("T")

MAJOR_VERSION: int = 1
MAP_SOURCE_MFF_RELIEF: str = "mff-relief"
MAP_SOURCE_OSM_CYCLE_MAP: str = "osm-cyclemap"
MAP_SOURCE_OSM_MAPNIK: str = "osm-mapnik"
MAP_SOURCE_OSM_TRANSPORT_MAP: str = "osm-transportmap"
MAP_SOURCE_OWM_CLOUDS: str = "owm-clouds"
MAP_SOURCE_OWM_PRECIPITATION: str = "owm-precipitation"
MAP_SOURCE_OWM_PRESSURE: str = "owm-pressure"
MAP_SOURCE_OWM_TEMPERATURE: str = "owm-temperature"
MAP_SOURCE_OWM_WIND: str = "owm-wind"
MAX_LATITUDE: float = 85.0511287798
MAX_LONGITUDE: float = 180.0
MICRO_VERSION: int = 2
MINOR_VERSION: int = 2
MIN_LATITUDE: float = -85.0511287798
MIN_LONGITUDE: float = -180.0
_lock = ...  # FIXME Constant
_namespace: str = "Shumate"
_version: str = "1.0"

def file_cache_error_quark() -> int: ...
def get_user_agent() -> str: ...
def set_user_agent(new_user_agent: typing.Optional[str] = None) -> None: ...
def style_error_quark() -> int: ...
def tile_downloader_error_quark() -> int: ...

class Compass(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Compass(**properties)
        new(viewport:Shumate.Viewport=None) -> Shumate.Compass

    Object ShumateCompass

    Properties from ShumateCompass:
      viewport -> ShumateViewport: The viewport
        The viewport

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        viewport: typing.Optional[Viewport]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        viewport: typing.Optional[Viewport] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_viewport(self) -> typing.Optional[Viewport]: ...
    @classmethod
    def new(cls, viewport: typing.Optional[Viewport] = None) -> Compass: ...
    def set_viewport(self, viewport: typing.Optional[Viewport] = None) -> None: ...

class CompassClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CompassClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Coordinate(GObject.InitiallyUnowned, Location):
    """
    :Constructors:

    ::

        Coordinate(**properties)
        new() -> Shumate.Coordinate
        new_full(latitude:float, longitude:float) -> Shumate.Coordinate

    Object ShumateCoordinate

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        latitude: float
        longitude: float

    props: Props = ...
    parent_instance: GObject.InitiallyUnowned = ...
    def __init__(self, latitude: float = ..., longitude: float = ...) -> None: ...
    @classmethod
    def new(cls) -> Coordinate: ...
    @classmethod
    def new_full(cls, latitude: float, longitude: float) -> Coordinate: ...

class CoordinateClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CoordinateClass()
    """

    parent_class: GObject.InitiallyUnownedClass = ...
    padding: list[None] = ...

class DataSource(GObject.Object):
    """
    :Constructors:

    ::

        DataSource(**properties)

    Object ShumateDataSource

    Signals from ShumateDataSource:
      received-data (gint, gint, gint, GBytes)

    Properties from ShumateDataSource:
      min-zoom-level -> guint: min-zoom-level
        min-zoom-level
      max-zoom-level -> guint: max-zoom-level
        max-zoom-level

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        max_zoom_level: int
        min_zoom_level: int

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self, max_zoom_level: int = ..., min_zoom_level: int = ...
    ) -> None: ...
    def do_get_tile_data_async(
        self,
        x: int,
        y: int,
        zoom_level: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_get_tile_data_finish(self, result: Gio.AsyncResult) -> GLib.Bytes: ...
    def do_start_request(
        self,
        x: int,
        y: int,
        zoom_level: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> DataSourceRequest: ...
    def get_max_zoom_level(self) -> int: ...
    def get_min_zoom_level(self) -> int: ...
    def get_tile_data_async(
        self,
        x: int,
        y: int,
        zoom_level: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_tile_data_finish(self, result: Gio.AsyncResult) -> GLib.Bytes: ...
    def set_max_zoom_level(self, zoom_level: int) -> None: ...
    def set_min_zoom_level(self, zoom_level: int) -> None: ...
    def start_request(
        self,
        x: int,
        y: int,
        zoom_level: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> DataSourceRequest: ...

class DataSourceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DataSourceClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_tile_data_async: typing.Callable[..., None] = ...
    get_tile_data_finish: typing.Callable[[DataSource, Gio.AsyncResult], GLib.Bytes] = (
        ...
    )
    start_request: typing.Callable[
        [DataSource, int, int, int, typing.Optional[Gio.Cancellable]], DataSourceRequest
    ] = ...
    padding: list[None] = ...

class DataSourceRequest(GObject.Object):
    """
    :Constructors:

    ::

        DataSourceRequest(**properties)
        new(x:int, y:int, zoom_level:int) -> Shumate.DataSourceRequest

    Object ShumateDataSourceRequest

    Properties from ShumateDataSourceRequest:
      x -> gint: x
        x
      y -> gint: y
        y
      zoom-level -> gint: zoom-level
        zoom-level
      data -> GBytes: data
        data
      error -> GError: error
        error
      completed -> gboolean: completed
        completed

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        completed: bool
        data: typing.Optional[GLib.Bytes]
        error: typing.Optional[GLib.Error]
        x: int
        y: int
        zoom_level: int

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, x: int = ..., y: int = ..., zoom_level: int = ...) -> None: ...
    def complete(self) -> None: ...
    def emit_data(self, data: GLib.Bytes, complete: bool) -> None: ...
    def emit_error(self, error: GLib.Error) -> None: ...
    def get_data(self) -> typing.Optional[GLib.Bytes]: ...
    def get_error(self) -> typing.Optional[GLib.Error]: ...
    def get_x(self) -> int: ...
    def get_y(self) -> int: ...
    def get_zoom_level(self) -> int: ...
    def is_completed(self) -> bool: ...
    @classmethod
    def new(cls, x: int, y: int, zoom_level: int) -> DataSourceRequest: ...

class DataSourceRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DataSourceRequestClass()
    """

    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class FileCache(GObject.Object):
    """
    :Constructors:

    ::

        FileCache(**properties)
        new_full(size_limit:int, cache_key:str, cache_dir:str=None) -> Shumate.FileCache

    Object ShumateFileCache

    Properties from ShumateFileCache:
      size-limit -> guint: Size Limit
        The cache's size limit (Mb)
      cache-dir -> gchararray: Cache Directory
        The directory of the cache
      cache-key -> gchararray: Cache Key
        The key used when storing and retrieving tiles

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        cache_dir: str
        cache_key: str
        size_limit: int

    props: Props = ...
    def __init__(
        self, cache_dir: str = ..., cache_key: str = ..., size_limit: int = ...
    ) -> None: ...
    def get_cache_dir(self) -> str: ...
    def get_cache_key(self) -> str: ...
    def get_size_limit(self) -> int: ...
    def get_tile_async(
        self,
        x: int,
        y: int,
        zoom_level: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_tile_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[GLib.Bytes, str, GLib.DateTime]: ...
    def mark_up_to_date(self, x: int, y: int, zoom_level: int) -> None: ...
    @classmethod
    def new_full(
        cls, size_limit: int, cache_key: str, cache_dir: typing.Optional[str] = None
    ) -> FileCache: ...
    def purge_cache_async(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def purge_cache_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_size_limit(self, size_limit: int) -> None: ...
    def store_tile_async(
        self,
        x: int,
        y: int,
        zoom_level: int,
        bytes: GLib.Bytes,
        etag: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def store_tile_finish(self, result: Gio.AsyncResult) -> bool: ...

class FileCacheClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileCacheClass()
    """

    parent_class: GObject.ObjectClass = ...

class Layer(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Layer(**properties)

    Object ShumateLayer

    Properties from ShumateLayer:
      viewport -> ShumateViewport: Viewport
        The viewport used to display the layer

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        viewport: Viewport
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    parent_instance: Gtk.Widget = ...
    def __init__(
        self,
        viewport: Viewport = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def do_get_debug_text(self) -> typing.Optional[str]: ...
    def get_viewport(self) -> Viewport: ...

class LayerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LayerClass()
    """

    parent_class: Gtk.WidgetClass = ...
    get_debug_text: typing.Callable[[Layer], typing.Optional[str]] = ...
    padding: list[None] = ...

class License(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        License(**properties)
        new() -> Shumate.License

    Object ShumateLicense

    Properties from ShumateLicense:
      extra-text -> gchararray: Additional license
        Additional license text
      xalign -> gfloat: Horizontal Alignment
        X alignment of the child

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        extra_text: str
        xalign: float
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        extra_text: str = ...,
        xalign: float = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def append_map_source(self, map_source: MapSource) -> None: ...
    def get_extra_text(self) -> str: ...
    def get_xalign(self) -> float: ...
    @classmethod
    def new(cls) -> License: ...
    def prepend_map_source(self, map_source: MapSource) -> None: ...
    def remove_map_source(self, map_source: MapSource) -> None: ...
    def set_extra_text(self, text: str) -> None: ...
    def set_xalign(self, xalign: float) -> None: ...

class LicenseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LicenseClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Location(GObject.GInterface):
    """
    Interface ShumateLocation

    Signals from GObject:
      notify (GParam)
    """

    def distance(self, other: Location) -> float: ...
    def get_latitude(self) -> float: ...
    def get_longitude(self) -> float: ...
    def set_location(self, latitude: float, longitude: float) -> None: ...

class LocationInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        LocationInterface()
    """

    g_iface: GObject.TypeInterface = ...
    get_latitude: typing.Callable[[Location], float] = ...
    get_longitude: typing.Callable[[Location], float] = ...
    set_location: typing.Callable[[Location, float, float], None] = ...

class Map(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Map(**properties)
        new() -> Shumate.Map
        new_simple() -> Shumate.Map

    Object ShumateMap

    Signals from ShumateMap:
      animation-completed ()

    Properties from ShumateMap:
      zoom-on-double-click -> gboolean: Zoom in on double click
        Zoom in and recenter on double click on the map
      animate-zoom -> gboolean: Animate zoom level change
        Animate zoom change when zooming in/out
      state -> ShumateState: View's state
        View's global state
      go-to-duration -> guint: Go to animation duration
        The duration of an animation when going to a location
      viewport -> ShumateViewport: Viewport
        Viewport

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        animate_zoom: bool
        go_to_duration: int
        state: State
        viewport: Viewport
        zoom_on_double_click: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        animate_zoom: bool = ...,
        go_to_duration: int = ...,
        zoom_on_double_click: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_layer(self, layer: Layer) -> None: ...
    def center_on(self, latitude: float, longitude: float) -> None: ...
    def get_animate_zoom(self) -> bool: ...
    def get_go_to_duration(self) -> int: ...
    def get_state(self) -> State: ...
    def get_viewport(self) -> Viewport: ...
    def get_zoom_on_double_click(self) -> bool: ...
    def go_to(self, latitude: float, longitude: float) -> None: ...
    def go_to_full(
        self, latitude: float, longitude: float, zoom_level: float
    ) -> None: ...
    def go_to_full_with_duration(
        self, latitude: float, longitude: float, zoom_level: float, duration_ms: int
    ) -> None: ...
    def insert_layer_above(
        self, layer: Layer, next_sibling: typing.Optional[Layer] = None
    ) -> None: ...
    def insert_layer_behind(
        self, layer: Layer, next_sibling: typing.Optional[Layer] = None
    ) -> None: ...
    @classmethod
    def new(cls) -> Map: ...
    @classmethod
    def new_simple(cls) -> Map: ...
    def remove_layer(self, layer: Layer) -> None: ...
    def set_animate_zoom(self, value: bool) -> None: ...
    def set_go_to_duration(self, duration: int) -> None: ...
    def set_map_source(self, map_source: MapSource) -> None: ...
    def set_zoom_on_double_click(self, value: bool) -> None: ...
    def stop_go_to(self) -> None: ...
    def zoom_in(self) -> None: ...
    def zoom_out(self) -> None: ...

class MapClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MapClass()
    """

    parent_class: Gtk.WidgetClass = ...

class MapLayer(Layer, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        MapLayer(**properties)
        new(map_source:Shumate.MapSource, viewport:Shumate.Viewport) -> Shumate.MapLayer

    Object ShumateMapLayer

    Signals from ShumateMapLayer:
      symbol-clicked (ShumateSymbolEvent)

    Properties from ShumateMapLayer:
      map-source -> ShumateMapSource: Map Source
        The Map Source

    Properties from ShumateLayer:
      viewport -> ShumateViewport: Viewport
        The viewport used to display the layer

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        map_source: MapSource
        viewport: Viewport
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        map_source: MapSource = ...,
        viewport: Viewport = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    @classmethod
    def new(cls, map_source: MapSource, viewport: Viewport) -> MapLayer: ...

class MapLayerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MapLayerClass()
    """

    parent_class: LayerClass = ...

class MapSource(GObject.Object):
    """
    :Constructors:

    ::

        MapSource(**properties)

    Object ShumateMapSource

    Properties from ShumateMapSource:
      id -> gchararray: Id
        The id of the map source
      name -> gchararray: Name
        The name of the map source
      license -> gchararray: License
        The usage license of the map source
      license-uri -> gchararray: License-uri
        The usage license's uri for more information
      min-zoom-level -> guint: Minimum Zoom Level
        The minimum zoom level
      max-zoom-level -> guint: Maximum Zoom Level
        The maximum zoom level
      tile-size -> guint: Tile Size
        The map size
      projection -> ShumateMapProjection: Projection
        The map projection

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        id: str
        license: str
        license_uri: str
        max_zoom_level: int
        min_zoom_level: int
        name: str
        projection: MapProjection
        tile_size: int

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self,
        id: str = ...,
        license: str = ...,
        license_uri: str = ...,
        max_zoom_level: int = ...,
        min_zoom_level: int = ...,
        name: str = ...,
        projection: MapProjection = ...,
        tile_size: int = ...,
    ) -> None: ...
    def do_fill_tile_async(
        self,
        tile: Tile,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_fill_tile_finish(self, result: Gio.AsyncResult) -> bool: ...
    def fill_tile_async(
        self,
        tile: Tile,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def fill_tile_finish(self, result: Gio.AsyncResult) -> bool: ...
    def get_column_count(self, zoom_level: int) -> int: ...
    def get_id(self) -> str: ...
    def get_latitude(self, zoom_level: float, y: float) -> float: ...
    def get_license(self) -> str: ...
    def get_license_uri(self) -> str: ...
    def get_longitude(self, zoom_level: float, x: float) -> float: ...
    def get_max_zoom_level(self) -> int: ...
    def get_meters_per_pixel(
        self, zoom_level: float, latitude: float, longitude: float
    ) -> float: ...
    def get_min_zoom_level(self) -> int: ...
    def get_name(self) -> str: ...
    def get_projection(self) -> MapProjection: ...
    def get_row_count(self, zoom_level: int) -> int: ...
    def get_tile_size(self) -> int: ...
    def get_tile_size_at_zoom(self, zoom_level: float) -> float: ...
    def get_x(self, zoom_level: float, longitude: float) -> float: ...
    def get_y(self, zoom_level: float, latitude: float) -> float: ...
    def set_id(self, id: str) -> None: ...
    def set_license(self, license: str) -> None: ...
    def set_license_uri(self, license_uri: str) -> None: ...
    def set_max_zoom_level(self, zoom_level: int) -> None: ...
    def set_min_zoom_level(self, zoom_level: int) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_projection(self, projection: MapProjection) -> None: ...
    def set_tile_size(self, tile_size: int) -> None: ...

class MapSourceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MapSourceClass()
    """

    parent_class: GObject.ObjectClass = ...
    fill_tile_async: typing.Callable[..., None] = ...
    fill_tile_finish: typing.Callable[[MapSource, Gio.AsyncResult], bool] = ...
    padding: list[None] = ...

class MapSourceRegistry(GObject.Object, Gio.ListModel):
    """
    :Constructors:

    ::

        MapSourceRegistry(**properties)
        new() -> Shumate.MapSourceRegistry
        new_with_defaults() -> Shumate.MapSourceRegistry

    Object ShumateMapSourceRegistry

    Signals from GListModel:
      items-changed (guint, guint, guint)

    Signals from GObject:
      notify (GParam)
    """

    def add(self, map_source: MapSource) -> None: ...
    def get_by_id(self, id: str) -> typing.Optional[MapSource]: ...
    @classmethod
    def new(cls) -> MapSourceRegistry: ...
    @classmethod
    def new_with_defaults(cls) -> MapSourceRegistry: ...
    def populate_defaults(self) -> None: ...
    def remove(self, id: str) -> None: ...

class MapSourceRegistryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MapSourceRegistryClass()
    """

    parent_class: GObject.ObjectClass = ...

class Marker(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Location):
    """
    :Constructors:

    ::

        Marker(**properties)
        new() -> Shumate.Marker

    Object ShumateMarker

    Properties from ShumateMarker:
      selectable -> gboolean: Selectable
        The draggable state of the marker
      child -> GtkWidget: Child
        The child widget of the marker

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        child: typing.Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        latitude: float
        longitude: float

    props: Props = ...
    parent_instance: Gtk.Widget = ...
    def __init__(
        self,
        child: typing.Optional[Gtk.Widget] = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        latitude: float = ...,
        longitude: float = ...,
    ) -> None: ...
    def animate_in(self) -> None: ...
    def animate_in_with_delay(self, delay: int) -> None: ...
    def animate_out(self) -> None: ...
    def animate_out_with_delay(self, delay: int) -> None: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_draggable(self) -> bool: ...
    def get_selectable(self) -> bool: ...
    def is_selected(self) -> bool: ...
    @classmethod
    def new(cls) -> Marker: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_draggable(self, value: bool) -> None: ...
    def set_selectable(self, value: bool) -> None: ...

class MarkerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MarkerClass()
    """

    parent_class: Gtk.WidgetClass = ...
    padding: list[None] = ...

class MarkerLayer(Layer, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        MarkerLayer(**properties)
        new(viewport:Shumate.Viewport) -> Shumate.MarkerLayer
        new_full(viewport:Shumate.Viewport, mode:Gtk.SelectionMode) -> Shumate.MarkerLayer

    Object ShumateMarkerLayer

    Signals from ShumateMarkerLayer:
      marker-selected (ShumateMarker)
      marker-unselected (ShumateMarker)

    Properties from ShumateMarkerLayer:
      selection-mode -> GtkSelectionMode: Selection Mode
        Determines the type of selection that will be performed.

    Properties from ShumateLayer:
      viewport -> ShumateViewport: Viewport
        The viewport used to display the layer

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        selection_mode: Gtk.SelectionMode
        viewport: Viewport
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        selection_mode: Gtk.SelectionMode = ...,
        viewport: Viewport = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_marker(self, marker: Marker) -> None: ...
    def get_markers(self) -> list[Marker]: ...
    def get_selected(self) -> list[Marker]: ...
    def get_selection_mode(self) -> Gtk.SelectionMode: ...
    @classmethod
    def new(cls, viewport: Viewport) -> MarkerLayer: ...
    @classmethod
    def new_full(cls, viewport: Viewport, mode: Gtk.SelectionMode) -> MarkerLayer: ...
    def remove_all(self) -> None: ...
    def remove_marker(self, marker: Marker) -> None: ...
    def select_all_markers(self) -> None: ...
    def select_marker(self, marker: Marker) -> bool: ...
    def set_selection_mode(self, mode: Gtk.SelectionMode) -> None: ...
    def unselect_all_markers(self) -> None: ...
    def unselect_marker(self, marker: Marker) -> None: ...

class MarkerLayerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MarkerLayerClass()
    """

    parent_class: LayerClass = ...

class PathLayer(Layer, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        PathLayer(**properties)
        new(viewport:Shumate.Viewport) -> Shumate.PathLayer

    Object ShumatePathLayer

    Properties from ShumatePathLayer:
      closed -> gboolean: Closed Path
        The Path is Closed
      stroke-width -> gdouble: Stroke Width
        The path's stroke width
      stroke-color -> GdkRGBA: Stroke Color
        The path's stroke color
      fill -> gboolean: Fill
        The shape is filled
      fill-color -> GdkRGBA: Fill Color
        The path's fill color
      stroke -> gboolean: Stroke
        The shape is stroked
      outline-width -> gdouble: Outline Width
        The path's outline width
      outline-color -> GdkRGBA: Outline Color
        The path's outline color

    Properties from ShumateLayer:
      viewport -> ShumateViewport: Viewport
        The viewport used to display the layer

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        closed: bool
        fill: bool
        fill_color: Gdk.RGBA
        outline_color: Gdk.RGBA
        outline_width: float
        stroke: bool
        stroke_color: Gdk.RGBA
        stroke_width: float
        viewport: Viewport
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        closed: bool = ...,
        fill: bool = ...,
        fill_color: typing.Optional[Gdk.RGBA] = ...,
        outline_color: typing.Optional[Gdk.RGBA] = ...,
        outline_width: float = ...,
        stroke: bool = ...,
        stroke_color: typing.Optional[Gdk.RGBA] = ...,
        stroke_width: float = ...,
        viewport: Viewport = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_node(self, location: Location) -> None: ...
    def get_closed(self) -> bool: ...
    def get_dash(self) -> list[int]: ...
    def get_fill(self) -> bool: ...
    def get_fill_color(self) -> Gdk.RGBA: ...
    def get_nodes(self) -> list[Location]: ...
    def get_outline_color(self) -> Gdk.RGBA: ...
    def get_outline_width(self) -> float: ...
    def get_stroke(self) -> bool: ...
    def get_stroke_color(self) -> Gdk.RGBA: ...
    def get_stroke_width(self) -> float: ...
    def insert_node(self, location: Location, position: int) -> None: ...
    @classmethod
    def new(cls, viewport: Viewport) -> PathLayer: ...
    def remove_all(self) -> None: ...
    def remove_node(self, location: Location) -> None: ...
    def set_closed(self, value: bool) -> None: ...
    def set_dash(self, dash_pattern: list[int]) -> None: ...
    def set_fill(self, value: bool) -> None: ...
    def set_fill_color(self, color: typing.Optional[Gdk.RGBA] = None) -> None: ...
    def set_outline_color(self, color: typing.Optional[Gdk.RGBA] = None) -> None: ...
    def set_outline_width(self, value: float) -> None: ...
    def set_stroke(self, value: bool) -> None: ...
    def set_stroke_color(self, color: typing.Optional[Gdk.RGBA] = None) -> None: ...
    def set_stroke_width(self, value: float) -> None: ...

class PathLayerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PathLayerClass()
    """

    parent_class: LayerClass = ...

class Point(Marker, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Location):
    """
    :Constructors:

    ::

        Point(**properties)
        new() -> Shumate.Point

    Object ShumatePoint

    Properties from ShumateMarker:
      selectable -> gboolean: Selectable
        The draggable state of the marker
      child -> GtkWidget: Child
        The child widget of the marker

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        child: typing.Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        latitude: float
        longitude: float

    props: Props = ...
    def __init__(
        self,
        child: typing.Optional[Gtk.Widget] = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        latitude: float = ...,
        longitude: float = ...,
    ) -> None: ...
    @classmethod
    def new(cls) -> Point: ...

class PointClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PointClass()
    """

    parent_class: MarkerClass = ...

class RasterRenderer(MapSource):
    """
    :Constructors:

    ::

        RasterRenderer(**properties)
        new(data_source:Shumate.DataSource) -> Shumate.RasterRenderer
        new_from_url(url_template:str) -> Shumate.RasterRenderer
        new_full(id:str, name:str, license:str, license_uri:str, min_zoom:int, max_zoom:int, tile_size:int, projection:Shumate.MapProjection, data_source:Shumate.DataSource) -> Shumate.RasterRenderer
        new_full_from_url(id:str, name:str, license:str, license_uri:str, min_zoom:int, max_zoom:int, tile_size:int, projection:Shumate.MapProjection, url_template:str) -> Shumate.RasterRenderer

    Object ShumateRasterRenderer

    Properties from ShumateRasterRenderer:
      data-source -> ShumateDataSource: Data source
        Data source

    Properties from ShumateMapSource:
      id -> gchararray: Id
        The id of the map source
      name -> gchararray: Name
        The name of the map source
      license -> gchararray: License
        The usage license of the map source
      license-uri -> gchararray: License-uri
        The usage license's uri for more information
      min-zoom-level -> guint: Minimum Zoom Level
        The minimum zoom level
      max-zoom-level -> guint: Maximum Zoom Level
        The maximum zoom level
      tile-size -> guint: Tile Size
        The map size
      projection -> ShumateMapProjection: Projection
        The map projection

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        data_source: DataSource
        id: str
        license: str
        license_uri: str
        max_zoom_level: int
        min_zoom_level: int
        name: str
        projection: MapProjection
        tile_size: int

    props: Props = ...
    def __init__(
        self,
        data_source: DataSource = ...,
        id: str = ...,
        license: str = ...,
        license_uri: str = ...,
        max_zoom_level: int = ...,
        min_zoom_level: int = ...,
        name: str = ...,
        projection: MapProjection = ...,
        tile_size: int = ...,
    ) -> None: ...
    @classmethod
    def new(cls, data_source: DataSource) -> RasterRenderer: ...
    @classmethod
    def new_from_url(cls, url_template: str) -> RasterRenderer: ...
    @classmethod
    def new_full(
        cls,
        id: str,
        name: str,
        license: str,
        license_uri: str,
        min_zoom: int,
        max_zoom: int,
        tile_size: int,
        projection: MapProjection,
        data_source: DataSource,
    ) -> RasterRenderer: ...
    @classmethod
    def new_full_from_url(
        cls,
        id: str,
        name: str,
        license: str,
        license_uri: str,
        min_zoom: int,
        max_zoom: int,
        tile_size: int,
        projection: MapProjection,
        url_template: str,
    ) -> RasterRenderer: ...

class RasterRendererClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RasterRendererClass()
    """

    parent_class: MapSourceClass = ...

class Scale(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Scale(**properties)
        new(viewport:Shumate.Viewport=None) -> Shumate.Scale

    Object ShumateScale

    Properties from ShumateScale:
      unit -> ShumateUnit: The scale's unit
        The map scale's unit
      max-width -> guint: The width of the scale
        The max width of the scale on screen
      viewport -> ShumateViewport: The viewport
        The viewport

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        max_width: int
        unit: Unit
        viewport: typing.Optional[Viewport]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        max_width: int = ...,
        unit: Unit = ...,
        viewport: typing.Optional[Viewport] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_max_width(self) -> int: ...
    def get_unit(self) -> Unit: ...
    def get_viewport(self) -> typing.Optional[Viewport]: ...
    @classmethod
    def new(cls, viewport: typing.Optional[Viewport] = None) -> Scale: ...
    def set_max_width(self, value: int) -> None: ...
    def set_unit(self, unit: Unit) -> None: ...
    def set_viewport(self, viewport: typing.Optional[Viewport] = None) -> None: ...

class ScaleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ScaleClass()
    """

    parent_class: Gtk.WidgetClass = ...

class SimpleMap(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        SimpleMap(**properties)
        new() -> Shumate.SimpleMap

    Object ShumateSimpleMap

    Signals from ShumateSimpleMap:
      symbol-clicked (ShumateSymbolEvent)

    Properties from ShumateSimpleMap:
      map-source -> ShumateMapSource: Map source
        Map source
      viewport -> ShumateViewport: Viewport
        Viewport
      compass -> ShumateCompass: Compass
        Compass
      license -> ShumateLicense: License
        License
      scale -> ShumateScale: Scale
        Scale
      show-zoom-buttons -> gboolean: Show zoom buttons
        Show zoom buttons
      map -> ShumateMap: Map
        Map

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        compass: Compass
        license: License
        map: Map
        map_source: MapSource
        scale: Scale
        show_zoom_buttons: bool
        viewport: Viewport
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        map_source: typing.Optional[MapSource] = ...,
        show_zoom_buttons: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_overlay_layer(self, layer: Layer) -> None: ...
    def get_compass(self) -> Compass: ...
    def get_license(self) -> License: ...
    def get_map(self) -> Map: ...
    def get_map_source(self) -> MapSource: ...
    def get_scale(self) -> Scale: ...
    def get_show_zoom_buttons(self) -> bool: ...
    def get_viewport(self) -> Viewport: ...
    def insert_overlay_layer(self, layer: Layer, idx: int) -> None: ...
    @classmethod
    def new(cls) -> SimpleMap: ...
    def remove_overlay_layer(self, layer: Layer) -> None: ...
    def set_map_source(self, map_source: typing.Optional[MapSource] = None) -> None: ...
    def set_show_zoom_buttons(self, show_zoom_buttons: bool) -> None: ...

class SimpleMapClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SimpleMapClass()
    """

    parent_class: Gtk.WidgetClass = ...

class SymbolEvent(GObject.Object, Location):
    """
    :Constructors:

    ::

        SymbolEvent(**properties)

    Object ShumateSymbolEvent

    Properties from ShumateSymbolEvent:
      layer -> gchararray: layer
        layer
      source-layer -> gchararray: source-layer
        source-layer
      feature-id -> gchararray: Feature ID
        Feature ID

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        feature_id: str
        layer: str
        source_layer: str
        latitude: float
        longitude: float

    props: Props = ...
    def __init__(self, latitude: float = ..., longitude: float = ...) -> None: ...
    def get_feature_id(self) -> str: ...
    def get_keys(self) -> list[str]: ...
    def get_layer(self) -> str: ...
    def get_source_layer(self) -> str: ...
    def get_tag(self, tag_name: str) -> str: ...

class SymbolEventClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SymbolEventClass()
    """

    parent_class: GObject.ObjectClass = ...

class Tile(GObject.Object):
    """
    :Constructors:

    ::

        Tile(**properties)
        new() -> Shumate.Tile
        new_full(x:int, y:int, size:int, zoom_level:int) -> Shumate.Tile

    Object ShumateTile

    Properties from ShumateTile:
      x -> guint: x
        The X position of the tile
      y -> guint: y
        The Y position of the tile
      zoom-level -> guint: Zoom Level
        The zoom level of the tile
      size -> guint: Size
        The size of the tile
      state -> ShumateState: State
        The state of the tile
      fade-in -> gboolean: Fade In
        Tile should fade in
      paintable -> GdkPaintable: Paintable
        Paintable
      scale-factor -> gdouble: scale-factor
        scale-factor

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        fade_in: bool
        paintable: typing.Optional[Gdk.Paintable]
        scale_factor: float
        size: int
        state: State
        x: int
        y: int
        zoom_level: int

    props: Props = ...
    def __init__(
        self,
        fade_in: bool = ...,
        paintable: Gdk.Paintable = ...,
        scale_factor: float = ...,
        size: int = ...,
        state: State = ...,
        x: int = ...,
        y: int = ...,
        zoom_level: int = ...,
    ) -> None: ...
    def get_fade_in(self) -> bool: ...
    def get_paintable(self) -> typing.Optional[Gdk.Paintable]: ...
    def get_scale_factor(self) -> float: ...
    def get_size(self) -> int: ...
    def get_state(self) -> State: ...
    def get_x(self) -> int: ...
    def get_y(self) -> int: ...
    def get_zoom_level(self) -> int: ...
    @classmethod
    def new(cls) -> Tile: ...
    @classmethod
    def new_full(cls, x: int, y: int, size: int, zoom_level: int) -> Tile: ...
    def set_fade_in(self, fade_in: bool) -> None: ...
    def set_paintable(self, paintable: Gdk.Paintable) -> None: ...
    def set_scale_factor(self, scale_factor: float) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_state(self, state: State) -> None: ...
    def set_x(self, x: int) -> None: ...
    def set_y(self, y: int) -> None: ...
    def set_zoom_level(self, zoom_level: int) -> None: ...

class TileClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TileClass()
    """

    parent_class: GObject.ObjectClass = ...

class TileDownloader(DataSource):
    """
    :Constructors:

    ::

        TileDownloader(**properties)
        new(url_template:str) -> Shumate.TileDownloader

    Object ShumateTileDownloader

    Properties from ShumateTileDownloader:
      url-template -> gchararray: URL template
        URL template

    Signals from ShumateDataSource:
      received-data (gint, gint, gint, GBytes)

    Properties from ShumateDataSource:
      min-zoom-level -> guint: min-zoom-level
        min-zoom-level
      max-zoom-level -> guint: max-zoom-level
        max-zoom-level

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        url_template: str
        max_zoom_level: int
        min_zoom_level: int

    props: Props = ...
    def __init__(
        self,
        url_template: str = ...,
        max_zoom_level: int = ...,
        min_zoom_level: int = ...,
    ) -> None: ...
    @classmethod
    def new(cls, url_template: str) -> TileDownloader: ...

class TileDownloaderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TileDownloaderClass()
    """

    parent_class: DataSourceClass = ...

class VectorReader(GObject.Object):
    """
    :Constructors:

    ::

        VectorReader(**properties)
        new(bytes:GLib.Bytes) -> Shumate.VectorReader

    Object ShumateVectorReader

    Signals from GObject:
      notify (GParam)
    """

    def iterate(self) -> VectorReaderIter: ...
    @classmethod
    def new(cls, bytes: GLib.Bytes) -> VectorReader: ...

class VectorReaderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VectorReaderClass()
    """

    parent_class: GObject.ObjectClass = ...

class VectorReaderIter(GObject.Object):
    """
    :Constructors:

    ::

        VectorReaderIter(**properties)

    Object ShumateVectorReaderIter

    Properties from ShumateVectorReaderIter:
      reader -> ShumateVectorReader: reader
        reader

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        reader: VectorReader

    props: Props = ...
    def __init__(self, reader: VectorReader = ...) -> None: ...
    def feature_contains_point(self, x: float, y: float) -> bool: ...
    def get_feature_geometry_type(self) -> GeometryType: ...
    def get_feature_id(self) -> int: ...
    def get_feature_keys(self) -> list[str]: ...
    def get_feature_point(self) -> typing.Tuple[bool, float, float]: ...
    def get_feature_tag(self, key: str) -> typing.Tuple[bool, typing.Any]: ...
    def get_layer_count(self) -> int: ...
    def get_layer_extent(self) -> int: ...
    def get_layer_feature_count(self) -> int: ...
    def get_layer_name(self) -> str: ...
    def get_reader(self) -> VectorReader: ...
    def next_feature(self) -> bool: ...
    def read_feature(self, index: int) -> None: ...
    def read_layer(self, index: int) -> None: ...
    def read_layer_by_name(self, name: str) -> bool: ...

class VectorReaderIterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VectorReaderIterClass()
    """

    parent_class: GObject.ObjectClass = ...

class VectorRenderer(MapSource, Gio.Initable):
    """
    :Constructors:

    ::

        VectorRenderer(**properties)
        new(id:str, style_json:str) -> Shumate.VectorRenderer

    Object ShumateVectorRenderer

    Properties from ShumateVectorRenderer:
      style-json -> gchararray: Style JSON
        Style JSON
      sprite-sheet -> ShumateVectorSpriteSheet: sprite-sheet
        sprite-sheet

    Properties from ShumateMapSource:
      id -> gchararray: Id
        The id of the map source
      name -> gchararray: Name
        The name of the map source
      license -> gchararray: License
        The usage license of the map source
      license-uri -> gchararray: License-uri
        The usage license's uri for more information
      min-zoom-level -> guint: Minimum Zoom Level
        The minimum zoom level
      max-zoom-level -> guint: Maximum Zoom Level
        The maximum zoom level
      tile-size -> guint: Tile Size
        The map size
      projection -> ShumateMapProjection: Projection
        The map projection

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        sprite_sheet: VectorSpriteSheet
        style_json: str
        id: str
        license: str
        license_uri: str
        max_zoom_level: int
        min_zoom_level: int
        name: str
        projection: MapProjection
        tile_size: int

    props: Props = ...
    def __init__(
        self,
        sprite_sheet: VectorSpriteSheet = ...,
        style_json: str = ...,
        id: str = ...,
        license: str = ...,
        license_uri: str = ...,
        max_zoom_level: int = ...,
        min_zoom_level: int = ...,
        name: str = ...,
        projection: MapProjection = ...,
        tile_size: int = ...,
    ) -> None: ...
    def get_sprite_sheet(self) -> VectorSpriteSheet: ...
    @staticmethod
    def is_supported() -> bool: ...
    @classmethod
    def new(cls, id: str, style_json: str) -> VectorRenderer: ...
    def set_data_source(self, name: str, data_source: DataSource) -> None: ...
    def set_sprite_sheet(self, sprites: VectorSpriteSheet) -> None: ...
    def set_sprite_sheet_data(
        self, sprites_pixbuf: GdkPixbuf.Pixbuf, sprites_json: str
    ) -> bool: ...

class VectorRendererClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VectorRendererClass()
    """

    parent_class: MapSourceClass = ...

class VectorSprite(GObject.Object, Gdk.Paintable, Gtk.SymbolicPaintable):
    """
    :Constructors:

    ::

        VectorSprite(**properties)
        new(source_paintable:Gdk.Paintable) -> Shumate.VectorSprite
        new_full(source_paintable:Gdk.Paintable, width:int, height:int, scale_factor:float, source_rect:Gdk.Rectangle=None) -> Shumate.VectorSprite

    Object ShumateVectorSprite

    Properties from ShumateVectorSprite:
      width -> gint: width
        width
      height -> gint: height
        height
      scale-factor -> gdouble: scale-factor
        scale-factor
      source-paintable -> GdkPaintable: source-paintable
        source-paintable
      source-rect -> GdkRectangle: source-rect
        source-rect

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        height: int
        scale_factor: float
        source_paintable: Gdk.Paintable
        source_rect: typing.Optional[Gdk.Rectangle]
        width: int

    props: Props = ...
    def __init__(
        self,
        height: int = ...,
        scale_factor: float = ...,
        source_paintable: Gdk.Paintable = ...,
        source_rect: Gdk.Rectangle = ...,
        width: int = ...,
    ) -> None: ...
    def get_height(self) -> int: ...
    def get_scale_factor(self) -> float: ...
    def get_source_paintable(self) -> Gdk.Paintable: ...
    def get_source_rect(self) -> typing.Optional[Gdk.Rectangle]: ...
    def get_width(self) -> int: ...
    @classmethod
    def new(cls, source_paintable: Gdk.Paintable) -> VectorSprite: ...
    @classmethod
    def new_full(
        cls,
        source_paintable: Gdk.Paintable,
        width: int,
        height: int,
        scale_factor: float,
        source_rect: typing.Optional[Gdk.Rectangle] = None,
    ) -> VectorSprite: ...

class VectorSpriteClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VectorSpriteClass()
    """

    parent_class: GObject.ObjectClass = ...

class VectorSpriteSheet(GObject.Object):
    """
    :Constructors:

    ::

        VectorSpriteSheet(**properties)
        new() -> Shumate.VectorSpriteSheet

    Object ShumateVectorSpriteSheet

    Signals from GObject:
      notify (GParam)
    """

    def add_page(
        self, texture: Gdk.Texture, json: str, default_scale: float
    ) -> bool: ...
    def add_sprite(self, name: str, sprite: VectorSprite) -> None: ...
    def get_sprite(self, name: str, scale: float) -> typing.Optional[VectorSprite]: ...
    @classmethod
    def new(cls) -> VectorSpriteSheet: ...
    def set_fallback(
        self,
        fallback: typing.Optional[
            typing.Callable[..., typing.Optional[VectorSprite]]
        ] = None,
        *user_data: typing.Any,
    ) -> None: ...

class VectorSpriteSheetClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VectorSpriteSheetClass()
    """

    parent_class: GObject.ObjectClass = ...

class Viewport(GObject.Object, Location):
    """
    :Constructors:

    ::

        Viewport(**properties)
        new() -> Shumate.Viewport

    Object ShumateViewport

    Properties from ShumateViewport:
      zoom-level -> gdouble: Zoom level
        The level of zoom of the map
      min-zoom-level -> guint: Min zoom level
        The lowest allowed level of zoom
      max-zoom-level -> guint: Max zoom level
        The highest allowed level of zoom
      reference-map-source -> ShumateMapSource: Reference Map Source
        The reference map source being displayed
      rotation -> gdouble: Rotation
        The rotation of the map view in radians

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        max_zoom_level: int
        min_zoom_level: int
        reference_map_source: typing.Optional[MapSource]
        rotation: float
        zoom_level: float
        latitude: float
        longitude: float

    props: Props = ...
    def __init__(
        self,
        max_zoom_level: int = ...,
        min_zoom_level: int = ...,
        reference_map_source: typing.Optional[MapSource] = ...,
        rotation: float = ...,
        zoom_level: float = ...,
        latitude: float = ...,
        longitude: float = ...,
    ) -> None: ...
    def get_max_zoom_level(self) -> int: ...
    def get_min_zoom_level(self) -> int: ...
    def get_reference_map_source(self) -> typing.Optional[MapSource]: ...
    def get_rotation(self) -> float: ...
    def get_zoom_level(self) -> float: ...
    def location_to_widget_coords(
        self, widget: Gtk.Widget, latitude: float, longitude: float
    ) -> typing.Tuple[float, float]: ...
    @classmethod
    def new(cls) -> Viewport: ...
    def set_max_zoom_level(self, max_zoom_level: int) -> None: ...
    def set_min_zoom_level(self, min_zoom_level: int) -> None: ...
    def set_reference_map_source(
        self, map_source: typing.Optional[MapSource] = None
    ) -> None: ...
    def set_rotation(self, rotation: float) -> None: ...
    def set_zoom_level(self, zoom_level: float) -> None: ...
    def widget_coords_to_location(
        self, widget: Gtk.Widget, x: float, y: float
    ) -> typing.Tuple[float, float]: ...

class ViewportClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewportClass()
    """

    parent_class: GObject.ObjectClass = ...

class FileCacheError(GObject.GEnum):
    FAILED = 0
    @staticmethod
    def quark() -> int: ...

class GeometryType(GObject.GEnum):
    LINESTRING = 3
    MULTILINESTRING = 4
    MULTIPOINT = 2
    MULTIPOLYGON = 6
    POINT = 1
    POLYGON = 5
    UNKNOWN = 0

class MapProjection(GObject.GEnum):
    MERCATOR = 0

class State(GObject.GEnum):
    DONE = 3
    LOADED = 2
    LOADING = 1
    NONE = 0

class StyleError(GObject.GEnum):
    FAILED = 0
    INVALID_EXPRESSION = 3
    MALFORMED_STYLE = 1
    SUPPORT_OMITTED = 4
    UNSUPPORTED = 5
    UNSUPPORTED_LAYER = 2
    @staticmethod
    def quark() -> int: ...

class TileDownloaderError(GObject.GEnum):
    BAD_RESPONSE = 1
    COULD_NOT_CONNECT = 2
    FAILED = 0
    MALFORMED_URL = 3
    OFFLINE = 4
    @staticmethod
    def quark() -> int: ...

class Unit(GObject.GEnum):
    BOTH = 0
    IMPERIAL = 2
    METRIC = 1
