from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import Adw
from gi.repository import Gdk
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk

MAJOR_VERSION: int = 1
MICRO_VERSION: int = 1
MINOR_VERSION: int = 4
VERSION_S: str = "1.4.1"
WIDGET_KIND_ANY: str = "*"
WIDGET_KIND_DOCUMENT: str = "document"
WIDGET_KIND_UNKNOWN: str = "unknown"
WIDGET_KIND_UTILITY: str = "utility"
_lock = ...  # FIXME Constant
_namespace: str = "Panel"
_version: str = "1"

def check_version(major: int, minor: int, micro: int) -> bool: ...
def finalize() -> None: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def get_resource() -> Gio.Resource: ...
def init() -> None: ...
def marshal_BOOLEAN__OBJECT_OBJECT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def marshal_OBJECT__OBJECT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...

class Action(GObject.GPointer): ...

class ActionMuxer(GObject.Object, Gio.ActionGroup):
    """
    :Constructors:

    ::

        ActionMuxer(**properties)
        new() -> Panel.ActionMuxer

    Object PanelActionMuxer

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    def get_action_group(self, prefix: str) -> Optional[Gio.ActionGroup]: ...
    def insert_action_group(
        self, prefix: str, action_group: Gio.ActionGroup
    ) -> None: ...
    def list_groups(self) -> list[str]: ...
    @classmethod
    def new(cls) -> ActionMuxer: ...
    def remove_action_group(self, prefix: str) -> None: ...
    def remove_all(self) -> None: ...

class ActionMuxerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionMuxerClass()
    """

    parent_class: GObject.ObjectClass = ...

class Application(Adw.Application, Gio.ActionGroup, Gio.ActionMap):
    """
    :Constructors:

    ::

        Application(**properties)
        new(application_id:str, flags:Gio.ApplicationFlags) -> Panel.Application

    Object PanelApplication

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Properties from AdwApplication:
      style-manager -> AdwStyleManager: style-manager

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GtkApplication:
      window-added (GtkWindow)
      window-removed (GtkWindow)
      query-end ()

    Properties from GtkApplication:
      register-session -> gboolean: register-session
      screensaver-active -> gboolean: screensaver-active
      menubar -> GMenuModel: menubar
      active-window -> GtkWindow: active-window

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GApplication:
      startup ()
      shutdown ()
      activate ()
      open (gpointer, gint, gchararray)
      command-line (GApplicationCommandLine) -> gint
      handle-local-options (GVariantDict) -> gint
      name-lost () -> gboolean

    Properties from GApplication:
      application-id -> gchararray: Application identifier
        The unique identifier for the application
      flags -> GApplicationFlags: Application flags
        Flags specifying the behaviour of the application
      resource-base-path -> gchararray: Resource base path
        The base resource path for the application
      is-registered -> gboolean: Is registered
        If g_application_register() has been called
      is-remote -> gboolean: Is remote
        If this application instance is remote
      inactivity-timeout -> guint: Inactivity timeout
        Time (ms) to stay alive after becoming idle
      action-group -> GActionGroup: Action group
        The group of actions that the application exports
      is-busy -> gboolean: Is busy
        If this application is currently marked busy

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        style_manager: Adw.StyleManager
        active_window: Optional[Gtk.Window]
        menubar: Optional[Gio.MenuModel]
        register_session: bool
        screensaver_active: bool
        application_id: Optional[str]
        flags: Gio.ApplicationFlags
        inactivity_timeout: int
        is_busy: bool
        is_registered: bool
        is_remote: bool
        resource_base_path: Optional[str]
        action_group: Optional[Gio.ActionGroup]

    props: Props = ...
    parent_instance: Adw.Application = ...
    def __init__(
        self,
        menubar: Optional[Gio.MenuModel] = ...,
        register_session: bool = ...,
        action_group: Optional[Gio.ActionGroup] = ...,
        application_id: Optional[str] = ...,
        flags: Gio.ApplicationFlags = ...,
        inactivity_timeout: int = ...,
        resource_base_path: Optional[str] = ...,
    ): ...
    @classmethod
    def new(cls, application_id: str, flags: Gio.ApplicationFlags) -> Application: ...

class ApplicationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ApplicationClass()
    """

    parent_class: Adw.ApplicationClass = ...
    _reserved: list[None] = ...

class Dock(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Dock(**properties)
        new() -> Gtk.Widget

    Object PanelDock

    Signals from PanelDock:
      panel-drag-begin (PanelWidget)
      panel-drag-end (PanelWidget)
      create-frame (PanelPosition) -> PanelFrame
      adopt-widget (PanelWidget) -> gboolean

    Properties from PanelDock:
      reveal-bottom -> gboolean: Reveal bottom
        Reveal bottom
      reveal-end -> gboolean: Reveal end
        Reveal end
      reveal-start -> gboolean: Reveal start
        Reveal start
      reveal-top -> gboolean: Reveal top
        Reveal top
      can-reveal-bottom -> gboolean: Can reveal bottom
        Can reveal bottom
      can-reveal-end -> gboolean: Can reveal end
        Can reveal end
      can-reveal-start -> gboolean: Can reveal start
        Can reveal start
      can-reveal-top -> gboolean: Can reveal top
        Can reveal top
      start-width -> gint: Start Width
        Start Width
      end-width -> gint: End Width
        End Width
      top-height -> gint: Top Height
        Top Height
      bottom-height -> gint: Bottom Height
        Bottom Height

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
        bottom_height: int
        can_reveal_bottom: bool
        can_reveal_end: bool
        can_reveal_start: bool
        can_reveal_top: bool
        end_width: int
        reveal_bottom: bool
        reveal_end: bool
        reveal_start: bool
        reveal_top: bool
        start_width: int
        top_height: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
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
        bottom_height: int = ...,
        end_width: int = ...,
        reveal_bottom: bool = ...,
        reveal_end: bool = ...,
        reveal_start: bool = ...,
        reveal_top: bool = ...,
        start_width: int = ...,
        top_height: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def do_panel_drag_begin(self, widget: Widget) -> None: ...
    def do_panel_drag_end(self, widget: Widget) -> None: ...
    def foreach_frame(self, callback: Callable[..., None], *user_data: Any) -> None: ...
    def get_can_reveal_area(self, area: Area) -> bool: ...
    def get_can_reveal_bottom(self) -> bool: ...
    def get_can_reveal_end(self) -> bool: ...
    def get_can_reveal_start(self) -> bool: ...
    def get_can_reveal_top(self) -> bool: ...
    def get_reveal_area(self, area: Area) -> bool: ...
    def get_reveal_bottom(self) -> bool: ...
    def get_reveal_end(self) -> bool: ...
    def get_reveal_start(self) -> bool: ...
    def get_reveal_top(self) -> bool: ...
    @classmethod
    def new(cls) -> Dock: ...
    def remove(self, widget: Gtk.Widget) -> None: ...
    def set_bottom_height(self, height: int) -> None: ...
    def set_end_width(self, width: int) -> None: ...
    def set_reveal_area(self, area: Area, reveal: bool) -> None: ...
    def set_reveal_bottom(self, reveal_bottom: bool) -> None: ...
    def set_reveal_end(self, reveal_end: bool) -> None: ...
    def set_reveal_start(self, reveal_start: bool) -> None: ...
    def set_reveal_top(self, reveal_top: bool) -> None: ...
    def set_start_width(self, width: int) -> None: ...
    def set_top_height(self, height: int) -> None: ...

class DockClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DockClass()
    """

    parent_class: Gtk.WidgetClass = ...
    panel_drag_begin: Callable[[Dock, Widget], None] = ...
    panel_drag_end: Callable[[Dock, Widget], None] = ...

class DocumentWorkspace(
    Workspace,
    Gio.ActionGroup,
    Gio.ActionMap,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Native,
    Gtk.Root,
    Gtk.ShortcutManager,
):
    """
    :Constructors:

    ::

        DocumentWorkspace(**properties)
        new() -> Panel.DocumentWorkspace

    Object PanelDocumentWorkspace

    Signals from PanelDocumentWorkspace:
      create-frame (PanelPosition) -> PanelFrame
      add-widget (PanelWidget, PanelPosition) -> gboolean

    Properties from PanelDocumentWorkspace:
      dock -> PanelDock: dock
      grid -> PanelGrid: grid
      statusbar -> PanelStatusbar: statusbar

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Properties from PanelWorkspace:
      id -> gchararray: id

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Properties from AdwApplicationWindow:
      content -> GtkWidget: content
      current-breakpoint -> AdwBreakpoint: current-breakpoint

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Properties from GtkApplicationWindow:
      show-menubar -> gboolean: show-menubar

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GtkWindow:
      keys-changed ()
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean

    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      suspended -> gboolean: suspended
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened

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
        dock: Dock
        grid: Grid
        statusbar: Optional[Statusbar]
        id: str
        content: Optional[Gtk.Widget]
        current_breakpoint: Optional[Adw.Breakpoint]
        show_menubar: bool
        application: Optional[Gtk.Application]
        child: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Gtk.Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        suspended: bool
        title: Optional[str]
        titlebar: Optional[Gtk.Widget]
        transient_for: Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        startup_id: str

    props: Props = ...
    parent_instance: Workspace = ...
    def __init__(
        self,
        id: str = ...,
        content: Optional[Gtk.Widget] = ...,
        show_menubar: bool = ...,
        application: Optional[Gtk.Application] = ...,
        child: Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Optional[Gtk.Widget] = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Gtk.Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: Optional[str] = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: Optional[str] = ...,
        titlebar: Optional[Gtk.Widget] = ...,
        transient_for: Optional[Gtk.Window] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add_widget(
        self, widget: Widget, position: Optional[Position] = None
    ) -> bool: ...
    def do_add_widget(
        self, widget: Widget, position: Optional[Position] = None
    ) -> bool: ...
    def get_dock(self) -> Dock: ...
    def get_grid(self) -> Grid: ...
    def get_statusbar(self) -> Optional[Statusbar]: ...
    def get_titlebar(self) -> Optional[Gtk.Widget]: ...
    @classmethod
    def new(cls) -> DocumentWorkspace: ...
    def set_titlebar(self, titlebar: Gtk.Widget) -> None: ...

class DocumentWorkspaceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DocumentWorkspaceClass()
    """

    parent_class: WorkspaceClass = ...
    create_frame: None = ...
    add_widget: Callable[[DocumentWorkspace, Widget, Optional[Position]], bool] = ...
    _reserved: list[None] = ...

class Frame(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    """
    :Constructors:

    ::

        Frame(**properties)
        new() -> Gtk.Widget

    Object PanelFrame

    Signals from PanelFrame:
      adopt-widget (PanelWidget) -> gboolean
      page-closed (PanelWidget)

    Properties from PanelFrame:
      closeable -> gboolean: Closeable
        If the frame may be closed
      empty -> gboolean: Empty
        If there are any panels added
      placeholder -> GtkWidget: Placeholder
        Placeholder
      visible-child -> PanelWidget: Visible Child
        Visible Child

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
        closeable: bool
        empty: bool
        placeholder: Optional[Gtk.Widget]
        visible_child: Optional[Widget]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation

    props: Props = ...
    parent_instance: Gtk.Widget = ...
    def __init__(
        self,
        placeholder: Optional[Gtk.Widget] = ...,
        visible_child: Widget = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def add(self, panel: Widget) -> None: ...
    def add_before(self, panel: Widget, sibling: Widget) -> None: ...
    def do_adopt_widget(self, widget: Widget) -> bool: ...
    def do_page_closed(self, widget: Widget) -> None: ...
    def get_closeable(self) -> bool: ...
    def get_empty(self) -> bool: ...
    def get_header(self) -> Optional[FrameHeader]: ...
    def get_n_pages(self) -> int: ...
    def get_page(self, n: int) -> Optional[Widget]: ...
    def get_pages(self) -> Gtk.SelectionModel: ...
    def get_placeholder(self) -> Optional[Gtk.Widget]: ...
    def get_position(self) -> Position: ...
    def get_requested_size(self) -> int: ...
    def get_visible_child(self) -> Optional[Widget]: ...
    @classmethod
    def new(cls) -> Frame: ...
    def remove(self, panel: Widget) -> None: ...
    def set_child_pinned(self, child: Widget, pinned: bool) -> None: ...
    def set_header(self, header: Optional[FrameHeader] = None) -> None: ...
    def set_placeholder(self, placeholder: Optional[Gtk.Widget] = None) -> None: ...
    def set_requested_size(self, requested_size: int) -> None: ...
    def set_visible_child(self, widget: Widget) -> None: ...

class FrameClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FrameClass()
    """

    parent_class: Gtk.WidgetClass = ...
    page_closed: Callable[[Frame, Widget], None] = ...
    adopt_widget: Callable[[Frame, Widget], bool] = ...
    _reserved: list[None] = ...

class FrameHeader(GObject.GInterface):
    """
    Interface PanelFrameHeader

    Signals from GObject:
      notify (GParam)
    """

    def add_prefix(self, priority: int, child: Gtk.Widget) -> None: ...
    def add_suffix(self, priority: int, child: Gtk.Widget) -> None: ...
    def can_drop(self, widget: Widget) -> bool: ...
    def get_frame(self) -> Optional[Frame]: ...
    def page_changed(self, widget: Optional[Widget] = None) -> None: ...
    def set_frame(self, frame: Optional[Frame] = None) -> None: ...

class FrameHeaderBar(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, FrameHeader
):
    """
    :Constructors:

    ::

        FrameHeaderBar(**properties)
        new() -> Gtk.Widget

    Object PanelFrameHeaderBar

    Properties from PanelFrameHeaderBar:
      show-icon -> gboolean: Show Icon
        Show Icon

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
        show_icon: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        frame: Optional[Frame]

    props: Props = ...
    def __init__(
        self,
        show_icon: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        frame: Optional[Frame] = ...,
    ): ...
    def get_menu_popover(self) -> Gtk.PopoverMenu: ...
    def get_show_icon(self) -> bool: ...
    @classmethod
    def new(cls) -> FrameHeaderBar: ...
    def set_show_icon(self, show_icon: bool) -> None: ...

class FrameHeaderBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FrameHeaderBarClass()
    """

    parent_class: Gtk.WidgetClass = ...

class FrameHeaderInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        FrameHeaderInterface()
    """

    parent_iface: GObject.TypeInterface = ...
    page_changed: Callable[[FrameHeader, Optional[Widget]], None] = ...
    can_drop: Callable[[FrameHeader, Widget], bool] = ...
    add_prefix: Callable[[FrameHeader, int, Gtk.Widget], None] = ...
    add_suffix: Callable[[FrameHeader, int, Gtk.Widget], None] = ...

class FrameSwitcher(
    Gtk.Widget,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Orientable,
    FrameHeader,
):
    """
    :Constructors:

    ::

        FrameSwitcher(**properties)
        new() -> Gtk.Widget

    Object PanelFrameSwitcher

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
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
        frame: Optional[Frame]

    props: Props = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
        frame: Optional[Frame] = ...,
    ): ...
    @classmethod
    def new(cls) -> FrameSwitcher: ...

class FrameSwitcherClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FrameSwitcherClass()
    """

    parent_class: Gtk.WidgetClass = ...

class FrameTabBar(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, FrameHeader
):
    """
    :Constructors:

    ::

        FrameTabBar(**properties)
        new() -> Gtk.Widget

    Object PanelFrameTabBar

    Properties from PanelFrameTabBar:
      autohide -> gboolean: Autohide
        Autohide
      inverted -> gboolean: Inverted
        Inverted
      expand-tabs -> gboolean: Expand Tabs
        Expand Tabs

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
        autohide: bool
        expand_tabs: bool
        inverted: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        frame: Optional[Frame]

    props: Props = ...
    def __init__(
        self,
        autohide: bool = ...,
        expand_tabs: bool = ...,
        inverted: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        frame: Optional[Frame] = ...,
    ): ...
    def get_autohide(self) -> bool: ...
    def get_expand_tabs(self) -> bool: ...
    def get_inverted(self) -> bool: ...
    @classmethod
    def new(cls) -> FrameTabBar: ...
    def set_autohide(self, autohide: bool) -> None: ...
    def set_expand_tabs(self, expand_tabs: bool) -> None: ...
    def set_inverted(self, inverted: bool) -> None: ...

class FrameTabBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FrameTabBarClass()
    """

    parent_class: Gtk.WidgetClass = ...

class GSettingsActionGroup(GObject.Object, Gio.ActionGroup):
    """
    :Constructors:

    ::

        GSettingsActionGroup(**properties)

    Object PanelGSettingsActionGroup

    Properties from PanelGSettingsActionGroup:
      settings -> GSettings: settings

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        settings: Gio.Settings

    props: Props = ...
    def __init__(self, settings: Gio.Settings = ...): ...
    @staticmethod
    def new(settings: Gio.Settings) -> Gio.ActionGroup: ...

class GSettingsActionGroupClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GSettingsActionGroupClass()
    """

    parent_class: GObject.ObjectClass = ...

class Grid(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Grid(**properties)
        new() -> Gtk.Widget

    Object PanelGrid

    Signals from PanelGrid:
      create-frame () -> PanelFrame

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
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
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
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add(self, widget: Widget) -> None: ...
    def agree_to_close_async(
        self,
        cancellable: Optional[Gio.Cancellable],
        callback: Callable[..., None],
        *user_data: Any,
    ) -> None: ...
    def agree_to_close_finish(self, result: Gio.AsyncResult) -> bool: ...
    def foreach_frame(self, callback: Callable[..., None], *user_data: Any) -> None: ...
    def get_column(self, column: int) -> GridColumn: ...
    def get_most_recent_column(self) -> GridColumn: ...
    def get_most_recent_frame(self) -> Frame: ...
    def get_n_columns(self) -> int: ...
    def insert_column(self, position: int) -> None: ...
    @classmethod
    def new(cls) -> Grid: ...

class GridClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GridClass()
    """

    parent_class: Gtk.WidgetClass = ...
    create_frame: None = ...
    _reserved: list[None] = ...

class GridColumn(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        GridColumn(**properties)
        new() -> Gtk.Widget

    Object PanelGridColumn

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
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def foreach_frame(self, callback: Callable[..., None], *user_data: Any) -> None: ...
    def get_empty(self) -> bool: ...
    def get_most_recent_frame(self) -> Frame: ...
    def get_n_rows(self) -> int: ...
    def get_row(self, row: int) -> Frame: ...
    @classmethod
    def new(cls) -> GridColumn: ...

class GridColumnClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GridColumnClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Inhibitor(GObject.Object):
    """
    :Constructors:

    ::

        Inhibitor(**properties)

    Object PanelInhibitor

    Signals from GObject:
      notify (GParam)
    """

    def uninhibit(self) -> None: ...

class InhibitorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InhibitorClass()
    """

    parent_class: GObject.ObjectClass = ...

class LayeredSettings(GObject.Object):
    """
    :Constructors:

    ::

        LayeredSettings(**properties)
        new(schema_id:str, path:str) -> Panel.LayeredSettings

    Object PanelLayeredSettings

    Signals from PanelLayeredSettings:
      changed (gchararray)

    Properties from PanelLayeredSettings:
      path -> gchararray: Settings Path
        Settings Path
      schema-id -> gchararray: Schema Id
        Schema Id

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        path: str
        schema_id: str

    props: Props = ...
    def __init__(self, path: str = ..., schema_id: str = ...): ...
    def append(self, settings: Gio.Settings) -> None: ...
    def bind(
        self, key: str, object: None, property: str, flags: Gio.SettingsBindFlags
    ) -> None: ...
    def bind_with_mapping(
        self,
        key: str,
        object: None,
        property: str,
        flags: Gio.SettingsBindFlags,
        get_mapping: Callable[..., bool],
        set_mapping: Callable[..., GLib.Variant],
        *user_data: Any,
    ) -> None: ...
    def get_boolean(self, key: str) -> bool: ...
    def get_default_value(self, key: str) -> GLib.Variant: ...
    def get_double(self, key: str) -> float: ...
    def get_int(self, key: str) -> int: ...
    def get_key(self, key: str) -> Gio.SettingsSchemaKey: ...
    def get_string(self, key: str) -> str: ...
    def get_uint(self, key: str) -> int: ...
    def get_user_value(self, key: str) -> Optional[GLib.Variant]: ...
    def get_value(self, key: str) -> GLib.Variant: ...
    def list_keys(self) -> list[str]: ...
    @classmethod
    def new(cls, schema_id: str, path: str) -> LayeredSettings: ...
    def set_boolean(self, key: str, val: bool) -> None: ...
    def set_double(self, key: str, val: float) -> None: ...
    def set_int(self, key: str, val: int) -> None: ...
    def set_string(self, key: str, val: str) -> None: ...
    def set_uint(self, key: str, val: int) -> None: ...
    def set_value(self, key: str, value: GLib.Variant) -> None: ...
    def unbind(self, property: str) -> None: ...

class LayeredSettingsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LayeredSettingsClass()
    """

    parent_class: GObject.ObjectClass = ...

class MenuManager(GObject.Object):
    """
    :Constructors:

    ::

        MenuManager(**properties)
        new() -> Panel.MenuManager

    Object PanelMenuManager

    Signals from GObject:
      notify (GParam)
    """

    def add_filename(self, filename: str) -> int: ...
    def add_resource(self, resource: str) -> int: ...
    def find_item_by_id(self, id: str) -> Tuple[Optional[Gio.Menu], int]: ...
    def get_menu_by_id(self, menu_id: str) -> Gio.Menu: ...
    def get_menu_ids(self) -> list[str]: ...
    def merge(self, menu_id: str, menu_model: Gio.MenuModel) -> int: ...
    @classmethod
    def new(cls) -> MenuManager: ...
    def remove(self, merge_id: int) -> None: ...
    def set_attribute_string(
        self, menu: Gio.Menu, position: int, attribute: str, value: str
    ) -> None: ...

class MenuManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MenuManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class OmniBar(
    Gtk.Widget, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        OmniBar(**properties)
        new() -> Gtk.Widget

    Object PanelOmniBar

    Properties from PanelOmniBar:
      action-tooltip -> gchararray: action-tooltip
      popover -> GtkPopover: Popover
        Popover
      progress -> gdouble: Progress
        Progress bar fraction
      icon-name -> gchararray: Icon Name
        Icon Name
      menu-model -> GMenuModel: Menu Model
        Menu Model

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
        action_tooltip: str
        icon_name: str
        menu_model: Gio.MenuModel
        popover: Optional[Gtk.Popover]
        progress: float
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: Optional[str]
        action_target: GLib.Variant

    props: Props = ...
    parent_instance: Gtk.Widget = ...
    def __init__(
        self,
        action_tooltip: str = ...,
        icon_name: str = ...,
        menu_model: Gio.MenuModel = ...,
        popover: Optional[Gtk.Popover] = ...,
        progress: float = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def add_prefix(self, priority: int, widget: Gtk.Widget) -> None: ...
    def add_suffix(self, priority: int, widget: Gtk.Widget) -> None: ...
    def get_popover(self) -> Optional[Gtk.Popover]: ...
    def get_progress(self) -> float: ...
    @classmethod
    def new(cls) -> OmniBar: ...
    def remove(self, widget: Gtk.Widget) -> None: ...
    def set_popover(self, popover: Optional[Gtk.Popover] = None) -> None: ...
    def set_progress(self, progress: float) -> None: ...
    def start_pulsing(self) -> None: ...
    def stop_pulsing(self) -> None: ...

class OmniBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OmniBarClass()
    """

    parent_class: Gtk.WidgetClass = ...
    _reserved: list[None] = ...

class Paned(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    """
    :Constructors:

    ::

        Paned(**properties)
        new() -> Gtk.Widget

    Object PanelPaned

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
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation

    props: Props = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def append(self, child: Gtk.Widget) -> None: ...
    def get_n_children(self) -> int: ...
    def get_nth_child(self, nth: int) -> Optional[Gtk.Widget]: ...
    def insert(self, position: int, child: Gtk.Widget) -> None: ...
    def insert_after(self, child: Gtk.Widget, sibling: Gtk.Widget) -> None: ...
    @classmethod
    def new(cls) -> Paned: ...
    def prepend(self, child: Gtk.Widget) -> None: ...
    def remove(self, child: Gtk.Widget) -> None: ...

class PanedClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PanedClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Position(GObject.Object):
    """
    :Constructors:

    ::

        Position(**properties)
        new() -> Panel.Position
        new_from_variant(variant:GLib.Variant) -> Panel.Position or None

    Object PanelPosition

    Properties from PanelPosition:
      area -> PanelArea: area
      area-set -> gboolean: area-set
      column -> guint: column
      column-set -> gboolean: column-set
      depth -> guint: depth
      depth-set -> gboolean: depth-set
      row -> guint: row
      row-set -> gboolean: row-set

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        area: Area
        area_set: bool
        column: int
        column_set: bool
        depth: int
        depth_set: bool
        row: int
        row_set: bool

    props: Props = ...
    def __init__(
        self,
        area: Area = ...,
        area_set: bool = ...,
        column: int = ...,
        column_set: bool = ...,
        depth: int = ...,
        depth_set: bool = ...,
        row: int = ...,
        row_set: bool = ...,
    ): ...
    def equal(self, b: Position) -> bool: ...
    def get_area(self) -> Area: ...
    def get_area_set(self) -> bool: ...
    def get_column(self) -> int: ...
    def get_column_set(self) -> bool: ...
    def get_depth(self) -> int: ...
    def get_depth_set(self) -> bool: ...
    def get_row(self) -> int: ...
    def get_row_set(self) -> bool: ...
    def is_indeterminate(self) -> bool: ...
    @classmethod
    def new(cls) -> Position: ...
    @classmethod
    def new_from_variant(cls, variant: GLib.Variant) -> Optional[Position]: ...
    def set_area(self, area: Area) -> None: ...
    def set_area_set(self, area_set: bool) -> None: ...
    def set_column(self, column: int) -> None: ...
    def set_column_set(self, column_set: bool) -> None: ...
    def set_depth(self, depth: int) -> None: ...
    def set_depth_set(self, depth_set: bool) -> None: ...
    def set_row(self, row: int) -> None: ...
    def set_row_set(self, row_set: bool) -> None: ...
    def to_variant(self) -> Optional[GLib.Variant]: ...

class PositionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PositionClass()
    """

    parent_class: GObject.ObjectClass = ...

class SaveDelegate(GObject.Object):
    """
    :Constructors:

    ::

        SaveDelegate(**properties)
        new() -> Panel.SaveDelegate

    Object PanelSaveDelegate

    Signals from PanelSaveDelegate:
      save (GTask) -> gboolean
      close ()
      discard ()

    Properties from PanelSaveDelegate:
      icon -> GIcon: Icon
        A GIcon representing the save operation
      icon-name -> gchararray: Icon Name
        Icon Name
      is-draft -> gboolean: Is Draft
        If the delegate contents are ephemeral until saved
      progress -> gdouble: Progress
        The progress of the save operation
      subtitle -> gchararray: Subtitle
        The subtitle of the document or documents to save
      title -> gchararray: Title
        The title of the document or documents to save

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        icon: Optional[Gio.Icon]
        icon_name: Optional[str]
        is_draft: bool
        progress: float
        subtitle: Optional[str]
        title: Optional[str]

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self,
        icon: Optional[Gio.Icon] = ...,
        icon_name: Optional[str] = ...,
        is_draft: bool = ...,
        progress: float = ...,
        subtitle: Optional[str] = ...,
        title: Optional[str] = ...,
    ): ...
    def close(self) -> None: ...
    def discard(self) -> None: ...
    def do_close(self) -> None: ...
    def do_discard(self) -> None: ...
    def do_save(self, task: Gio.Task) -> bool: ...
    def do_save_async(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def do_save_finish(self, result: Gio.AsyncResult) -> bool: ...
    def get_icon(self) -> Optional[Gio.Icon]: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_is_draft(self) -> bool: ...
    def get_progress(self) -> float: ...
    def get_subtitle(self) -> Optional[str]: ...
    def get_title(self) -> Optional[str]: ...
    @classmethod
    def new(cls) -> SaveDelegate: ...
    def save_async(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def save_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_icon(self, icon: Optional[Gio.Icon] = None) -> None: ...
    def set_icon_name(self, icon: Optional[str] = None) -> None: ...
    def set_is_draft(self, is_draft: bool) -> None: ...
    def set_progress(self, progress: float) -> None: ...
    def set_subtitle(self, subtitle: Optional[str] = None) -> None: ...
    def set_title(self, title: Optional[str] = None) -> None: ...

class SaveDelegateClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SaveDelegateClass()
    """

    parent_class: GObject.ObjectClass = ...
    save_async: Callable[..., None] = ...
    save_finish: Callable[[SaveDelegate, Gio.AsyncResult], bool] = ...
    save: Callable[[SaveDelegate, Gio.Task], bool] = ...
    discard: Callable[[SaveDelegate], None] = ...
    close: Callable[[SaveDelegate], None] = ...
    _reserved: list[None] = ...

class SaveDialog(
    Adw.MessageDialog,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Native,
    Gtk.Root,
    Gtk.ShortcutManager,
):
    """
    :Constructors:

    ::

        SaveDialog(**properties)
        new() -> Gtk.Widget

    Object PanelSaveDialog

    Properties from PanelSaveDialog:
      close-after-save -> gboolean: close-after-save

    Signals from AdwMessageDialog:
      response (gchararray)

    Properties from AdwMessageDialog:
      heading -> gchararray: heading
      heading-use-markup -> gboolean: heading-use-markup
      body -> gchararray: body
      body-use-markup -> gboolean: body-use-markup
      extra-child -> GtkWidget: extra-child
      default-response -> gchararray: default-response
      close-response -> gchararray: close-response

    Signals from GtkWindow:
      keys-changed ()
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean

    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      suspended -> gboolean: suspended
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened

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
        close_after_save: bool
        body: str
        body_use_markup: bool
        close_response: str
        default_response: Optional[str]
        extra_child: Optional[Gtk.Widget]
        heading: Optional[str]
        heading_use_markup: bool
        application: Optional[Gtk.Application]
        child: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Gtk.Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        suspended: bool
        title: Optional[str]
        titlebar: Optional[Gtk.Widget]
        transient_for: Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        startup_id: str

    props: Props = ...
    def __init__(
        self,
        close_after_save: bool = ...,
        body: str = ...,
        body_use_markup: bool = ...,
        close_response: str = ...,
        default_response: Optional[str] = ...,
        extra_child: Optional[Gtk.Widget] = ...,
        heading: Optional[str] = ...,
        heading_use_markup: bool = ...,
        application: Optional[Gtk.Application] = ...,
        child: Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Optional[Gtk.Widget] = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Gtk.Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: Optional[str] = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: Optional[str] = ...,
        titlebar: Optional[Gtk.Widget] = ...,
        transient_for: Optional[Gtk.Window] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add_delegate(self, delegate: SaveDelegate) -> None: ...
    def get_close_after_save(self) -> bool: ...
    @classmethod
    def new(cls) -> SaveDialog: ...
    def run_async(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def run_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_close_after_save(self, close_after_save: bool) -> None: ...

class SaveDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SaveDialogClass()
    """

    parent_class: Adw.MessageDialogClass = ...

class Session(GObject.Object):
    """
    :Constructors:

    ::

        Session(**properties)
        new() -> Panel.Session
        new_from_variant(variant:GLib.Variant) -> Panel.Session

    Object PanelSession

    Signals from GObject:
      notify (GParam)
    """

    def append(self, item: SessionItem) -> None: ...
    def get_item(self, position: int) -> Optional[SessionItem]: ...
    def get_n_items(self) -> int: ...
    def insert(self, position: int, item: SessionItem) -> None: ...
    def lookup_by_id(self, id: str) -> Optional[SessionItem]: ...
    @classmethod
    def new(cls) -> Session: ...
    @classmethod
    def new_from_variant(cls, variant: GLib.Variant) -> Session: ...
    def prepend(self, item: SessionItem) -> None: ...
    def remove(self, item: SessionItem) -> None: ...
    def remove_at(self, position: int) -> None: ...
    def to_variant(self) -> GLib.Variant: ...

class SessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SessionClass()
    """

    parent_class: GObject.ObjectClass = ...

class SessionItem(GObject.Object):
    """
    :Constructors:

    ::

        SessionItem(**properties)
        new() -> Panel.SessionItem

    Object PanelSessionItem

    Properties from PanelSessionItem:
      id -> gchararray: id
      module-name -> gchararray: module-name
      position -> PanelPosition: position
      type-hint -> gchararray: type-hint
      workspace -> gchararray: workspace

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        id: Optional[str]
        module_name: Optional[str]
        position: Optional[Position]
        type_hint: Optional[str]
        workspace: Optional[str]

    props: Props = ...
    def __init__(
        self,
        id: Optional[str] = ...,
        module_name: Optional[str] = ...,
        position: Optional[Position] = ...,
        type_hint: Optional[str] = ...,
        workspace: Optional[str] = ...,
    ): ...
    def get_id(self) -> Optional[str]: ...
    def get_metadata_value(
        self, key: str, expected_type: Optional[GLib.VariantType] = None
    ) -> Optional[GLib.Variant]: ...
    def get_module_name(self) -> Optional[str]: ...
    def get_position(self) -> Optional[Position]: ...
    def get_type_hint(self) -> Optional[str]: ...
    def get_workspace(self) -> Optional[str]: ...
    def has_metadata(self, key: str) -> Tuple[bool, GLib.VariantType]: ...
    def has_metadata_with_type(
        self, key: str, expected_type: GLib.VariantType
    ) -> bool: ...
    @classmethod
    def new(cls) -> SessionItem: ...
    def set_id(self, id: Optional[str] = None) -> None: ...
    def set_metadata_value(
        self, key: str, value: Optional[GLib.Variant] = None
    ) -> None: ...
    def set_module_name(self, module_name: Optional[str] = None) -> None: ...
    def set_position(self, position: Optional[Position] = None) -> None: ...
    def set_type_hint(self, type_hint: Optional[str] = None) -> None: ...
    def set_workspace(self, workspace: Optional[str] = None) -> None: ...

class SessionItemClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SessionItemClass()
    """

    parent_class: GObject.ObjectClass = ...

class Settings(GObject.Object, Gio.ActionGroup):
    """
    :Constructors:

    ::

        Settings(**properties)
        new(identifier:str, schema_id:str) -> Panel.Settings
        new_relocatable(identifier:str, schema_id:str, schema_id_prefix:str, path_prefix:str, path_suffix:str) -> Panel.Settings
        new_with_path(identifier:str, schema_id:str, path:str) -> Panel.Settings

    Object PanelSettings

    Signals from PanelSettings:
      changed (gchararray)

    Properties from PanelSettings:
      path -> gchararray: Path
        The path to use for for app settings
      path-prefix -> gchararray: Path Suffix
        A path prefix to preprend when generating schema paths
      path-suffix -> gchararray: Path Suffix
        A path suffix to append when generating schema paths
      identifier -> gchararray: Identifier
        The identifier used to unique'ify this settings instance
      schema-id -> gchararray: Schema ID
        Schema ID
      schema-id-prefix -> gchararray: Schema ID Prefix
        The prefix for schema-ids used when generating paths

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        identifier: str
        path: str
        path_prefix: str
        path_suffix: str
        schema_id: str
        schema_id_prefix: str

    props: Props = ...
    def __init__(
        self,
        identifier: str = ...,
        path: str = ...,
        path_prefix: str = ...,
        path_suffix: str = ...,
        schema_id: str = ...,
        schema_id_prefix: str = ...,
    ): ...
    def bind(
        self, key: str, object: None, property: str, flags: Gio.SettingsBindFlags
    ) -> None: ...
    def bind_with_mapping(
        self,
        key: str,
        object: None,
        property: str,
        flags: Gio.SettingsBindFlags,
        get_mapping: Optional[Callable[..., bool]] = None,
        set_mapping: Optional[Callable[..., GLib.Variant]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_boolean(self, key: str) -> bool: ...
    def get_default_value(self, key: str) -> GLib.Variant: ...
    def get_double(self, key: str) -> float: ...
    def get_int(self, key: str) -> int: ...
    def get_schema_id(self) -> str: ...
    def get_string(self, key: str) -> str: ...
    def get_uint(self, key: str) -> int: ...
    def get_user_value(self, key: str) -> Optional[GLib.Variant]: ...
    def get_value(self, key: str) -> GLib.Variant: ...
    @classmethod
    def new(cls, identifier: str, schema_id: str) -> Settings: ...
    @classmethod
    def new_relocatable(
        cls,
        identifier: str,
        schema_id: str,
        schema_id_prefix: str,
        path_prefix: str,
        path_suffix: str,
    ) -> Settings: ...
    @classmethod
    def new_with_path(cls, identifier: str, schema_id: str, path: str) -> Settings: ...
    @staticmethod
    def resolve_schema_path(
        schema_id_prefix: str,
        schema_id: str,
        identifier: str,
        path_prefix: str,
        path_suffix: str,
    ) -> str: ...
    def set_boolean(self, key: str, val: bool) -> None: ...
    def set_double(self, key: str, val: float) -> None: ...
    def set_int(self, key: str, val: int) -> None: ...
    def set_string(self, key: str, val: str) -> None: ...
    def set_uint(self, key: str, val: int) -> None: ...
    def set_value(self, key: str, value: GLib.Variant) -> None: ...
    def unbind(self, property: str) -> None: ...

class SettingsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SettingsClass()
    """

    parent_class: GObject.ObjectClass = ...

class Statusbar(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Statusbar(**properties)
        new() -> Gtk.Widget

    Object PanelStatusbar

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
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add_prefix(self, priority: int, widget: Gtk.Widget) -> None: ...
    def add_suffix(self, priority: int, widget: Gtk.Widget) -> None: ...
    @classmethod
    def new(cls) -> Statusbar: ...
    def remove(self, widget: Gtk.Widget) -> None: ...

class StatusbarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StatusbarClass()
    """

    parent_class: Gtk.WidgetClass = ...

class ThemeSelector(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        ThemeSelector(**properties)
        new() -> Gtk.Widget

    Object PanelThemeSelector

    Properties from PanelThemeSelector:
      action-name -> gchararray: Action Name
        The action to bind choices to

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
        action_name: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        action_name: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_action_name(self) -> str: ...
    @classmethod
    def new(cls) -> ThemeSelector: ...
    def set_action_name(self, action_name: str) -> None: ...

class ThemeSelectorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ThemeSelectorClass()
    """

    parent_class: Gtk.WidgetClass = ...

class ToggleButton(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        ToggleButton(**properties)
        new(dock:Panel.Dock, area:Panel.Area) -> Gtk.Widget

    Object PanelToggleButton

    Properties from PanelToggleButton:
      dock -> PanelDock: dock
      area -> PanelArea: area

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
        area: Area
        dock: Dock
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        area: Area = ...,
        dock: Dock = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    @classmethod
    def new(cls, dock: Dock, area: Area) -> ToggleButton: ...

class ToggleButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ToggleButtonClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Widget(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Widget(**properties)
        new() -> Gtk.Widget

    Object PanelWidget

    Signals from PanelWidget:
      get-default-focus () -> GtkWidget
      presented ()

    Properties from PanelWidget:
      busy -> gboolean: Busy
        If the widget is busy, such as loading or saving a file
      can-maximize -> gboolean: Can Maximize
        Can Maximize
      child -> GtkWidget: Child
        Child
      icon -> GIcon: Icon
        A GIcon for the panel
      icon-name -> gchararray: Icon Name
        Icon Name
      id -> gchararray: Identifier
        The identifier for the widget which can be used for saving state
      menu-model -> GMenuModel: Menu Model
        Menu Model
      modified -> gboolean: Modified
        If the widget contains unsaved state
      needs-attention -> gboolean: Needs Attention
        Needs Attention
      kind -> gchararray: Kind
        The kind of panel widget
      reorderable -> gboolean: Reorderable
        If the panel may be reordered
      save-delegate -> PanelSaveDelegate: Save Delegate
        A save delegate to perform a save operation on the page
      title -> gchararray: Title
        Title
      tooltip -> gchararray: tooltip

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
        busy: bool
        can_maximize: bool
        child: Optional[Gtk.Widget]
        icon: Optional[Gio.Icon]
        icon_name: Optional[str]
        id: str
        kind: str
        menu_model: Optional[Gio.MenuModel]
        modified: bool
        needs_attention: bool
        reorderable: bool
        save_delegate: Optional[SaveDelegate]
        title: Optional[str]
        tooltip: Optional[str]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
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
        can_maximize: bool = ...,
        child: Optional[Gtk.Widget] = ...,
        icon: Optional[Gio.Icon] = ...,
        icon_name: Optional[str] = ...,
        id: str = ...,
        kind: Optional[str] = ...,
        menu_model: Optional[Gio.MenuModel] = ...,
        modified: bool = ...,
        needs_attention: bool = ...,
        reorderable: bool = ...,
        save_delegate: Optional[SaveDelegate] = ...,
        title: Optional[str] = ...,
        tooltip: Optional[str] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def action_set_enabled(self, action_name: str, enabled: bool) -> None: ...
    def close(self) -> None: ...
    def do_get_default_focus(self) -> Optional[Gtk.Widget]: ...
    def do_presented(self) -> None: ...
    def focus_default(self) -> bool: ...
    def force_close(self) -> None: ...
    def get_busy(self) -> bool: ...
    def get_can_maximize(self) -> bool: ...
    def get_child(self) -> Optional[Gtk.Widget]: ...
    def get_default_focus(self) -> Optional[Gtk.Widget]: ...
    def get_icon(self) -> Optional[Gio.Icon]: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_id(self) -> str: ...
    def get_kind(self) -> str: ...
    def get_menu_model(self) -> Optional[Gio.MenuModel]: ...
    def get_modified(self) -> bool: ...
    def get_needs_attention(self) -> bool: ...
    def get_position(self) -> Optional[Position]: ...
    def get_reorderable(self) -> bool: ...
    def get_save_delegate(self) -> Optional[SaveDelegate]: ...
    def get_title(self) -> Optional[str]: ...
    def get_tooltip(self) -> Optional[str]: ...
    def insert_action_group(self, prefix: str, group: Gio.ActionGroup) -> None: ...
    def mark_busy(self) -> None: ...
    def maximize(self) -> None: ...
    @classmethod
    def new(cls) -> Widget: ...
    def raise_(self) -> None: ...
    def set_can_maximize(self, can_maximize: bool) -> None: ...
    def set_child(self, child: Optional[Gtk.Widget] = None) -> None: ...
    def set_icon(self, icon: Optional[Gio.Icon] = None) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_id(self, id: str) -> None: ...
    def set_kind(self, kind: Optional[str] = None) -> None: ...
    def set_menu_model(self, menu_model: Optional[Gio.MenuModel] = None) -> None: ...
    def set_modified(self, modified: bool) -> None: ...
    def set_needs_attention(self, needs_attention: bool) -> None: ...
    def set_reorderable(self, reorderable: bool) -> None: ...
    def set_save_delegate(
        self, save_delegate: Optional[SaveDelegate] = None
    ) -> None: ...
    def set_title(self, title: Optional[str] = None) -> None: ...
    def set_tooltip(self, tooltip: Optional[str] = None) -> None: ...
    def unmark_busy(self) -> None: ...
    def unmaximize(self) -> None: ...

class WidgetClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WidgetClass()
    """

    parent_instance: Gtk.WidgetClass = ...
    get_default_focus: Callable[[Widget], Optional[Gtk.Widget]] = ...
    presented: Callable[[Widget], None] = ...
    _reserved: list[None] = ...
    def install_action(
        self,
        action_name: str,
        parameter_type: Optional[str],
        activate: Callable[[Gtk.Widget, str, Optional[GLib.Variant]], None],
    ) -> None: ...
    def install_property_action(self, action_name: str, property_name: str) -> None: ...

class Workbench(Gtk.WindowGroup):
    """
    :Constructors:

    ::

        Workbench(**properties)
        new() -> Panel.Workbench

    Object PanelWorkbench

    Signals from PanelWorkbench:
      activate ()

    Properties from PanelWorkbench:
      id -> gchararray: id

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        id: str

    props: Props = ...
    parent_instance: Gtk.WindowGroup = ...
    def __init__(self, id: str = ...): ...
    def action_set_enabled(self, action_name: str, enabled: bool) -> None: ...
    def activate(self) -> None: ...
    def add_workspace(self, workspace: Workspace) -> None: ...
    def do_activate(self) -> None: ...
    def do_unload_async(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def do_unload_finish(self, result: Gio.AsyncResult) -> bool: ...
    @staticmethod
    def find_from_widget(widget: Gtk.Widget) -> Optional[Workbench]: ...
    def find_workspace_typed(self, workspace_type: Type) -> Optional[Workspace]: ...
    def focus_workspace(self, workspace: Workspace) -> None: ...
    def foreach_workspace(
        self, foreach_func: Callable[..., None], *foreach_func_data: Any
    ) -> None: ...
    def get_id(self) -> str: ...
    def install_action(
        self,
        action_name: str,
        parameter_type: Optional[str],
        activate: Callable[[None, str, GLib.Variant], None],
    ) -> None: ...
    def install_property_action(self, action_name: str, property_name: str) -> None: ...
    @classmethod
    def new(cls) -> Workbench: ...
    def remove_workspace(self, workspace: Workspace) -> None: ...
    def set_id(self, id: str) -> None: ...

class WorkbenchClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WorkbenchClass()
    """

    parent_class: Gtk.WindowGroupClass = ...
    activate: Callable[[Workbench], None] = ...
    unload_async: Callable[..., None] = ...
    unload_finish: Callable[[Workbench, Gio.AsyncResult], bool] = ...
    _reserved: list[None] = ...
    def install_action(
        self,
        action_name: str,
        parameter_type: Optional[str],
        activate: Callable[[None, str, GLib.Variant], None],
    ) -> None: ...
    def install_property_action(self, action_name: str, property_name: str) -> None: ...

class Workspace(
    Adw.ApplicationWindow,
    Gio.ActionGroup,
    Gio.ActionMap,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Native,
    Gtk.Root,
    Gtk.ShortcutManager,
):
    """
    :Constructors:

    ::

        Workspace(**properties)

    Object PanelWorkspace

    Properties from PanelWorkspace:
      id -> gchararray: id

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Properties from AdwApplicationWindow:
      content -> GtkWidget: content
      current-breakpoint -> AdwBreakpoint: current-breakpoint

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Properties from GtkApplicationWindow:
      show-menubar -> gboolean: show-menubar

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GtkWindow:
      keys-changed ()
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean

    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      suspended -> gboolean: suspended
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened

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
        id: str
        content: Optional[Gtk.Widget]
        current_breakpoint: Optional[Adw.Breakpoint]
        show_menubar: bool
        application: Optional[Gtk.Application]
        child: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Gtk.Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        suspended: bool
        title: Optional[str]
        titlebar: Optional[Gtk.Widget]
        transient_for: Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        startup_id: str

    props: Props = ...
    parent_instance: Adw.ApplicationWindow = ...
    def __init__(
        self,
        id: str = ...,
        content: Optional[Gtk.Widget] = ...,
        show_menubar: bool = ...,
        application: Optional[Gtk.Application] = ...,
        child: Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Optional[Gtk.Widget] = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Gtk.Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: Optional[str] = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: Optional[str] = ...,
        titlebar: Optional[Gtk.Widget] = ...,
        transient_for: Optional[Gtk.Window] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Optional[Gtk.LayoutManager] = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def action_set_enabled(self, action_name: str, enabled: bool) -> None: ...
    @staticmethod
    def find_from_widget(widget: Gtk.Widget) -> Optional[Workspace]: ...
    def get_id(self) -> str: ...
    def get_workbench(self) -> Optional[Workbench]: ...
    def inhibit(
        self, flags: Gtk.ApplicationInhibitFlags, reason: str
    ) -> Optional[Inhibitor]: ...
    def set_id(self, id: str) -> None: ...

class WorkspaceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WorkspaceClass()
    """

    parent_class: Adw.ApplicationWindowClass = ...
    _reserved: list[None] = ...
    def install_action(
        self,
        action_name: str,
        parameter_type: Optional[str],
        activate: Callable[[None, str, GLib.Variant], None],
    ) -> None: ...
    def install_property_action(self, action_name: str, property_name: str) -> None: ...

class Area(GObject.GEnum):
    BOTTOM = 3
    CENTER = 4
    END = 1
    START = 0
    TOP = 2
