from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import Atk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk

_lock = ...  # FIXME Constant
_namespace: str = "XApp"
_version: str = "1.0"

def get_tmp_dir() -> str: ...
def pango_font_string_to_css(pango_font_string: str) -> str: ...
def set_window_icon_from_file(
    window: Gtk.Window, file_name: Optional[str] = None
) -> None: ...
def set_window_icon_name(
    window: Gtk.Window, icon_name: Optional[str] = None
) -> None: ...
def set_window_progress(window: Gtk.Window, progress: int) -> None: ...
def set_window_progress_pulse(window: Gtk.Window, pulse: bool) -> None: ...
def set_xid_icon_from_file(xid: int, file_name: Optional[str] = None) -> None: ...
def set_xid_icon_name(xid: int, icon_name: Optional[str] = None) -> None: ...
def set_xid_progress(xid: int, progress: int) -> None: ...
def set_xid_progress_pulse(xid: int, pulse: bool) -> None: ...
def status_icon_interface_interface_info() -> Gio.DBusInterfaceInfo: ...
def status_icon_interface_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def switcheroo_control_interface_info() -> Gio.DBusInterfaceInfo: ...
def switcheroo_control_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def util_get_session_is_running() -> bool: ...
def util_gpu_offload_supported() -> bool: ...

class DarkModeManager(GObject.Object):
    """
    :Constructors:

    ::

        DarkModeManager(**properties)
        new(prefer_dark_mode:bool) -> XApp.DarkModeManager

    Object XAppDarkModeManager

    Signals from GObject:
      notify (GParam)
    """

    @classmethod
    def new(cls, prefer_dark_mode: bool) -> DarkModeManager: ...

class DarkModeManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DarkModeManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class FavoriteInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        FavoriteInfo()
    """

    uri: str = ...
    display_name: str = ...
    cached_mimetype: str = ...
    def copy(self) -> FavoriteInfo: ...
    def free(self) -> None: ...

class Favorites(GObject.Object):
    """
    :Constructors:

    ::

        Favorites(**properties)

    Object XAppFavorites

    Signals from XAppFavorites:
      changed ()

    Signals from GObject:
      notify (GParam)
    """

    def add(self, uri: str) -> None: ...
    def create_actions(self, mimetypes: Optional[str] = None) -> list[Gtk.Action]: ...
    def create_menu(
        self, mimetypes: Optional[str], callback: Callable[..., None], *user_data: Any
    ) -> Gtk.Widget: ...
    def find_by_display_name(self, display_name: str) -> FavoriteInfo: ...
    def find_by_uri(self, uri: str) -> FavoriteInfo: ...
    @staticmethod
    def get_default() -> Favorites: ...
    def get_favorites(
        self, mimetypes: Optional[Sequence[str]] = None
    ) -> list[FavoriteInfo]: ...
    def get_n_favorites(self) -> int: ...
    def launch(self, uri: str, timestamp: int) -> None: ...
    def remove(self, uri: str) -> None: ...
    def rename(self, old_uri: str, new_uri: str) -> None: ...

class FavoritesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FavoritesClass()
    """

    parent_class: GObject.ObjectClass = ...

class GpuInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        GpuInfo()
    """

    id: int = ...
    is_default: bool = ...
    display_name: str = ...
    env_strv: list[str] = ...
    def get_shell_env_prefix(self) -> str: ...

class GpuOffloadHelper(GObject.Object):
    """
    :Constructors:

    ::

        GpuOffloadHelper(**properties)

    Object XAppGpuOffloadHelper

    Signals from XAppGpuOffloadHelper:
      ready (gboolean)

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def get() -> GpuOffloadHelper: ...
    def get_default_info(self) -> GpuInfo: ...
    def get_info_by_id(self, id: int) -> GpuInfo: ...
    def get_n_gpus(self) -> int: ...
    def get_offload_infos(self) -> list[GpuInfo]: ...
    @staticmethod
    def get_sync() -> GpuOffloadHelper: ...
    def is_offload_supported(self) -> bool: ...
    def is_ready(self) -> bool: ...

class GpuOffloadHelperClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GpuOffloadHelperClass()
    """

    parent_class: GObject.ObjectClass = ...

class GtkWindow(Gtk.Window, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        GtkWindow(**properties)
        new(type:Gtk.WindowType) -> Gtk.Widget

    Object XAppGtkWindow

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accept_focus: bool
        application: Optional[Gtk.Application]
        attached_to: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: Optional[GdkPixbuf.Pixbuf]
        icon_name: Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: Optional[str]
        transient_for: Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        startup_id: str
        child: Gtk.Widget

    props: Props = ...
    parent_instance: Gtk.Window = ...
    def __init__(
        self,
        accept_focus: bool = ...,
        application: Optional[Gtk.Application] = ...,
        attached_to: Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        focus_on_map: bool = ...,
        focus_visible: bool = ...,
        gravity: Gdk.Gravity = ...,
        has_resize_grip: bool = ...,
        hide_titlebar_when_maximized: bool = ...,
        icon: Optional[GdkPixbuf.Pixbuf] = ...,
        icon_name: Optional[str] = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        role: str = ...,
        screen: Gdk.Screen = ...,
        skip_pager_hint: bool = ...,
        skip_taskbar_hint: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: Optional[Gtk.Window] = ...,
        type: Gtk.WindowType = ...,
        type_hint: Gdk.WindowTypeHint = ...,
        urgency_hint: bool = ...,
        window_position: Gtk.WindowPosition = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    @classmethod
    def new(cls, type: Gtk.WindowType) -> GtkWindow: ...
    def set_icon_from_file(self, file_name: Optional[str] = None) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_progress(self, progress: int) -> None: ...
    def set_progress_pulse(self, pulse: bool) -> None: ...

class GtkWindowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GtkWindowClass()
    """

    parent_class: Gtk.WindowClass = ...
    padding: list[None] = ...

class IconChooserButton(
    Gtk.Button, Atk.ImplementorIface, Gtk.Actionable, Gtk.Activatable, Gtk.Buildable
):
    """
    :Constructors:

    ::

        IconChooserButton(**properties)
        new() -> XApp.IconChooserButton
        new_with_size(icon_size:Gtk.IconSize) -> XApp.IconChooserButton

    Object XAppIconChooserButton

    Properties from XAppIconChooserButton:
      icon-size -> GtkIconSize: Icon size
        The preferred icon size.
      icon -> gchararray: Icon
        The string representing the icon.
      category -> gchararray: Category
        The default category.

    Signals from GtkButton:
      clicked ()
      activate ()
      pressed ()
      released ()
      enter ()
      leave ()

    Properties from GtkButton:
      label -> gchararray: Label
        Text of the label widget inside the button, if the button contains a label widget
      image -> GtkWidget: Image widget
        Child widget to appear next to the button text
      relief -> GtkReliefStyle: Border relief
        The border relief style
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key
      use-stock -> gboolean: Use stock
        If set, the label is used to pick a stock item instead of being displayed
      xalign -> gfloat: Horizontal alignment for child
        Horizontal position of child in available space. 0.0 is left aligned, 1.0 is right aligned
      yalign -> gfloat: Vertical alignment for child
        Vertical position of child in available space. 0.0 is top aligned, 1.0 is bottom aligned
      image-position -> GtkPositionType: Image position
        The position of the image relative to the text
      always-show-image -> gboolean: Always show image
        Whether the image will always be shown

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        category: str
        icon: str
        icon_size: Gtk.IconSize
        always_show_image: bool
        image: Optional[Gtk.Widget]
        image_position: Gtk.PositionType
        label: str
        relief: Gtk.ReliefStyle
        use_stock: bool
        use_underline: bool
        xalign: float
        yalign: float
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        action_name: Optional[str]
        action_target: GLib.Variant
        related_action: Gtk.Action
        use_action_appearance: bool
        child: Gtk.Widget

    props: Props = ...
    def __init__(
        self,
        category: str = ...,
        icon: Optional[str] = ...,
        icon_size: Gtk.IconSize = ...,
        always_show_image: bool = ...,
        image: Optional[Gtk.Widget] = ...,
        image_position: Gtk.PositionType = ...,
        label: str = ...,
        relief: Gtk.ReliefStyle = ...,
        use_stock: bool = ...,
        use_underline: bool = ...,
        xalign: float = ...,
        yalign: float = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        action_name: Optional[str] = ...,
        action_target: GLib.Variant = ...,
        related_action: Gtk.Action = ...,
        use_action_appearance: bool = ...,
    ): ...
    def get_dialog(self) -> IconChooserDialog: ...
    def get_icon(self) -> str: ...
    @classmethod
    def new(cls) -> IconChooserButton: ...
    @classmethod
    def new_with_size(cls, icon_size: Gtk.IconSize) -> IconChooserButton: ...
    def set_default_category(self, category: Optional[str] = None) -> None: ...
    def set_icon(self, icon: Optional[str] = None) -> None: ...
    def set_icon_size(self, icon_size: Gtk.IconSize) -> None: ...

class IconChooserButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        IconChooserButtonClass()
    """

    parent_class: Gtk.ButtonClass = ...

class IconChooserDialog(GtkWindow, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        IconChooserDialog(**properties)
        new() -> XApp.IconChooserDialog

    Object XAppIconChooserDialog

    Signals from XAppIconChooserDialog:
      close ()
      select ()

    Properties from XAppIconChooserDialog:
      icon-size -> XAppIconSize: Icon size
        The preferred icon size.
      allow-paths -> gboolean: Allow Paths
        Whether to allow paths.
      default-icon -> gchararray: Default Icon
        The icon to use by default

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        allow_paths: bool
        default_icon: str
        icon_size: IconSize
        accept_focus: bool
        application: Optional[Gtk.Application]
        attached_to: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: Optional[GdkPixbuf.Pixbuf]
        icon_name: Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: Optional[str]
        transient_for: Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        startup_id: str
        child: Gtk.Widget

    props: Props = ...
    def __init__(
        self,
        allow_paths: bool = ...,
        default_icon: str = ...,
        icon_size: IconSize = ...,
        accept_focus: bool = ...,
        application: Optional[Gtk.Application] = ...,
        attached_to: Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        focus_on_map: bool = ...,
        focus_visible: bool = ...,
        gravity: Gdk.Gravity = ...,
        has_resize_grip: bool = ...,
        hide_titlebar_when_maximized: bool = ...,
        icon: Optional[GdkPixbuf.Pixbuf] = ...,
        icon_name: Optional[str] = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        role: str = ...,
        screen: Gdk.Screen = ...,
        skip_pager_hint: bool = ...,
        skip_taskbar_hint: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: Optional[Gtk.Window] = ...,
        type: Gtk.WindowType = ...,
        type_hint: Gdk.WindowTypeHint = ...,
        urgency_hint: bool = ...,
        window_position: Gtk.WindowPosition = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def add_button(
        self, button: Gtk.Widget, packing: Gtk.PackType, response_id: Gtk.ResponseType
    ) -> None: ...
    def add_custom_category(self, name: str, icons: list[str]) -> None: ...
    def get_default_icon(self) -> str: ...
    def get_icon_string(self) -> str: ...
    @classmethod
    def new(cls) -> IconChooserDialog: ...
    def run(self) -> int: ...
    def run_with_category(self, category: str) -> int: ...
    def run_with_icon(self, icon: str) -> int: ...
    def set_default_icon(self, icon: str) -> None: ...

class IconChooserDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        IconChooserDialogClass()
    """

    parent_class: GtkWindowClass = ...

class KbdLayoutController(GObject.Object):
    """
    :Constructors:

    ::

        KbdLayoutController(**properties)
        new() -> XApp.KbdLayoutController

    Object XAppKbdLayoutController

    Signals from XAppKbdLayoutController:
      layout-changed (guint)
      config-changed ()

    Properties from XAppKbdLayoutController:
      enabled -> gboolean: Enabled
        Whether we're enabled (more than one keyboard layout is installed)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        enabled: bool

    props: Props = ...
    parent_object: GObject.Object = ...
    priv: KbdLayoutControllerPrivate = ...
    def get_all_names(self) -> list[str]: ...
    def get_current_flag_id(self) -> int: ...
    def get_current_group(self) -> int: ...
    def get_current_icon_name(self) -> str: ...
    def get_current_name(self) -> str: ...
    def get_current_short_group_label(self) -> str: ...
    def get_current_variant_label(self) -> str: ...
    def get_enabled(self) -> bool: ...
    def get_flag_id_for_group(self, group: int) -> int: ...
    def get_icon_name_for_group(self, group: int) -> str: ...
    def get_short_group_label_for_group(self, group: int) -> str: ...
    def get_variant_label_for_group(self, group: int) -> str: ...
    @classmethod
    def new(cls) -> KbdLayoutController: ...
    def next_group(self) -> None: ...
    def previous_group(self) -> None: ...
    @staticmethod
    def render_cairo_subscript(
        cr: cairo.Context[_SomeSurface],
        x: float,
        y: float,
        width: float,
        height: float,
        subscript: int,
    ) -> None: ...
    def set_current_group(self, group: int) -> None: ...

class KbdLayoutControllerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        KbdLayoutControllerClass()
    """

    parent_class: GObject.ObjectClass = ...

class KbdLayoutControllerPrivate(GObject.GPointer): ...

class MonitorBlanker(GObject.Object):
    """
    :Constructors:

    ::

        MonitorBlanker(**properties)
        new() -> XApp.MonitorBlanker

    Object XAppMonitorBlanker

    Signals from GObject:
      notify (GParam)
    """

    def are_monitors_blanked(self) -> bool: ...
    def blank_other_monitors(self, window: Gtk.Window) -> None: ...
    @classmethod
    def new(cls) -> MonitorBlanker: ...
    def unblank_monitors(self) -> None: ...

class MonitorBlankerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MonitorBlankerClass()
    """

    parent_class: GObject.ObjectClass = ...

class Object(GObject.GInterface):
    """
    Interface XAppObject

    Signals from GObject:
      notify (GParam)
    """

    def get_status_icon_interface(self) -> Optional[StatusIconInterface]: ...

class ObjectIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectIface()
    """

    parent_iface: GObject.TypeInterface = ...

class ObjectManagerClient(
    Gio.DBusObjectManagerClient, Gio.AsyncInitable, Gio.DBusObjectManager, Gio.Initable
):
    """
    :Constructors:

    ::

        ObjectManagerClient(**properties)
        new_finish(res:Gio.AsyncResult) -> XApp.ObjectManagerClient
        new_for_bus_finish(res:Gio.AsyncResult) -> XApp.ObjectManagerClient
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusObjectManagerClientFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> XApp.ObjectManagerClient
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusObjectManagerClientFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> XApp.ObjectManagerClient

    Object XAppObjectManagerClient

    Signals from GDBusObjectManager:
      object-added (GDBusObject)
      object-removed (GDBusObject)
      interface-added (GDBusObject, GDBusInterface)
      interface-removed (GDBusObject, GDBusInterface)

    Signals from GDBusObjectManagerClient:
      interface-proxy-signal (GDBusObjectProxy, GDBusProxy, gchararray, gchararray, GVariant)
      interface-proxy-properties-changed (GDBusObjectProxy, GDBusProxy, GVariant, GStrv)

    Properties from GDBusObjectManagerClient:
      bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      connection -> GDBusConnection: Connection
        The connection to use
      flags -> GDBusObjectManagerClientFlags: Flags
        Flags for the proxy manager
      object-path -> gchararray: Object Path
        The object path of the control object
      name -> gchararray: Name
        Name that the manager is for
      name-owner -> gchararray: Name Owner
        The owner of the name we are watching
      get-proxy-type-func -> gpointer: GDBusProxyTypeFunc Function Pointer
        The GDBusProxyTypeFunc pointer to use
      get-proxy-type-user-data -> gpointer: GDBusProxyTypeFunc User Data
        The GDBusProxyTypeFunc user_data
      get-proxy-type-destroy-notify -> gpointer: GDBusProxyTypeFunc user data free function
        The GDBusProxyTypeFunc user data free function

    Signals from GDBusObjectManager:
      object-added (GDBusObject)
      object-removed (GDBusObject)
      interface-added (GDBusObject, GDBusInterface)
      interface-removed (GDBusObject, GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connection: Gio.DBusConnection
        flags: Gio.DBusObjectManagerClientFlags
        get_proxy_type_destroy_notify: None
        get_proxy_type_func: None
        get_proxy_type_user_data: None
        name: str
        name_owner: Optional[str]
        object_path: str
        bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusObjectManagerClient = ...
    priv: ObjectManagerClientPrivate = ...
    def __init__(
        self,
        bus_type: Gio.BusType = ...,
        connection: Gio.DBusConnection = ...,
        flags: Gio.DBusObjectManagerClientFlags = ...,
        get_proxy_type_destroy_notify: None = ...,
        get_proxy_type_func: None = ...,
        get_proxy_type_user_data: None = ...,
        name: str = ...,
        object_path: str = ...,
    ): ...
    @staticmethod
    def get_proxy_type(
        manager: Gio.DBusObjectManagerClient,
        object_path: str,
        interface_name: Optional[str],
        user_data: None,
    ) -> Type: ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusObjectManagerClientFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> ObjectManagerClient: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusObjectManagerClientFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ObjectManagerClient: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusObjectManagerClientFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ObjectManagerClient: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusObjectManagerClientFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ObjectManagerClient: ...

class ObjectManagerClientClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectManagerClientClass()
    """

    parent_class: Gio.DBusObjectManagerClientClass = ...

class ObjectManagerClientPrivate(GObject.GPointer): ...

class ObjectProxy(Gio.DBusObjectProxy, Gio.DBusObject, Object):
    """
    :Constructors:

    ::

        ObjectProxy(**properties)
        new(connection:Gio.DBusConnection, object_path:str) -> XApp.ObjectProxy

    Object XAppObjectProxy

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Properties from GDBusObjectProxy:
      g-object-path -> gchararray: Object Path
        The object path of the proxy
      g-connection -> GDBusConnection: Connection
        The connection of the proxy

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_connection: Gio.DBusConnection
        g_object_path: str
        status_icon_interface: Optional[StatusIconInterface]

    props: Props = ...
    parent_instance: Gio.DBusObjectProxy = ...
    priv: ObjectProxyPrivate = ...
    def __init__(
        self,
        g_connection: Gio.DBusConnection = ...,
        g_object_path: str = ...,
        status_icon_interface: StatusIconInterface = ...,
    ): ...
    @classmethod
    def new(cls, connection: Gio.DBusConnection, object_path: str) -> ObjectProxy: ...

class ObjectProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectProxyClass()
    """

    parent_class: Gio.DBusObjectProxyClass = ...

class ObjectProxyPrivate(GObject.GPointer): ...

class ObjectSkeleton(Gio.DBusObjectSkeleton, Gio.DBusObject, Object):
    """
    :Constructors:

    ::

        ObjectSkeleton(**properties)
        new(object_path:str) -> XApp.ObjectSkeleton

    Object XAppObjectSkeleton

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Signals from GDBusObjectSkeleton:
      authorize-method (GDBusInterfaceSkeleton, GDBusMethodInvocation) -> gboolean

    Properties from GDBusObjectSkeleton:
      g-object-path -> gchararray: Object Path
        The object path where the object is exported

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_object_path: str
        status_icon_interface: Optional[StatusIconInterface]

    props: Props = ...
    parent_instance: Gio.DBusObjectSkeleton = ...
    priv: ObjectSkeletonPrivate = ...
    def __init__(
        self, g_object_path: str = ..., status_icon_interface: StatusIconInterface = ...
    ): ...
    @classmethod
    def new(cls, object_path: str) -> ObjectSkeleton: ...
    def set_status_icon_interface(
        self, interface_: Optional[StatusIconInterface] = None
    ) -> None: ...

class ObjectSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectSkeletonClass()
    """

    parent_class: Gio.DBusObjectSkeletonClass = ...

class ObjectSkeletonPrivate(GObject.GPointer): ...

class PreferencesWindow(Gtk.Window, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        PreferencesWindow(**properties)
        new() -> XApp.PreferencesWindow

    Object XAppPreferencesWindow

    Signals from XAppPreferencesWindow:
      close ()

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accept_focus: bool
        application: Optional[Gtk.Application]
        attached_to: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: Optional[GdkPixbuf.Pixbuf]
        icon_name: Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: Optional[str]
        transient_for: Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        startup_id: str
        child: Gtk.Widget

    props: Props = ...
    parent_instance: Gtk.Window = ...
    def __init__(
        self,
        accept_focus: bool = ...,
        application: Optional[Gtk.Application] = ...,
        attached_to: Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        focus_on_map: bool = ...,
        focus_visible: bool = ...,
        gravity: Gdk.Gravity = ...,
        has_resize_grip: bool = ...,
        hide_titlebar_when_maximized: bool = ...,
        icon: Optional[GdkPixbuf.Pixbuf] = ...,
        icon_name: Optional[str] = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        role: str = ...,
        screen: Gdk.Screen = ...,
        skip_pager_hint: bool = ...,
        skip_taskbar_hint: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: Optional[Gtk.Window] = ...,
        type: Gtk.WindowType = ...,
        type_hint: Gdk.WindowTypeHint = ...,
        urgency_hint: bool = ...,
        window_position: Gtk.WindowPosition = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def add_button(self, button: Gtk.Widget, pack_type: Gtk.PackType) -> None: ...
    def add_page(self, widget: Gtk.Widget, name: str, title: str) -> None: ...
    def do_close(self) -> None: ...
    @classmethod
    def new(cls) -> PreferencesWindow: ...

class PreferencesWindowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PreferencesWindowClass()
    """

    parent_class: Gtk.WindowClass = ...
    close: Callable[[PreferencesWindow], None] = ...

class StackSidebar(Gtk.Bin, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        StackSidebar(**properties)
        new() -> XApp.StackSidebar

    Object XAppStackSidebar

    Properties from XAppStackSidebar:
      stack -> GtkStack: Stack
        Associated stack for this XAppStackSidebar

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        stack: Optional[Gtk.Stack]
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        child: Gtk.Widget

    props: Props = ...
    def __init__(
        self,
        stack: Gtk.Stack = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
    ): ...
    def get_stack(self) -> Optional[Gtk.Stack]: ...
    @classmethod
    def new(cls) -> StackSidebar: ...
    def set_stack(self, stack: Gtk.Stack) -> None: ...

class StackSidebarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StackSidebarClass()
    """

    parent_class: Gtk.BinClass = ...

class StatusIcon(GObject.Object):
    """
    :Constructors:

    ::

        StatusIcon(**properties)
        new() -> XApp.StatusIcon
        new_with_name(name:str) -> XApp.StatusIcon

    Object XAppStatusIcon

    Signals from XAppStatusIcon:
      state-changed (XAppStatusIconState)
      button-press-event (gint, gint, guint, guint, gint)
      button-release-event (gint, gint, guint, guint, gint)
      scroll-event (gint, XAppScrollDirection, guint)
      activate (guint, guint)

    Properties from XAppStatusIcon:
      primary-menu -> GtkWidget: Status icon primary (left-click) menu
        A menu to bring up when the status icon is left-clicked
      secondary-menu -> GtkWidget: Status icon secondary (right-click) menu
        A menu to bring up when the status icon is right-clicked
      icon-size -> gint: The icon size the monitor/host prefers
        The icon size that should be used, if the client is supplying absolute icon paths
      name -> gchararray: The name of the icon for sorting purposes.

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        icon_size: int
        name: str
        primary_menu: Gtk.Widget
        secondary_menu: Gtk.Widget

    props: Props = ...
    def __init__(
        self,
        icon_size: int = ...,
        name: str = ...,
        primary_menu: Optional[Gtk.Widget] = ...,
        secondary_menu: Optional[Gtk.Widget] = ...,
    ): ...
    @staticmethod
    def any_monitors() -> bool: ...
    def get_icon_size(self) -> int: ...
    def get_primary_menu(self) -> Gtk.Widget: ...
    def get_secondary_menu(self) -> Gtk.Widget: ...
    def get_state(self) -> StatusIconState: ...
    def get_visible(self) -> bool: ...
    @classmethod
    def new(cls) -> StatusIcon: ...
    @classmethod
    def new_with_name(cls, name: str) -> StatusIcon: ...
    def popup_menu(
        self,
        menu: Optional[Gtk.Menu],
        x: int,
        y: int,
        button: int,
        _time: int,
        panel_position: int,
    ) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_label(self, label: str) -> None: ...
    def set_metadata(self, metadata: Optional[str] = None) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_primary_menu(self, menu: Optional[Gtk.Menu] = None) -> None: ...
    def set_secondary_menu(self, menu: Optional[Gtk.Menu] = None) -> None: ...
    def set_tooltip_text(self, tooltip_text: str) -> None: ...
    def set_visible(self, visible: bool) -> None: ...

class StatusIconClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StatusIconClass()
    """

    parent_class: GObject.ObjectClass = ...

class StatusIconInterface(GObject.GInterface):
    """
    Interface XAppStatusIconInterface

    Signals from GObject:
      notify (GParam)
    """

    def call_button_press(
        self,
        arg_x: int,
        arg_y: int,
        arg_button: int,
        arg_time: int,
        arg_panel_position: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_button_press_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_button_press_sync(
        self,
        arg_x: int,
        arg_y: int,
        arg_button: int,
        arg_time: int,
        arg_panel_position: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def call_button_release(
        self,
        arg_x: int,
        arg_y: int,
        arg_button: int,
        arg_time: int,
        arg_panel_position: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_button_release_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_button_release_sync(
        self,
        arg_x: int,
        arg_y: int,
        arg_button: int,
        arg_time: int,
        arg_panel_position: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def call_scroll(
        self,
        arg_delta: int,
        arg_orientation: int,
        arg_time: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_scroll_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_scroll_sync(
        self,
        arg_delta: int,
        arg_orientation: int,
        arg_time: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def complete_button_press(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    def complete_button_release(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    def complete_scroll(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class StatusIconInterfaceIface(GObject.GPointer):
    """
    :Constructors:

    ::

        StatusIconInterfaceIface()
    """

    parent_iface: GObject.TypeInterface = ...
    handle_button_press: Callable[
        [StatusIconInterface, Gio.DBusMethodInvocation, int, int, int, int, int], bool
    ] = ...
    handle_button_release: Callable[
        [StatusIconInterface, Gio.DBusMethodInvocation, int, int, int, int, int], bool
    ] = ...
    handle_scroll: Callable[
        [StatusIconInterface, Gio.DBusMethodInvocation, int, int, int], bool
    ] = ...
    get_icon_name: Callable[[StatusIconInterface], Optional[str]] = ...
    get_icon_size: Callable[[StatusIconInterface], int] = ...
    get_label: Callable[[StatusIconInterface], Optional[str]] = ...
    get_metadata: Callable[[StatusIconInterface], Optional[str]] = ...
    get_name: Callable[[StatusIconInterface], Optional[str]] = ...
    get_primary_menu_is_open: Callable[[StatusIconInterface], bool] = ...
    get_secondary_menu_is_open: Callable[[StatusIconInterface], bool] = ...
    get_tooltip_text: Callable[[StatusIconInterface], Optional[str]] = ...
    get_visible: Callable[[StatusIconInterface], bool] = ...

class StatusIconInterfaceProxy(
    Gio.DBusProxy,
    Gio.AsyncInitable,
    Gio.DBusInterface,
    Gio.Initable,
    StatusIconInterface,
):
    """
    :Constructors:

    ::

        StatusIconInterfaceProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> XApp.StatusIconInterfaceProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> XApp.StatusIconInterfaceProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> XApp.StatusIconInterfaceProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> XApp.StatusIconInterfaceProxy

    Object XAppStatusIconInterfaceProxy

    Signals from XAppStatusIconInterface:
      handle-button-press (GDBusMethodInvocation, gint, gint, guint, guint, gint) -> gboolean
      handle-button-release (GDBusMethodInvocation, gint, gint, guint, guint, gint) -> gboolean
      handle-scroll (GDBusMethodInvocation, gint, gint, guint) -> gboolean

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        icon_name: str
        icon_size: int
        label: str
        metadata: str
        name: str
        primary_menu_is_open: bool
        secondary_menu_is_open: bool
        tooltip_text: str
        visible: bool
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: StatusIconInterfaceProxyPrivate = ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        icon_name: str = ...,
        icon_size: int = ...,
        label: str = ...,
        metadata: str = ...,
        name: str = ...,
        primary_menu_is_open: bool = ...,
        secondary_menu_is_open: bool = ...,
        tooltip_text: str = ...,
        visible: bool = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> StatusIconInterfaceProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> StatusIconInterfaceProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> StatusIconInterfaceProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> StatusIconInterfaceProxy: ...

class StatusIconInterfaceProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StatusIconInterfaceProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class StatusIconInterfaceProxyPrivate(GObject.GPointer): ...

class StatusIconInterfaceSkeleton(
    Gio.DBusInterfaceSkeleton, Gio.DBusInterface, StatusIconInterface
):
    """
    :Constructors:

    ::

        StatusIconInterfaceSkeleton(**properties)
        new() -> XApp.StatusIconInterfaceSkeleton

    Object XAppStatusIconInterfaceSkeleton

    Signals from XAppStatusIconInterface:
      handle-button-press (GDBusMethodInvocation, gint, gint, guint, guint, gint) -> gboolean
      handle-button-release (GDBusMethodInvocation, gint, gint, guint, guint, gint) -> gboolean
      handle-scroll (GDBusMethodInvocation, gint, gint, guint) -> gboolean

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_flags: Gio.DBusInterfaceSkeletonFlags
        icon_name: str
        icon_size: int
        label: str
        metadata: str
        name: str
        primary_menu_is_open: bool
        secondary_menu_is_open: bool
        tooltip_text: str
        visible: bool

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: StatusIconInterfaceSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        icon_name: str = ...,
        icon_size: int = ...,
        label: str = ...,
        metadata: str = ...,
        name: str = ...,
        primary_menu_is_open: bool = ...,
        secondary_menu_is_open: bool = ...,
        tooltip_text: str = ...,
        visible: bool = ...,
    ): ...
    @classmethod
    def new(cls) -> StatusIconInterfaceSkeleton: ...

class StatusIconInterfaceSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StatusIconInterfaceSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class StatusIconInterfaceSkeletonPrivate(GObject.GPointer): ...

class StatusIconMonitor(GObject.Object):
    """
    :Constructors:

    ::

        StatusIconMonitor(**properties)
        new() -> XApp.StatusIconMonitor

    Object XAppStatusIconMonitor

    Signals from XAppStatusIconMonitor:
      icon-added (XAppStatusIconInterfaceProxy)
      icon-removed (XAppStatusIconInterfaceProxy)

    Signals from GObject:
      notify (GParam)
    """

    def list_icons(self) -> list[StatusIconMonitor]: ...
    @classmethod
    def new(cls) -> StatusIconMonitor: ...

class StatusIconMonitorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StatusIconMonitorClass()
    """

    parent_class: GObject.ObjectClass = ...

class StyleManager(GObject.Object):
    """
    :Constructors:

    ::

        StyleManager(**properties)
        new() -> XApp.StyleManager

    Object XAppStyleManager

    Properties from XAppStyleManager:
      widget -> GtkWidget: Widget
        The widget to be styled.

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        widget: Gtk.Widget

    props: Props = ...
    def __init__(self, widget: Gtk.Widget = ...): ...
    def get_widget(self) -> Gtk.Widget: ...
    @classmethod
    def new(cls) -> StyleManager: ...
    def remove_style_property(self, name: str) -> None: ...
    def set_from_pango_font_string(self, desc_string: str) -> None: ...
    def set_style_property(self, name: str, value: str) -> None: ...
    def set_widget(self, widget: Gtk.Widget) -> None: ...

class StyleManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class SwitcherooControl(GObject.GInterface):
    """
    Interface XAppSwitcherooControl

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class SwitcherooControlIface(GObject.GPointer):
    """
    :Constructors:

    ::

        SwitcherooControlIface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_gpus: Callable[[SwitcherooControl], Optional[GLib.Variant]] = ...
    get_has_dual_gpu: Callable[[SwitcherooControl], bool] = ...
    get_num_gpus: Callable[[SwitcherooControl], int] = ...

class SwitcherooControlProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, SwitcherooControl
):
    """
    :Constructors:

    ::

        SwitcherooControlProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> XApp.SwitcherooControlProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> XApp.SwitcherooControlProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> XApp.SwitcherooControlProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> XApp.SwitcherooControlProxy

    Object XAppSwitcherooControlProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        gpus: GLib.Variant
        has_dual_gpu: bool
        num_gpus: int
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: SwitcherooControlProxyPrivate = ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        gpus: GLib.Variant = ...,
        has_dual_gpu: bool = ...,
        num_gpus: int = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> SwitcherooControlProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> SwitcherooControlProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> SwitcherooControlProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> SwitcherooControlProxy: ...

class SwitcherooControlProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SwitcherooControlProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class SwitcherooControlProxyPrivate(GObject.GPointer): ...

class SwitcherooControlSkeleton(
    Gio.DBusInterfaceSkeleton, Gio.DBusInterface, SwitcherooControl
):
    """
    :Constructors:

    ::

        SwitcherooControlSkeleton(**properties)
        new() -> XApp.SwitcherooControlSkeleton

    Object XAppSwitcherooControlSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_flags: Gio.DBusInterfaceSkeletonFlags
        gpus: GLib.Variant
        has_dual_gpu: bool
        num_gpus: int

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: SwitcherooControlSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        gpus: GLib.Variant = ...,
        has_dual_gpu: bool = ...,
        num_gpus: int = ...,
    ): ...
    @classmethod
    def new(cls) -> SwitcherooControlSkeleton: ...

class SwitcherooControlSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SwitcherooControlSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class SwitcherooControlSkeletonPrivate(GObject.GPointer): ...

class VisibilityGroup(GObject.GBoxed):
    """
    :Constructors:

    ::

        VisibilityGroup()
        new(visible:bool, sensitive:bool, widgets:list=None) -> XApp.VisibilityGroup
    """

    widgets: list[Gtk.Widget] = ...
    visible: bool = ...
    sensitive: bool = ...
    def add_widget(self, widget: Gtk.Widget) -> None: ...
    def get_sensitive(self) -> bool: ...
    def get_visible(self) -> bool: ...
    def get_widgets(self) -> list[Gtk.Widget]: ...
    def hide(self) -> None: ...
    @classmethod
    def new(
        cls, visible: bool, sensitive: bool, widgets: Optional[list[Gtk.Widget]] = None
    ) -> VisibilityGroup: ...
    def remove_widget(self, widget: Gtk.Widget) -> bool: ...
    def set_sensitive(self, sensitive: bool) -> None: ...
    def set_visible(self, visible: bool) -> None: ...
    def set_widgets(self, widgets: Optional[list[Gtk.Widget]] = None) -> None: ...
    def show(self) -> None: ...

# override
class IconSize(GObject.GEnum):
    _16 = 16
    _22 = 22
    _24 = 24
    _32 = 32
    _48 = 48
    _96 = 96

class ScrollDirection(GObject.GEnum):
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    UP = 0

class StatusIconState(GObject.GEnum):
    FALLBACK = 1
    NATIVE = 0
    NO_SUPPORT = 2
