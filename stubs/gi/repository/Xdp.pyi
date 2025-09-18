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
from gi.repository import GObject

WALLPAPER_TARGET_BOTH: int = 0
_lock = ...  # FIXME Constant
_namespace: str = "Xdp"
_version: str = "1.0"

class Parent(GObject.GBoxed):
    def copy(self) -> Parent: ...
    def free(self) -> None: ...

class Portal(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        Portal(**properties)
        initable_new() -> Xdp.Portal or None
        new() -> Xdp.Portal

    Object XdpPortal

    Signals from XdpPortal:
      spawn-exited (guint, guint)
      session-state-changed (gboolean, XdpLoginSessionState)
      update-available (gchararray, gchararray, gchararray)
      update-progress (guint, guint, guint, XdpUpdateStatus, gchararray, gchararray)
      location-updated (gdouble, gdouble, gdouble, gdouble, gdouble, gdouble, gchararray, gint64, gint64)
      notification-action-invoked (gchararray, gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    def access_camera(
        self,
        parent: Optional[Parent],
        flags: CameraFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def access_camera_finish(self, result: Gio.AsyncResult) -> bool: ...
    def add_notification(
        self,
        id: str,
        notification: GLib.Variant,
        flags: NotificationFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def add_notification_finish(self, result: Gio.AsyncResult) -> bool: ...
    def compose_email(
        self,
        parent: Optional[Parent],
        addresses: Optional[Sequence[str]],
        cc: Optional[Sequence[str]],
        bcc: Optional[Sequence[str]],
        subject: Optional[str],
        body: Optional[str],
        attachments: Optional[Sequence[str]],
        flags: EmailFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def compose_email_finish(self, result: Gio.AsyncResult) -> bool: ...
    def create_remote_desktop_session(
        self,
        devices: DeviceType,
        outputs: OutputType,
        flags: RemoteDesktopFlags,
        cursor_mode: CursorMode,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def create_remote_desktop_session_finish(
        self, result: Gio.AsyncResult
    ) -> Session: ...
    def create_screencast_session(
        self,
        outputs: OutputType,
        flags: ScreencastFlags,
        cursor_mode: CursorMode,
        persist_mode: PersistMode,
        restore_token: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def create_screencast_session_finish(self, result: Gio.AsyncResult) -> Session: ...
    def dynamic_launcher_get_desktop_entry(self, desktop_file_id: str) -> str: ...
    def dynamic_launcher_get_icon(
        self,
        desktop_file_id: str,
        out_icon_format: Optional[str] = None,
        out_icon_size: Optional[int] = None,
    ) -> GLib.Variant: ...
    def dynamic_launcher_install(
        self, token: str, desktop_file_id: str, desktop_entry: str
    ) -> bool: ...
    def dynamic_launcher_launch(
        self, desktop_file_id: str, activation_token: str
    ) -> bool: ...
    def dynamic_launcher_prepare_install(
        self,
        parent: Optional[Parent],
        name: str,
        icon_v: GLib.Variant,
        launcher_type: LauncherType,
        target: Optional[str],
        editable_name: bool,
        editable_icon: bool,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def dynamic_launcher_prepare_install_finish(
        self, result: Gio.AsyncResult
    ) -> GLib.Variant: ...
    def dynamic_launcher_request_install_token(
        self, name: str, icon_v: GLib.Variant
    ) -> str: ...
    def dynamic_launcher_uninstall(self, desktop_file_id: str) -> bool: ...
    def get_user_information(
        self,
        parent: Optional[Parent],
        reason: Optional[str],
        flags: UserInformationFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def get_user_information_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    @classmethod
    def initable_new(cls) -> Optional[Portal]: ...
    def is_camera_present(self) -> bool: ...
    def location_monitor_start(
        self,
        parent: Optional[Parent],
        distance_threshold: int,
        time_threshold: int,
        accuracy: LocationAccuracy,
        flags: LocationMonitorFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def location_monitor_start_finish(self, result: Gio.AsyncResult) -> bool: ...
    def location_monitor_stop(self) -> None: ...
    @classmethod
    def new(cls) -> Portal: ...
    def open_directory(
        self,
        parent: Parent,
        uri: str,
        flags: OpenUriFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def open_directory_finish(self, result: Gio.AsyncResult) -> bool: ...
    def open_file(
        self,
        parent: Optional[Parent],
        title: str,
        filters: Optional[GLib.Variant],
        current_filter: Optional[GLib.Variant],
        choices: Optional[GLib.Variant],
        flags: OpenFileFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def open_file_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def open_pipewire_remote_for_camera(self) -> int: ...
    def open_uri(
        self,
        parent: Parent,
        uri: str,
        flags: OpenUriFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def open_uri_finish(self, result: Gio.AsyncResult) -> bool: ...
    def pick_color(
        self,
        parent: Optional[Parent] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def pick_color_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def prepare_print(
        self,
        parent: Optional[Parent],
        title: str,
        settings: Optional[GLib.Variant],
        page_setup: Optional[GLib.Variant],
        flags: PrintFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def prepare_print_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def print_file(
        self,
        parent: Optional[Parent],
        title: str,
        token: int,
        file: str,
        flags: PrintFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def print_file_finish(self, result: Gio.AsyncResult) -> bool: ...
    def remove_notification(self, id: str) -> None: ...
    def request_background(
        self,
        parent: Optional[Parent],
        reason: Optional[str],
        commandline: Sequence[str],
        flags: BackgroundFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def request_background_finish(self, result: Gio.AsyncResult) -> bool: ...
    @staticmethod
    def running_under_flatpak() -> bool: ...
    @staticmethod
    def running_under_sandbox() -> bool: ...
    @staticmethod
    def running_under_snap() -> bool: ...
    def save_file(
        self,
        parent: Optional[Parent],
        title: str,
        current_name: Optional[str],
        current_folder: Optional[str],
        current_file: Optional[str],
        filters: Optional[GLib.Variant],
        current_filter: Optional[GLib.Variant],
        choices: Optional[GLib.Variant],
        flags: SaveFileFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def save_file_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def save_files(
        self,
        parent: Optional[Parent],
        title: str,
        current_name: Optional[str],
        current_folder: Optional[str],
        files: GLib.Variant,
        choices: Optional[GLib.Variant],
        flags: SaveFileFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def save_files_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def session_inhibit(
        self,
        parent: Optional[Parent],
        reason: Optional[str],
        flags: InhibitFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def session_inhibit_finish(self, result: Gio.AsyncResult) -> int: ...
    def session_monitor_query_end_response(self) -> None: ...
    def session_monitor_start(
        self,
        parent: Optional[Parent],
        flags: SessionMonitorFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def session_monitor_start_finish(self, result: Gio.AsyncResult) -> bool: ...
    def session_monitor_stop(self) -> None: ...
    def session_uninhibit(self, id: int) -> None: ...
    def set_background_status(
        self,
        status_message: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def set_background_status_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_wallpaper(
        self,
        parent: Optional[Parent],
        uri: str,
        flags: WallpaperFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def set_wallpaper_finish(self, result: Gio.AsyncResult) -> bool: ...
    def spawn(
        self,
        cwd: str,
        argv: Sequence[str],
        fds: Optional[Sequence[int]],
        map_to: Optional[Sequence[int]],
        env: Optional[Sequence[str]],
        flags: SpawnFlags,
        sandbox_expose: Optional[Sequence[str]] = None,
        sandbox_expose_ro: Optional[Sequence[str]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def spawn_finish(self, result: Gio.AsyncResult) -> int: ...
    def spawn_signal(self, pid: int, signal: int, to_process_group: bool) -> None: ...
    def take_screenshot(
        self,
        parent: Optional[Parent],
        flags: ScreenshotFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def take_screenshot_finish(self, result: Gio.AsyncResult) -> Optional[str]: ...
    def trash_file(
        self,
        path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def trash_file_finish(self, result: Gio.AsyncResult) -> bool: ...
    def update_install(
        self,
        parent: Parent,
        flags: UpdateInstallFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def update_install_finish(self, result: Gio.AsyncResult) -> bool: ...
    def update_monitor_start(
        self,
        flags: UpdateMonitorFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def update_monitor_start_finish(self, result: Gio.AsyncResult) -> bool: ...
    def update_monitor_stop(self) -> None: ...

class PortalClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PortalClass()
    """

    parent_class: GObject.ObjectClass = ...

class Session(GObject.Object):
    """
    :Constructors:

    ::

        Session(**properties)

    Object XdpSession

    Signals from XdpSession:
      closed ()

    Signals from GObject:
      notify (GParam)
    """

    def close(self) -> None: ...
    def connect_to_eis(self) -> int: ...
    def get_devices(self) -> DeviceType: ...
    def get_persist_mode(self) -> PersistMode: ...
    def get_restore_token(self) -> Optional[str]: ...
    def get_session_state(self) -> SessionState: ...
    def get_session_type(self) -> SessionType: ...
    def get_streams(self) -> GLib.Variant: ...
    def keyboard_key(self, keysym: bool, key: int, state: KeyState) -> None: ...
    def open_pipewire_remote(self) -> int: ...
    def pointer_axis(self, finish: bool, dx: float, dy: float) -> None: ...
    def pointer_axis_discrete(self, axis: DiscreteAxis, steps: int) -> None: ...
    def pointer_button(self, button: int, state: ButtonState) -> None: ...
    def pointer_motion(self, dx: float, dy: float) -> None: ...
    def pointer_position(self, stream: int, x: float, y: float) -> None: ...
    def start(
        self,
        parent: Optional[Parent] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def start_finish(self, result: Gio.AsyncResult) -> bool: ...
    def touch_down(self, stream: int, slot: int, x: float, y: float) -> None: ...
    def touch_position(self, stream: int, slot: int, x: float, y: float) -> None: ...
    def touch_up(self, slot: int) -> None: ...

class SessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SessionClass()
    """

    parent_class: GObject.ObjectClass = ...

class BackgroundFlags(GObject.GFlags):
    ACTIVATABLE = 2
    AUTOSTART = 1
    NONE = 0

class CursorMode(GObject.GFlags):
    EMBEDDED = 2
    HIDDEN = 1
    METADATA = 4

class DeviceType(GObject.GFlags):
    KEYBOARD = 1
    NONE = 0
    POINTER = 2
    TOUCHSCREEN = 4

class InhibitFlags(GObject.GFlags):
    IDLE = 8
    LOGOUT = 1
    SUSPEND = 4
    USER_SWITCH = 2

class LauncherType(GObject.GFlags):
    APPLICATION = 1
    WEBAPP = 2

class OpenFileFlags(GObject.GFlags):
    MULTIPLE = 1
    NONE = 0

class OpenUriFlags(GObject.GFlags):
    ASK = 1
    NONE = 0
    WRITABLE = 2

class OutputType(GObject.GFlags):
    MONITOR = 1
    NONE = 0
    VIRTUAL = 4
    WINDOW = 2

class RemoteDesktopFlags(GObject.GFlags):
    MULTIPLE = 1
    NONE = 0

class ScreencastFlags(GObject.GFlags):
    MULTIPLE = 1
    NONE = 0

class ScreenshotFlags(GObject.GFlags):
    INTERACTIVE = 1
    NONE = 0

class SpawnFlags(GObject.GFlags):
    CLEARENV = 1
    LATEST = 2
    NONE = 0
    NO_NETWORK = 8
    SANDBOX = 4
    WATCH = 16

class WallpaperFlags(GObject.GFlags):
    BACKGROUND = 1
    LOCKSCREEN = 2
    NONE = 0
    PREVIEW = 4

class ButtonState(GObject.GEnum):
    PRESSED = 1
    RELEASED = 0

class CameraFlags(GObject.GEnum):
    NONE = 0

class DiscreteAxis(GObject.GEnum):
    HORIZONTAL_SCROLL = 0
    VERTICAL_SCROLL = 1

class EmailFlags(GObject.GEnum):
    NONE = 0

class KeyState(GObject.GEnum):
    PRESSED = 1
    RELEASED = 0

class LocationAccuracy(GObject.GEnum):
    CITY = 2
    COUNTRY = 1
    EXACT = 5
    NEIGHBORHOOD = 3
    NONE = 0
    STREET = 4

class LocationMonitorFlags(GObject.GEnum):
    NONE = 0

class LoginSessionState(GObject.GEnum):
    ENDING = 3
    QUERY_END = 2
    RUNNING = 1

class NotificationFlags(GObject.GEnum):
    NONE = 0

class PersistMode(GObject.GEnum):
    NONE = 0
    PERSISTENT = 2
    TRANSIENT = 1

class PrintFlags(GObject.GEnum):
    NONE = 0

class SaveFileFlags(GObject.GEnum):
    NONE = 0

class SessionMonitorFlags(GObject.GEnum):
    NONE = 0

class SessionState(GObject.GEnum):
    ACTIVE = 1
    CLOSED = 2
    INITIAL = 0

class SessionType(GObject.GEnum):
    REMOTE_DESKTOP = 1
    SCREENCAST = 0

class UpdateInstallFlags(GObject.GEnum):
    NONE = 0

class UpdateMonitorFlags(GObject.GEnum):
    NONE = 0

class UpdateStatus(GObject.GEnum):
    DONE = 2
    EMPTY = 1
    FAILED = 3
    RUNNING = 0

class UserInformationFlags(GObject.GEnum):
    NONE = 0
