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

BACKEND_EXTENSION_POINT_NAME: str = "secret-backend"
COLLECTION_DEFAULT: str = "default"
COLLECTION_SESSION: str = "session"
MAJOR_VERSION: int = 0
MICRO_VERSION: int = 2
MINOR_VERSION: int = 21
_lock = ...  # FIXME Constant
_namespace: str = "Secret"
_version: str = "1"

def attributes_validate(schema: Schema, attributes: dict[None, None]) -> bool: ...
def backend_get(
    flags: BackendFlags,
    cancellable: Optional[Gio.Cancellable] = None,
    callback: Optional[Callable[..., None]] = None,
    *user_data: Any,
) -> None: ...
def backend_get_finish(result: Gio.AsyncResult) -> Backend: ...
def error_get_quark() -> int: ...
def get_schema(type: SchemaType) -> Schema: ...
def password_clear(
    schema: Optional[Schema],
    attributes: dict[str, str],
    cancellable: Optional[Gio.Cancellable] = None,
    callback: Optional[Callable[..., None]] = None,
    *user_data: Any,
) -> None: ...
def password_clear_finish(result: Gio.AsyncResult) -> bool: ...
def password_clear_sync(
    schema: Optional[Schema],
    attributes: dict[str, str],
    cancellable: Optional[Gio.Cancellable] = None,
) -> bool: ...
def password_lookup(
    schema: Optional[Schema],
    attributes: dict[str, str],
    cancellable: Optional[Gio.Cancellable] = None,
    callback: Optional[Callable[..., None]] = None,
    *user_data: Any,
) -> None: ...
def password_lookup_finish(result: Gio.AsyncResult) -> str: ...
def password_lookup_sync(
    schema: Optional[Schema],
    attributes: dict[str, str],
    cancellable: Optional[Gio.Cancellable] = None,
) -> str: ...
def password_search(
    schema: Optional[Schema],
    attributes: dict[str, str],
    flags: SearchFlags,
    cancellable: Optional[Gio.Cancellable] = None,
    callback: Optional[Callable[..., None]] = None,
    *user_data: Any,
) -> None: ...
def password_search_finish(result: Gio.AsyncResult) -> list[Retrievable]: ...
def password_search_sync(
    schema: Optional[Schema],
    attributes: dict[str, str],
    flags: SearchFlags,
    cancellable: Optional[Gio.Cancellable] = None,
) -> list[Retrievable]: ...
def password_store(
    schema: Optional[Schema],
    attributes: dict[str, str],
    collection: Optional[str],
    label: str,
    password: str,
    cancellable: Optional[Gio.Cancellable] = None,
    callback: Optional[Callable[..., None]] = None,
    *user_data: Any,
) -> None: ...
def password_store_binary(
    schema: Optional[Schema],
    attributes: dict[str, str],
    collection: Optional[str],
    label: str,
    value: Value,
    cancellable: Optional[Gio.Cancellable] = None,
    callback: Optional[Callable[..., None]] = None,
    *user_data: Any,
) -> None: ...
def password_store_binary_sync(
    schema: Optional[Schema],
    attributes: dict[str, str],
    collection: Optional[str],
    label: str,
    value: Value,
    cancellable: Optional[Gio.Cancellable] = None,
) -> bool: ...
def password_store_finish(result: Gio.AsyncResult) -> bool: ...
def password_store_sync(
    schema: Optional[Schema],
    attributes: dict[str, str],
    collection: Optional[str],
    label: str,
    password: str,
    cancellable: Optional[Gio.Cancellable] = None,
) -> bool: ...
def password_wipe(password: Optional[str] = None) -> None: ...

class Backend(GObject.GInterface):
    """
    Interface SecretBackend

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def get(
        flags: BackendFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def get_finish(result: Gio.AsyncResult) -> Backend: ...

class BackendInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        BackendInterface()
    """

    parent_iface: GObject.TypeInterface = ...
    ensure_for_flags: Callable[..., None] = ...
    ensure_for_flags_finish: Callable[[Backend, Gio.AsyncResult], bool] = ...
    store: Callable[..., None] = ...
    store_finish: Callable[[Backend, Gio.AsyncResult], bool] = ...
    lookup: Callable[..., None] = ...
    lookup_finish: Callable[[Backend, Gio.AsyncResult], Value] = ...
    clear: Callable[..., None] = ...
    clear_finish: Callable[[Backend, Gio.AsyncResult], bool] = ...
    search: Callable[..., None] = ...
    search_finish: None = ...

class Collection(Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable):
    """
    :Constructors:

    ::

        Collection(**properties)

    Object SecretCollection

    Properties from SecretCollection:
      service -> SecretService: Service
        Secret Service
      flags -> SecretCollectionFlags: Flags
        Collection flags
      items -> SecretObjectList: Items
        Items in collection
      label -> gchararray: Label
        Item label
      locked -> gboolean: Locked
        Item locked
      created -> guint64: Created
        Item creation date
      modified -> guint64: Modified
        Item modified date

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
        created: int
        flags: CollectionFlags
        label: str
        locked: bool
        modified: int
        service: Service
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
    parent: Gio.DBusProxy = ...
    pv: CollectionPrivate = ...
    def __init__(
        self,
        created: int = ...,
        flags: CollectionFlags = ...,
        label: str = ...,
        modified: int = ...,
        service: Service = ...,
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
    def create(
        service: Optional[Service],
        label: str,
        alias: Optional[str],
        flags: CollectionCreateFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def create_finish(result: Gio.AsyncResult) -> Collection: ...
    @staticmethod
    def create_sync(
        service: Optional[Service],
        label: str,
        alias: Optional[str],
        flags: CollectionCreateFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Collection: ...
    def delete(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def delete_finish(self, result: Gio.AsyncResult) -> bool: ...
    def delete_sync(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    @staticmethod
    def for_alias(
        service: Optional[Service],
        alias: str,
        flags: CollectionFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def for_alias_finish(result: Gio.AsyncResult) -> Optional[Collection]: ...
    @staticmethod
    def for_alias_sync(
        service: Optional[Service],
        alias: str,
        flags: CollectionFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Optional[Collection]: ...
    def get_created(self) -> int: ...
    def get_flags(self) -> CollectionFlags: ...
    def get_items(self) -> list[Item]: ...
    def get_label(self) -> str: ...
    def get_locked(self) -> bool: ...
    def get_modified(self) -> int: ...
    def get_service(self) -> Service: ...
    def load_items(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def load_items_finish(self, result: Gio.AsyncResult) -> bool: ...
    def load_items_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def refresh(self) -> None: ...
    def search(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        flags: SearchFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def search_finish(self, result: Gio.AsyncResult) -> list[Item]: ...
    def search_sync(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        flags: SearchFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> list[Item]: ...
    def set_label(
        self,
        label: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def set_label_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_label_sync(
        self, label: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...

class CollectionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CollectionClass()
    """

    parent_class: Gio.DBusProxyClass = ...
    padding: list[None] = ...

class CollectionPrivate(GObject.GPointer): ...

class Item(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Retrievable
):
    """
    :Constructors:

    ::

        Item(**properties)

    Object SecretItem

    Properties from SecretItem:
      service -> SecretService: Service
        Secret Service
      flags -> SecretItemFlags: Flags
        Item flags
      locked -> gboolean: Locked
        Item locked

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
        flags: ItemFlags
        locked: bool
        service: Service
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        attributes: dict[str, str]
        created: int
        label: str
        modified: int
        g_bus_type: Gio.BusType

    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    pv: ItemPrivate = ...
    def __init__(
        self,
        flags: ItemFlags = ...,
        service: Service = ...,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        attributes: dict[str, str] = ...,
        created: int = ...,
        label: str = ...,
        modified: int = ...,
    ): ...
    @staticmethod
    def create(
        collection: Collection,
        schema: Optional[Schema],
        attributes: dict[str, str],
        label: str,
        value: Value,
        flags: ItemCreateFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def create_finish(result: Gio.AsyncResult) -> Item: ...
    @staticmethod
    def create_sync(
        collection: Collection,
        schema: Optional[Schema],
        attributes: dict[str, str],
        label: str,
        value: Value,
        flags: ItemCreateFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Item: ...
    def delete(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def delete_finish(self, result: Gio.AsyncResult) -> bool: ...
    def delete_sync(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def get_attributes(self) -> dict[str, str]: ...
    def get_created(self) -> int: ...
    def get_flags(self) -> ItemFlags: ...
    def get_label(self) -> str: ...
    def get_locked(self) -> bool: ...
    def get_modified(self) -> int: ...
    def get_schema_name(self) -> Optional[str]: ...
    def get_secret(self) -> Optional[Value]: ...
    def get_service(self) -> Service: ...
    def load_secret(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def load_secret_finish(self, result: Gio.AsyncResult) -> bool: ...
    def load_secret_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    @staticmethod
    def load_secrets(
        items: list[Item],
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def load_secrets_finish(result: Gio.AsyncResult) -> bool: ...
    @staticmethod
    def load_secrets_sync(
        items: list[Item], cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def refresh(self) -> None: ...
    def set_attributes(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def set_attributes_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_attributes_sync(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def set_label(
        self,
        label: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def set_label_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_label_sync(
        self, label: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def set_secret(
        self,
        value: Value,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def set_secret_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_secret_sync(
        self, value: Value, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...

class ItemClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ItemClass()
    """

    parent_class: Gio.DBusProxyClass = ...
    padding: list[None] = ...

class ItemPrivate(GObject.GPointer): ...

class Prompt(Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable):
    """
    :Constructors:

    ::

        Prompt(**properties)

    Object SecretPrompt

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
    pv: PromptPrivate = ...
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
    def perform(
        self,
        window_id: Optional[str],
        return_type: GLib.VariantType,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def perform_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def perform_sync(
        self,
        window_id: Optional[str],
        cancellable: Optional[Gio.Cancellable],
        return_type: GLib.VariantType,
    ) -> GLib.Variant: ...
    def run(
        self,
        window_id: Optional[str],
        cancellable: Optional[Gio.Cancellable],
        return_type: GLib.VariantType,
    ) -> GLib.Variant: ...

class PromptClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PromptClass()
    """

    parent_class: Gio.DBusProxyClass = ...
    padding: list[None] = ...

class PromptPrivate(GObject.GPointer): ...

class Retrievable(GObject.GInterface):
    """
    Interface SecretRetrievable

    Signals from GObject:
      notify (GParam)
    """

    def get_attributes(self) -> dict[str, str]: ...
    def get_created(self) -> int: ...
    def get_label(self) -> str: ...
    def get_modified(self) -> int: ...
    def retrieve_secret(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def retrieve_secret_finish(self, result: Gio.AsyncResult) -> Optional[Value]: ...
    def retrieve_secret_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Optional[Value]: ...

class RetrievableInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        RetrievableInterface()
    """

    parent_iface: GObject.TypeInterface = ...
    retrieve_secret: Callable[..., None] = ...
    retrieve_secret_finish: Callable[
        [Retrievable, Gio.AsyncResult], Optional[Value]
    ] = ...

class Schema(GObject.GBoxed):
    """
    :Constructors:

    ::

        Schema()
        new(name:str, flags:Secret.SchemaFlags, attribute_names_and_types:dict) -> Secret.Schema
    """

    name: str = ...
    flags: SchemaFlags = ...
    attributes: list[SchemaAttribute] = ...
    reserved: int = ...
    reserved1: None = ...
    reserved2: None = ...
    reserved3: None = ...
    reserved4: None = ...
    reserved5: None = ...
    reserved6: None = ...
    reserved7: None = ...
    @classmethod
    def new(
        cls,
        name: str,
        flags: SchemaFlags,
        attribute_names_and_types: dict[str, SchemaAttributeType],
    ) -> Schema: ...
    def ref(self) -> Schema: ...
    def unref(self) -> None: ...

class SchemaAttribute(GObject.GBoxed):
    """
    :Constructors:

    ::

        SchemaAttribute()
    """

    name: str = ...
    type: SchemaAttributeType = ...

class Service(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Backend
):
    """
    :Constructors:

    ::

        Service(**properties)

    Object SecretService

    Properties from SecretService:
      collections -> SecretObjectList: Collections
        Secret Service Collections

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
        flags: ServiceFlags
        g_bus_type: Gio.BusType

    props: Props = ...
    parent: Gio.DBusProxy = ...
    pv: ServicePrivate = ...
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
        flags: ServiceFlags = ...,
    ): ...
    def clear(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def clear_finish(self, result: Gio.AsyncResult) -> bool: ...
    def clear_sync(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def create_item_dbus_path_sync(
        self,
        collection_path: str,
        properties: dict[str, GLib.Variant],
        value: Value,
        flags: ItemCreateFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> str: ...
    def decode_dbus_secret(self, value: GLib.Variant) -> Value: ...
    @staticmethod
    def disconnect() -> None: ...
    def do_get_collection_gtype(self) -> Type: ...
    def do_get_item_gtype(self) -> Type: ...
    def do_prompt_async(
        self,
        prompt: Prompt,
        return_type: GLib.VariantType,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def do_prompt_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def do_prompt_sync(
        self,
        prompt: Prompt,
        cancellable: Optional[Gio.Cancellable],
        return_type: GLib.VariantType,
    ) -> GLib.Variant: ...
    def encode_dbus_secret(self, value: Value) -> GLib.Variant: ...
    def ensure_session(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def ensure_session_finish(self, result: Gio.AsyncResult) -> bool: ...
    def ensure_session_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    @staticmethod
    def get(
        flags: ServiceFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_collection_gtype(self) -> Type: ...
    def get_collections(self) -> Optional[list[Collection]]: ...
    @staticmethod
    def get_finish(result: Gio.AsyncResult) -> Service: ...
    def get_flags(self) -> ServiceFlags: ...
    def get_item_gtype(self) -> Type: ...
    def get_session_algorithms(self) -> Optional[str]: ...
    def get_session_dbus_path(self) -> Optional[str]: ...
    @staticmethod
    def get_sync(
        flags: ServiceFlags, cancellable: Optional[Gio.Cancellable] = None
    ) -> Service: ...
    def load_collections(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def load_collections_finish(self, result: Gio.AsyncResult) -> bool: ...
    def load_collections_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def lock(
        self,
        objects: list[Gio.DBusProxy],
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def lock_finish(
        self, result: Gio.AsyncResult
    ) -> Tuple[int, list[Gio.DBusProxy]]: ...
    def lock_sync(
        self,
        objects: list[Gio.DBusProxy],
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[int, list[Gio.DBusProxy]]: ...
    def lookup(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def lookup_finish(self, result: Gio.AsyncResult) -> Value: ...
    def lookup_sync(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Value: ...
    @staticmethod
    def open(
        service_gtype: Type,
        service_bus_name: Optional[str],
        flags: ServiceFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def open_finish(result: Gio.AsyncResult) -> Service: ...
    @staticmethod
    def open_sync(
        service_gtype: Type,
        service_bus_name: Optional[str],
        flags: ServiceFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Service: ...
    def prompt(
        self,
        prompt: Prompt,
        return_type: Optional[GLib.VariantType] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def prompt_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def prompt_sync(
        self,
        prompt: Prompt,
        cancellable: Optional[Gio.Cancellable],
        return_type: GLib.VariantType,
    ) -> GLib.Variant: ...
    def search(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        flags: SearchFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def search_finish(self, result: Gio.AsyncResult) -> list[Item]: ...
    def search_sync(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        flags: SearchFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> list[Item]: ...
    def set_alias(
        self,
        alias: str,
        collection: Optional[Collection] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def set_alias_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_alias_sync(
        self,
        alias: str,
        collection: Optional[Collection] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def store(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        collection: Optional[str],
        label: str,
        value: Value,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def store_finish(self, result: Gio.AsyncResult) -> bool: ...
    def store_sync(
        self,
        schema: Optional[Schema],
        attributes: dict[str, str],
        collection: Optional[str],
        label: str,
        value: Value,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def unlock(
        self,
        objects: list[Gio.DBusProxy],
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def unlock_finish(
        self, result: Gio.AsyncResult
    ) -> Tuple[int, list[Gio.DBusProxy]]: ...
    def unlock_sync(
        self,
        objects: list[Gio.DBusProxy],
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[int, list[Gio.DBusProxy]]: ...

class ServiceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ServiceClass()
    """

    parent_class: Gio.DBusProxyClass = ...
    collection_gtype: Type = ...
    item_gtype: Type = ...
    prompt_sync: Callable[
        [Service, Prompt, Optional[Gio.Cancellable], GLib.VariantType], GLib.Variant
    ] = ...
    prompt_async: Callable[..., None] = ...
    prompt_finish: Callable[[Service, Gio.AsyncResult], GLib.Variant] = ...
    get_collection_gtype: Callable[[Service], Type] = ...
    get_item_gtype: Callable[[Service], Type] = ...
    padding: list[None] = ...

class ServicePrivate(GObject.GPointer): ...

class Value(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(secret:str, length:int, content_type:str) -> Secret.Value
        new_full(secret:str, length:int, content_type:str, destroy:GLib.DestroyNotify) -> Secret.Value
    """

    def get(self) -> bytes: ...
    def get_content_type(self) -> str: ...
    def get_text(self) -> Optional[str]: ...
    @classmethod
    def new(cls, secret: str, length: int, content_type: str) -> Value: ...
    @classmethod
    def new_full(
        cls,
        secret: str,
        length: int,
        content_type: str,
        destroy: Callable[[None], None],
    ) -> Value: ...
    def ref(self) -> Value: ...
    def unref(self) -> None: ...
    def unref_to_password(self) -> Tuple[str, int]: ...

class CollectionCreateFlags(GObject.GFlags):
    NONE = 0

class CollectionFlags(GObject.GFlags):
    LOAD_ITEMS = 2
    NONE = 0

class ItemCreateFlags(GObject.GFlags):
    NONE = 0
    REPLACE = 2

class ItemFlags(GObject.GFlags):
    LOAD_SECRET = 2
    NONE = 0

class SchemaFlags(GObject.GFlags):
    DONT_MATCH_NAME = 2
    NONE = 0

class SearchFlags(GObject.GFlags):
    ALL = 2
    LOAD_SECRETS = 8
    NONE = 0
    UNLOCK = 4

class ServiceFlags(GObject.GFlags):
    LOAD_COLLECTIONS = 4
    NONE = 0
    OPEN_SESSION = 2

class BackendFlags(GObject.GEnum):
    LOAD_COLLECTIONS = 4
    NONE = 0
    OPEN_SESSION = 2

class Error(GObject.GEnum):
    ALREADY_EXISTS = 4
    EMPTY_TABLE = 9
    INVALID_FILE_FORMAT = 5
    IS_LOCKED = 2
    MISMATCHED_SCHEMA = 6
    NO_MATCHING_ATTRIBUTE = 7
    NO_SUCH_OBJECT = 3
    PROTOCOL = 1
    WRONG_TYPE = 8
    @staticmethod
    def get_quark() -> int: ...

class SchemaAttributeType(GObject.GEnum):
    BOOLEAN = 2
    INTEGER = 1
    STRING = 0

class SchemaType(GObject.GEnum):
    COMPAT_NETWORK = 1
    NOTE = 0
