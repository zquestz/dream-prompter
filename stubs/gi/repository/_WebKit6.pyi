from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import Gdk
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import JavaScriptCore
from gi.repository import Soup

EDITING_COMMAND_COPY: str = "Copy"
EDITING_COMMAND_CREATE_LINK: str = "CreateLink"
EDITING_COMMAND_CUT: str = "Cut"
EDITING_COMMAND_INSERT_IMAGE: str = "InsertImage"
EDITING_COMMAND_PASTE: str = "Paste"
EDITING_COMMAND_PASTE_AS_PLAIN_TEXT: str = "PasteAsPlainText"
EDITING_COMMAND_REDO: str = "Redo"
EDITING_COMMAND_SELECT_ALL: str = "SelectAll"
EDITING_COMMAND_UNDO: str = "Undo"
MAJOR_VERSION: int = 2
MICRO_VERSION: int = 3
MINOR_VERSION: int = 42
_lock = ...  # FIXME Constant
_namespace: str = "WebKit"
_version: str = "6.0"

def download_error_quark() -> int: ...
def favicon_database_error_quark() -> int: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def javascript_error_quark() -> int: ...
def media_error_quark() -> int: ...
def media_key_system_permission_get_name(
    request: MediaKeySystemPermissionRequest,
) -> str: ...
def network_error_quark() -> int: ...
def policy_error_quark() -> int: ...
def print_error_quark() -> int: ...
def snapshot_error_quark() -> int: ...
def uri_for_display(uri: str) -> Optional[str]: ...
def user_content_filter_error_quark() -> int: ...
def user_media_permission_is_for_audio_device(
    request: UserMediaPermissionRequest,
) -> bool: ...
def user_media_permission_is_for_display_device(
    request: UserMediaPermissionRequest,
) -> bool: ...
def user_media_permission_is_for_video_device(
    request: UserMediaPermissionRequest,
) -> bool: ...
def user_message_error_quark() -> int: ...

class ApplicationInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> WebKit.ApplicationInfo
    """

    def get_name(self) -> str: ...
    def get_version(self) -> Tuple[int, int, int]: ...
    @classmethod
    def new(cls) -> ApplicationInfo: ...
    def ref(self) -> ApplicationInfo: ...
    def set_name(self, name: str) -> None: ...
    def set_version(self, major: int, minor: int, micro: int) -> None: ...
    def unref(self) -> None: ...

class AuthenticationRequest(GObject.Object):
    """
    :Constructors:

    ::

        AuthenticationRequest(**properties)

    Object WebKitAuthenticationRequest

    Signals from WebKitAuthenticationRequest:
      cancelled ()
      authenticated (WebKitCredential)

    Signals from GObject:
      notify (GParam)
    """

    def authenticate(self, credential: Optional[Credential] = None) -> None: ...
    def can_save_credentials(self) -> bool: ...
    def cancel(self) -> None: ...
    def get_certificate_pin_flags(self) -> Gio.TlsPasswordFlags: ...
    def get_host(self) -> str: ...
    def get_port(self) -> int: ...
    def get_proposed_credential(self) -> Credential: ...
    def get_realm(self) -> str: ...
    def get_scheme(self) -> AuthenticationScheme: ...
    def get_security_origin(self) -> SecurityOrigin: ...
    def is_for_proxy(self) -> bool: ...
    def is_retry(self) -> bool: ...
    def set_can_save_credentials(self, enabled: bool) -> None: ...
    def set_proposed_credential(self, credential: Credential) -> None: ...

class AuthenticationRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthenticationRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class AutomationSession(GObject.Object):
    """
    :Constructors:

    ::

        AutomationSession(**properties)

    Object WebKitAutomationSession

    Signals from WebKitAutomationSession:
      create-web-view () -> WebKitWebView

    Properties from WebKitAutomationSession:
      id -> gchararray: id

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        id: str

    props: Props = ...
    def __init__(self, id: str = ...): ...
    def get_application_info(self) -> ApplicationInfo: ...
    def get_id(self) -> str: ...
    def set_application_info(self, info: ApplicationInfo) -> None: ...

class AutomationSessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AutomationSessionClass()
    """

    parent_class: GObject.ObjectClass = ...

class BackForwardList(GObject.Object):
    """
    :Constructors:

    ::

        BackForwardList(**properties)

    Object WebKitBackForwardList

    Signals from WebKitBackForwardList:
      changed (WebKitBackForwardListItem, gpointer)

    Signals from GObject:
      notify (GParam)
    """

    def get_back_item(self) -> Optional[BackForwardListItem]: ...
    def get_back_list(self) -> list[BackForwardListItem]: ...
    def get_back_list_with_limit(self, limit: int) -> list[BackForwardListItem]: ...
    def get_current_item(self) -> Optional[BackForwardListItem]: ...
    def get_forward_item(self) -> Optional[BackForwardListItem]: ...
    def get_forward_list(self) -> list[BackForwardListItem]: ...
    def get_forward_list_with_limit(self, limit: int) -> list[BackForwardListItem]: ...
    def get_length(self) -> int: ...
    def get_nth_item(self, index: int) -> Optional[BackForwardListItem]: ...

class BackForwardListClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BackForwardListClass()
    """

    parent_class: GObject.ObjectClass = ...

class BackForwardListItem(GObject.InitiallyUnowned):
    """
    :Constructors:

    ::

        BackForwardListItem(**properties)

    Object WebKitBackForwardListItem

    Signals from GObject:
      notify (GParam)
    """

    def get_original_uri(self) -> str: ...
    def get_title(self) -> str: ...
    def get_uri(self) -> str: ...

class BackForwardListItemClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BackForwardListItemClass()
    """

    parent_class: GObject.InitiallyUnownedClass = ...

class ClipboardPermissionRequest(GObject.Object, PermissionRequest): ...

class ClipboardPermissionRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClipboardPermissionRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class ColorChooserRequest(GObject.Object):
    """
    :Constructors:

    ::

        ColorChooserRequest(**properties)

    Object WebKitColorChooserRequest

    Signals from WebKitColorChooserRequest:
      finished ()

    Properties from WebKitColorChooserRequest:
      rgba -> GdkRGBA: rgba

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        rgba: Gdk.RGBA

    props: Props = ...
    def __init__(self, rgba: Gdk.RGBA = ...): ...
    def cancel(self) -> None: ...
    def finish(self) -> None: ...
    def get_element_rectangle(self) -> Gdk.Rectangle: ...
    def get_rgba(self) -> Gdk.RGBA: ...
    def set_rgba(self, rgba: Gdk.RGBA) -> None: ...

class ColorChooserRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorChooserRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class ContextMenu(GObject.Object):
    """
    :Constructors:

    ::

        ContextMenu(**properties)
        new() -> WebKit.ContextMenu
        new_with_items(items:list) -> WebKit.ContextMenu

    Object WebKitContextMenu

    Signals from GObject:
      notify (GParam)
    """

    def append(self, item: ContextMenuItem) -> None: ...
    def first(self) -> ContextMenuItem: ...
    def get_event(self) -> Gdk.Event: ...
    def get_item_at_position(self, position: int) -> ContextMenuItem: ...
    def get_items(self) -> list[ContextMenuItem]: ...
    def get_n_items(self) -> int: ...
    def get_user_data(self) -> GLib.Variant: ...
    def insert(self, item: ContextMenuItem, position: int) -> None: ...
    def last(self) -> ContextMenuItem: ...
    def move_item(self, item: ContextMenuItem, position: int) -> None: ...
    @classmethod
    def new(cls) -> ContextMenu: ...
    @classmethod
    def new_with_items(cls, items: list[ContextMenuItem]) -> ContextMenu: ...
    def prepend(self, item: ContextMenuItem) -> None: ...
    def remove(self, item: ContextMenuItem) -> None: ...
    def remove_all(self) -> None: ...
    def set_user_data(self, user_data: GLib.Variant) -> None: ...

class ContextMenuClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContextMenuClass()
    """

    parent_class: GObject.ObjectClass = ...

class ContextMenuItem(GObject.InitiallyUnowned):
    """
    :Constructors:

    ::

        ContextMenuItem(**properties)
        new_from_gaction(action:Gio.Action, label:str, target:GLib.Variant=None) -> WebKit.ContextMenuItem
        new_from_stock_action(action:WebKit.ContextMenuAction) -> WebKit.ContextMenuItem
        new_from_stock_action_with_label(action:WebKit.ContextMenuAction, label:str) -> WebKit.ContextMenuItem
        new_separator() -> WebKit.ContextMenuItem
        new_with_submenu(label:str, submenu:WebKit.ContextMenu) -> WebKit.ContextMenuItem

    Object WebKitContextMenuItem

    Signals from GObject:
      notify (GParam)
    """

    def get_gaction(self) -> Gio.Action: ...
    def get_stock_action(self) -> ContextMenuAction: ...
    def get_submenu(self) -> ContextMenu: ...
    def is_separator(self) -> bool: ...
    @classmethod
    def new_from_gaction(
        cls, action: Gio.Action, label: str, target: Optional[GLib.Variant] = None
    ) -> ContextMenuItem: ...
    @classmethod
    def new_from_stock_action(cls, action: ContextMenuAction) -> ContextMenuItem: ...
    @classmethod
    def new_from_stock_action_with_label(
        cls, action: ContextMenuAction, label: str
    ) -> ContextMenuItem: ...
    @classmethod
    def new_separator(cls) -> ContextMenuItem: ...
    @classmethod
    def new_with_submenu(cls, label: str, submenu: ContextMenu) -> ContextMenuItem: ...
    def set_submenu(self, submenu: Optional[ContextMenu] = None) -> None: ...

class ContextMenuItemClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContextMenuItemClass()
    """

    parent_class: GObject.InitiallyUnownedClass = ...

class CookieManager(GObject.Object):
    """
    :Constructors:

    ::

        CookieManager(**properties)

    Object WebKitCookieManager

    Signals from WebKitCookieManager:
      changed ()

    Signals from GObject:
      notify (GParam)
    """

    def add_cookie(
        self,
        cookie: Soup.Cookie,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def add_cookie_finish(self, result: Gio.AsyncResult) -> bool: ...
    def delete_cookie(
        self,
        cookie: Soup.Cookie,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def delete_cookie_finish(self, result: Gio.AsyncResult) -> bool: ...
    def get_accept_policy(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_accept_policy_finish(
        self, result: Gio.AsyncResult
    ) -> CookieAcceptPolicy: ...
    def get_all_cookies(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_all_cookies_finish(self, result: Gio.AsyncResult) -> list[Soup.Cookie]: ...
    def get_cookies(
        self,
        uri: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_cookies_finish(self, result: Gio.AsyncResult) -> list[Soup.Cookie]: ...
    def replace_cookies(
        self,
        cookies: list[Soup.Cookie],
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def replace_cookies_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_accept_policy(self, policy: CookieAcceptPolicy) -> None: ...
    def set_persistent_storage(
        self, filename: str, storage: CookiePersistentStorage
    ) -> None: ...

class CookieManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CookieManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class Credential(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(username:str, password:str, persistence:WebKit.CredentialPersistence) -> WebKit.Credential
        new_for_certificate(certificate:Gio.TlsCertificate=None, persistence:WebKit.CredentialPersistence) -> WebKit.Credential
        new_for_certificate_pin(pin:str, persistence:WebKit.CredentialPersistence) -> WebKit.Credential
    """

    def copy(self) -> Credential: ...
    def free(self) -> None: ...
    def get_certificate(self) -> Gio.TlsCertificate: ...
    def get_password(self) -> str: ...
    def get_persistence(self) -> CredentialPersistence: ...
    def get_username(self) -> str: ...
    def has_password(self) -> bool: ...
    @classmethod
    def new(
        cls, username: str, password: str, persistence: CredentialPersistence
    ) -> Credential: ...
    @classmethod
    def new_for_certificate(
        cls,
        certificate: Optional[Gio.TlsCertificate],
        persistence: CredentialPersistence,
    ) -> Credential: ...
    @classmethod
    def new_for_certificate_pin(
        cls, pin: str, persistence: CredentialPersistence
    ) -> Credential: ...

class DeviceInfoPermissionRequest(GObject.Object, PermissionRequest): ...

class DeviceInfoPermissionRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceInfoPermissionRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class Download(GObject.Object):
    """
    :Constructors:

    ::

        Download(**properties)

    Object WebKitDownload

    Signals from WebKitDownload:
      finished ()
      received-data (guint64)
      failed (GError)
      decide-destination (gchararray) -> gboolean
      created-destination (gchararray)

    Properties from WebKitDownload:
      destination -> gchararray: destination
      response -> WebKitURIResponse: response
      estimated-progress -> gdouble: estimated-progress
      allow-overwrite -> gboolean: allow-overwrite

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        allow_overwrite: bool
        destination: Optional[str]
        estimated_progress: float
        response: URIResponse

    props: Props = ...
    def __init__(self, allow_overwrite: bool = ...): ...
    def cancel(self) -> None: ...
    def get_allow_overwrite(self) -> bool: ...
    def get_destination(self) -> Optional[str]: ...
    def get_elapsed_time(self) -> float: ...
    def get_estimated_progress(self) -> float: ...
    def get_received_data_length(self) -> int: ...
    def get_request(self) -> URIRequest: ...
    def get_response(self) -> URIResponse: ...
    def get_web_view(self) -> WebView: ...
    def set_allow_overwrite(self, allowed: bool) -> None: ...
    def set_destination(self, destination: str) -> None: ...

class DownloadClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DownloadClass()
    """

    parent_class: GObject.ObjectClass = ...

class EditorState(GObject.Object):
    """
    :Constructors:

    ::

        EditorState(**properties)

    Object WebKitEditorState

    Properties from WebKitEditorState:
      typing-attributes -> guint: typing-attributes

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        typing_attributes: int

    props: Props = ...
    def get_typing_attributes(self) -> int: ...
    def is_copy_available(self) -> bool: ...
    def is_cut_available(self) -> bool: ...
    def is_paste_available(self) -> bool: ...
    def is_redo_available(self) -> bool: ...
    def is_undo_available(self) -> bool: ...

class EditorStateClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EditorStateClass()
    """

    parent_class: GObject.ObjectClass = ...

class FaviconDatabase(GObject.Object):
    """
    :Constructors:

    ::

        FaviconDatabase(**properties)

    Object WebKitFaviconDatabase

    Signals from WebKitFaviconDatabase:
      favicon-changed (gchararray, gchararray)

    Signals from GObject:
      notify (GParam)
    """

    def clear(self) -> None: ...
    def get_favicon(
        self,
        page_uri: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_favicon_finish(self, result: Gio.AsyncResult) -> Gdk.Texture: ...
    def get_favicon_uri(self, page_uri: str) -> str: ...

class FaviconDatabaseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FaviconDatabaseClass()
    """

    parent_class: GObject.ObjectClass = ...

class Feature(GObject.GBoxed):
    def get_category(self) -> str: ...
    def get_default_value(self) -> bool: ...
    def get_details(self) -> Optional[str]: ...
    def get_identifier(self) -> str: ...
    def get_name(self) -> Optional[str]: ...
    def get_status(self) -> FeatureStatus: ...
    def ref(self) -> Feature: ...
    def unref(self) -> None: ...

class FeatureList(GObject.GBoxed):
    def get(self, index: int) -> Feature: ...
    def get_length(self) -> int: ...
    def ref(self) -> FeatureList: ...
    def unref(self) -> None: ...

class FileChooserRequest(GObject.Object):
    """
    :Constructors:

    ::

        FileChooserRequest(**properties)

    Object WebKitFileChooserRequest

    Properties from WebKitFileChooserRequest:
      filter -> GtkFileFilter: filter
      mime-types -> GStrv: mime-types
      select-multiple -> gboolean: select-multiple
      selected-files -> GStrv: selected-files

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        filter: Gtk.FileFilter
        mime_types: list[str]
        select_multiple: bool
        selected_files: list[str]

    props: Props = ...
    def cancel(self) -> None: ...
    def get_mime_types(self) -> list[str]: ...
    def get_mime_types_filter(self) -> Gtk.FileFilter: ...
    def get_select_multiple(self) -> bool: ...
    def get_selected_files(self) -> list[str]: ...
    def select_files(self, files: Sequence[str]) -> None: ...

class FileChooserRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileChooserRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class FindController(GObject.Object):
    """
    :Constructors:

    ::

        FindController(**properties)

    Object WebKitFindController

    Signals from WebKitFindController:
      found-text (guint)
      failed-to-find-text ()
      counted-matches (guint)

    Properties from WebKitFindController:
      text -> gchararray: text
      options -> WebKitFindOptions: options
      max-match-count -> guint: max-match-count
      web-view -> WebKitWebView: web-view

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        max_match_count: int
        options: FindOptions
        text: str
        web_view: WebView

    props: Props = ...
    def __init__(self, web_view: WebView = ...): ...
    def count_matches(
        self, search_text: str, find_options: int, max_match_count: int
    ) -> None: ...
    def get_max_match_count(self) -> int: ...
    def get_options(self) -> int: ...
    def get_search_text(self) -> str: ...
    def get_web_view(self) -> WebView: ...
    def search(
        self, search_text: str, find_options: int, max_match_count: int
    ) -> None: ...
    def search_finish(self) -> None: ...
    def search_next(self) -> None: ...
    def search_previous(self) -> None: ...

class FindControllerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FindControllerClass()
    """

    parent_class: GObject.ObjectClass = ...

class FormSubmissionRequest(GObject.Object):
    """
    :Constructors:

    ::

        FormSubmissionRequest(**properties)

    Object WebKitFormSubmissionRequest

    Signals from GObject:
      notify (GParam)
    """

    def list_text_fields(self) -> Tuple[bool, list[str], list[str]]: ...
    def submit(self) -> None: ...

class FormSubmissionRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FormSubmissionRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class GeolocationManager(GObject.Object):
    """
    :Constructors:

    ::

        GeolocationManager(**properties)

    Object WebKitGeolocationManager

    Signals from WebKitGeolocationManager:
      start () -> gboolean
      stop ()

    Properties from WebKitGeolocationManager:
      enable-high-accuracy -> gboolean: enable-high-accuracy

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        enable_high_accuracy: bool

    props: Props = ...
    def failed(self, error_message: str) -> None: ...
    def get_enable_high_accuracy(self) -> bool: ...
    def update_position(self, position: GeolocationPosition) -> None: ...

class GeolocationManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GeolocationManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class GeolocationPermissionRequest(GObject.Object, PermissionRequest): ...

class GeolocationPermissionRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GeolocationPermissionRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class GeolocationPosition(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(latitude:float, longitude:float, accuracy:float) -> WebKit.GeolocationPosition
    """

    def copy(self) -> GeolocationPosition: ...
    def free(self) -> None: ...
    @classmethod
    def new(
        cls, latitude: float, longitude: float, accuracy: float
    ) -> GeolocationPosition: ...
    def set_altitude(self, altitude: float) -> None: ...
    def set_altitude_accuracy(self, altitude_accuracy: float) -> None: ...
    def set_heading(self, heading: float) -> None: ...
    def set_speed(self, speed: float) -> None: ...
    def set_timestamp(self, timestamp: int) -> None: ...

class HitTestResult(GObject.Object):
    """
    :Constructors:

    ::

        HitTestResult(**properties)

    Object WebKitHitTestResult

    Properties from WebKitHitTestResult:
      context -> guint: context
      link-uri -> gchararray: link-uri
      link-title -> gchararray: link-title
      link-label -> gchararray: link-label
      image-uri -> gchararray: image-uri
      media-uri -> gchararray: media-uri

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        context: int
        image_uri: str
        link_label: str
        link_title: str
        link_uri: str
        media_uri: str

    props: Props = ...
    def __init__(
        self,
        context: int = ...,
        image_uri: str = ...,
        link_label: str = ...,
        link_title: str = ...,
        link_uri: str = ...,
        media_uri: str = ...,
    ): ...
    def context_is_editable(self) -> bool: ...
    def context_is_image(self) -> bool: ...
    def context_is_link(self) -> bool: ...
    def context_is_media(self) -> bool: ...
    def context_is_scrollbar(self) -> bool: ...
    def context_is_selection(self) -> bool: ...
    def get_context(self) -> int: ...
    def get_image_uri(self) -> str: ...
    def get_link_label(self) -> str: ...
    def get_link_title(self) -> str: ...
    def get_link_uri(self) -> str: ...
    def get_media_uri(self) -> str: ...

class HitTestResultClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HitTestResultClass()
    """

    parent_class: GObject.ObjectClass = ...

class ITPFirstParty(GObject.GBoxed):
    def get_domain(self) -> str: ...
    def get_last_update_time(self) -> GLib.DateTime: ...
    def get_website_data_access_allowed(self) -> bool: ...
    def ref(self) -> ITPFirstParty: ...
    def unref(self) -> None: ...

class ITPThirdParty(GObject.GBoxed):
    def get_domain(self) -> str: ...
    def get_first_parties(self) -> list[ITPFirstParty]: ...
    def ref(self) -> ITPThirdParty: ...
    def unref(self) -> None: ...

class InputMethodContext(GObject.Object):
    """
    :Constructors:

    ::

        InputMethodContext(**properties)

    Object WebKitInputMethodContext

    Signals from WebKitInputMethodContext:
      preedit-started ()
      preedit-changed ()
      preedit-finished ()
      committed (gchararray)
      delete-surrounding (gint, guint)

    Properties from WebKitInputMethodContext:
      input-purpose -> WebKitInputPurpose: input-purpose
      input-hints -> WebKitInputHints: input-hints

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        input_hints: InputHints
        input_purpose: InputPurpose

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: InputMethodContextPrivate = ...
    def __init__(
        self, input_hints: InputHints = ..., input_purpose: InputPurpose = ...
    ): ...
    def do_committed(self, text: str) -> None: ...
    def do_delete_surrounding(self, offset: int, n_chars: int) -> None: ...
    def do_filter_key_event(self, key_event: Gdk.Event) -> bool: ...
    def do_get_preedit(self) -> Tuple[str, list[InputMethodUnderline], int]: ...
    def do_notify_cursor_area(
        self, x: int, y: int, width: int, height: int
    ) -> None: ...
    def do_notify_focus_in(self) -> None: ...
    def do_notify_focus_out(self) -> None: ...
    def do_notify_surrounding(
        self, text: str, length: int, cursor_index: int, selection_index: int
    ) -> None: ...
    def do_preedit_changed(self) -> None: ...
    def do_preedit_finished(self) -> None: ...
    def do_preedit_started(self) -> None: ...
    def do_reset(self) -> None: ...
    def do_set_enable_preedit(self, enabled: bool) -> None: ...
    def filter_key_event(self, key_event: Gdk.Event) -> bool: ...
    def get_input_hints(self) -> InputHints: ...
    def get_input_purpose(self) -> InputPurpose: ...
    def get_preedit(self) -> Tuple[str, list[InputMethodUnderline], int]: ...
    def notify_cursor_area(self, x: int, y: int, width: int, height: int) -> None: ...
    def notify_focus_in(self) -> None: ...
    def notify_focus_out(self) -> None: ...
    def notify_surrounding(
        self, text: str, length: int, cursor_index: int, selection_index: int
    ) -> None: ...
    def reset(self) -> None: ...
    def set_enable_preedit(self, enabled: bool) -> None: ...
    def set_input_hints(self, hints: InputHints) -> None: ...
    def set_input_purpose(self, purpose: InputPurpose) -> None: ...

class InputMethodContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InputMethodContextClass()
    """

    parent_class: GObject.ObjectClass = ...
    preedit_started: Callable[[InputMethodContext], None] = ...
    preedit_changed: Callable[[InputMethodContext], None] = ...
    preedit_finished: Callable[[InputMethodContext], None] = ...
    committed: Callable[[InputMethodContext, str], None] = ...
    delete_surrounding: Callable[[InputMethodContext, int, int], None] = ...
    set_enable_preedit: Callable[[InputMethodContext, bool], None] = ...
    get_preedit: Callable[
        [InputMethodContext], Tuple[str, list[InputMethodUnderline], int]
    ] = ...
    filter_key_event: Callable[[InputMethodContext, Gdk.Event], bool] = ...
    notify_focus_in: Callable[[InputMethodContext], None] = ...
    notify_focus_out: Callable[[InputMethodContext], None] = ...
    notify_cursor_area: Callable[[InputMethodContext, int, int, int, int], None] = ...
    notify_surrounding: Callable[[InputMethodContext, str, int, int, int], None] = ...
    reset: Callable[[InputMethodContext], None] = ...
    _webkit_reserved0: None = ...
    _webkit_reserved1: None = ...
    _webkit_reserved2: None = ...
    _webkit_reserved3: None = ...
    _webkit_reserved4: None = ...
    _webkit_reserved5: None = ...
    _webkit_reserved6: None = ...
    _webkit_reserved7: None = ...
    _webkit_reserved8: None = ...
    _webkit_reserved9: None = ...
    _webkit_reserved10: None = ...
    _webkit_reserved11: None = ...
    _webkit_reserved12: None = ...
    _webkit_reserved13: None = ...
    _webkit_reserved14: None = ...
    _webkit_reserved15: None = ...

class InputMethodContextPrivate(GObject.GPointer): ...

class InputMethodUnderline(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(start_offset:int, end_offset:int) -> WebKit.InputMethodUnderline
    """

    def copy(self) -> InputMethodUnderline: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls, start_offset: int, end_offset: int) -> InputMethodUnderline: ...
    def set_color(self, rgba: Optional[Gdk.RGBA] = None) -> None: ...

class MediaKeySystemPermissionRequest(GObject.Object, PermissionRequest): ...

class MediaKeySystemPermissionRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MediaKeySystemPermissionRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class MemoryPressureSettings(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> WebKit.MemoryPressureSettings
    """

    def copy(self) -> MemoryPressureSettings: ...
    def free(self) -> None: ...
    def get_conservative_threshold(self) -> float: ...
    def get_kill_threshold(self) -> float: ...
    def get_memory_limit(self) -> int: ...
    def get_poll_interval(self) -> float: ...
    def get_strict_threshold(self) -> float: ...
    @classmethod
    def new(cls) -> MemoryPressureSettings: ...
    def set_conservative_threshold(self, value: float) -> None: ...
    def set_kill_threshold(self, value: float) -> None: ...
    def set_memory_limit(self, memory_limit: int) -> None: ...
    def set_poll_interval(self, value: float) -> None: ...
    def set_strict_threshold(self, value: float) -> None: ...

class NavigationAction(GObject.GBoxed):
    def copy(self) -> NavigationAction: ...
    def free(self) -> None: ...
    def get_frame_name(self) -> Optional[str]: ...
    def get_modifiers(self) -> int: ...
    def get_mouse_button(self) -> int: ...
    def get_navigation_type(self) -> NavigationType: ...
    def get_request(self) -> URIRequest: ...
    def is_redirect(self) -> bool: ...
    def is_user_gesture(self) -> bool: ...

class NavigationPolicyDecision(PolicyDecision):
    """
    :Constructors:

    ::

        NavigationPolicyDecision(**properties)

    Object WebKitNavigationPolicyDecision

    Properties from WebKitNavigationPolicyDecision:
      navigation-action -> WebKitNavigationAction: navigation-action

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        navigation_action: NavigationAction

    props: Props = ...
    def get_navigation_action(self) -> NavigationAction: ...

class NavigationPolicyDecisionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NavigationPolicyDecisionClass()
    """

    parent_class: PolicyDecisionClass = ...

class NetworkProxySettings(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(default_proxy_uri:str=None, ignore_hosts:list=None) -> WebKit.NetworkProxySettings
    """

    def add_proxy_for_scheme(self, scheme: str, proxy_uri: str) -> None: ...
    def copy(self) -> NetworkProxySettings: ...
    def free(self) -> None: ...
    @classmethod
    def new(
        cls,
        default_proxy_uri: Optional[str] = None,
        ignore_hosts: Optional[Sequence[str]] = None,
    ) -> NetworkProxySettings: ...

class NetworkSession(GObject.Object):
    """
    :Constructors:

    ::

        NetworkSession(**properties)
        new(data_directory:str=None, cache_directory:str=None) -> WebKit.NetworkSession
        new_ephemeral() -> WebKit.NetworkSession

    Object WebKitNetworkSession

    Signals from WebKitNetworkSession:
      download-started (WebKitDownload)

    Properties from WebKitNetworkSession:
      data-directory -> gchararray: data-directory
      cache-directory -> gchararray: cache-directory
      is-ephemeral -> gboolean: is-ephemeral

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        is_ephemeral: bool
        cache_directory: str
        data_directory: str

    props: Props = ...
    def __init__(
        self,
        cache_directory: str = ...,
        data_directory: str = ...,
        is_ephemeral: bool = ...,
    ): ...
    def allow_tls_certificate_for_host(
        self, certificate: Gio.TlsCertificate, host: str
    ) -> None: ...
    def download_uri(self, uri: str) -> Download: ...
    def get_cookie_manager(self) -> CookieManager: ...
    @staticmethod
    def get_default() -> NetworkSession: ...
    def get_itp_enabled(self) -> bool: ...
    def get_itp_summary(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_itp_summary_finish(
        self, result: Gio.AsyncResult
    ) -> list[ITPThirdParty]: ...
    def get_persistent_credential_storage_enabled(self) -> bool: ...
    def get_tls_errors_policy(self) -> TLSErrorsPolicy: ...
    def get_website_data_manager(self) -> WebsiteDataManager: ...
    def is_ephemeral(self) -> bool: ...
    @classmethod
    def new(
        cls, data_directory: Optional[str] = None, cache_directory: Optional[str] = None
    ) -> NetworkSession: ...
    @classmethod
    def new_ephemeral(cls) -> NetworkSession: ...
    def prefetch_dns(self, hostname: str) -> None: ...
    def set_itp_enabled(self, enabled: bool) -> None: ...
    @staticmethod
    def set_memory_pressure_settings(settings: MemoryPressureSettings) -> None: ...
    def set_persistent_credential_storage_enabled(self, enabled: bool) -> None: ...
    def set_proxy_settings(
        self,
        proxy_mode: NetworkProxyMode,
        proxy_settings: Optional[NetworkProxySettings] = None,
    ) -> None: ...
    def set_tls_errors_policy(self, policy: TLSErrorsPolicy) -> None: ...

class NetworkSessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NetworkSessionClass()
    """

    parent_class: GObject.ObjectClass = ...

class Notification(GObject.Object):
    """
    :Constructors:

    ::

        Notification(**properties)

    Object WebKitNotification

    Signals from WebKitNotification:
      closed ()
      clicked ()

    Properties from WebKitNotification:
      id -> guint64: id
      title -> gchararray: title
      body -> gchararray: body
      tag -> gchararray: tag

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        body: str
        id: int
        tag: Optional[str]
        title: str

    props: Props = ...
    def clicked(self) -> None: ...
    def close(self) -> None: ...
    def get_body(self) -> str: ...
    def get_id(self) -> int: ...
    def get_tag(self) -> Optional[str]: ...
    def get_title(self) -> str: ...

class NotificationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NotificationClass()
    """

    parent_class: GObject.ObjectClass = ...

class NotificationPermissionRequest(GObject.Object, PermissionRequest): ...

class NotificationPermissionRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NotificationPermissionRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class OptionMenu(GObject.Object):
    """
    :Constructors:

    ::

        OptionMenu(**properties)

    Object WebKitOptionMenu

    Signals from WebKitOptionMenu:
      close ()

    Signals from GObject:
      notify (GParam)
    """

    def activate_item(self, index: int) -> None: ...
    def close(self) -> None: ...
    def get_event(self) -> Gdk.Event: ...
    def get_item(self, index: int) -> OptionMenuItem: ...
    def get_n_items(self) -> int: ...
    def select_item(self, index: int) -> None: ...

class OptionMenuClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OptionMenuClass()
    """

    parent_class: GObject.ObjectClass = ...

class OptionMenuItem(GObject.GBoxed):
    def copy(self) -> OptionMenuItem: ...
    def free(self) -> None: ...
    def get_label(self) -> str: ...
    def get_tooltip(self) -> str: ...
    def is_enabled(self) -> bool: ...
    def is_group_child(self) -> bool: ...
    def is_group_label(self) -> bool: ...
    def is_selected(self) -> bool: ...

class PermissionRequest(GObject.GInterface):
    """
    Interface WebKitPermissionRequest

    Signals from GObject:
      notify (GParam)
    """

    def allow(self) -> None: ...
    def deny(self) -> None: ...

class PermissionRequestInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        PermissionRequestInterface()
    """

    parent_interface: GObject.TypeInterface = ...
    allow: Callable[[PermissionRequest], None] = ...
    deny: Callable[[PermissionRequest], None] = ...

class PermissionStateQuery(GObject.GBoxed):
    def finish(self, state: PermissionState) -> None: ...
    def get_name(self) -> str: ...
    def get_security_origin(self) -> SecurityOrigin: ...
    def ref(self) -> PermissionStateQuery: ...
    def unref(self) -> None: ...

class PointerLockPermissionRequest(GObject.Object, PermissionRequest): ...

class PointerLockPermissionRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PointerLockPermissionRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class PolicyDecision(GObject.Object):
    """
    :Constructors:

    ::

        PolicyDecision(**properties)

    Object WebKitPolicyDecision

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: PolicyDecisionPrivate = ...
    def download(self) -> None: ...
    def ignore(self) -> None: ...
    def use(self) -> None: ...
    def use_with_policies(self, policies: WebsitePolicies) -> None: ...

class PolicyDecisionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PolicyDecisionClass()
    """

    parent_class: GObject.ObjectClass = ...
    _webkit_reserved0: None = ...
    _webkit_reserved1: None = ...
    _webkit_reserved2: None = ...
    _webkit_reserved3: None = ...
    _webkit_reserved4: None = ...
    _webkit_reserved5: None = ...
    _webkit_reserved6: None = ...
    _webkit_reserved7: None = ...

class PolicyDecisionPrivate(GObject.GPointer): ...

class PrintOperation(GObject.Object):
    """
    :Constructors:

    ::

        PrintOperation(**properties)
        new(web_view:WebKit.WebView) -> WebKit.PrintOperation

    Object WebKitPrintOperation

    Signals from WebKitPrintOperation:
      finished ()
      failed (GError)

    Properties from WebKitPrintOperation:
      web-view -> WebKitWebView: web-view
      print-settings -> GtkPrintSettings: print-settings
      page-setup -> GtkPageSetup: page-setup

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        page_setup: Gtk.PageSetup
        print_settings: Gtk.PrintSettings
        web_view: WebView

    props: Props = ...
    def __init__(
        self,
        page_setup: Gtk.PageSetup = ...,
        print_settings: Gtk.PrintSettings = ...,
        web_view: WebView = ...,
    ): ...
    def get_page_setup(self) -> Gtk.PageSetup: ...
    def get_print_settings(self) -> Gtk.PrintSettings: ...
    @classmethod
    def new(cls, web_view: WebView) -> PrintOperation: ...
    def print_(self) -> None: ...
    def run_dialog(
        self, parent: Optional[Gtk.Window] = None
    ) -> PrintOperationResponse: ...
    def set_page_setup(self, page_setup: Gtk.PageSetup) -> None: ...
    def set_print_settings(self, print_settings: Gtk.PrintSettings) -> None: ...

class PrintOperationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PrintOperationClass()
    """

    parent_class: GObject.ObjectClass = ...

class ResponsePolicyDecision(PolicyDecision):
    """
    :Constructors:

    ::

        ResponsePolicyDecision(**properties)

    Object WebKitResponsePolicyDecision

    Properties from WebKitResponsePolicyDecision:
      request -> WebKitURIRequest: request
      response -> WebKitURIResponse: response

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        request: URIRequest
        response: URIResponse

    props: Props = ...
    def get_request(self) -> URIRequest: ...
    def get_response(self) -> URIResponse: ...
    def is_main_frame_main_resource(self) -> bool: ...
    def is_mime_type_supported(self) -> bool: ...

class ResponsePolicyDecisionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ResponsePolicyDecisionClass()
    """

    parent_class: PolicyDecisionClass = ...

class ScriptDialog(GObject.GBoxed):
    def close(self) -> None: ...
    def confirm_set_confirmed(self, confirmed: bool) -> None: ...
    def get_dialog_type(self) -> ScriptDialogType: ...
    def get_message(self) -> str: ...
    def prompt_get_default_text(self) -> str: ...
    def prompt_set_text(self, text: str) -> None: ...
    def ref(self) -> ScriptDialog: ...
    def unref(self) -> None: ...

class ScriptMessageReply(GObject.GBoxed):
    def ref(self) -> ScriptMessageReply: ...
    def return_error_message(self, error_message: str) -> None: ...
    def return_value(self, reply_value: JavaScriptCore.Value) -> None: ...
    def unref(self) -> None: ...

class SecurityManager(GObject.Object):
    """
    :Constructors:

    ::

        SecurityManager(**properties)

    Object WebKitSecurityManager

    Signals from GObject:
      notify (GParam)
    """

    def register_uri_scheme_as_cors_enabled(self, scheme: str) -> None: ...
    def register_uri_scheme_as_display_isolated(self, scheme: str) -> None: ...
    def register_uri_scheme_as_empty_document(self, scheme: str) -> None: ...
    def register_uri_scheme_as_local(self, scheme: str) -> None: ...
    def register_uri_scheme_as_no_access(self, scheme: str) -> None: ...
    def register_uri_scheme_as_secure(self, scheme: str) -> None: ...
    def uri_scheme_is_cors_enabled(self, scheme: str) -> bool: ...
    def uri_scheme_is_display_isolated(self, scheme: str) -> bool: ...
    def uri_scheme_is_empty_document(self, scheme: str) -> bool: ...
    def uri_scheme_is_local(self, scheme: str) -> bool: ...
    def uri_scheme_is_no_access(self, scheme: str) -> bool: ...
    def uri_scheme_is_secure(self, scheme: str) -> bool: ...

class SecurityManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SecurityManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class SecurityOrigin(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(protocol:str, host:str, port:int) -> WebKit.SecurityOrigin
        new_for_uri(uri:str) -> WebKit.SecurityOrigin
    """

    def get_host(self) -> Optional[str]: ...
    def get_port(self) -> int: ...
    def get_protocol(self) -> Optional[str]: ...
    @classmethod
    def new(cls, protocol: str, host: str, port: int) -> SecurityOrigin: ...
    @classmethod
    def new_for_uri(cls, uri: str) -> SecurityOrigin: ...
    def ref(self) -> SecurityOrigin: ...
    def to_string(self) -> Optional[str]: ...
    def unref(self) -> None: ...

class Settings(GObject.Object):
    """
    :Constructors:

    ::

        Settings(**properties)
        new() -> WebKit.Settings

    Object WebKitSettings

    Properties from WebKitSettings:
      enable-javascript -> gboolean: Enable JavaScript
        Enable JavaScript.
      auto-load-images -> gboolean: Auto load images
        Load images automatically.
      load-icons-ignoring-image-load-setting -> gboolean: Load icons ignoring image load setting
        Whether to load site icons ignoring image load setting.
      enable-offline-web-application-cache -> gboolean: Enable offline web application cache
        Whether to enable offline web application cache.
      enable-html5-local-storage -> gboolean: Enable HTML5 local storage
        Whether to enable HTML5 Local Storage support.
      enable-html5-database -> gboolean: Enable HTML5 database
        Whether to enable HTML5 database support.
      javascript-can-open-windows-automatically -> gboolean: JavaScript can open windows automatically
        Whether JavaScript can open windows automatically.
      enable-hyperlink-auditing -> gboolean: Enable hyperlink auditing
        Whether <a ping> should be able to send pings.
      default-font-family -> gchararray: Default font family
        The font family to use as the default for content that does not specify a font.
      monospace-font-family -> gchararray: Monospace font family
        The font family used as the default for content using monospace font.
      serif-font-family -> gchararray: Serif font family
        The font family used as the default for content using serif font.
      sans-serif-font-family -> gchararray: Sans-serif font family
        The font family used as the default for content using sans-serif font.
      cursive-font-family -> gchararray: Cursive font family
        The font family used as the default for content using cursive font.
      fantasy-font-family -> gchararray: Fantasy font family
        The font family used as the default for content using fantasy font.
      pictograph-font-family -> gchararray: Pictograph font family
        The font family used as the default for content using pictograph font.
      default-font-size -> guint: Default font size
        The default font size used to display text.
      default-monospace-font-size -> guint: Default monospace font size
        The default font size used to display monospace text.
      minimum-font-size -> guint: Minimum font size
        The minimum font size used to display text.
      default-charset -> gchararray: Default charset
        The default text charset used when interpreting content with unspecified charset.
      enable-developer-extras -> gboolean: Enable developer extras
        Whether to enable developer extras
      enable-resizable-text-areas -> gboolean: Enable resizable text areas
        Whether to enable resizable text areas
      enable-tabs-to-links -> gboolean: Enable tabs to links
        Whether to enable tabs to links
      enable-dns-prefetching -> gboolean: Enable DNS prefetching
        Whether to enable DNS prefetching
      enable-caret-browsing -> gboolean: Enable Caret Browsing
        Whether to enable accessibility enhanced keyboard navigation
      enable-fullscreen -> gboolean: Enable Fullscreen
        Whether to enable the Javascript Fullscreen API
      print-backgrounds -> gboolean: Print Backgrounds
        Whether background images should be drawn during printing
      enable-webaudio -> gboolean: Enable WebAudio
        Whether WebAudio content should be handled
      enable-webgl -> gboolean: Enable WebGL
        Whether WebGL content should be rendered
      allow-modal-dialogs -> gboolean: Allow modal dialogs
        Whether it is possible to create modal dialogs
      zoom-text-only -> gboolean: Zoom Text Only
        Whether zoom level of web view changes only the text size
      javascript-can-access-clipboard -> gboolean: JavaScript can access clipboard
        Whether JavaScript can access Clipboard
      media-playback-requires-user-gesture -> gboolean: Media playback requires user gesture
        Whether media playback requires user gesture
      media-playback-allows-inline -> gboolean: Media playback allows inline
        Whether media playback allows inline
      draw-compositing-indicators -> gboolean: Draw compositing indicators
        Whether to draw compositing borders and repaint counters
      enable-site-specific-quirks -> gboolean: Enable Site Specific Quirks
        Enables the site-specific compatibility workarounds
      enable-page-cache -> gboolean: Enable page cache
        Whether the page cache should be used
      user-agent -> gchararray: User agent string
        The user agent string
      enable-smooth-scrolling -> gboolean: Enable smooth scrolling
        Whether to enable smooth scrolling
      enable-write-console-messages-to-stdout -> gboolean: Write console messages on stdout
        Whether to write console messages on stdout
      enable-media-stream -> gboolean: Enable MediaStream
        Whether MediaStream content should be handled
      enable-mock-capture-devices -> gboolean: Enable mock capture devices
        Whether we expose mock capture devices or not
      enable-spatial-navigation -> gboolean: Enable Spatial Navigation
        Whether to enable Spatial Navigation support.
      enable-mediasource -> gboolean: Enable MediaSource
        Whether MediaSource should be enabled.
      enable-encrypted-media -> gboolean: Enable EncryptedMedia
        Whether EncryptedMedia should be enabled.
      enable-media-capabilities -> gboolean: Enable MediaCapabilities
        Whether MediaCapabilities should be enabled.
      allow-file-access-from-file-urls -> gboolean: Allow file access from file URLs
        Whether file access is allowed from file URLs.
      allow-universal-access-from-file-urls -> gboolean: Allow universal access from the context of file scheme URLs
        Whether or not universal access is allowed from the context of file scheme URLs
      allow-top-navigation-to-data-urls -> gboolean: Allow top frame navigation to data URLs
        Whether or not top frame navigation is allowed to data URLs
      hardware-acceleration-policy -> WebKitHardwareAccelerationPolicy: Hardware Acceleration Policy
        The policy to decide how to enable and disable hardware acceleration
      enable-back-forward-navigation-gestures -> gboolean: Enable back-forward navigation gestures
        Whether horizontal swipe gesture will trigger back-forward navigation
      enable-javascript-markup -> gboolean: Enable JavaScript Markup
        Enable JavaScript in document markup.
      enable-media -> gboolean: Enable media
        Whether media content should be handled
      media-content-types-requiring-hardware-support -> gchararray: Media content types requiring hardware support
        List of media content types requiring hardware support.
      enable-webrtc -> gboolean: Enable WebRTC
        Whether WebRTC content should be handled
      disable-web-security -> gboolean: Disable web security
        Whether web security should be disabled.

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        allow_file_access_from_file_urls: bool
        allow_modal_dialogs: bool
        allow_top_navigation_to_data_urls: bool
        allow_universal_access_from_file_urls: bool
        auto_load_images: bool
        cursive_font_family: str
        default_charset: str
        default_font_family: str
        default_font_size: int
        default_monospace_font_size: int
        disable_web_security: bool
        draw_compositing_indicators: bool
        enable_back_forward_navigation_gestures: bool
        enable_caret_browsing: bool
        enable_developer_extras: bool
        enable_dns_prefetching: bool
        enable_encrypted_media: bool
        enable_fullscreen: bool
        enable_html5_database: bool
        enable_html5_local_storage: bool
        enable_hyperlink_auditing: bool
        enable_javascript: bool
        enable_javascript_markup: bool
        enable_media: bool
        enable_media_capabilities: bool
        enable_media_stream: bool
        enable_mediasource: bool
        enable_mock_capture_devices: bool
        enable_offline_web_application_cache: bool
        enable_page_cache: bool
        enable_resizable_text_areas: bool
        enable_site_specific_quirks: bool
        enable_smooth_scrolling: bool
        enable_spatial_navigation: bool
        enable_tabs_to_links: bool
        enable_webaudio: bool
        enable_webgl: bool
        enable_webrtc: bool
        enable_write_console_messages_to_stdout: bool
        fantasy_font_family: str
        hardware_acceleration_policy: HardwareAccelerationPolicy
        javascript_can_access_clipboard: bool
        javascript_can_open_windows_automatically: bool
        load_icons_ignoring_image_load_setting: bool
        media_content_types_requiring_hardware_support: str
        media_playback_allows_inline: bool
        media_playback_requires_user_gesture: bool
        minimum_font_size: int
        monospace_font_family: str
        pictograph_font_family: str
        print_backgrounds: bool
        sans_serif_font_family: str
        serif_font_family: str
        user_agent: str
        zoom_text_only: bool

    props: Props = ...
    def __init__(
        self,
        allow_file_access_from_file_urls: bool = ...,
        allow_modal_dialogs: bool = ...,
        allow_top_navigation_to_data_urls: bool = ...,
        allow_universal_access_from_file_urls: bool = ...,
        auto_load_images: bool = ...,
        cursive_font_family: str = ...,
        default_charset: str = ...,
        default_font_family: str = ...,
        default_font_size: int = ...,
        default_monospace_font_size: int = ...,
        disable_web_security: bool = ...,
        draw_compositing_indicators: bool = ...,
        enable_back_forward_navigation_gestures: bool = ...,
        enable_caret_browsing: bool = ...,
        enable_developer_extras: bool = ...,
        enable_dns_prefetching: bool = ...,
        enable_encrypted_media: bool = ...,
        enable_fullscreen: bool = ...,
        enable_html5_database: bool = ...,
        enable_html5_local_storage: bool = ...,
        enable_hyperlink_auditing: bool = ...,
        enable_javascript: bool = ...,
        enable_javascript_markup: bool = ...,
        enable_media: bool = ...,
        enable_media_capabilities: bool = ...,
        enable_media_stream: bool = ...,
        enable_mediasource: bool = ...,
        enable_mock_capture_devices: bool = ...,
        enable_offline_web_application_cache: bool = ...,
        enable_page_cache: bool = ...,
        enable_resizable_text_areas: bool = ...,
        enable_site_specific_quirks: bool = ...,
        enable_smooth_scrolling: bool = ...,
        enable_spatial_navigation: bool = ...,
        enable_tabs_to_links: bool = ...,
        enable_webaudio: bool = ...,
        enable_webgl: bool = ...,
        enable_webrtc: bool = ...,
        enable_write_console_messages_to_stdout: bool = ...,
        fantasy_font_family: str = ...,
        hardware_acceleration_policy: HardwareAccelerationPolicy = ...,
        javascript_can_access_clipboard: bool = ...,
        javascript_can_open_windows_automatically: bool = ...,
        load_icons_ignoring_image_load_setting: bool = ...,
        media_content_types_requiring_hardware_support: Optional[str] = ...,
        media_playback_allows_inline: bool = ...,
        media_playback_requires_user_gesture: bool = ...,
        minimum_font_size: int = ...,
        monospace_font_family: str = ...,
        pictograph_font_family: str = ...,
        print_backgrounds: bool = ...,
        sans_serif_font_family: str = ...,
        serif_font_family: str = ...,
        user_agent: Optional[str] = ...,
        zoom_text_only: bool = ...,
    ): ...
    @staticmethod
    def font_size_to_pixels(points: int) -> int: ...
    @staticmethod
    def font_size_to_points(pixels: int) -> int: ...
    @staticmethod
    def get_all_features() -> FeatureList: ...
    def get_allow_file_access_from_file_urls(self) -> bool: ...
    def get_allow_modal_dialogs(self) -> bool: ...
    def get_allow_top_navigation_to_data_urls(self) -> bool: ...
    def get_allow_universal_access_from_file_urls(self) -> bool: ...
    def get_auto_load_images(self) -> bool: ...
    def get_cursive_font_family(self) -> str: ...
    def get_default_charset(self) -> str: ...
    def get_default_font_family(self) -> str: ...
    def get_default_font_size(self) -> int: ...
    def get_default_monospace_font_size(self) -> int: ...
    @staticmethod
    def get_development_features() -> FeatureList: ...
    def get_disable_web_security(self) -> bool: ...
    def get_draw_compositing_indicators(self) -> bool: ...
    def get_enable_back_forward_navigation_gestures(self) -> bool: ...
    def get_enable_caret_browsing(self) -> bool: ...
    def get_enable_developer_extras(self) -> bool: ...
    def get_enable_dns_prefetching(self) -> bool: ...
    def get_enable_encrypted_media(self) -> bool: ...
    def get_enable_fullscreen(self) -> bool: ...
    def get_enable_html5_database(self) -> bool: ...
    def get_enable_html5_local_storage(self) -> bool: ...
    def get_enable_hyperlink_auditing(self) -> bool: ...
    def get_enable_javascript(self) -> bool: ...
    def get_enable_javascript_markup(self) -> bool: ...
    def get_enable_media(self) -> bool: ...
    def get_enable_media_capabilities(self) -> bool: ...
    def get_enable_media_stream(self) -> bool: ...
    def get_enable_mediasource(self) -> bool: ...
    def get_enable_mock_capture_devices(self) -> bool: ...
    def get_enable_offline_web_application_cache(self) -> bool: ...
    def get_enable_page_cache(self) -> bool: ...
    def get_enable_resizable_text_areas(self) -> bool: ...
    def get_enable_site_specific_quirks(self) -> bool: ...
    def get_enable_smooth_scrolling(self) -> bool: ...
    def get_enable_spatial_navigation(self) -> bool: ...
    def get_enable_tabs_to_links(self) -> bool: ...
    def get_enable_webaudio(self) -> bool: ...
    def get_enable_webgl(self) -> bool: ...
    def get_enable_webrtc(self) -> bool: ...
    def get_enable_write_console_messages_to_stdout(self) -> bool: ...
    @staticmethod
    def get_experimental_features() -> FeatureList: ...
    def get_fantasy_font_family(self) -> str: ...
    def get_feature_enabled(self, feature: Feature) -> bool: ...
    def get_hardware_acceleration_policy(self) -> HardwareAccelerationPolicy: ...
    def get_javascript_can_access_clipboard(self) -> bool: ...
    def get_javascript_can_open_windows_automatically(self) -> bool: ...
    def get_load_icons_ignoring_image_load_setting(self) -> bool: ...
    def get_media_content_types_requiring_hardware_support(self) -> str: ...
    def get_media_playback_allows_inline(self) -> bool: ...
    def get_media_playback_requires_user_gesture(self) -> bool: ...
    def get_minimum_font_size(self) -> int: ...
    def get_monospace_font_family(self) -> str: ...
    def get_pictograph_font_family(self) -> str: ...
    def get_print_backgrounds(self) -> bool: ...
    def get_sans_serif_font_family(self) -> str: ...
    def get_serif_font_family(self) -> str: ...
    def get_user_agent(self) -> str: ...
    def get_zoom_text_only(self) -> bool: ...
    @classmethod
    def new(cls) -> Settings: ...
    def set_allow_file_access_from_file_urls(self, allowed: bool) -> None: ...
    def set_allow_modal_dialogs(self, allowed: bool) -> None: ...
    def set_allow_top_navigation_to_data_urls(self, allowed: bool) -> None: ...
    def set_allow_universal_access_from_file_urls(self, allowed: bool) -> None: ...
    def set_auto_load_images(self, enabled: bool) -> None: ...
    def set_cursive_font_family(self, cursive_font_family: str) -> None: ...
    def set_default_charset(self, default_charset: str) -> None: ...
    def set_default_font_family(self, default_font_family: str) -> None: ...
    def set_default_font_size(self, font_size: int) -> None: ...
    def set_default_monospace_font_size(self, font_size: int) -> None: ...
    def set_disable_web_security(self, disabled: bool) -> None: ...
    def set_draw_compositing_indicators(self, enabled: bool) -> None: ...
    def set_enable_back_forward_navigation_gestures(self, enabled: bool) -> None: ...
    def set_enable_caret_browsing(self, enabled: bool) -> None: ...
    def set_enable_developer_extras(self, enabled: bool) -> None: ...
    def set_enable_dns_prefetching(self, enabled: bool) -> None: ...
    def set_enable_encrypted_media(self, enabled: bool) -> None: ...
    def set_enable_fullscreen(self, enabled: bool) -> None: ...
    def set_enable_html5_database(self, enabled: bool) -> None: ...
    def set_enable_html5_local_storage(self, enabled: bool) -> None: ...
    def set_enable_hyperlink_auditing(self, enabled: bool) -> None: ...
    def set_enable_javascript(self, enabled: bool) -> None: ...
    def set_enable_javascript_markup(self, enabled: bool) -> None: ...
    def set_enable_media(self, enabled: bool) -> None: ...
    def set_enable_media_capabilities(self, enabled: bool) -> None: ...
    def set_enable_media_stream(self, enabled: bool) -> None: ...
    def set_enable_mediasource(self, enabled: bool) -> None: ...
    def set_enable_mock_capture_devices(self, enabled: bool) -> None: ...
    def set_enable_offline_web_application_cache(self, enabled: bool) -> None: ...
    def set_enable_page_cache(self, enabled: bool) -> None: ...
    def set_enable_resizable_text_areas(self, enabled: bool) -> None: ...
    def set_enable_site_specific_quirks(self, enabled: bool) -> None: ...
    def set_enable_smooth_scrolling(self, enabled: bool) -> None: ...
    def set_enable_spatial_navigation(self, enabled: bool) -> None: ...
    def set_enable_tabs_to_links(self, enabled: bool) -> None: ...
    def set_enable_webaudio(self, enabled: bool) -> None: ...
    def set_enable_webgl(self, enabled: bool) -> None: ...
    def set_enable_webrtc(self, enabled: bool) -> None: ...
    def set_enable_write_console_messages_to_stdout(self, enabled: bool) -> None: ...
    def set_fantasy_font_family(self, fantasy_font_family: str) -> None: ...
    def set_feature_enabled(self, feature: Feature, enabled: bool) -> None: ...
    def set_hardware_acceleration_policy(
        self, policy: HardwareAccelerationPolicy
    ) -> None: ...
    def set_javascript_can_access_clipboard(self, enabled: bool) -> None: ...
    def set_javascript_can_open_windows_automatically(self, enabled: bool) -> None: ...
    def set_load_icons_ignoring_image_load_setting(self, enabled: bool) -> None: ...
    def set_media_content_types_requiring_hardware_support(
        self, content_types: Optional[str] = None
    ) -> None: ...
    def set_media_playback_allows_inline(self, enabled: bool) -> None: ...
    def set_media_playback_requires_user_gesture(self, enabled: bool) -> None: ...
    def set_minimum_font_size(self, font_size: int) -> None: ...
    def set_monospace_font_family(self, monospace_font_family: str) -> None: ...
    def set_pictograph_font_family(self, pictograph_font_family: str) -> None: ...
    def set_print_backgrounds(self, print_backgrounds: bool) -> None: ...
    def set_sans_serif_font_family(self, sans_serif_font_family: str) -> None: ...
    def set_serif_font_family(self, serif_font_family: str) -> None: ...
    def set_user_agent(self, user_agent: Optional[str] = None) -> None: ...
    def set_user_agent_with_application_details(
        self,
        application_name: Optional[str] = None,
        application_version: Optional[str] = None,
    ) -> None: ...
    def set_zoom_text_only(self, zoom_text_only: bool) -> None: ...

class SettingsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SettingsClass()
    """

    parent_class: GObject.ObjectClass = ...

class URIRequest(GObject.Object):
    """
    :Constructors:

    ::

        URIRequest(**properties)
        new(uri:str) -> WebKit.URIRequest

    Object WebKitURIRequest

    Properties from WebKitURIRequest:
      uri -> gchararray: uri

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        uri: str

    props: Props = ...
    def __init__(self, uri: str = ...): ...
    def get_http_headers(self) -> Soup.MessageHeaders: ...
    def get_http_method(self) -> str: ...
    def get_uri(self) -> str: ...
    @classmethod
    def new(cls, uri: str) -> URIRequest: ...
    def set_uri(self, uri: str) -> None: ...

class URIRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        URIRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class URIResponse(GObject.Object):
    """
    :Constructors:

    ::

        URIResponse(**properties)

    Object WebKitURIResponse

    Properties from WebKitURIResponse:
      uri -> gchararray: uri
      status-code -> guint: status-code
      content-length -> guint64: content-length
      mime-type -> gchararray: mime-type
      suggested-filename -> gchararray: suggested-filename
      http-headers -> SoupMessageHeaders: http-headers

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        content_length: int
        http_headers: Soup.MessageHeaders
        mime_type: str
        status_code: int
        suggested_filename: str
        uri: str

    props: Props = ...
    def get_content_length(self) -> int: ...
    def get_http_headers(self) -> Soup.MessageHeaders: ...
    def get_mime_type(self) -> str: ...
    def get_status_code(self) -> int: ...
    def get_suggested_filename(self) -> str: ...
    def get_uri(self) -> str: ...

class URIResponseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        URIResponseClass()
    """

    parent_class: GObject.ObjectClass = ...

class URISchemeRequest(GObject.Object):
    """
    :Constructors:

    ::

        URISchemeRequest(**properties)

    Object WebKitURISchemeRequest

    Signals from GObject:
      notify (GParam)
    """

    def finish(
        self,
        stream: Gio.InputStream,
        stream_length: int,
        content_type: Optional[str] = None,
    ) -> None: ...
    def finish_error(self, error: GLib.Error) -> None: ...
    def finish_with_response(self, response: URISchemeResponse) -> None: ...
    def get_http_body(self) -> Gio.InputStream: ...
    def get_http_headers(self) -> Soup.MessageHeaders: ...
    def get_http_method(self) -> str: ...
    def get_path(self) -> str: ...
    def get_scheme(self) -> str: ...
    def get_uri(self) -> str: ...
    def get_web_view(self) -> WebView: ...

class URISchemeRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        URISchemeRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class URISchemeResponse(GObject.Object):
    """
    :Constructors:

    ::

        URISchemeResponse(**properties)
        new(input_stream:Gio.InputStream, stream_length:int) -> WebKit.URISchemeResponse

    Object WebKitURISchemeResponse

    Properties from WebKitURISchemeResponse:
      stream -> GInputStream: stream
      stream-length -> gint64: stream-length

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        stream: Gio.InputStream
        stream_length: int

    props: Props = ...
    def __init__(self, stream: Gio.InputStream = ..., stream_length: int = ...): ...
    @classmethod
    def new(
        cls, input_stream: Gio.InputStream, stream_length: int
    ) -> URISchemeResponse: ...
    def set_content_type(self, content_type: str) -> None: ...
    def set_http_headers(self, headers: Soup.MessageHeaders) -> None: ...
    def set_status(
        self, status_code: int, reason_phrase: Optional[str] = None
    ) -> None: ...

class URISchemeResponseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        URISchemeResponseClass()
    """

    parent_class: GObject.ObjectClass = ...

class UserContentFilter(GObject.GBoxed):
    def get_identifier(self) -> str: ...
    def ref(self) -> UserContentFilter: ...
    def unref(self) -> None: ...

class UserContentFilterStore(GObject.Object):
    """
    :Constructors:

    ::

        UserContentFilterStore(**properties)
        new(storage_path:str) -> WebKit.UserContentFilterStore

    Object WebKitUserContentFilterStore

    Properties from WebKitUserContentFilterStore:
      path -> gchararray: path

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        path: str

    props: Props = ...
    def __init__(self, path: str = ...): ...
    def fetch_identifiers(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def fetch_identifiers_finish(self, result: Gio.AsyncResult) -> list[str]: ...
    def get_path(self) -> str: ...
    def load(
        self,
        identifier: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def load_finish(self, result: Gio.AsyncResult) -> UserContentFilter: ...
    @classmethod
    def new(cls, storage_path: str) -> UserContentFilterStore: ...
    def remove(
        self,
        identifier: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def remove_finish(self, result: Gio.AsyncResult) -> bool: ...
    def save(
        self,
        identifier: str,
        source: GLib.Bytes,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def save_finish(self, result: Gio.AsyncResult) -> UserContentFilter: ...
    def save_from_file(
        self,
        identifier: str,
        file: Gio.File,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def save_from_file_finish(self, result: Gio.AsyncResult) -> UserContentFilter: ...

class UserContentFilterStoreClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UserContentFilterStoreClass()
    """

    parent_class: GObject.ObjectClass = ...

class UserContentManager(GObject.Object):
    """
    :Constructors:

    ::

        UserContentManager(**properties)
        new() -> WebKit.UserContentManager

    Object WebKitUserContentManager

    Signals from WebKitUserContentManager:
      script-message-received (JSCValue)
      script-message-with-reply-received (JSCValue, WebKitScriptMessageReply) -> gboolean

    Signals from GObject:
      notify (GParam)
    """

    def add_filter(self, filter: UserContentFilter) -> None: ...
    def add_script(self, script: UserScript) -> None: ...
    def add_style_sheet(self, stylesheet: UserStyleSheet) -> None: ...
    @classmethod
    def new(cls) -> UserContentManager: ...
    def register_script_message_handler(
        self, name: str, world_name: Optional[str] = None
    ) -> bool: ...
    def register_script_message_handler_with_reply(
        self, name: str, world_name: str
    ) -> bool: ...
    def remove_all_filters(self) -> None: ...
    def remove_all_scripts(self) -> None: ...
    def remove_all_style_sheets(self) -> None: ...
    def remove_filter(self, filter: UserContentFilter) -> None: ...
    def remove_filter_by_id(self, filter_id: str) -> None: ...
    def remove_script(self, script: UserScript) -> None: ...
    def remove_style_sheet(self, stylesheet: UserStyleSheet) -> None: ...
    def unregister_script_message_handler(
        self, name: str, world_name: Optional[str] = None
    ) -> None: ...

class UserContentManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UserContentManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class UserMediaPermissionRequest(GObject.Object, PermissionRequest):
    """
    :Constructors:

    ::

        UserMediaPermissionRequest(**properties)

    Object WebKitUserMediaPermissionRequest

    Properties from WebKitUserMediaPermissionRequest:
      is-for-audio-device -> gboolean: is-for-audio-device
      is-for-video-device -> gboolean: is-for-video-device

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        is_for_audio_device: bool
        is_for_video_device: bool

    props: Props = ...

class UserMediaPermissionRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UserMediaPermissionRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class UserMessage(GObject.InitiallyUnowned):
    """
    :Constructors:

    ::

        UserMessage(**properties)
        new(name:str, parameters:GLib.Variant=None) -> WebKit.UserMessage
        new_with_fd_list(name:str, parameters:GLib.Variant=None, fd_list:Gio.UnixFDList=None) -> WebKit.UserMessage

    Object WebKitUserMessage

    Properties from WebKitUserMessage:
      name -> gchararray: name
      parameters -> GVariant: parameters
      fd-list -> GUnixFDList: fd-list

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        fd_list: Optional[Gio.UnixFDList]
        name: str
        parameters: Optional[GLib.Variant]

    props: Props = ...
    def __init__(
        self,
        fd_list: Gio.UnixFDList = ...,
        name: str = ...,
        parameters: GLib.Variant = ...,
    ): ...
    def get_fd_list(self) -> Optional[Gio.UnixFDList]: ...
    def get_name(self) -> str: ...
    def get_parameters(self) -> Optional[GLib.Variant]: ...
    @classmethod
    def new(
        cls, name: str, parameters: Optional[GLib.Variant] = None
    ) -> UserMessage: ...
    @classmethod
    def new_with_fd_list(
        cls,
        name: str,
        parameters: Optional[GLib.Variant] = None,
        fd_list: Optional[Gio.UnixFDList] = None,
    ) -> UserMessage: ...
    def send_reply(self, reply: UserMessage) -> None: ...

class UserMessageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UserMessageClass()
    """

    parent_class: GObject.InitiallyUnownedClass = ...

class UserScript(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(source:str, injected_frames:WebKit.UserContentInjectedFrames, injection_time:WebKit.UserScriptInjectionTime, allow_list:list=None, block_list:list=None) -> WebKit.UserScript
        new_for_world(source:str, injected_frames:WebKit.UserContentInjectedFrames, injection_time:WebKit.UserScriptInjectionTime, world_name:str, allow_list:list=None, block_list:list=None) -> WebKit.UserScript
    """

    @classmethod
    def new(
        cls,
        source: str,
        injected_frames: UserContentInjectedFrames,
        injection_time: UserScriptInjectionTime,
        allow_list: Optional[Sequence[str]] = None,
        block_list: Optional[Sequence[str]] = None,
    ) -> UserScript: ...
    @classmethod
    def new_for_world(
        cls,
        source: str,
        injected_frames: UserContentInjectedFrames,
        injection_time: UserScriptInjectionTime,
        world_name: str,
        allow_list: Optional[Sequence[str]] = None,
        block_list: Optional[Sequence[str]] = None,
    ) -> UserScript: ...
    def ref(self) -> UserScript: ...
    def unref(self) -> None: ...

class UserStyleSheet(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(source:str, injected_frames:WebKit.UserContentInjectedFrames, level:WebKit.UserStyleLevel, allow_list:list=None, block_list:list=None) -> WebKit.UserStyleSheet
        new_for_world(source:str, injected_frames:WebKit.UserContentInjectedFrames, level:WebKit.UserStyleLevel, world_name:str, allow_list:list=None, block_list:list=None) -> WebKit.UserStyleSheet
    """

    @classmethod
    def new(
        cls,
        source: str,
        injected_frames: UserContentInjectedFrames,
        level: UserStyleLevel,
        allow_list: Optional[Sequence[str]] = None,
        block_list: Optional[Sequence[str]] = None,
    ) -> UserStyleSheet: ...
    @classmethod
    def new_for_world(
        cls,
        source: str,
        injected_frames: UserContentInjectedFrames,
        level: UserStyleLevel,
        world_name: str,
        allow_list: Optional[Sequence[str]] = None,
        block_list: Optional[Sequence[str]] = None,
    ) -> UserStyleSheet: ...
    def ref(self) -> UserStyleSheet: ...
    def unref(self) -> None: ...

class WebContext(GObject.Object):
    """
    :Constructors:

    ::

        WebContext(**properties)
        new() -> WebKit.WebContext

    Object WebKitWebContext

    Signals from WebKitWebContext:
      initialize-web-process-extensions ()
      initialize-notification-permissions ()
      automation-started (WebKitAutomationSession)
      user-message-received (WebKitUserMessage) -> gboolean

    Properties from WebKitWebContext:
      memory-pressure-settings -> WebKitMemoryPressureSettings: memory-pressure-settings
      time-zone-override -> gchararray: time-zone-override

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        time_zone_override: str
        memory_pressure_settings: MemoryPressureSettings

    props: Props = ...
    def __init__(
        self,
        memory_pressure_settings: MemoryPressureSettings = ...,
        time_zone_override: str = ...,
    ): ...
    def add_path_to_sandbox(self, path: str, read_only: bool) -> None: ...
    def get_cache_model(self) -> CacheModel: ...
    @staticmethod
    def get_default() -> WebContext: ...
    def get_geolocation_manager(self) -> GeolocationManager: ...
    def get_network_session_for_automation(self) -> Optional[NetworkSession]: ...
    def get_security_manager(self) -> SecurityManager: ...
    def get_spell_checking_enabled(self) -> bool: ...
    def get_spell_checking_languages(self) -> list[str]: ...
    def get_time_zone_override(self) -> str: ...
    def initialize_notification_permissions(
        self,
        allowed_origins: list[SecurityOrigin],
        disallowed_origins: list[SecurityOrigin],
    ) -> None: ...
    def is_automation_allowed(self) -> bool: ...
    @classmethod
    def new(cls) -> WebContext: ...
    def register_uri_scheme(
        self, scheme: str, callback: Callable[..., None], *user_data: Any
    ) -> None: ...
    def send_message_to_all_extensions(self, message: UserMessage) -> None: ...
    def set_automation_allowed(self, allowed: bool) -> None: ...
    def set_cache_model(self, cache_model: CacheModel) -> None: ...
    def set_preferred_languages(
        self, languages: Optional[Sequence[str]] = None
    ) -> None: ...
    def set_spell_checking_enabled(self, enabled: bool) -> None: ...
    def set_spell_checking_languages(self, languages: Sequence[str]) -> None: ...
    def set_web_process_extensions_directory(self, directory: str) -> None: ...
    def set_web_process_extensions_initialization_user_data(
        self, user_data: GLib.Variant
    ) -> None: ...

class WebContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebContextClass()
    """

    parent_class: GObject.ObjectClass = ...

class WebInspector(GObject.Object):
    """
    :Constructors:

    ::

        WebInspector(**properties)

    Object WebKitWebInspector

    Signals from WebKitWebInspector:
      closed ()
      open-window () -> gboolean
      bring-to-front () -> gboolean
      attach () -> gboolean
      detach () -> gboolean

    Properties from WebKitWebInspector:
      inspected-uri -> gchararray: inspected-uri
      attached-height -> guint: attached-height
      can-attach -> gboolean: can-attach

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        attached_height: int
        can_attach: bool
        inspected_uri: str

    props: Props = ...
    def attach(self) -> None: ...
    def close(self) -> None: ...
    def detach(self) -> None: ...
    def get_attached_height(self) -> int: ...
    def get_can_attach(self) -> bool: ...
    def get_inspected_uri(self) -> str: ...
    def get_web_view(self) -> WebViewBase: ...
    def is_attached(self) -> bool: ...
    def show(self) -> None: ...

class WebInspectorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebInspectorClass()
    """

    parent_class: GObject.ObjectClass = ...

class WebResource(GObject.Object):
    """
    :Constructors:

    ::

        WebResource(**properties)

    Object WebKitWebResource

    Signals from WebKitWebResource:
      finished ()
      failed (GError)
      sent-request (WebKitURIRequest, WebKitURIResponse)
      failed-with-tls-errors (GTlsCertificate, GTlsCertificateFlags)

    Properties from WebKitWebResource:
      uri -> gchararray: uri
      response -> WebKitURIResponse: response

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        response: URIResponse
        uri: str

    props: Props = ...
    def get_data(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_data_finish(self, result: Gio.AsyncResult) -> bytes: ...
    def get_response(self) -> URIResponse: ...
    def get_uri(self) -> str: ...

class WebResourceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebResourceClass()
    """

    parent_class: GObject.ObjectClass = ...

class WebView(WebViewBase, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        WebView(**properties)
        new() -> Gtk.Widget

    Object WebKitWebView

    Signals from WebKitWebView:
      close ()
      user-message-received (WebKitUserMessage) -> gboolean
      load-changed (WebKitLoadEvent)
      load-failed (WebKitLoadEvent, gchararray, GError) -> gboolean
      load-failed-with-tls-errors (gchararray, GTlsCertificate, GTlsCertificateFlags) -> gboolean
      create (WebKitNavigationAction) -> GtkWidget
      ready-to-show ()
      run-as-modal ()
      script-dialog (WebKitScriptDialog) -> gboolean
      decide-policy (WebKitPolicyDecision, WebKitPolicyDecisionType) -> gboolean
      permission-request (WebKitPermissionRequest) -> gboolean
      mouse-target-changed (WebKitHitTestResult, guint)
      print (WebKitPrintOperation) -> gboolean
      resource-load-started (WebKitWebResource, WebKitURIRequest)
      enter-fullscreen () -> gboolean
      leave-fullscreen () -> gboolean
      run-file-chooser (WebKitFileChooserRequest) -> gboolean
      context-menu (WebKitContextMenu, WebKitHitTestResult) -> gboolean
      context-menu-dismissed ()
      submit-form (WebKitFormSubmissionRequest)
      insecure-content-detected (WebKitInsecureContentEvent)
      web-process-terminated (WebKitWebProcessTerminationReason)
      authenticate (WebKitAuthenticationRequest) -> gboolean
      show-notification (WebKitNotification) -> gboolean
      run-color-chooser (WebKitColorChooserRequest) -> gboolean
      show-option-menu (WebKitOptionMenu, GdkRectangle) -> gboolean
      query-permission-state (WebKitPermissionStateQuery) -> gboolean

    Properties from WebKitWebView:
      web-context -> WebKitWebContext: web-context
      related-view -> WebKitWebView: related-view
      settings -> WebKitSettings: settings
      user-content-manager -> WebKitUserContentManager: user-content-manager
      network-session -> WebKitNetworkSession: network-session
      title -> gchararray: title
      estimated-load-progress -> gdouble: estimated-load-progress
      favicon -> GdkTexture: favicon
      uri -> gchararray: uri
      zoom-level -> gdouble: zoom-level
      is-loading -> gboolean: is-loading
      is-playing-audio -> gboolean: is-playing-audio
      is-controlled-by-automation -> gboolean: is-controlled-by-automation
      automation-presentation-type -> WebKitAutomationBrowsingContextPresentation: automation-presentation-type
      editable -> gboolean: editable
      page-id -> guint64: page-id
      is-muted -> gboolean: is-muted
      website-policies -> WebKitWebsitePolicies: website-policies
      is-web-process-responsive -> gboolean: is-web-process-responsive
      camera-capture-state -> WebKitMediaCaptureState: camera-capture-state
      microphone-capture-state -> WebKitMediaCaptureState: microphone-capture-state
      display-capture-state -> WebKitMediaCaptureState: display-capture-state
      web-extension-mode -> WebKitWebExtensionMode: web-extension-mode
      default-content-security-policy -> gchararray: default-content-security-policy

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
        automation_presentation_type: AutomationBrowsingContextPresentation
        camera_capture_state: MediaCaptureState
        default_content_security_policy: Optional[str]
        display_capture_state: MediaCaptureState
        editable: bool
        estimated_load_progress: float
        favicon: Gdk.Texture
        is_controlled_by_automation: bool
        is_loading: bool
        is_muted: bool
        is_playing_audio: bool
        is_web_process_responsive: bool
        microphone_capture_state: MediaCaptureState
        network_session: NetworkSession
        page_id: int
        title: str
        uri: str
        user_content_manager: UserContentManager
        web_context: WebContext
        web_extension_mode: WebExtensionMode
        website_policies: WebsitePolicies
        zoom_level: float
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
        related_view: WebView
        settings: Settings

    props: Props = ...
    parent_instance: WebViewBase = ...
    priv: WebViewPrivate = ...
    def __init__(
        self,
        automation_presentation_type: AutomationBrowsingContextPresentation = ...,
        camera_capture_state: MediaCaptureState = ...,
        default_content_security_policy: str = ...,
        display_capture_state: MediaCaptureState = ...,
        editable: bool = ...,
        is_controlled_by_automation: bool = ...,
        is_muted: bool = ...,
        microphone_capture_state: MediaCaptureState = ...,
        network_session: NetworkSession = ...,
        related_view: WebView = ...,
        settings: Settings = ...,
        user_content_manager: UserContentManager = ...,
        web_context: WebContext = ...,
        web_extension_mode: WebExtensionMode = ...,
        website_policies: WebsitePolicies = ...,
        zoom_level: float = ...,
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
    def call_async_javascript_function(
        self,
        body: str,
        length: int,
        arguments: Optional[GLib.Variant] = None,
        world_name: Optional[str] = None,
        source_uri: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_async_javascript_function_finish(
        self, result: Gio.AsyncResult
    ) -> JavaScriptCore.Value: ...
    def can_execute_editing_command(
        self,
        command: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def can_execute_editing_command_finish(self, result: Gio.AsyncResult) -> bool: ...
    def can_go_back(self) -> bool: ...
    def can_go_forward(self) -> bool: ...
    def can_show_mime_type(self, mime_type: str) -> bool: ...
    def do_authenticate(self, request: AuthenticationRequest) -> bool: ...
    def do_close(self) -> None: ...
    def do_context_menu(
        self, context_menu: ContextMenu, hit_test_result: HitTestResult
    ) -> bool: ...
    def do_context_menu_dismissed(self) -> None: ...
    def do_decide_policy(
        self, decision: PolicyDecision, type: PolicyDecisionType
    ) -> bool: ...
    def do_enter_fullscreen(self) -> bool: ...
    def do_insecure_content_detected(self, event: InsecureContentEvent) -> None: ...
    def do_leave_fullscreen(self) -> bool: ...
    def do_load_changed(self, load_event: LoadEvent) -> None: ...
    def do_load_failed(
        self, load_event: LoadEvent, failing_uri: str, error: GLib.Error
    ) -> bool: ...
    def do_load_failed_with_tls_errors(
        self,
        failing_uri: str,
        certificate: Gio.TlsCertificate,
        errors: Gio.TlsCertificateFlags,
    ) -> bool: ...
    def do_mouse_target_changed(
        self, hit_test_result: HitTestResult, modifiers: int
    ) -> None: ...
    def do_permission_request(self, permission_request: PermissionRequest) -> bool: ...
    def do_print_(self, print_operation: PrintOperation) -> bool: ...
    def do_query_permission_state(self, query: PermissionStateQuery) -> bool: ...
    def do_ready_to_show(self) -> None: ...
    def do_resource_load_started(
        self, resource: WebResource, request: URIRequest
    ) -> None: ...
    def do_run_as_modal(self) -> None: ...
    def do_run_color_chooser(self, request: ColorChooserRequest) -> bool: ...
    def do_run_file_chooser(self, request: FileChooserRequest) -> bool: ...
    def do_script_dialog(self, dialog: ScriptDialog) -> bool: ...
    def do_show_notification(self, notification: Notification) -> bool: ...
    def do_show_option_menu(
        self, menu: OptionMenu, rectangle: Gdk.Rectangle
    ) -> bool: ...
    def do_submit_form(self, request: FormSubmissionRequest) -> None: ...
    def do_user_message_received(self, message: UserMessage) -> bool: ...
    def do_web_process_crashed(self) -> bool: ...
    def do_web_process_terminated(
        self, reason: WebProcessTerminationReason
    ) -> None: ...
    def download_uri(self, uri: str) -> Download: ...
    def evaluate_javascript(
        self,
        script: str,
        length: int,
        world_name: Optional[str] = None,
        source_uri: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def evaluate_javascript_finish(
        self, result: Gio.AsyncResult
    ) -> JavaScriptCore.Value: ...
    def execute_editing_command(self, command: str) -> None: ...
    def execute_editing_command_with_argument(
        self, command: str, argument: str
    ) -> None: ...
    def get_automation_presentation_type(
        self,
    ) -> AutomationBrowsingContextPresentation: ...
    def get_back_forward_list(self) -> BackForwardList: ...
    def get_background_color(self) -> Gdk.RGBA: ...
    def get_camera_capture_state(self) -> MediaCaptureState: ...
    def get_context(self) -> WebContext: ...
    def get_custom_charset(self) -> str: ...
    def get_default_content_security_policy(self) -> Optional[str]: ...
    def get_display_capture_state(self) -> MediaCaptureState: ...
    def get_editor_state(self) -> EditorState: ...
    def get_estimated_load_progress(self) -> float: ...
    def get_favicon(self) -> Gdk.Texture: ...
    def get_find_controller(self) -> FindController: ...
    def get_input_method_context(self) -> Optional[InputMethodContext]: ...
    def get_inspector(self) -> WebInspector: ...
    def get_is_muted(self) -> bool: ...
    def get_is_web_process_responsive(self) -> bool: ...
    def get_main_resource(self) -> WebResource: ...
    def get_microphone_capture_state(self) -> MediaCaptureState: ...
    def get_network_session(self) -> NetworkSession: ...
    def get_page_id(self) -> int: ...
    def get_session_state(self) -> WebViewSessionState: ...
    def get_settings(self) -> Settings: ...
    def get_snapshot(
        self,
        region: SnapshotRegion,
        options: SnapshotOptions,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_snapshot_finish(self, result: Gio.AsyncResult) -> Gdk.Texture: ...
    def get_title(self) -> str: ...
    def get_tls_info(
        self,
    ) -> Tuple[bool, Gio.TlsCertificate, Gio.TlsCertificateFlags]: ...
    def get_uri(self) -> str: ...
    def get_user_content_manager(self) -> UserContentManager: ...
    def get_web_extension_mode(self) -> WebExtensionMode: ...
    def get_website_policies(self) -> WebsitePolicies: ...
    def get_window_properties(self) -> WindowProperties: ...
    def get_zoom_level(self) -> float: ...
    def go_back(self) -> None: ...
    def go_forward(self) -> None: ...
    def go_to_back_forward_list_item(self, list_item: BackForwardListItem) -> None: ...
    def is_controlled_by_automation(self) -> bool: ...
    def is_editable(self) -> bool: ...
    def is_loading(self) -> bool: ...
    def is_playing_audio(self) -> bool: ...
    def load_alternate_html(
        self, content: str, content_uri: str, base_uri: Optional[str] = None
    ) -> None: ...
    def load_bytes(
        self,
        bytes: GLib.Bytes,
        mime_type: Optional[str] = None,
        encoding: Optional[str] = None,
        base_uri: Optional[str] = None,
    ) -> None: ...
    def load_html(self, content: str, base_uri: Optional[str] = None) -> None: ...
    def load_plain_text(self, plain_text: str) -> None: ...
    def load_request(self, request: URIRequest) -> None: ...
    def load_uri(self, uri: str) -> None: ...
    @classmethod
    def new(cls) -> WebView: ...
    def reload(self) -> None: ...
    def reload_bypass_cache(self) -> None: ...
    def restore_session_state(self, state: WebViewSessionState) -> None: ...
    def save(
        self,
        save_mode: SaveMode,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def save_finish(self, result: Gio.AsyncResult) -> Gio.InputStream: ...
    def save_to_file(
        self,
        file: Gio.File,
        save_mode: SaveMode,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def save_to_file_finish(self, result: Gio.AsyncResult) -> bool: ...
    def send_message_to_page(
        self,
        message: UserMessage,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def send_message_to_page_finish(self, result: Gio.AsyncResult) -> UserMessage: ...
    def set_background_color(self, rgba: Gdk.RGBA) -> None: ...
    def set_camera_capture_state(self, state: MediaCaptureState) -> None: ...
    def set_cors_allowlist(self, allowlist: Optional[Sequence[str]] = None) -> None: ...
    def set_custom_charset(self, charset: Optional[str] = None) -> None: ...
    def set_display_capture_state(self, state: MediaCaptureState) -> None: ...
    def set_editable(self, editable: bool) -> None: ...
    def set_input_method_context(
        self, context: Optional[InputMethodContext] = None
    ) -> None: ...
    def set_is_muted(self, muted: bool) -> None: ...
    def set_microphone_capture_state(self, state: MediaCaptureState) -> None: ...
    def set_settings(self, settings: Settings) -> None: ...
    def set_zoom_level(self, zoom_level: float) -> None: ...
    def stop_loading(self) -> None: ...
    def terminate_web_process(self) -> None: ...
    def try_close(self) -> None: ...

class WebViewBase(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        WebViewBase(**properties)

    Object WebKitWebViewBase

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
    priv: WebViewBasePrivate = ...
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

class WebViewBaseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebViewBaseClass()
    """

    parentClass: Gtk.WidgetClass = ...
    _webkit_reserved0: None = ...
    _webkit_reserved1: None = ...
    _webkit_reserved2: None = ...
    _webkit_reserved3: None = ...

class WebViewBasePrivate(GObject.GPointer): ...

class WebViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebViewClass()
    """

    parent: WebViewBaseClass = ...
    load_changed: Callable[[WebView, LoadEvent], None] = ...
    load_failed: Callable[[WebView, LoadEvent, str, GLib.Error], bool] = ...
    create: None = ...
    ready_to_show: Callable[[WebView], None] = ...
    run_as_modal: Callable[[WebView], None] = ...
    close: Callable[[WebView], None] = ...
    script_dialog: Callable[[WebView, ScriptDialog], bool] = ...
    decide_policy: Callable[[WebView, PolicyDecision, PolicyDecisionType], bool] = ...
    permission_request: Callable[[WebView, PermissionRequest], bool] = ...
    mouse_target_changed: Callable[[WebView, HitTestResult, int], None] = ...
    print_: Callable[[WebView, PrintOperation], bool] = ...
    resource_load_started: Callable[[WebView, WebResource, URIRequest], None] = ...
    enter_fullscreen: Callable[[WebView], bool] = ...
    leave_fullscreen: Callable[[WebView], bool] = ...
    run_file_chooser: Callable[[WebView, FileChooserRequest], bool] = ...
    context_menu: Callable[[WebView, ContextMenu, HitTestResult], bool] = ...
    context_menu_dismissed: Callable[[WebView], None] = ...
    submit_form: Callable[[WebView, FormSubmissionRequest], None] = ...
    insecure_content_detected: Callable[[WebView, InsecureContentEvent], None] = ...
    web_process_crashed: Callable[[WebView], bool] = ...
    authenticate: Callable[[WebView, AuthenticationRequest], bool] = ...
    load_failed_with_tls_errors: Callable[
        [WebView, str, Gio.TlsCertificate, Gio.TlsCertificateFlags], bool
    ] = ...
    show_notification: Callable[[WebView, Notification], bool] = ...
    run_color_chooser: Callable[[WebView, ColorChooserRequest], bool] = ...
    show_option_menu: Callable[[WebView, OptionMenu, Gdk.Rectangle], bool] = ...
    web_process_terminated: Callable[[WebView, WebProcessTerminationReason], None] = ...
    user_message_received: Callable[[WebView, UserMessage], bool] = ...
    query_permission_state: Callable[[WebView, PermissionStateQuery], bool] = ...
    _webkit_reserved0: None = ...
    _webkit_reserved1: None = ...
    _webkit_reserved2: None = ...
    _webkit_reserved3: None = ...
    _webkit_reserved4: None = ...
    _webkit_reserved5: None = ...
    _webkit_reserved6: None = ...
    _webkit_reserved7: None = ...
    _webkit_reserved8: None = ...
    _webkit_reserved9: None = ...
    _webkit_reserved10: None = ...
    _webkit_reserved11: None = ...
    _webkit_reserved12: None = ...
    _webkit_reserved13: None = ...
    _webkit_reserved14: None = ...
    _webkit_reserved15: None = ...
    _webkit_reserved16: None = ...
    _webkit_reserved17: None = ...
    _webkit_reserved18: None = ...
    _webkit_reserved19: None = ...
    _webkit_reserved20: None = ...
    _webkit_reserved21: None = ...
    _webkit_reserved22: None = ...
    _webkit_reserved23: None = ...
    _webkit_reserved24: None = ...
    _webkit_reserved25: None = ...
    _webkit_reserved26: None = ...
    _webkit_reserved27: None = ...
    _webkit_reserved28: None = ...
    _webkit_reserved29: None = ...
    _webkit_reserved30: None = ...

class WebViewPrivate(GObject.GPointer): ...

class WebViewSessionState(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(data:GLib.Bytes) -> WebKit.WebViewSessionState
    """

    @classmethod
    def new(cls, data: GLib.Bytes) -> WebViewSessionState: ...
    def ref(self) -> WebViewSessionState: ...
    def serialize(self) -> GLib.Bytes: ...
    def unref(self) -> None: ...

class WebsiteData(GObject.GBoxed):
    def get_name(self) -> str: ...
    def get_size(self, types: WebsiteDataTypes) -> int: ...
    def get_types(self) -> WebsiteDataTypes: ...
    def ref(self) -> WebsiteData: ...
    def unref(self) -> None: ...

class WebsiteDataAccessPermissionRequest(GObject.Object, PermissionRequest):
    """
    :Constructors:

    ::

        WebsiteDataAccessPermissionRequest(**properties)

    Object WebKitWebsiteDataAccessPermissionRequest

    Signals from GObject:
      notify (GParam)
    """

    def get_current_domain(self) -> str: ...
    def get_requesting_domain(self) -> str: ...

class WebsiteDataAccessPermissionRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebsiteDataAccessPermissionRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class WebsiteDataManager(GObject.Object):
    """
    :Constructors:

    ::

        WebsiteDataManager(**properties)

    Object WebKitWebsiteDataManager

    Properties from WebKitWebsiteDataManager:
      base-data-directory -> gchararray: base-data-directory
      base-cache-directory -> gchararray: base-cache-directory
      is-ephemeral -> gboolean: is-ephemeral
      origin-storage-ratio -> gdouble: origin-storage-ratio
      total-storage-ratio -> gdouble: total-storage-ratio

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        base_cache_directory: Optional[str]
        base_data_directory: Optional[str]
        is_ephemeral: bool
        origin_storage_ratio: float
        total_storage_ratio: float

    props: Props = ...
    def __init__(
        self,
        base_cache_directory: str = ...,
        base_data_directory: str = ...,
        is_ephemeral: bool = ...,
        origin_storage_ratio: float = ...,
        total_storage_ratio: float = ...,
    ): ...
    def clear(
        self,
        types: WebsiteDataTypes,
        timespan: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def clear_finish(self, result: Gio.AsyncResult) -> bool: ...
    def fetch(
        self,
        types: WebsiteDataTypes,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def fetch_finish(self, result: Gio.AsyncResult) -> list[WebsiteData]: ...
    def get_base_cache_directory(self) -> Optional[str]: ...
    def get_base_data_directory(self) -> Optional[str]: ...
    def get_favicon_database(self) -> Optional[FaviconDatabase]: ...
    def get_favicons_enabled(self) -> bool: ...
    def get_itp_summary(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_itp_summary_finish(
        self, result: Gio.AsyncResult
    ) -> list[ITPThirdParty]: ...
    def is_ephemeral(self) -> bool: ...
    def remove(
        self,
        types: WebsiteDataTypes,
        website_data: list[WebsiteData],
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def remove_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_favicons_enabled(self, enabled: bool) -> None: ...

class WebsiteDataManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebsiteDataManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class WebsitePolicies(GObject.Object):
    """
    :Constructors:

    ::

        WebsitePolicies(**properties)
        new() -> WebKit.WebsitePolicies

    Object WebKitWebsitePolicies

    Properties from WebKitWebsitePolicies:
      autoplay -> WebKitAutoplayPolicy: autoplay

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        autoplay: AutoplayPolicy

    props: Props = ...
    def __init__(self, autoplay: AutoplayPolicy = ...): ...
    def get_autoplay_policy(self) -> AutoplayPolicy: ...
    @classmethod
    def new(cls) -> WebsitePolicies: ...

class WebsitePoliciesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebsitePoliciesClass()
    """

    parent_class: GObject.ObjectClass = ...

class WindowProperties(GObject.Object):
    """
    :Constructors:

    ::

        WindowProperties(**properties)

    Object WebKitWindowProperties

    Properties from WebKitWindowProperties:
      geometry -> GdkRectangle: geometry
      toolbar-visible -> gboolean: toolbar-visible
      statusbar-visible -> gboolean: statusbar-visible
      scrollbars-visible -> gboolean: scrollbars-visible
      menubar-visible -> gboolean: menubar-visible
      locationbar-visible -> gboolean: locationbar-visible
      resizable -> gboolean: resizable
      fullscreen -> gboolean: fullscreen

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        fullscreen: bool
        geometry: Gdk.Rectangle
        locationbar_visible: bool
        menubar_visible: bool
        resizable: bool
        scrollbars_visible: bool
        statusbar_visible: bool
        toolbar_visible: bool

    props: Props = ...
    def __init__(
        self,
        fullscreen: bool = ...,
        geometry: Gdk.Rectangle = ...,
        locationbar_visible: bool = ...,
        menubar_visible: bool = ...,
        resizable: bool = ...,
        scrollbars_visible: bool = ...,
        statusbar_visible: bool = ...,
        toolbar_visible: bool = ...,
    ): ...
    def get_fullscreen(self) -> bool: ...
    def get_geometry(self) -> Gdk.Rectangle: ...
    def get_locationbar_visible(self) -> bool: ...
    def get_menubar_visible(self) -> bool: ...
    def get_resizable(self) -> bool: ...
    def get_scrollbars_visible(self) -> bool: ...
    def get_statusbar_visible(self) -> bool: ...
    def get_toolbar_visible(self) -> bool: ...

class WindowPropertiesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WindowPropertiesClass()
    """

    parent_class: GObject.ObjectClass = ...

class EditorTypingAttributes(GObject.GFlags):
    BOLD = 4
    ITALIC = 8
    NONE = 2
    STRIKETHROUGH = 32
    UNDERLINE = 16

class FindOptions(GObject.GFlags):
    AT_WORD_STARTS = 2
    BACKWARDS = 8
    CASE_INSENSITIVE = 1
    NONE = 0
    TREAT_MEDIAL_CAPITAL_AS_WORD_START = 4
    WRAP_AROUND = 16

class HitTestResultContext(GObject.GFlags):
    DOCUMENT = 2
    EDITABLE = 32
    IMAGE = 8
    LINK = 4
    MEDIA = 16
    SCROLLBAR = 64
    SELECTION = 128

class InputHints(GObject.GFlags):
    INHIBIT_OSK = 32
    LOWERCASE = 2
    NONE = 0
    SPELLCHECK = 1
    UPPERCASE_CHARS = 4
    UPPERCASE_SENTENCES = 16
    UPPERCASE_WORDS = 8

class SnapshotOptions(GObject.GFlags):
    INCLUDE_SELECTION_HIGHLIGHTING = 1
    NONE = 0
    TRANSPARENT_BACKGROUND = 2

class WebsiteDataTypes(GObject.GFlags):
    ALL = 4095
    COOKIES = 64
    DEVICE_ID_HASH_SALT = 128
    DISK_CACHE = 2
    DOM_CACHE = 2048
    HSTS_CACHE = 256
    INDEXEDDB_DATABASES = 32
    ITP = 512
    LOCAL_STORAGE = 16
    MEMORY_CACHE = 1
    OFFLINE_APPLICATION_CACHE = 4
    SERVICE_WORKER_REGISTRATIONS = 1024
    SESSION_STORAGE = 8

class AuthenticationScheme(GObject.GEnum):
    CLIENT_CERTIFICATE_PIN_REQUESTED = 9
    CLIENT_CERTIFICATE_REQUESTED = 7
    DEFAULT = 1
    HTML_FORM = 4
    HTTP_BASIC = 2
    HTTP_DIGEST = 3
    NEGOTIATE = 6
    NTLM = 5
    SERVER_TRUST_EVALUATION_REQUESTED = 8
    UNKNOWN = 100

class AutomationBrowsingContextPresentation(GObject.GEnum):
    TAB = 1
    WINDOW = 0

class AutoplayPolicy(GObject.GEnum):
    ALLOW = 0
    ALLOW_WITHOUT_SOUND = 1
    DENY = 2

class CacheModel(GObject.GEnum):
    DOCUMENT_BROWSER = 2
    DOCUMENT_VIEWER = 0
    WEB_BROWSER = 1

class ContextMenuAction(GObject.GEnum):
    BOLD = 27
    COPY = 14
    COPY_AUDIO_LINK_TO_CLIPBOARD = 35
    COPY_IMAGE_TO_CLIPBOARD = 7
    COPY_IMAGE_URL_TO_CLIPBOARD = 8
    COPY_LINK_TO_CLIPBOARD = 4
    COPY_VIDEO_LINK_TO_CLIPBOARD = 34
    CUSTOM = 10000
    CUT = 15
    DELETE = 17
    DOWNLOAD_AUDIO_TO_DISK = 43
    DOWNLOAD_IMAGE_TO_DISK = 6
    DOWNLOAD_LINK_TO_DISK = 3
    DOWNLOAD_VIDEO_TO_DISK = 42
    ENTER_VIDEO_FULLSCREEN = 38
    FONT_MENU = 26
    GO_BACK = 10
    GO_FORWARD = 11
    IGNORE_GRAMMAR = 25
    IGNORE_SPELLING = 23
    INPUT_METHODS = 19
    INSERT_EMOJI = 44
    INSPECT_ELEMENT = 31
    ITALIC = 28
    LEARN_SPELLING = 24
    MEDIA_MUTE = 41
    MEDIA_PAUSE = 40
    MEDIA_PLAY = 39
    NO_ACTION = 0
    NO_GUESSES_FOUND = 22
    OPEN_AUDIO_IN_NEW_WINDOW = 33
    OPEN_FRAME_IN_NEW_WINDOW = 9
    OPEN_IMAGE_IN_NEW_WINDOW = 5
    OPEN_LINK = 1
    OPEN_LINK_IN_NEW_WINDOW = 2
    OPEN_VIDEO_IN_NEW_WINDOW = 32
    OUTLINE = 30
    PASTE = 16
    PASTE_AS_PLAIN_TEXT = 45
    RELOAD = 13
    SELECT_ALL = 18
    SPELLING_GUESS = 21
    STOP = 12
    TOGGLE_MEDIA_CONTROLS = 36
    TOGGLE_MEDIA_LOOP = 37
    UNDERLINE = 29
    UNICODE = 20

class CookieAcceptPolicy(GObject.GEnum):
    ALWAYS = 0
    NEVER = 1
    NO_THIRD_PARTY = 2

class CookiePersistentStorage(GObject.GEnum):
    SQLITE = 1
    TEXT = 0

class CredentialPersistence(GObject.GEnum):
    FOR_SESSION = 1
    NONE = 0
    PERMANENT = 2

class DownloadError(GObject.GEnum):
    CANCELLED_BY_USER = 400
    DESTINATION = 401
    NETWORK = 499
    @staticmethod
    def quark() -> int: ...

class FaviconDatabaseError(GObject.GEnum):
    FAVICON_NOT_FOUND = 1
    FAVICON_UNKNOWN = 2
    NOT_INITIALIZED = 0
    @staticmethod
    def quark() -> int: ...

class FeatureStatus(GObject.GEnum):
    DEVELOPER = 3
    EMBEDDER = 0
    INTERNAL = 2
    MATURE = 7
    PREVIEW = 5
    STABLE = 6
    TESTABLE = 4
    UNSTABLE = 1

class HardwareAccelerationPolicy(GObject.GEnum):
    ALWAYS = 0
    NEVER = 1

class InputPurpose(GObject.GEnum):
    DIGITS = 1
    EMAIL = 5
    FREE_FORM = 0
    NUMBER = 2
    PASSWORD = 6
    PHONE = 3
    URL = 4

class InsecureContentEvent(GObject.GEnum):
    DISPLAYED = 1
    RUN = 0

class JavascriptError(GObject.GEnum):
    INVALID_PARAMETER = 600
    INVALID_RESULT = 601
    SCRIPT_FAILED = 699
    @staticmethod
    def quark() -> int: ...

class LoadEvent(GObject.GEnum):
    COMMITTED = 2
    FINISHED = 3
    REDIRECTED = 1
    STARTED = 0

class MediaCaptureState(GObject.GEnum):
    ACTIVE = 1
    MUTED = 2
    NONE = 0

class MediaError(GObject.GEnum):
    LOAD = 204
    @staticmethod
    def quark() -> int: ...

class NavigationType(GObject.GEnum):
    BACK_FORWARD = 2
    FORM_RESUBMITTED = 4
    FORM_SUBMITTED = 1
    LINK_CLICKED = 0
    OTHER = 5
    RELOAD = 3

class NetworkError(GObject.GEnum):
    CANCELLED = 302
    FAILED = 399
    FILE_DOES_NOT_EXIST = 303
    TRANSPORT = 300
    UNKNOWN_PROTOCOL = 301
    @staticmethod
    def quark() -> int: ...

class NetworkProxyMode(GObject.GEnum):
    CUSTOM = 2
    DEFAULT = 0
    NO_PROXY = 1

class PermissionState(GObject.GEnum):
    DENIED = 1
    GRANTED = 0
    PROMPT = 2

class PolicyDecisionType(GObject.GEnum):
    NAVIGATION_ACTION = 0
    NEW_WINDOW_ACTION = 1
    RESPONSE = 2

class PolicyError(GObject.GEnum):
    CANNOT_SHOW_MIME_TYPE = 100
    CANNOT_SHOW_URI = 101
    CANNOT_USE_RESTRICTED_PORT = 103
    FAILED = 199
    FRAME_LOAD_INTERRUPTED_BY_POLICY_CHANGE = 102
    @staticmethod
    def quark() -> int: ...

class PrintError(GObject.GEnum):
    GENERAL = 599
    INVALID_PAGE_RANGE = 501
    PRINTER_NOT_FOUND = 500
    @staticmethod
    def quark() -> int: ...

class PrintOperationResponse(GObject.GEnum):
    CANCEL = 1
    PRINT = 0

class SaveMode(GObject.GEnum):
    MHTML = 0

class ScriptDialogType(GObject.GEnum):
    ALERT = 0
    BEFORE_UNLOAD_CONFIRM = 3
    CONFIRM = 1
    PROMPT = 2

class SnapshotError(GObject.GEnum):
    CREATE = 799
    @staticmethod
    def quark() -> int: ...

class SnapshotRegion(GObject.GEnum):
    FULL_DOCUMENT = 1
    VISIBLE = 0

class TLSErrorsPolicy(GObject.GEnum):
    FAIL = 1
    IGNORE = 0

class UserContentFilterError(GObject.GEnum):
    INVALID_SOURCE = 0
    NOT_FOUND = 1
    @staticmethod
    def quark() -> int: ...

class UserContentInjectedFrames(GObject.GEnum):
    ALL_FRAMES = 0
    TOP_FRAME = 1

class UserMessageError(GObject.GEnum):
    MESSAGE = 0
    @staticmethod
    def quark() -> int: ...

class UserScriptInjectionTime(GObject.GEnum):
    END = 1
    START = 0

class UserStyleLevel(GObject.GEnum):
    AUTHOR = 1
    USER = 0

class WebExtensionMode(GObject.GEnum):
    MANIFESTV2 = 1
    MANIFESTV3 = 2
    NONE = 0

class WebProcessTerminationReason(GObject.GEnum):
    CRASHED = 0
    EXCEEDED_MEMORY_LIMIT = 1
    TERMINATED_BY_API = 2
