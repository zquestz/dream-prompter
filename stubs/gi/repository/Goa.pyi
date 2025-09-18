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

ERROR_NUM_ENTRIES: int = 6
MAJOR_VERSION: int = 3
MICRO_VERSION: int = 0
MINOR_VERSION: int = 48
_lock = ...  # FIXME Constant
_namespace: str = "Goa"
_version: str = "1.0"

def account_interface_info() -> Gio.DBusInterfaceInfo: ...
def account_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def calendar_interface_info() -> Gio.DBusInterfaceInfo: ...
def calendar_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def chat_interface_info() -> Gio.DBusInterfaceInfo: ...
def chat_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def check_version(
    required_major: int, required_minor: int, required_micro: int
) -> str: ...
def contacts_interface_info() -> Gio.DBusInterfaceInfo: ...
def contacts_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def documents_interface_info() -> Gio.DBusInterfaceInfo: ...
def documents_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def error_quark() -> int: ...
def exchange_interface_info() -> Gio.DBusInterfaceInfo: ...
def exchange_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def files_interface_info() -> Gio.DBusInterfaceInfo: ...
def files_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def mail_interface_info() -> Gio.DBusInterfaceInfo: ...
def mail_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def manager_interface_info() -> Gio.DBusInterfaceInfo: ...
def manager_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def maps_interface_info() -> Gio.DBusInterfaceInfo: ...
def maps_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def media_server_interface_info() -> Gio.DBusInterfaceInfo: ...
def media_server_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def music_interface_info() -> Gio.DBusInterfaceInfo: ...
def music_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def oauth2_based_interface_info() -> Gio.DBusInterfaceInfo: ...
def oauth2_based_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def oauth_based_interface_info() -> Gio.DBusInterfaceInfo: ...
def oauth_based_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def password_based_interface_info() -> Gio.DBusInterfaceInfo: ...
def password_based_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def photos_interface_info() -> Gio.DBusInterfaceInfo: ...
def photos_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def printers_interface_info() -> Gio.DBusInterfaceInfo: ...
def printers_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def read_later_interface_info() -> Gio.DBusInterfaceInfo: ...
def read_later_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def ticketing_interface_info() -> Gio.DBusInterfaceInfo: ...
def ticketing_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def todo_interface_info() -> Gio.DBusInterfaceInfo: ...
def todo_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...

class Account(GObject.GInterface):
    """
    Interface GoaAccount

    Signals from GObject:
      notify (GParam)
    """

    def call_ensure_credentials(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_ensure_credentials_finish(
        self, res: Gio.AsyncResult
    ) -> Tuple[bool, int]: ...
    def call_ensure_credentials_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, int]: ...
    def call_remove(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_remove_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_remove_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def complete_ensure_credentials(
        self, invocation: Gio.DBusMethodInvocation, expires_in: int
    ) -> None: ...
    def complete_remove(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class AccountIface(GObject.GPointer):
    """
    :Constructors:

    ::

        AccountIface()
    """

    parent_iface: GObject.TypeInterface = ...
    handle_ensure_credentials: Callable[[Account, Gio.DBusMethodInvocation], bool] = ...
    handle_remove: Callable[[Account, Gio.DBusMethodInvocation], bool] = ...
    get_attention_needed: Callable[[Account], bool] = ...
    get_calendar_disabled: Callable[[Account], bool] = ...
    get_chat_disabled: Callable[[Account], bool] = ...
    get_contacts_disabled: Callable[[Account], bool] = ...
    get_documents_disabled: Callable[[Account], bool] = ...
    get_id: Callable[[Account], Optional[str]] = ...
    get_identity: Callable[[Account], Optional[str]] = ...
    get_is_temporary: Callable[[Account], bool] = ...
    get_mail_disabled: Callable[[Account], bool] = ...
    get_presentation_identity: Callable[[Account], Optional[str]] = ...
    get_provider_icon: Callable[[Account], Optional[str]] = ...
    get_provider_name: Callable[[Account], Optional[str]] = ...
    get_provider_type: Callable[[Account], Optional[str]] = ...
    get_ticketing_disabled: Callable[[Account], bool] = ...
    get_files_disabled: Callable[[Account], bool] = ...
    get_photos_disabled: Callable[[Account], bool] = ...
    get_printers_disabled: Callable[[Account], bool] = ...
    get_read_later_disabled: Callable[[Account], bool] = ...
    get_maps_disabled: Callable[[Account], bool] = ...
    get_is_locked: Callable[[Account], bool] = ...
    get_music_disabled: Callable[[Account], bool] = ...
    get_todo_disabled: Callable[[Account], bool] = ...

class AccountProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Account
):
    """
    :Constructors:

    ::

        AccountProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.AccountProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.AccountProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.AccountProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.AccountProxy

    Object GoaAccountProxy

    Signals from GoaAccount:
      handle-remove (GDBusMethodInvocation) -> gboolean
      handle-ensure-credentials (GDBusMethodInvocation) -> gboolean

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
        attention_needed: bool
        calendar_disabled: bool
        chat_disabled: bool
        contacts_disabled: bool
        documents_disabled: bool
        files_disabled: bool
        id: str
        identity: str
        is_locked: bool
        is_temporary: bool
        mail_disabled: bool
        maps_disabled: bool
        music_disabled: bool
        photos_disabled: bool
        presentation_identity: str
        printers_disabled: bool
        provider_icon: str
        provider_name: str
        provider_type: str
        read_later_disabled: bool
        ticketing_disabled: bool
        todo_disabled: bool
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: AccountProxyPrivate = ...
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
        attention_needed: bool = ...,
        calendar_disabled: bool = ...,
        chat_disabled: bool = ...,
        contacts_disabled: bool = ...,
        documents_disabled: bool = ...,
        files_disabled: bool = ...,
        id: str = ...,
        identity: str = ...,
        is_locked: bool = ...,
        is_temporary: bool = ...,
        mail_disabled: bool = ...,
        maps_disabled: bool = ...,
        music_disabled: bool = ...,
        photos_disabled: bool = ...,
        presentation_identity: str = ...,
        printers_disabled: bool = ...,
        provider_icon: str = ...,
        provider_name: str = ...,
        provider_type: str = ...,
        read_later_disabled: bool = ...,
        ticketing_disabled: bool = ...,
        todo_disabled: bool = ...,
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
    def new_finish(cls, res: Gio.AsyncResult) -> AccountProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> AccountProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> AccountProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> AccountProxy: ...

class AccountProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AccountProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class AccountProxyPrivate(GObject.GPointer): ...

class AccountSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Account):
    """
    :Constructors:

    ::

        AccountSkeleton(**properties)
        new() -> Goa.AccountSkeleton

    Object GoaAccountSkeleton

    Signals from GoaAccount:
      handle-remove (GDBusMethodInvocation) -> gboolean
      handle-ensure-credentials (GDBusMethodInvocation) -> gboolean

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
        attention_needed: bool
        calendar_disabled: bool
        chat_disabled: bool
        contacts_disabled: bool
        documents_disabled: bool
        files_disabled: bool
        id: str
        identity: str
        is_locked: bool
        is_temporary: bool
        mail_disabled: bool
        maps_disabled: bool
        music_disabled: bool
        photos_disabled: bool
        presentation_identity: str
        printers_disabled: bool
        provider_icon: str
        provider_name: str
        provider_type: str
        read_later_disabled: bool
        ticketing_disabled: bool
        todo_disabled: bool

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: AccountSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        attention_needed: bool = ...,
        calendar_disabled: bool = ...,
        chat_disabled: bool = ...,
        contacts_disabled: bool = ...,
        documents_disabled: bool = ...,
        files_disabled: bool = ...,
        id: str = ...,
        identity: str = ...,
        is_locked: bool = ...,
        is_temporary: bool = ...,
        mail_disabled: bool = ...,
        maps_disabled: bool = ...,
        music_disabled: bool = ...,
        photos_disabled: bool = ...,
        presentation_identity: str = ...,
        printers_disabled: bool = ...,
        provider_icon: str = ...,
        provider_name: str = ...,
        provider_type: str = ...,
        read_later_disabled: bool = ...,
        ticketing_disabled: bool = ...,
        todo_disabled: bool = ...,
    ): ...
    @classmethod
    def new(cls) -> AccountSkeleton: ...

class AccountSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AccountSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class AccountSkeletonPrivate(GObject.GPointer): ...

class Calendar(GObject.GInterface):
    """
    Interface GoaCalendar

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class CalendarIface(GObject.GPointer):
    """
    :Constructors:

    ::

        CalendarIface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_accept_ssl_errors: Callable[[Calendar], bool] = ...
    get_uri: Callable[[Calendar], Optional[str]] = ...

class CalendarProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Calendar
):
    """
    :Constructors:

    ::

        CalendarProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.CalendarProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.CalendarProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.CalendarProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.CalendarProxy

    Object GoaCalendarProxy

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
        accept_ssl_errors: bool
        uri: str
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: CalendarProxyPrivate = ...
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
        accept_ssl_errors: bool = ...,
        uri: str = ...,
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
    def new_finish(cls, res: Gio.AsyncResult) -> CalendarProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> CalendarProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> CalendarProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> CalendarProxy: ...

class CalendarProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CalendarProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class CalendarProxyPrivate(GObject.GPointer): ...

class CalendarSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Calendar):
    """
    :Constructors:

    ::

        CalendarSkeleton(**properties)
        new() -> Goa.CalendarSkeleton

    Object GoaCalendarSkeleton

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
        accept_ssl_errors: bool
        uri: str

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: CalendarSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        accept_ssl_errors: bool = ...,
        uri: str = ...,
    ): ...
    @classmethod
    def new(cls) -> CalendarSkeleton: ...

class CalendarSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CalendarSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class CalendarSkeletonPrivate(GObject.GPointer): ...

class Chat(GObject.GInterface):
    """
    Interface GoaChat

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ChatIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ChatIface()
    """

    parent_iface: GObject.TypeInterface = ...

class ChatProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Chat
):
    """
    :Constructors:

    ::

        ChatProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.ChatProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ChatProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ChatProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ChatProxy

    Object GoaChatProxy

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
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: ChatProxyPrivate = ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> ChatProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ChatProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ChatProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ChatProxy: ...

class ChatProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ChatProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class ChatProxyPrivate(GObject.GPointer): ...

class ChatSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Chat):
    """
    :Constructors:

    ::

        ChatSkeleton(**properties)
        new() -> Goa.ChatSkeleton

    Object GoaChatSkeleton

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

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: ChatSkeletonPrivate = ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> ChatSkeleton: ...

class ChatSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ChatSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class ChatSkeletonPrivate(GObject.GPointer): ...

class Client(GObject.Object, Gio.AsyncInitable, Gio.Initable):
    """
    :Constructors:

    ::

        Client(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.Client
        new_sync(cancellable:Gio.Cancellable=None) -> Goa.Client

    Object GoaClient

    Signals from GoaClient:
      account-added (GoaObject)
      account-removed (GoaObject)
      account-changed (GoaObject)

    Properties from GoaClient:
      object-manager -> GDBusObjectManager: object manager
        The GDBusObjectManager used by the GoaClient

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        object_manager: Gio.DBusObjectManager

    props: Props = ...
    def get_accounts(self) -> list[Object]: ...
    def get_manager(self) -> Optional[Manager]: ...
    def get_object_manager(self) -> Gio.DBusObjectManager: ...
    def lookup_by_id(self, id: str) -> Object: ...
    @staticmethod
    def new(
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> Client: ...
    @classmethod
    def new_sync(cls, cancellable: Optional[Gio.Cancellable] = None) -> Client: ...

class ClientClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClientClass()
    """

    parent_class: GObject.ObjectClass = ...

class Contacts(GObject.GInterface):
    """
    Interface GoaContacts

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ContactsIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ContactsIface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_accept_ssl_errors: Callable[[Contacts], bool] = ...
    get_uri: Callable[[Contacts], Optional[str]] = ...

class ContactsProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Contacts
):
    """
    :Constructors:

    ::

        ContactsProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.ContactsProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ContactsProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ContactsProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ContactsProxy

    Object GoaContactsProxy

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
        accept_ssl_errors: bool
        uri: str
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: ContactsProxyPrivate = ...
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
        accept_ssl_errors: bool = ...,
        uri: str = ...,
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
    def new_finish(cls, res: Gio.AsyncResult) -> ContactsProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ContactsProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ContactsProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ContactsProxy: ...

class ContactsProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContactsProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class ContactsProxyPrivate(GObject.GPointer): ...

class ContactsSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Contacts):
    """
    :Constructors:

    ::

        ContactsSkeleton(**properties)
        new() -> Goa.ContactsSkeleton

    Object GoaContactsSkeleton

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
        accept_ssl_errors: bool
        uri: str

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: ContactsSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        accept_ssl_errors: bool = ...,
        uri: str = ...,
    ): ...
    @classmethod
    def new(cls) -> ContactsSkeleton: ...

class ContactsSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContactsSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class ContactsSkeletonPrivate(GObject.GPointer): ...

class Documents(GObject.GInterface):
    """
    Interface GoaDocuments

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class DocumentsIface(GObject.GPointer):
    """
    :Constructors:

    ::

        DocumentsIface()
    """

    parent_iface: GObject.TypeInterface = ...

class DocumentsProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Documents
):
    """
    :Constructors:

    ::

        DocumentsProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.DocumentsProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.DocumentsProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.DocumentsProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.DocumentsProxy

    Object GoaDocumentsProxy

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
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: DocumentsProxyPrivate = ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> DocumentsProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> DocumentsProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> DocumentsProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> DocumentsProxy: ...

class DocumentsProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DocumentsProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class DocumentsProxyPrivate(GObject.GPointer): ...

class DocumentsSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Documents):
    """
    :Constructors:

    ::

        DocumentsSkeleton(**properties)
        new() -> Goa.DocumentsSkeleton

    Object GoaDocumentsSkeleton

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

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: DocumentsSkeletonPrivate = ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> DocumentsSkeleton: ...

class DocumentsSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DocumentsSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class DocumentsSkeletonPrivate(GObject.GPointer): ...

class Exchange(GObject.GInterface):
    """
    Interface GoaExchange

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ExchangeIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ExchangeIface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_host: Callable[[Exchange], Optional[str]] = ...
    get_accept_ssl_errors: Callable[[Exchange], bool] = ...

class ExchangeProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Exchange
):
    """
    :Constructors:

    ::

        ExchangeProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.ExchangeProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ExchangeProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ExchangeProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ExchangeProxy

    Object GoaExchangeProxy

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
        accept_ssl_errors: bool
        host: str
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: ExchangeProxyPrivate = ...
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
        accept_ssl_errors: bool = ...,
        host: str = ...,
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
    def new_finish(cls, res: Gio.AsyncResult) -> ExchangeProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ExchangeProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ExchangeProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ExchangeProxy: ...

class ExchangeProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ExchangeProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class ExchangeProxyPrivate(GObject.GPointer): ...

class ExchangeSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Exchange):
    """
    :Constructors:

    ::

        ExchangeSkeleton(**properties)
        new() -> Goa.ExchangeSkeleton

    Object GoaExchangeSkeleton

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
        accept_ssl_errors: bool
        host: str

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: ExchangeSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        accept_ssl_errors: bool = ...,
        host: str = ...,
    ): ...
    @classmethod
    def new(cls) -> ExchangeSkeleton: ...

class ExchangeSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ExchangeSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class ExchangeSkeletonPrivate(GObject.GPointer): ...

class Files(GObject.GInterface):
    """
    Interface GoaFiles

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class FilesIface(GObject.GPointer):
    """
    :Constructors:

    ::

        FilesIface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_accept_ssl_errors: Callable[[Files], bool] = ...
    get_uri: Callable[[Files], Optional[str]] = ...

class FilesProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Files
):
    """
    :Constructors:

    ::

        FilesProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.FilesProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.FilesProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.FilesProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.FilesProxy

    Object GoaFilesProxy

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
        accept_ssl_errors: bool
        uri: str
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: FilesProxyPrivate = ...
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
        accept_ssl_errors: bool = ...,
        uri: str = ...,
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
    def new_finish(cls, res: Gio.AsyncResult) -> FilesProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> FilesProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> FilesProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> FilesProxy: ...

class FilesProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FilesProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class FilesProxyPrivate(GObject.GPointer): ...

class FilesSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Files):
    """
    :Constructors:

    ::

        FilesSkeleton(**properties)
        new() -> Goa.FilesSkeleton

    Object GoaFilesSkeleton

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
        accept_ssl_errors: bool
        uri: str

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: FilesSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        accept_ssl_errors: bool = ...,
        uri: str = ...,
    ): ...
    @classmethod
    def new(cls) -> FilesSkeleton: ...

class FilesSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FilesSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class FilesSkeletonPrivate(GObject.GPointer): ...

class Mail(GObject.GInterface):
    """
    Interface GoaMail

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class MailIface(GObject.GPointer):
    """
    :Constructors:

    ::

        MailIface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_email_address: Callable[[Mail], Optional[str]] = ...
    get_imap_host: Callable[[Mail], Optional[str]] = ...
    get_imap_supported: Callable[[Mail], bool] = ...
    get_imap_use_tls: Callable[[Mail], bool] = ...
    get_imap_user_name: Callable[[Mail], Optional[str]] = ...
    get_smtp_host: Callable[[Mail], Optional[str]] = ...
    get_smtp_supported: Callable[[Mail], bool] = ...
    get_smtp_use_tls: Callable[[Mail], bool] = ...
    get_smtp_user_name: Callable[[Mail], Optional[str]] = ...
    get_imap_accept_ssl_errors: Callable[[Mail], bool] = ...
    get_imap_use_ssl: Callable[[Mail], bool] = ...
    get_name: Callable[[Mail], Optional[str]] = ...
    get_smtp_accept_ssl_errors: Callable[[Mail], bool] = ...
    get_smtp_use_auth: Callable[[Mail], bool] = ...
    get_smtp_use_ssl: Callable[[Mail], bool] = ...
    get_smtp_auth_login: Callable[[Mail], bool] = ...
    get_smtp_auth_plain: Callable[[Mail], bool] = ...
    get_smtp_auth_xoauth2: Callable[[Mail], bool] = ...

class MailProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Mail
):
    """
    :Constructors:

    ::

        MailProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.MailProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.MailProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MailProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MailProxy

    Object GoaMailProxy

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
        email_address: str
        imap_accept_ssl_errors: bool
        imap_host: str
        imap_supported: bool
        imap_use_ssl: bool
        imap_use_tls: bool
        imap_user_name: str
        name: str
        smtp_accept_ssl_errors: bool
        smtp_auth_login: bool
        smtp_auth_plain: bool
        smtp_auth_xoauth2: bool
        smtp_host: str
        smtp_supported: bool
        smtp_use_auth: bool
        smtp_use_ssl: bool
        smtp_use_tls: bool
        smtp_user_name: str
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: MailProxyPrivate = ...
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
        email_address: str = ...,
        imap_accept_ssl_errors: bool = ...,
        imap_host: str = ...,
        imap_supported: bool = ...,
        imap_use_ssl: bool = ...,
        imap_use_tls: bool = ...,
        imap_user_name: str = ...,
        name: str = ...,
        smtp_accept_ssl_errors: bool = ...,
        smtp_auth_login: bool = ...,
        smtp_auth_plain: bool = ...,
        smtp_auth_xoauth2: bool = ...,
        smtp_host: str = ...,
        smtp_supported: bool = ...,
        smtp_use_auth: bool = ...,
        smtp_use_ssl: bool = ...,
        smtp_use_tls: bool = ...,
        smtp_user_name: str = ...,
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
    def new_finish(cls, res: Gio.AsyncResult) -> MailProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> MailProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> MailProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> MailProxy: ...

class MailProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MailProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class MailProxyPrivate(GObject.GPointer): ...

class MailSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Mail):
    """
    :Constructors:

    ::

        MailSkeleton(**properties)
        new() -> Goa.MailSkeleton

    Object GoaMailSkeleton

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
        email_address: str
        imap_accept_ssl_errors: bool
        imap_host: str
        imap_supported: bool
        imap_use_ssl: bool
        imap_use_tls: bool
        imap_user_name: str
        name: str
        smtp_accept_ssl_errors: bool
        smtp_auth_login: bool
        smtp_auth_plain: bool
        smtp_auth_xoauth2: bool
        smtp_host: str
        smtp_supported: bool
        smtp_use_auth: bool
        smtp_use_ssl: bool
        smtp_use_tls: bool
        smtp_user_name: str

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: MailSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        email_address: str = ...,
        imap_accept_ssl_errors: bool = ...,
        imap_host: str = ...,
        imap_supported: bool = ...,
        imap_use_ssl: bool = ...,
        imap_use_tls: bool = ...,
        imap_user_name: str = ...,
        name: str = ...,
        smtp_accept_ssl_errors: bool = ...,
        smtp_auth_login: bool = ...,
        smtp_auth_plain: bool = ...,
        smtp_auth_xoauth2: bool = ...,
        smtp_host: str = ...,
        smtp_supported: bool = ...,
        smtp_use_auth: bool = ...,
        smtp_use_ssl: bool = ...,
        smtp_use_tls: bool = ...,
        smtp_user_name: str = ...,
    ): ...
    @classmethod
    def new(cls) -> MailSkeleton: ...

class MailSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MailSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class MailSkeletonPrivate(GObject.GPointer): ...

class Manager(GObject.GInterface):
    """
    Interface GoaManager

    Signals from GObject:
      notify (GParam)
    """

    def call_add_account(
        self,
        arg_provider: str,
        arg_identity: str,
        arg_presentation_identity: str,
        arg_credentials: GLib.Variant,
        arg_details: GLib.Variant,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_add_account_finish(self, res: Gio.AsyncResult) -> Tuple[bool, str]: ...
    def call_add_account_sync(
        self,
        arg_provider: str,
        arg_identity: str,
        arg_presentation_identity: str,
        arg_credentials: GLib.Variant,
        arg_details: GLib.Variant,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[bool, str]: ...
    def call_is_supported_provider(
        self,
        arg_provider_type: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_is_supported_provider_finish(
        self, res: Gio.AsyncResult
    ) -> Tuple[bool, bool]: ...
    def call_is_supported_provider_sync(
        self, arg_provider_type: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, bool]: ...
    def complete_add_account(
        self, invocation: Gio.DBusMethodInvocation, account_object_path: str
    ) -> None: ...
    def complete_is_supported_provider(
        self, invocation: Gio.DBusMethodInvocation, is_supported: bool
    ) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ManagerIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ManagerIface()
    """

    parent_iface: GObject.TypeInterface = ...
    handle_add_account: Callable[
        [Manager, Gio.DBusMethodInvocation, str, str, str, GLib.Variant, GLib.Variant],
        bool,
    ] = ...
    handle_is_supported_provider: Callable[
        [Manager, Gio.DBusMethodInvocation, str], bool
    ] = ...

class ManagerProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Manager
):
    """
    :Constructors:

    ::

        ManagerProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.ManagerProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ManagerProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ManagerProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ManagerProxy

    Object GoaManagerProxy

    Signals from GoaManager:
      handle-add-account (GDBusMethodInvocation, gchararray, gchararray, gchararray, GVariant, GVariant) -> gboolean
      handle-is-supported-provider (GDBusMethodInvocation, gchararray) -> gboolean

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
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: ManagerProxyPrivate = ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> ManagerProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ManagerProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ManagerProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ManagerProxy: ...

class ManagerProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ManagerProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class ManagerProxyPrivate(GObject.GPointer): ...

class ManagerSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Manager):
    """
    :Constructors:

    ::

        ManagerSkeleton(**properties)
        new() -> Goa.ManagerSkeleton

    Object GoaManagerSkeleton

    Signals from GoaManager:
      handle-add-account (GDBusMethodInvocation, gchararray, gchararray, gchararray, GVariant, GVariant) -> gboolean
      handle-is-supported-provider (GDBusMethodInvocation, gchararray) -> gboolean

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

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: ManagerSkeletonPrivate = ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> ManagerSkeleton: ...

class ManagerSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ManagerSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class ManagerSkeletonPrivate(GObject.GPointer): ...

class Maps(GObject.GInterface):
    """
    Interface GoaMaps

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class MapsIface(GObject.GPointer):
    """
    :Constructors:

    ::

        MapsIface()
    """

    parent_iface: GObject.TypeInterface = ...

class MapsProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Maps
):
    """
    :Constructors:

    ::

        MapsProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.MapsProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.MapsProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MapsProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MapsProxy

    Object GoaMapsProxy

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
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: MapsProxyPrivate = ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> MapsProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> MapsProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> MapsProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> MapsProxy: ...

class MapsProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MapsProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class MapsProxyPrivate(GObject.GPointer): ...

class MapsSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Maps):
    """
    :Constructors:

    ::

        MapsSkeleton(**properties)
        new() -> Goa.MapsSkeleton

    Object GoaMapsSkeleton

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

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: MapsSkeletonPrivate = ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> MapsSkeleton: ...

class MapsSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MapsSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class MapsSkeletonPrivate(GObject.GPointer): ...

class MediaServer(GObject.GInterface):
    """
    Interface GoaMediaServer

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class MediaServerIface(GObject.GPointer):
    """
    :Constructors:

    ::

        MediaServerIface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_dlna_supported: Callable[[MediaServer], bool] = ...
    get_udn: Callable[[MediaServer], Optional[str]] = ...

class MediaServerProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, MediaServer
):
    """
    :Constructors:

    ::

        MediaServerProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.MediaServerProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.MediaServerProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MediaServerProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MediaServerProxy

    Object GoaMediaServerProxy

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
        dlna_supported: bool
        udn: str
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: MediaServerProxyPrivate = ...
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
        dlna_supported: bool = ...,
        udn: str = ...,
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
    def new_finish(cls, res: Gio.AsyncResult) -> MediaServerProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> MediaServerProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> MediaServerProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> MediaServerProxy: ...

class MediaServerProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MediaServerProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class MediaServerProxyPrivate(GObject.GPointer): ...

class MediaServerSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, MediaServer):
    """
    :Constructors:

    ::

        MediaServerSkeleton(**properties)
        new() -> Goa.MediaServerSkeleton

    Object GoaMediaServerSkeleton

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
        dlna_supported: bool
        udn: str

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: MediaServerSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        dlna_supported: bool = ...,
        udn: str = ...,
    ): ...
    @classmethod
    def new(cls) -> MediaServerSkeleton: ...

class MediaServerSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MediaServerSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class MediaServerSkeletonPrivate(GObject.GPointer): ...

class Music(GObject.GInterface):
    """
    Interface GoaMusic

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class MusicIface(GObject.GPointer):
    """
    :Constructors:

    ::

        MusicIface()
    """

    parent_iface: GObject.TypeInterface = ...

class MusicProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Music
):
    """
    :Constructors:

    ::

        MusicProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.MusicProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.MusicProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MusicProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MusicProxy

    Object GoaMusicProxy

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
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: MusicProxyPrivate = ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> MusicProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> MusicProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> MusicProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> MusicProxy: ...

class MusicProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MusicProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class MusicProxyPrivate(GObject.GPointer): ...

class MusicSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Music):
    """
    :Constructors:

    ::

        MusicSkeleton(**properties)
        new() -> Goa.MusicSkeleton

    Object GoaMusicSkeleton

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

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: MusicSkeletonPrivate = ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> MusicSkeleton: ...

class MusicSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MusicSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class MusicSkeletonPrivate(GObject.GPointer): ...

class OAuth2Based(GObject.GInterface):
    """
    Interface GoaOAuth2Based

    Signals from GObject:
      notify (GParam)
    """

    def call_get_access_token(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_get_access_token_finish(
        self, res: Gio.AsyncResult
    ) -> Tuple[bool, str, int]: ...
    def call_get_access_token_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, str, int]: ...
    def complete_get_access_token(
        self, invocation: Gio.DBusMethodInvocation, access_token: str, expires_in: int
    ) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class OAuth2BasedIface(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2BasedIface()
    """

    parent_iface: GObject.TypeInterface = ...
    handle_get_access_token: Callable[[OAuth2Based, Gio.DBusMethodInvocation], bool] = (
        ...
    )
    get_client_id: Callable[[OAuth2Based], Optional[str]] = ...
    get_client_secret: Callable[[OAuth2Based], Optional[str]] = ...

class OAuth2BasedProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, OAuth2Based
):
    """
    :Constructors:

    ::

        OAuth2BasedProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.OAuth2BasedProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.OAuth2BasedProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.OAuth2BasedProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.OAuth2BasedProxy

    Object GoaOAuth2BasedProxy

    Signals from GoaOAuth2Based:
      handle-get-access-token (GDBusMethodInvocation) -> gboolean

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
        client_id: str
        client_secret: str
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: OAuth2BasedProxyPrivate = ...
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
        client_id: str = ...,
        client_secret: str = ...,
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
    def new_finish(cls, res: Gio.AsyncResult) -> OAuth2BasedProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> OAuth2BasedProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> OAuth2BasedProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> OAuth2BasedProxy: ...

class OAuth2BasedProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2BasedProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class OAuth2BasedProxyPrivate(GObject.GPointer): ...

class OAuth2BasedSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, OAuth2Based):
    """
    :Constructors:

    ::

        OAuth2BasedSkeleton(**properties)
        new() -> Goa.OAuth2BasedSkeleton

    Object GoaOAuth2BasedSkeleton

    Signals from GoaOAuth2Based:
      handle-get-access-token (GDBusMethodInvocation) -> gboolean

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
        client_id: str
        client_secret: str

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: OAuth2BasedSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        client_id: str = ...,
        client_secret: str = ...,
    ): ...
    @classmethod
    def new(cls) -> OAuth2BasedSkeleton: ...

class OAuth2BasedSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2BasedSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class OAuth2BasedSkeletonPrivate(GObject.GPointer): ...

class OAuthBased(GObject.GInterface):
    """
    Interface GoaOAuthBased

    Signals from GObject:
      notify (GParam)
    """

    def call_get_access_token(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_get_access_token_finish(
        self, res: Gio.AsyncResult
    ) -> Tuple[bool, str, str, int]: ...
    def call_get_access_token_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, str, str, int]: ...
    def complete_get_access_token(
        self,
        invocation: Gio.DBusMethodInvocation,
        access_token: str,
        access_token_secret: str,
        expires_in: int,
    ) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class OAuthBasedIface(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuthBasedIface()
    """

    parent_iface: GObject.TypeInterface = ...
    handle_get_access_token: Callable[[OAuthBased, Gio.DBusMethodInvocation], bool] = (
        ...
    )
    get_consumer_key: Callable[[OAuthBased], Optional[str]] = ...
    get_consumer_secret: Callable[[OAuthBased], Optional[str]] = ...

class OAuthBasedProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, OAuthBased
):
    """
    :Constructors:

    ::

        OAuthBasedProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.OAuthBasedProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.OAuthBasedProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.OAuthBasedProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.OAuthBasedProxy

    Object GoaOAuthBasedProxy

    Signals from GoaOAuthBased:
      handle-get-access-token (GDBusMethodInvocation) -> gboolean

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
        consumer_key: str
        consumer_secret: str
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: OAuthBasedProxyPrivate = ...
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
        consumer_key: str = ...,
        consumer_secret: str = ...,
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
    def new_finish(cls, res: Gio.AsyncResult) -> OAuthBasedProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> OAuthBasedProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> OAuthBasedProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> OAuthBasedProxy: ...

class OAuthBasedProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuthBasedProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class OAuthBasedProxyPrivate(GObject.GPointer): ...

class OAuthBasedSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, OAuthBased):
    """
    :Constructors:

    ::

        OAuthBasedSkeleton(**properties)
        new() -> Goa.OAuthBasedSkeleton

    Object GoaOAuthBasedSkeleton

    Signals from GoaOAuthBased:
      handle-get-access-token (GDBusMethodInvocation) -> gboolean

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
        consumer_key: str
        consumer_secret: str

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: OAuthBasedSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        consumer_key: str = ...,
        consumer_secret: str = ...,
    ): ...
    @classmethod
    def new(cls) -> OAuthBasedSkeleton: ...

class OAuthBasedSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuthBasedSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class OAuthBasedSkeletonPrivate(GObject.GPointer): ...

class Object(GObject.GInterface):
    """
    Interface GoaObject

    Signals from GObject:
      notify (GParam)
    """

    def get_account(self) -> Optional[Account]: ...
    def get_calendar(self) -> Optional[Calendar]: ...
    def get_chat(self) -> Optional[Chat]: ...
    def get_contacts(self) -> Optional[Contacts]: ...
    def get_documents(self) -> Optional[Documents]: ...
    def get_exchange(self) -> Optional[Exchange]: ...
    def get_files(self) -> Optional[Files]: ...
    def get_mail(self) -> Optional[Mail]: ...
    def get_manager(self) -> Optional[Manager]: ...
    def get_maps(self) -> Optional[Maps]: ...
    def get_media_server(self) -> Optional[MediaServer]: ...
    def get_music(self) -> Optional[Music]: ...
    def get_oauth2_based(self) -> Optional[OAuth2Based]: ...
    def get_oauth_based(self) -> Optional[OAuthBased]: ...
    def get_password_based(self) -> Optional[PasswordBased]: ...
    def get_photos(self) -> Optional[Photos]: ...
    def get_printers(self) -> Optional[Printers]: ...
    def get_read_later(self) -> Optional[ReadLater]: ...
    def get_ticketing(self) -> Optional[Ticketing]: ...
    def get_todo(self) -> Optional[Todo]: ...

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
        new_finish(res:Gio.AsyncResult) -> Goa.ObjectManagerClient
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ObjectManagerClient
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusObjectManagerClientFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ObjectManagerClient
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusObjectManagerClientFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ObjectManagerClient

    Object GoaObjectManagerClient

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
        new(connection:Gio.DBusConnection, object_path:str) -> Goa.ObjectProxy

    Object GoaObjectProxy

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
        account: Optional[Account]
        calendar: Optional[Calendar]
        chat: Optional[Chat]
        contacts: Optional[Contacts]
        documents: Optional[Documents]
        exchange: Optional[Exchange]
        files: Optional[Files]
        mail: Optional[Mail]
        manager: Optional[Manager]
        maps: Optional[Maps]
        media_server: Optional[MediaServer]
        music: Optional[Music]
        oauth_based: Optional[OAuthBased]
        oauth2_based: Optional[OAuth2Based]
        password_based: Optional[PasswordBased]
        photos: Optional[Photos]
        printers: Optional[Printers]
        read_later: Optional[ReadLater]
        ticketing: Optional[Ticketing]
        todo: Optional[Todo]

    props: Props = ...
    parent_instance: Gio.DBusObjectProxy = ...
    priv: ObjectProxyPrivate = ...
    def __init__(
        self,
        g_connection: Gio.DBusConnection = ...,
        g_object_path: str = ...,
        account: Account = ...,
        calendar: Calendar = ...,
        chat: Chat = ...,
        contacts: Contacts = ...,
        documents: Documents = ...,
        exchange: Exchange = ...,
        files: Files = ...,
        mail: Mail = ...,
        manager: Manager = ...,
        maps: Maps = ...,
        media_server: MediaServer = ...,
        music: Music = ...,
        oauth_based: OAuthBased = ...,
        oauth2_based: OAuth2Based = ...,
        password_based: PasswordBased = ...,
        photos: Photos = ...,
        printers: Printers = ...,
        read_later: ReadLater = ...,
        ticketing: Ticketing = ...,
        todo: Todo = ...,
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
        new(object_path:str) -> Goa.ObjectSkeleton

    Object GoaObjectSkeleton

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
        account: Optional[Account]
        calendar: Optional[Calendar]
        chat: Optional[Chat]
        contacts: Optional[Contacts]
        documents: Optional[Documents]
        exchange: Optional[Exchange]
        files: Optional[Files]
        mail: Optional[Mail]
        manager: Optional[Manager]
        maps: Optional[Maps]
        media_server: Optional[MediaServer]
        music: Optional[Music]
        oauth_based: Optional[OAuthBased]
        oauth2_based: Optional[OAuth2Based]
        password_based: Optional[PasswordBased]
        photos: Optional[Photos]
        printers: Optional[Printers]
        read_later: Optional[ReadLater]
        ticketing: Optional[Ticketing]
        todo: Optional[Todo]

    props: Props = ...
    parent_instance: Gio.DBusObjectSkeleton = ...
    priv: ObjectSkeletonPrivate = ...
    def __init__(
        self,
        g_object_path: str = ...,
        account: Account = ...,
        calendar: Calendar = ...,
        chat: Chat = ...,
        contacts: Contacts = ...,
        documents: Documents = ...,
        exchange: Exchange = ...,
        files: Files = ...,
        mail: Mail = ...,
        manager: Manager = ...,
        maps: Maps = ...,
        media_server: MediaServer = ...,
        music: Music = ...,
        oauth_based: OAuthBased = ...,
        oauth2_based: OAuth2Based = ...,
        password_based: PasswordBased = ...,
        photos: Photos = ...,
        printers: Printers = ...,
        read_later: ReadLater = ...,
        ticketing: Ticketing = ...,
        todo: Todo = ...,
    ): ...
    @classmethod
    def new(cls, object_path: str) -> ObjectSkeleton: ...
    def set_account(self, interface_: Optional[Account] = None) -> None: ...
    def set_calendar(self, interface_: Optional[Calendar] = None) -> None: ...
    def set_chat(self, interface_: Optional[Chat] = None) -> None: ...
    def set_contacts(self, interface_: Optional[Contacts] = None) -> None: ...
    def set_documents(self, interface_: Optional[Documents] = None) -> None: ...
    def set_exchange(self, interface_: Optional[Exchange] = None) -> None: ...
    def set_files(self, interface_: Optional[Files] = None) -> None: ...
    def set_mail(self, interface_: Optional[Mail] = None) -> None: ...
    def set_manager(self, interface_: Optional[Manager] = None) -> None: ...
    def set_maps(self, interface_: Optional[Maps] = None) -> None: ...
    def set_media_server(self, interface_: Optional[MediaServer] = None) -> None: ...
    def set_music(self, interface_: Optional[Music] = None) -> None: ...
    def set_oauth2_based(self, interface_: Optional[OAuth2Based] = None) -> None: ...
    def set_oauth_based(self, interface_: Optional[OAuthBased] = None) -> None: ...
    def set_password_based(
        self, interface_: Optional[PasswordBased] = None
    ) -> None: ...
    def set_photos(self, interface_: Optional[Photos] = None) -> None: ...
    def set_printers(self, interface_: Optional[Printers] = None) -> None: ...
    def set_read_later(self, interface_: Optional[ReadLater] = None) -> None: ...
    def set_ticketing(self, interface_: Optional[Ticketing] = None) -> None: ...
    def set_todo(self, interface_: Optional[Todo] = None) -> None: ...

class ObjectSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectSkeletonClass()
    """

    parent_class: Gio.DBusObjectSkeletonClass = ...

class ObjectSkeletonPrivate(GObject.GPointer): ...

class PasswordBased(GObject.GInterface):
    """
    Interface GoaPasswordBased

    Signals from GObject:
      notify (GParam)
    """

    def call_get_password(
        self,
        arg_id: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_get_password_finish(self, res: Gio.AsyncResult) -> Tuple[bool, str]: ...
    def call_get_password_sync(
        self, arg_id: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, str]: ...
    def complete_get_password(
        self, invocation: Gio.DBusMethodInvocation, password: str
    ) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class PasswordBasedIface(GObject.GPointer):
    """
    :Constructors:

    ::

        PasswordBasedIface()
    """

    parent_iface: GObject.TypeInterface = ...
    handle_get_password: Callable[
        [PasswordBased, Gio.DBusMethodInvocation, str], bool
    ] = ...

class PasswordBasedProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, PasswordBased
):
    """
    :Constructors:

    ::

        PasswordBasedProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.PasswordBasedProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.PasswordBasedProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PasswordBasedProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PasswordBasedProxy

    Object GoaPasswordBasedProxy

    Signals from GoaPasswordBased:
      handle-get-password (GDBusMethodInvocation, gchararray) -> gboolean

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
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: PasswordBasedProxyPrivate = ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> PasswordBasedProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> PasswordBasedProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> PasswordBasedProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> PasswordBasedProxy: ...

class PasswordBasedProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PasswordBasedProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class PasswordBasedProxyPrivate(GObject.GPointer): ...

class PasswordBasedSkeleton(
    Gio.DBusInterfaceSkeleton, Gio.DBusInterface, PasswordBased
):
    """
    :Constructors:

    ::

        PasswordBasedSkeleton(**properties)
        new() -> Goa.PasswordBasedSkeleton

    Object GoaPasswordBasedSkeleton

    Signals from GoaPasswordBased:
      handle-get-password (GDBusMethodInvocation, gchararray) -> gboolean

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

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: PasswordBasedSkeletonPrivate = ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> PasswordBasedSkeleton: ...

class PasswordBasedSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PasswordBasedSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class PasswordBasedSkeletonPrivate(GObject.GPointer): ...

class Photos(GObject.GInterface):
    """
    Interface GoaPhotos

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class PhotosIface(GObject.GPointer):
    """
    :Constructors:

    ::

        PhotosIface()
    """

    parent_iface: GObject.TypeInterface = ...

class PhotosProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Photos
):
    """
    :Constructors:

    ::

        PhotosProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.PhotosProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.PhotosProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PhotosProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PhotosProxy

    Object GoaPhotosProxy

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
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: PhotosProxyPrivate = ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> PhotosProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> PhotosProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> PhotosProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> PhotosProxy: ...

class PhotosProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PhotosProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class PhotosProxyPrivate(GObject.GPointer): ...

class PhotosSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Photos):
    """
    :Constructors:

    ::

        PhotosSkeleton(**properties)
        new() -> Goa.PhotosSkeleton

    Object GoaPhotosSkeleton

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

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: PhotosSkeletonPrivate = ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> PhotosSkeleton: ...

class PhotosSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PhotosSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class PhotosSkeletonPrivate(GObject.GPointer): ...

class Printers(GObject.GInterface):
    """
    Interface GoaPrinters

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class PrintersIface(GObject.GPointer):
    """
    :Constructors:

    ::

        PrintersIface()
    """

    parent_iface: GObject.TypeInterface = ...

class PrintersProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Printers
):
    """
    :Constructors:

    ::

        PrintersProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.PrintersProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.PrintersProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PrintersProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PrintersProxy

    Object GoaPrintersProxy

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
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: PrintersProxyPrivate = ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> PrintersProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> PrintersProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> PrintersProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> PrintersProxy: ...

class PrintersProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PrintersProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class PrintersProxyPrivate(GObject.GPointer): ...

class PrintersSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Printers):
    """
    :Constructors:

    ::

        PrintersSkeleton(**properties)
        new() -> Goa.PrintersSkeleton

    Object GoaPrintersSkeleton

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

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: PrintersSkeletonPrivate = ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> PrintersSkeleton: ...

class PrintersSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PrintersSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class PrintersSkeletonPrivate(GObject.GPointer): ...

class ReadLater(GObject.GInterface):
    """
    Interface GoaReadLater

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ReadLaterIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ReadLaterIface()
    """

    parent_iface: GObject.TypeInterface = ...

class ReadLaterProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, ReadLater
):
    """
    :Constructors:

    ::

        ReadLaterProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.ReadLaterProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ReadLaterProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ReadLaterProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ReadLaterProxy

    Object GoaReadLaterProxy

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
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: ReadLaterProxyPrivate = ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> ReadLaterProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ReadLaterProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ReadLaterProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ReadLaterProxy: ...

class ReadLaterProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ReadLaterProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class ReadLaterProxyPrivate(GObject.GPointer): ...

class ReadLaterSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, ReadLater):
    """
    :Constructors:

    ::

        ReadLaterSkeleton(**properties)
        new() -> Goa.ReadLaterSkeleton

    Object GoaReadLaterSkeleton

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

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: ReadLaterSkeletonPrivate = ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> ReadLaterSkeleton: ...

class ReadLaterSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ReadLaterSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class ReadLaterSkeletonPrivate(GObject.GPointer): ...

class Ticketing(GObject.GInterface):
    """
    Interface GoaTicketing

    Signals from GObject:
      notify (GParam)
    """

    def call_get_ticket(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_get_ticket_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_get_ticket_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def complete_get_ticket(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class TicketingIface(GObject.GPointer):
    """
    :Constructors:

    ::

        TicketingIface()
    """

    parent_iface: GObject.TypeInterface = ...
    handle_get_ticket: Callable[[Ticketing, Gio.DBusMethodInvocation], bool] = ...
    get_details: Callable[[Ticketing], Optional[GLib.Variant]] = ...

class TicketingProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Ticketing
):
    """
    :Constructors:

    ::

        TicketingProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.TicketingProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.TicketingProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.TicketingProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.TicketingProxy

    Object GoaTicketingProxy

    Signals from GoaTicketing:
      handle-get-ticket (GDBusMethodInvocation) -> gboolean

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
        details: GLib.Variant
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: TicketingProxyPrivate = ...
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
        details: GLib.Variant = ...,
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
    def new_finish(cls, res: Gio.AsyncResult) -> TicketingProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> TicketingProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> TicketingProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> TicketingProxy: ...

class TicketingProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TicketingProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class TicketingProxyPrivate(GObject.GPointer): ...

class TicketingSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Ticketing):
    """
    :Constructors:

    ::

        TicketingSkeleton(**properties)
        new() -> Goa.TicketingSkeleton

    Object GoaTicketingSkeleton

    Signals from GoaTicketing:
      handle-get-ticket (GDBusMethodInvocation) -> gboolean

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
        details: GLib.Variant

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: TicketingSkeletonPrivate = ...
    def __init__(
        self, g_flags: Gio.DBusInterfaceSkeletonFlags = ..., details: GLib.Variant = ...
    ): ...
    @classmethod
    def new(cls) -> TicketingSkeleton: ...

class TicketingSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TicketingSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class TicketingSkeletonPrivate(GObject.GPointer): ...

class Todo(GObject.GInterface):
    """
    Interface GoaTodo

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class TodoIface(GObject.GPointer):
    """
    :Constructors:

    ::

        TodoIface()
    """

    parent_iface: GObject.TypeInterface = ...

class TodoProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Todo
):
    """
    :Constructors:

    ::

        TodoProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.TodoProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.TodoProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.TodoProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.TodoProxy

    Object GoaTodoProxy

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
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: TodoProxyPrivate = ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> TodoProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> TodoProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> TodoProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> TodoProxy: ...

class TodoProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TodoProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class TodoProxyPrivate(GObject.GPointer): ...

class TodoSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Todo):
    """
    :Constructors:

    ::

        TodoSkeleton(**properties)
        new() -> Goa.TodoSkeleton

    Object GoaTodoSkeleton

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

    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: TodoSkeletonPrivate = ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> TodoSkeleton: ...

class TodoSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TodoSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class TodoSkeletonPrivate(GObject.GPointer): ...

class Error(GObject.GEnum):
    ACCOUNT_EXISTS = 3
    DIALOG_DISMISSED = 2
    FAILED = 0
    NOT_AUTHORIZED = 4
    NOT_SUPPORTED = 1
    SSL = 5
    @staticmethod
    def quark() -> int: ...
