import typing

from gi.repository import GLib
from gi.repository import GObject

T = typing.TypeVar("T")

DBUS_METHOD_INVOCATION_HANDLED: bool = True
DBUS_METHOD_INVOCATION_UNHANDLED: bool = False
DEBUG_CONTROLLER_EXTENSION_POINT_NAME: str = "gio-debug-controller"
DESKTOP_APP_INFO_LOOKUP_EXTENSION_POINT_NAME: str = "gio-desktop-app-info-lookup"
DRIVE_IDENTIFIER_KIND_UNIX_DEVICE: str = "unix-device"
FILE_ATTRIBUTE_ACCESS_CAN_DELETE: str = "access::can-delete"
FILE_ATTRIBUTE_ACCESS_CAN_EXECUTE: str = "access::can-execute"
FILE_ATTRIBUTE_ACCESS_CAN_READ: str = "access::can-read"
FILE_ATTRIBUTE_ACCESS_CAN_RENAME: str = "access::can-rename"
FILE_ATTRIBUTE_ACCESS_CAN_TRASH: str = "access::can-trash"
FILE_ATTRIBUTE_ACCESS_CAN_WRITE: str = "access::can-write"
FILE_ATTRIBUTE_DOS_IS_ARCHIVE: str = "dos::is-archive"
FILE_ATTRIBUTE_DOS_IS_MOUNTPOINT: str = "dos::is-mountpoint"
FILE_ATTRIBUTE_DOS_IS_SYSTEM: str = "dos::is-system"
FILE_ATTRIBUTE_DOS_REPARSE_POINT_TAG: str = "dos::reparse-point-tag"
FILE_ATTRIBUTE_ETAG_VALUE: str = "etag::value"
FILE_ATTRIBUTE_FILESYSTEM_FREE: str = "filesystem::free"
FILE_ATTRIBUTE_FILESYSTEM_READONLY: str = "filesystem::readonly"
FILE_ATTRIBUTE_FILESYSTEM_REMOTE: str = "filesystem::remote"
FILE_ATTRIBUTE_FILESYSTEM_SIZE: str = "filesystem::size"
FILE_ATTRIBUTE_FILESYSTEM_TYPE: str = "filesystem::type"
FILE_ATTRIBUTE_FILESYSTEM_USED: str = "filesystem::used"
FILE_ATTRIBUTE_FILESYSTEM_USE_PREVIEW: str = "filesystem::use-preview"
FILE_ATTRIBUTE_GVFS_BACKEND: str = "gvfs::backend"
FILE_ATTRIBUTE_ID_FILE: str = "id::file"
FILE_ATTRIBUTE_ID_FILESYSTEM: str = "id::filesystem"
FILE_ATTRIBUTE_MOUNTABLE_CAN_EJECT: str = "mountable::can-eject"
FILE_ATTRIBUTE_MOUNTABLE_CAN_MOUNT: str = "mountable::can-mount"
FILE_ATTRIBUTE_MOUNTABLE_CAN_POLL: str = "mountable::can-poll"
FILE_ATTRIBUTE_MOUNTABLE_CAN_START: str = "mountable::can-start"
FILE_ATTRIBUTE_MOUNTABLE_CAN_START_DEGRADED: str = "mountable::can-start-degraded"
FILE_ATTRIBUTE_MOUNTABLE_CAN_STOP: str = "mountable::can-stop"
FILE_ATTRIBUTE_MOUNTABLE_CAN_UNMOUNT: str = "mountable::can-unmount"
FILE_ATTRIBUTE_MOUNTABLE_HAL_UDI: str = "mountable::hal-udi"
FILE_ATTRIBUTE_MOUNTABLE_IS_MEDIA_CHECK_AUTOMATIC: str = (
    "mountable::is-media-check-automatic"
)
FILE_ATTRIBUTE_MOUNTABLE_START_STOP_TYPE: str = "mountable::start-stop-type"
FILE_ATTRIBUTE_MOUNTABLE_UNIX_DEVICE: str = "mountable::unix-device"
FILE_ATTRIBUTE_MOUNTABLE_UNIX_DEVICE_FILE: str = "mountable::unix-device-file"
FILE_ATTRIBUTE_OWNER_GROUP: str = "owner::group"
FILE_ATTRIBUTE_OWNER_USER: str = "owner::user"
FILE_ATTRIBUTE_OWNER_USER_REAL: str = "owner::user-real"
FILE_ATTRIBUTE_PREVIEW_ICON: str = "preview::icon"
FILE_ATTRIBUTE_RECENT_MODIFIED: str = "recent::modified"
FILE_ATTRIBUTE_SELINUX_CONTEXT: str = "selinux::context"
FILE_ATTRIBUTE_STANDARD_ALLOCATED_SIZE: str = "standard::allocated-size"
FILE_ATTRIBUTE_STANDARD_CONTENT_TYPE: str = "standard::content-type"
FILE_ATTRIBUTE_STANDARD_COPY_NAME: str = "standard::copy-name"
FILE_ATTRIBUTE_STANDARD_DESCRIPTION: str = "standard::description"
FILE_ATTRIBUTE_STANDARD_DISPLAY_NAME: str = "standard::display-name"
FILE_ATTRIBUTE_STANDARD_EDIT_NAME: str = "standard::edit-name"
FILE_ATTRIBUTE_STANDARD_FAST_CONTENT_TYPE: str = "standard::fast-content-type"
FILE_ATTRIBUTE_STANDARD_ICON: str = "standard::icon"
FILE_ATTRIBUTE_STANDARD_IS_BACKUP: str = "standard::is-backup"
FILE_ATTRIBUTE_STANDARD_IS_HIDDEN: str = "standard::is-hidden"
FILE_ATTRIBUTE_STANDARD_IS_SYMLINK: str = "standard::is-symlink"
FILE_ATTRIBUTE_STANDARD_IS_VIRTUAL: str = "standard::is-virtual"
FILE_ATTRIBUTE_STANDARD_IS_VOLATILE: str = "standard::is-volatile"
FILE_ATTRIBUTE_STANDARD_NAME: str = "standard::name"
FILE_ATTRIBUTE_STANDARD_SIZE: str = "standard::size"
FILE_ATTRIBUTE_STANDARD_SORT_ORDER: str = "standard::sort-order"
FILE_ATTRIBUTE_STANDARD_SYMBOLIC_ICON: str = "standard::symbolic-icon"
FILE_ATTRIBUTE_STANDARD_SYMLINK_TARGET: str = "standard::symlink-target"
FILE_ATTRIBUTE_STANDARD_TARGET_URI: str = "standard::target-uri"
FILE_ATTRIBUTE_STANDARD_TYPE: str = "standard::type"
FILE_ATTRIBUTE_THUMBNAILING_FAILED: str = "thumbnail::failed"
FILE_ATTRIBUTE_THUMBNAILING_FAILED_LARGE: str = "thumbnail::failed-large"
FILE_ATTRIBUTE_THUMBNAILING_FAILED_NORMAL: str = "thumbnail::failed-normal"
FILE_ATTRIBUTE_THUMBNAILING_FAILED_XLARGE: str = "thumbnail::failed-xlarge"
FILE_ATTRIBUTE_THUMBNAILING_FAILED_XXLARGE: str = "thumbnail::failed-xxlarge"
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID: str = "thumbnail::is-valid"
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_LARGE: str = "thumbnail::is-valid-large"
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_NORMAL: str = "thumbnail::is-valid-normal"
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_XLARGE: str = "thumbnail::is-valid-xlarge"
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_XXLARGE: str = "thumbnail::is-valid-xxlarge"
FILE_ATTRIBUTE_THUMBNAIL_PATH: str = "thumbnail::path"
FILE_ATTRIBUTE_THUMBNAIL_PATH_LARGE: str = "thumbnail::path-large"
FILE_ATTRIBUTE_THUMBNAIL_PATH_NORMAL: str = "thumbnail::path-normal"
FILE_ATTRIBUTE_THUMBNAIL_PATH_XLARGE: str = "thumbnail::path-xlarge"
FILE_ATTRIBUTE_THUMBNAIL_PATH_XXLARGE: str = "thumbnail::path-xxlarge"
FILE_ATTRIBUTE_TIME_ACCESS: str = "time::access"
FILE_ATTRIBUTE_TIME_ACCESS_NSEC: str = "time::access-nsec"
FILE_ATTRIBUTE_TIME_ACCESS_USEC: str = "time::access-usec"
FILE_ATTRIBUTE_TIME_CHANGED: str = "time::changed"
FILE_ATTRIBUTE_TIME_CHANGED_NSEC: str = "time::changed-nsec"
FILE_ATTRIBUTE_TIME_CHANGED_USEC: str = "time::changed-usec"
FILE_ATTRIBUTE_TIME_CREATED: str = "time::created"
FILE_ATTRIBUTE_TIME_CREATED_NSEC: str = "time::created-nsec"
FILE_ATTRIBUTE_TIME_CREATED_USEC: str = "time::created-usec"
FILE_ATTRIBUTE_TIME_MODIFIED: str = "time::modified"
FILE_ATTRIBUTE_TIME_MODIFIED_NSEC: str = "time::modified-nsec"
FILE_ATTRIBUTE_TIME_MODIFIED_USEC: str = "time::modified-usec"
FILE_ATTRIBUTE_TRASH_DELETION_DATE: str = "trash::deletion-date"
FILE_ATTRIBUTE_TRASH_ITEM_COUNT: str = "trash::item-count"
FILE_ATTRIBUTE_TRASH_ORIG_PATH: str = "trash::orig-path"
FILE_ATTRIBUTE_UNIX_BLOCKS: str = "unix::blocks"
FILE_ATTRIBUTE_UNIX_BLOCK_SIZE: str = "unix::block-size"
FILE_ATTRIBUTE_UNIX_DEVICE: str = "unix::device"
FILE_ATTRIBUTE_UNIX_GID: str = "unix::gid"
FILE_ATTRIBUTE_UNIX_INODE: str = "unix::inode"
FILE_ATTRIBUTE_UNIX_IS_MOUNTPOINT: str = "unix::is-mountpoint"
FILE_ATTRIBUTE_UNIX_MODE: str = "unix::mode"
FILE_ATTRIBUTE_UNIX_NLINK: str = "unix::nlink"
FILE_ATTRIBUTE_UNIX_RDEV: str = "unix::rdev"
FILE_ATTRIBUTE_UNIX_UID: str = "unix::uid"
MEMORY_MONITOR_EXTENSION_POINT_NAME: str = "gio-memory-monitor"
MENU_ATTRIBUTE_ACTION: str = "action"
MENU_ATTRIBUTE_ACTION_NAMESPACE: str = "action-namespace"
MENU_ATTRIBUTE_ICON: str = "icon"
MENU_ATTRIBUTE_LABEL: str = "label"
MENU_ATTRIBUTE_TARGET: str = "target"
MENU_EXPORTER_MAX_SECTION_SIZE: int = 1000
MENU_LINK_SECTION: str = "section"
MENU_LINK_SUBMENU: str = "submenu"
NATIVE_VOLUME_MONITOR_EXTENSION_POINT_NAME: str = "gio-native-volume-monitor"
NETWORK_MONITOR_EXTENSION_POINT_NAME: str = "gio-network-monitor"
POWER_PROFILE_MONITOR_EXTENSION_POINT_NAME: str = "gio-power-profile-monitor"
PROXY_EXTENSION_POINT_NAME: str = "gio-proxy"
PROXY_RESOLVER_EXTENSION_POINT_NAME: str = "gio-proxy-resolver"
SETTINGS_BACKEND_EXTENSION_POINT_NAME: str = "gsettings-backend"
TLS_BACKEND_EXTENSION_POINT_NAME: str = "gio-tls-backend"
TLS_DATABASE_PURPOSE_AUTHENTICATE_CLIENT: str = "1.3.6.1.5.5.7.3.2"
TLS_DATABASE_PURPOSE_AUTHENTICATE_SERVER: str = "1.3.6.1.5.5.7.3.1"
VFS_EXTENSION_POINT_NAME: str = "gio-vfs"
VOLUME_IDENTIFIER_KIND_CLASS: str = "class"
VOLUME_IDENTIFIER_KIND_HAL_UDI: str = "hal-udi"
VOLUME_IDENTIFIER_KIND_LABEL: str = "label"
VOLUME_IDENTIFIER_KIND_NFS_MOUNT: str = "nfs-mount"
VOLUME_IDENTIFIER_KIND_UNIX_DEVICE: str = "unix-device"
VOLUME_IDENTIFIER_KIND_UUID: str = "uuid"
VOLUME_MONITOR_EXTENSION_POINT_NAME: str = "gio-volume-monitor"
_introspection_module = ...  # FIXME Constant
_lock = ...  # FIXME Constant
_namespace: str = "Gio"
_overrides_module = ...  # FIXME Constant
_version: str = "2.0"

def action_name_is_valid(action_name: str) -> bool: ...
def action_parse_detailed_name(
    detailed_name: str,
) -> typing.Tuple[bool, str, GLib.Variant]: ...
def action_print_detailed_name(
    action_name: str, target_value: typing.Optional[GLib.Variant] = None
) -> str: ...
def app_info_create_from_commandline(
    commandline: str, application_name: typing.Optional[str], flags: AppInfoCreateFlags
) -> AppInfo: ...
def app_info_get_all() -> list[AppInfo]: ...
def app_info_get_all_for_type(content_type: str) -> list[AppInfo]: ...
def app_info_get_default_for_type(
    content_type: str, must_support_uris: bool
) -> typing.Optional[AppInfo]: ...
def app_info_get_default_for_type_async(
    content_type: str,
    must_support_uris: bool,
    cancellable: typing.Optional[Cancellable] = None,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *user_data: typing.Any,
) -> None: ...
def app_info_get_default_for_type_finish(result: AsyncResult) -> AppInfo: ...
def app_info_get_default_for_uri_scheme(
    uri_scheme: str,
) -> typing.Optional[AppInfo]: ...
def app_info_get_default_for_uri_scheme_async(
    uri_scheme: str,
    cancellable: typing.Optional[Cancellable] = None,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *user_data: typing.Any,
) -> None: ...
def app_info_get_default_for_uri_scheme_finish(result: AsyncResult) -> AppInfo: ...
def app_info_get_fallback_for_type(content_type: str) -> list[AppInfo]: ...
def app_info_get_recommended_for_type(content_type: str) -> list[AppInfo]: ...
def app_info_launch_default_for_uri(
    uri: str, context: typing.Optional[AppLaunchContext] = None
) -> bool: ...
def app_info_launch_default_for_uri_async(
    uri: str,
    context: typing.Optional[AppLaunchContext] = None,
    cancellable: typing.Optional[Cancellable] = None,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *user_data: typing.Any,
) -> None: ...
def app_info_launch_default_for_uri_finish(result: AsyncResult) -> bool: ...
def app_info_reset_type_associations(content_type: str) -> None: ...
def async_initable_newv_async(
    object_type: typing.Type[typing.Any],
    n_parameters: int,
    parameters: GObject.Parameter,
    io_priority: int,
    cancellable: typing.Optional[Cancellable] = None,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *user_data: typing.Any,
) -> None: ...
def bus_get(
    bus_type: BusType,
    cancellable: typing.Optional[Cancellable] = None,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *user_data: typing.Any,
) -> None: ...
def bus_get_finish(res: AsyncResult) -> DBusConnection: ...
def bus_get_sync(
    bus_type: BusType, cancellable: typing.Optional[Cancellable] = None
) -> DBusConnection: ...
def bus_own_name(
    bus_type: BusType,
    name: str,
    flags: BusNameOwnerFlags,
    bus_acquired_closure: typing.Optional[typing.Callable[..., typing.Any]] = None,
    name_acquired_closure: typing.Optional[typing.Callable[..., typing.Any]] = None,
    name_lost_closure: typing.Optional[typing.Callable[..., typing.Any]] = None,
) -> int: ...
def bus_own_name_on_connection(
    connection: DBusConnection,
    name: str,
    flags: BusNameOwnerFlags,
    name_acquired_closure: typing.Optional[typing.Callable[..., typing.Any]] = None,
    name_lost_closure: typing.Optional[typing.Callable[..., typing.Any]] = None,
) -> int: ...
def bus_unown_name(owner_id: int) -> None: ...
def bus_unwatch_name(watcher_id: int) -> None: ...
def bus_watch_name(
    bus_type: BusType,
    name: str,
    flags: BusNameWatcherFlags,
    name_appeared_closure: typing.Optional[typing.Callable[..., typing.Any]] = None,
    name_vanished_closure: typing.Optional[typing.Callable[..., typing.Any]] = None,
) -> int: ...
def bus_watch_name_on_connection(
    connection: DBusConnection,
    name: str,
    flags: BusNameWatcherFlags,
    name_appeared_closure: typing.Optional[typing.Callable[..., typing.Any]] = None,
    name_vanished_closure: typing.Optional[typing.Callable[..., typing.Any]] = None,
) -> int: ...
def content_type_can_be_executable(type: str) -> bool: ...
def content_type_equals(type1: str, type2: str) -> bool: ...
def content_type_from_mime_type(mime_type: str) -> typing.Optional[str]: ...
def content_type_get_description(type: str) -> str: ...
def content_type_get_generic_icon_name(type: str) -> typing.Optional[str]: ...
def content_type_get_icon(type: str) -> Icon: ...
def content_type_get_mime_dirs() -> list[str]: ...
def content_type_get_mime_type(type: str) -> typing.Optional[str]: ...
def content_type_get_symbolic_icon(type: str) -> Icon: ...
def content_type_guess(
    filename: typing.Optional[str] = None,
    data: typing.Optional[typing.Sequence[int]] = None,
) -> typing.Tuple[str, bool]: ...
def content_type_guess_for_tree(root: File) -> list[str]: ...
def content_type_is_a(type: str, supertype: str) -> bool: ...
def content_type_is_mime_type(type: str, mime_type: str) -> bool: ...
def content_type_is_unknown(type: str) -> bool: ...
def content_type_set_mime_dirs(
    dirs: typing.Optional[typing.Sequence[str]] = None,
) -> None: ...
def content_types_get_registered() -> list[str]: ...
def dbus_address_escape_value(string: str) -> str: ...
def dbus_address_get_for_bus_sync(
    bus_type: BusType, cancellable: typing.Optional[Cancellable] = None
) -> str: ...
def dbus_address_get_stream(
    address: str,
    cancellable: typing.Optional[Cancellable] = None,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *user_data: typing.Any,
) -> None: ...
def dbus_address_get_stream_finish(res: AsyncResult) -> typing.Tuple[IOStream, str]: ...
def dbus_address_get_stream_sync(
    address: str, cancellable: typing.Optional[Cancellable] = None
) -> typing.Tuple[IOStream, str]: ...
def dbus_annotation_info_lookup(
    annotations: typing.Optional[typing.Sequence[DBusAnnotationInfo]], name: str
) -> typing.Optional[str]: ...
def dbus_error_encode_gerror(error: GLib.Error) -> str: ...
def dbus_error_get_remote_error(error: GLib.Error) -> typing.Optional[str]: ...
def dbus_error_is_remote_error(error: GLib.Error) -> bool: ...
def dbus_error_new_for_dbus_error(
    dbus_error_name: str, dbus_error_message: str
) -> GLib.Error: ...
def dbus_error_quark() -> int: ...
def dbus_error_register_error(
    error_domain: int, error_code: int, dbus_error_name: str
) -> bool: ...
def dbus_error_register_error_domain(
    error_domain_quark_name: str,
    quark_volatile: int,
    entries: typing.Sequence[DBusErrorEntry],
) -> None: ...
def dbus_error_strip_remote_error(error: GLib.Error) -> bool: ...
def dbus_error_unregister_error(
    error_domain: int, error_code: int, dbus_error_name: str
) -> bool: ...
def dbus_escape_object_path(s: str) -> str: ...
def dbus_escape_object_path_bytestring(bytes: typing.Sequence[int]) -> str: ...
def dbus_generate_guid() -> str: ...
def dbus_gvalue_to_gvariant(
    gvalue: typing.Any, type: GLib.VariantType
) -> GLib.Variant: ...
def dbus_gvariant_to_gvalue(value: GLib.Variant) -> typing.Any: ...
def dbus_is_address(string: str) -> bool: ...
def dbus_is_error_name(string: str) -> bool: ...
def dbus_is_guid(string: str) -> bool: ...
def dbus_is_interface_name(string: str) -> bool: ...
def dbus_is_member_name(string: str) -> bool: ...
def dbus_is_name(string: str) -> bool: ...
def dbus_is_supported_address(string: str) -> bool: ...
def dbus_is_unique_name(string: str) -> bool: ...
def dbus_unescape_object_path(s: str) -> typing.Optional[bytes]: ...
def dtls_client_connection_new(
    base_socket: DatagramBased,
    server_identity: typing.Optional[SocketConnectable] = None,
) -> DtlsClientConnection: ...
def dtls_server_connection_new(
    base_socket: DatagramBased, certificate: typing.Optional[TlsCertificate] = None
) -> DtlsServerConnection: ...
def file_new_build_filenamev(args: typing.Sequence[str]) -> File: ...
def file_new_for_commandline_arg(arg: str) -> File: ...
def file_new_for_commandline_arg_and_cwd(arg: str, cwd: str) -> File: ...
def file_new_for_path(path: str) -> File: ...
def file_new_for_uri(uri: str) -> File: ...
def file_new_tmp(
    tmpl: typing.Optional[str] = None,
) -> typing.Tuple[File, FileIOStream]: ...
def file_new_tmp_async(
    tmpl: typing.Optional[str],
    io_priority: int,
    cancellable: typing.Optional[Cancellable] = None,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *user_data: typing.Any,
) -> None: ...
def file_new_tmp_dir_async(
    tmpl: typing.Optional[str],
    io_priority: int,
    cancellable: typing.Optional[Cancellable] = None,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *user_data: typing.Any,
) -> None: ...
def file_new_tmp_dir_finish(result: AsyncResult) -> File: ...
def file_new_tmp_finish(result: AsyncResult) -> typing.Tuple[File, FileIOStream]: ...
def file_parse_name(parse_name: str) -> File: ...
def icon_deserialize(value: GLib.Variant) -> typing.Optional[Icon]: ...
def icon_new_for_string(str: str) -> Icon: ...
def initable_newv(
    object_type: typing.Type[typing.Any],
    parameters: typing.Sequence[GObject.Parameter],
    cancellable: typing.Optional[Cancellable] = None,
) -> GObject.Object: ...
def io_error_from_errno(err_no: int) -> IOErrorEnum: ...
def io_error_from_file_error(file_error: GLib.FileError) -> IOErrorEnum: ...
def io_error_quark() -> int: ...
def io_extension_point_implement(
    extension_point_name: str,
    type: typing.Type[typing.Any],
    extension_name: str,
    priority: int,
) -> IOExtension: ...
def io_extension_point_lookup(name: str) -> IOExtensionPoint: ...
def io_extension_point_register(name: str) -> IOExtensionPoint: ...
def io_modules_load_all_in_directory(dirname: str) -> list[IOModule]: ...
def io_modules_load_all_in_directory_with_scope(
    dirname: str, scope: IOModuleScope
) -> list[IOModule]: ...
def io_modules_scan_all_in_directory(dirname: str) -> None: ...
def io_modules_scan_all_in_directory_with_scope(
    dirname: str, scope: IOModuleScope
) -> None: ...
def io_scheduler_cancel_all_jobs() -> None: ...
def io_scheduler_push_job(
    job_func: typing.Callable[..., bool],
    io_priority: int,
    cancellable: typing.Optional[Cancellable] = None,
    *user_data: typing.Any,
) -> None: ...
def keyfile_settings_backend_new(
    filename: str, root_path: str, root_group: typing.Optional[str] = None
) -> SettingsBackend: ...
def memory_monitor_dup_default() -> MemoryMonitor: ...
def memory_settings_backend_new() -> SettingsBackend: ...
def network_monitor_get_default() -> NetworkMonitor: ...
def networking_init() -> None: ...
def null_settings_backend_new() -> SettingsBackend: ...
def pollable_source_new(pollable_stream: GObject.Object) -> GLib.Source: ...
def pollable_source_new_full(
    pollable_stream: GObject.Object,
    child_source: typing.Optional[GLib.Source] = None,
    cancellable: typing.Optional[Cancellable] = None,
) -> GLib.Source: ...
def pollable_stream_read(
    stream: InputStream,
    buffer: typing.Sequence[int],
    blocking: bool,
    cancellable: typing.Optional[Cancellable] = None,
) -> int: ...
def pollable_stream_write(
    stream: OutputStream,
    buffer: typing.Sequence[int],
    blocking: bool,
    cancellable: typing.Optional[Cancellable] = None,
) -> int: ...
def pollable_stream_write_all(
    stream: OutputStream,
    buffer: typing.Sequence[int],
    blocking: bool,
    cancellable: typing.Optional[Cancellable] = None,
) -> typing.Tuple[bool, int]: ...
def power_profile_monitor_dup_default() -> PowerProfileMonitor: ...
def proxy_get_default_for_protocol(protocol: str) -> typing.Optional[Proxy]: ...
def proxy_resolver_get_default() -> ProxyResolver: ...
def resolver_error_quark() -> int: ...
def resource_error_quark() -> int: ...
def resource_load(filename: str) -> Resource: ...
def resources_enumerate_children(
    path: str, lookup_flags: ResourceLookupFlags
) -> list[str]: ...
def resources_get_info(
    path: str, lookup_flags: ResourceLookupFlags
) -> typing.Tuple[bool, int, int]: ...
def resources_lookup_data(
    path: str, lookup_flags: ResourceLookupFlags
) -> GLib.Bytes: ...
def resources_open_stream(
    path: str, lookup_flags: ResourceLookupFlags
) -> InputStream: ...
def resources_register(resource: Resource) -> None: ...
def resources_unregister(resource: Resource) -> None: ...
def settings_schema_source_get_default() -> typing.Optional[SettingsSchemaSource]: ...
def simple_async_report_gerror_in_idle(
    object: typing.Optional[GObject.Object],
    callback: typing.Optional[typing.Callable[..., None]],
    error: GLib.Error,
    *user_data: typing.Any,
) -> None: ...
def tls_backend_get_default() -> TlsBackend: ...
def tls_channel_binding_error_quark() -> int: ...
def tls_client_connection_new(
    base_io_stream: IOStream, server_identity: typing.Optional[SocketConnectable] = None
) -> TlsClientConnection: ...
def tls_error_quark() -> int: ...
def tls_file_database_new(anchors: str) -> TlsFileDatabase: ...
def tls_server_connection_new(
    base_io_stream: IOStream, certificate: typing.Optional[TlsCertificate] = None
) -> TlsServerConnection: ...
def unix_is_mount_path_system_internal(mount_path: str) -> bool: ...
def unix_is_system_device_path(device_path: str) -> bool: ...
def unix_is_system_fs_type(fs_type: str) -> bool: ...
def unix_mount_at(
    mount_path: str,
) -> typing.Tuple[typing.Optional[UnixMountEntry], int]: ...
def unix_mount_compare(mount1: UnixMountEntry, mount2: UnixMountEntry) -> int: ...
def unix_mount_copy(mount_entry: UnixMountEntry) -> UnixMountEntry: ...
def unix_mount_for(
    file_path: str,
) -> typing.Tuple[typing.Optional[UnixMountEntry], int]: ...
def unix_mount_free(mount_entry: UnixMountEntry) -> None: ...
def unix_mount_get_device_path(mount_entry: UnixMountEntry) -> str: ...
def unix_mount_get_fs_type(mount_entry: UnixMountEntry) -> str: ...
def unix_mount_get_mount_path(mount_entry: UnixMountEntry) -> str: ...
def unix_mount_get_options(mount_entry: UnixMountEntry) -> typing.Optional[str]: ...
def unix_mount_get_root_path(mount_entry: UnixMountEntry) -> typing.Optional[str]: ...
def unix_mount_guess_can_eject(mount_entry: UnixMountEntry) -> bool: ...
def unix_mount_guess_icon(mount_entry: UnixMountEntry) -> Icon: ...
def unix_mount_guess_name(mount_entry: UnixMountEntry) -> str: ...
def unix_mount_guess_should_display(mount_entry: UnixMountEntry) -> bool: ...
def unix_mount_guess_symbolic_icon(mount_entry: UnixMountEntry) -> Icon: ...
def unix_mount_is_readonly(mount_entry: UnixMountEntry) -> bool: ...
def unix_mount_is_system_internal(mount_entry: UnixMountEntry) -> bool: ...
def unix_mount_point_at(
    mount_path: str,
) -> typing.Tuple[typing.Optional[UnixMountPoint], int]: ...
def unix_mount_points_changed_since(time: int) -> bool: ...
def unix_mount_points_get() -> typing.Tuple[list[UnixMountPoint], int]: ...
def unix_mount_points_get_from_file(
    table_path: str,
) -> typing.Tuple[typing.Optional[list[UnixMountPoint]], int]: ...
def unix_mounts_changed_since(time: int) -> bool: ...
def unix_mounts_get() -> typing.Tuple[list[UnixMountEntry], int]: ...
def unix_mounts_get_from_file(
    table_path: str,
) -> typing.Tuple[typing.Optional[list[UnixMountEntry]], int]: ...

class Action(GObject.GInterface):
    """
    Interface GAction

    Signals from GObject:
      notify (GParam)
    """

    def activate(self, parameter: typing.Optional[GLib.Variant] = None) -> None: ...
    def change_state(self, value: GLib.Variant) -> None: ...
    def get_enabled(self) -> bool: ...
    def get_name(self) -> str: ...
    def get_parameter_type(self) -> typing.Optional[GLib.VariantType]: ...
    def get_state(self) -> typing.Optional[GLib.Variant]: ...
    def get_state_hint(self) -> typing.Optional[GLib.Variant]: ...
    def get_state_type(self) -> typing.Optional[GLib.VariantType]: ...
    @staticmethod
    def name_is_valid(action_name: str) -> bool: ...
    @staticmethod
    def parse_detailed_name(
        detailed_name: str,
    ) -> typing.Tuple[bool, str, GLib.Variant]: ...
    @staticmethod
    def print_detailed_name(
        action_name: str, target_value: typing.Optional[GLib.Variant] = None
    ) -> str: ...

class ActionEntry(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionEntry()
    """

    name: str = ...
    activate: typing.Callable[..., None] = ...
    parameter_type: str = ...
    state: str = ...
    change_state: typing.Callable[..., None] = ...
    padding: list[int] = ...

class ActionGroup(GObject.GInterface):
    """
    Interface GActionGroup

    Signals from GObject:
      notify (GParam)
    """

    def action_added(self, action_name: str) -> None: ...
    def action_enabled_changed(self, action_name: str, enabled: bool) -> None: ...
    def action_removed(self, action_name: str) -> None: ...
    def action_state_changed(self, action_name: str, state: GLib.Variant) -> None: ...
    def activate_action(
        self, action_name: str, parameter: typing.Optional[GLib.Variant] = None
    ) -> None: ...
    def change_action_state(self, action_name: str, value: GLib.Variant) -> None: ...
    def get_action_enabled(self, action_name: str) -> bool: ...
    def get_action_parameter_type(
        self, action_name: str
    ) -> typing.Optional[GLib.VariantType]: ...
    def get_action_state(self, action_name: str) -> typing.Optional[GLib.Variant]: ...
    def get_action_state_hint(
        self, action_name: str
    ) -> typing.Optional[GLib.Variant]: ...
    def get_action_state_type(
        self, action_name: str
    ) -> typing.Optional[GLib.VariantType]: ...
    def has_action(self, action_name: str) -> bool: ...
    def list_actions(self) -> list[str]: ...
    def query_action(
        self, action_name: str
    ) -> typing.Tuple[
        bool, bool, GLib.VariantType, GLib.VariantType, GLib.Variant, GLib.Variant
    ]: ...

class ActionGroupInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionGroupInterface()
    """

    g_iface: GObject.TypeInterface = ...
    has_action: typing.Callable[[ActionGroup, str], bool] = ...
    list_actions: typing.Callable[[ActionGroup], list[str]] = ...
    get_action_enabled: typing.Callable[[ActionGroup, str], bool] = ...
    get_action_parameter_type: typing.Callable[
        [ActionGroup, str], typing.Optional[GLib.VariantType]
    ] = ...
    get_action_state_type: typing.Callable[
        [ActionGroup, str], typing.Optional[GLib.VariantType]
    ] = ...
    get_action_state_hint: typing.Callable[
        [ActionGroup, str], typing.Optional[GLib.Variant]
    ] = ...
    get_action_state: typing.Callable[
        [ActionGroup, str], typing.Optional[GLib.Variant]
    ] = ...
    change_action_state: typing.Callable[[ActionGroup, str, GLib.Variant], None] = ...
    activate_action: typing.Callable[
        [ActionGroup, str, typing.Optional[GLib.Variant]], None
    ] = ...
    action_added: typing.Callable[[ActionGroup, str], None] = ...
    action_removed: typing.Callable[[ActionGroup, str], None] = ...
    action_enabled_changed: typing.Callable[[ActionGroup, str, bool], None] = ...
    action_state_changed: typing.Callable[[ActionGroup, str, GLib.Variant], None] = ...
    query_action: typing.Callable[
        [ActionGroup, str],
        typing.Tuple[
            bool, bool, GLib.VariantType, GLib.VariantType, GLib.Variant, GLib.Variant
        ],
    ] = ...

class ActionInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionInterface()
    """

    g_iface: GObject.TypeInterface = ...
    get_name: typing.Callable[[Action], str] = ...
    get_parameter_type: typing.Callable[[Action], typing.Optional[GLib.VariantType]] = (
        ...
    )
    get_state_type: typing.Callable[[Action], typing.Optional[GLib.VariantType]] = ...
    get_state_hint: typing.Callable[[Action], typing.Optional[GLib.Variant]] = ...
    get_enabled: typing.Callable[[Action], bool] = ...
    get_state: typing.Callable[[Action], typing.Optional[GLib.Variant]] = ...
    change_state: typing.Callable[[Action, GLib.Variant], None] = ...
    activate: typing.Callable[[Action, typing.Optional[GLib.Variant]], None] = ...

class ActionMap(GObject.GInterface):
    """
    Interface GActionMap

    Signals from GObject:
      notify (GParam)
    """

    def add_action(self, action: Action) -> None: ...
    def add_action_entries(self, entries, user_data=None): ...  # FIXME Function
    def lookup_action(self, action_name: str) -> typing.Optional[Action]: ...
    def remove_action(self, action_name: str) -> None: ...
    def remove_action_entries(self, entries: typing.Sequence[ActionEntry]) -> None: ...

class ActionMapInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionMapInterface()
    """

    g_iface: GObject.TypeInterface = ...
    lookup_action: typing.Callable[[ActionMap, str], typing.Optional[Action]] = ...
    add_action: typing.Callable[[ActionMap, Action], None] = ...
    remove_action: typing.Callable[[ActionMap, str], None] = ...

class AppInfo(GObject.GInterface):
    """
    Interface GAppInfo

    Signals from GObject:
      notify (GParam)
    """

    def add_supports_type(self, content_type: str) -> bool: ...
    def can_delete(self) -> bool: ...
    def can_remove_supports_type(self) -> bool: ...
    @staticmethod
    def create_from_commandline(
        commandline: str,
        application_name: typing.Optional[str],
        flags: AppInfoCreateFlags,
    ) -> AppInfo: ...
    def delete(self) -> bool: ...
    def dup(self) -> AppInfo: ...
    def equal(self, appinfo2: AppInfo) -> bool: ...
    @staticmethod
    def get_all() -> list[AppInfo]: ...
    @staticmethod
    def get_all_for_type(content_type: str) -> list[AppInfo]: ...
    def get_commandline(self) -> typing.Optional[str]: ...
    @staticmethod
    def get_default_for_type(
        content_type: str, must_support_uris: bool
    ) -> typing.Optional[AppInfo]: ...
    @staticmethod
    def get_default_for_type_async(
        content_type: str,
        must_support_uris: bool,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @staticmethod
    def get_default_for_type_finish(result: AsyncResult) -> AppInfo: ...
    @staticmethod
    def get_default_for_uri_scheme(uri_scheme: str) -> typing.Optional[AppInfo]: ...
    @staticmethod
    def get_default_for_uri_scheme_async(
        uri_scheme: str,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @staticmethod
    def get_default_for_uri_scheme_finish(result: AsyncResult) -> AppInfo: ...
    def get_description(self) -> typing.Optional[str]: ...
    def get_display_name(self) -> str: ...
    def get_executable(self) -> str: ...
    @staticmethod
    def get_fallback_for_type(content_type: str) -> list[AppInfo]: ...
    def get_icon(self) -> typing.Optional[Icon]: ...
    def get_id(self) -> typing.Optional[str]: ...
    def get_name(self) -> str: ...
    @staticmethod
    def get_recommended_for_type(content_type: str) -> list[AppInfo]: ...
    def get_supported_types(self) -> list[str]: ...
    def launch(
        self,
        files: typing.Optional[list[File]] = None,
        context: typing.Optional[AppLaunchContext] = None,
    ) -> bool: ...
    @staticmethod
    def launch_default_for_uri(
        uri: str, context: typing.Optional[AppLaunchContext] = None
    ) -> bool: ...
    @staticmethod
    def launch_default_for_uri_async(
        uri: str,
        context: typing.Optional[AppLaunchContext] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @staticmethod
    def launch_default_for_uri_finish(result: AsyncResult) -> bool: ...
    def launch_uris(
        self,
        uris: typing.Optional[list[str]] = None,
        context: typing.Optional[AppLaunchContext] = None,
    ) -> bool: ...
    def launch_uris_async(
        self,
        uris: typing.Optional[list[str]] = None,
        context: typing.Optional[AppLaunchContext] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def launch_uris_finish(self, result: AsyncResult) -> bool: ...
    def remove_supports_type(self, content_type: str) -> bool: ...
    @staticmethod
    def reset_type_associations(content_type: str) -> None: ...
    def set_as_default_for_extension(self, extension: str) -> bool: ...
    def set_as_default_for_type(self, content_type: str) -> bool: ...
    def set_as_last_used_for_type(self, content_type: str) -> bool: ...
    def should_show(self) -> bool: ...
    def supports_files(self) -> bool: ...
    def supports_uris(self) -> bool: ...

class AppInfoIface(GObject.GPointer):
    """
    :Constructors:

    ::

        AppInfoIface()
    """

    g_iface: GObject.TypeInterface = ...
    dup: typing.Callable[[AppInfo], AppInfo] = ...
    equal: typing.Callable[[AppInfo, AppInfo], bool] = ...
    get_id: typing.Callable[[AppInfo], typing.Optional[str]] = ...
    get_name: typing.Callable[[AppInfo], str] = ...
    get_description: typing.Callable[[AppInfo], typing.Optional[str]] = ...
    get_executable: typing.Callable[[AppInfo], str] = ...
    get_icon: typing.Callable[[AppInfo], typing.Optional[Icon]] = ...
    launch: typing.Callable[
        [AppInfo, typing.Optional[list[File]], typing.Optional[AppLaunchContext]], bool
    ] = ...
    supports_uris: typing.Callable[[AppInfo], bool] = ...
    supports_files: typing.Callable[[AppInfo], bool] = ...
    launch_uris: typing.Callable[
        [AppInfo, typing.Optional[list[str]], typing.Optional[AppLaunchContext]], bool
    ] = ...
    should_show: typing.Callable[[AppInfo], bool] = ...
    set_as_default_for_type: typing.Callable[[AppInfo, str], bool] = ...
    set_as_default_for_extension: typing.Callable[[AppInfo, str], bool] = ...
    add_supports_type: typing.Callable[[AppInfo, str], bool] = ...
    can_remove_supports_type: typing.Callable[[AppInfo], bool] = ...
    remove_supports_type: typing.Callable[[AppInfo, str], bool] = ...
    can_delete: typing.Callable[[AppInfo], bool] = ...
    do_delete: typing.Callable[[AppInfo], bool] = ...
    get_commandline: typing.Callable[[AppInfo], typing.Optional[str]] = ...
    get_display_name: typing.Callable[[AppInfo], str] = ...
    set_as_last_used_for_type: typing.Callable[[AppInfo, str], bool] = ...
    get_supported_types: typing.Callable[[AppInfo], list[str]] = ...
    launch_uris_async: typing.Callable[..., None] = ...
    launch_uris_finish: typing.Callable[[AppInfo, AsyncResult], bool] = ...

class AppInfoMonitor(GObject.Object):
    """
    :Constructors:

    ::

        AppInfoMonitor(**properties)

    Object GAppInfoMonitor

    Signals from GAppInfoMonitor:
      changed ()

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def get() -> AppInfoMonitor: ...

class AppLaunchContext(GObject.Object):
    """
    :Constructors:

    ::

        AppLaunchContext(**properties)
        new() -> Gio.AppLaunchContext

    Object GAppLaunchContext

    Signals from GAppLaunchContext:
      launch-failed (gchararray)
      launch-started (GAppInfo, GVariant)
      launched (GAppInfo, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: AppLaunchContextPrivate = ...
    def do_get_display(
        self, info: AppInfo, files: list[File]
    ) -> typing.Optional[str]: ...
    def do_get_startup_notify_id(
        self,
        info: typing.Optional[AppInfo] = None,
        files: typing.Optional[list[File]] = None,
    ) -> typing.Optional[str]: ...
    def do_launch_failed(self, startup_notify_id: str) -> None: ...
    def do_launch_started(self, info: AppInfo, platform_data: GLib.Variant) -> None: ...
    def do_launched(self, info: AppInfo, platform_data: GLib.Variant) -> None: ...
    def get_display(self, info: AppInfo, files: list[File]) -> typing.Optional[str]: ...
    def get_environment(self) -> list[str]: ...
    def get_startup_notify_id(
        self,
        info: typing.Optional[AppInfo] = None,
        files: typing.Optional[list[File]] = None,
    ) -> typing.Optional[str]: ...
    def launch_failed(self, startup_notify_id: str) -> None: ...
    @classmethod
    def new(cls) -> AppLaunchContext: ...
    def setenv(self, variable: str, value: str) -> None: ...
    def unsetenv(self, variable: str) -> None: ...

class AppLaunchContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AppLaunchContextClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_display: typing.Callable[
        [AppLaunchContext, AppInfo, list[File]], typing.Optional[str]
    ] = ...
    get_startup_notify_id: typing.Callable[
        [AppLaunchContext, typing.Optional[AppInfo], typing.Optional[list[File]]],
        typing.Optional[str],
    ] = ...
    launch_failed: typing.Callable[[AppLaunchContext, str], None] = ...
    launched: typing.Callable[[AppLaunchContext, AppInfo, GLib.Variant], None] = ...
    launch_started: typing.Callable[[AppLaunchContext, AppInfo, GLib.Variant], None] = (
        ...
    )
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...

class AppLaunchContextPrivate(GObject.GPointer): ...

class Application(GObject.Object, ActionGroup, ActionMap):
    """
    :Constructors:

    ::

        Application(**properties)
        new(application_id:str=None, flags:Gio.ApplicationFlags) -> Gio.Application

    Object GApplication

    Signals from GApplication:
      startup ()
      shutdown ()
      activate ()
      open (gpointer, gint, gchararray)
      command-line (GApplicationCommandLine) -> gint
      handle-local-options (GVariantDict) -> gint
      name-lost () -> gboolean

    Properties from GApplication:
      application-id -> gchararray: application-id
      version -> gchararray: version
      flags -> GApplicationFlags: flags
      resource-base-path -> gchararray: resource-base-path
      is-registered -> gboolean: is-registered
      is-remote -> gboolean: is-remote
      inactivity-timeout -> guint: inactivity-timeout
      action-group -> GActionGroup: action-group
      is-busy -> gboolean: is-busy

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        application_id: typing.Optional[str]
        flags: ApplicationFlags
        inactivity_timeout: int
        is_busy: bool
        is_registered: bool
        is_remote: bool
        resource_base_path: typing.Optional[str]
        version: typing.Optional[str]
        action_group: typing.Optional[ActionGroup]

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: ApplicationPrivate = ...
    def __init__(
        self,
        action_group: typing.Optional[ActionGroup] = ...,
        application_id: typing.Optional[str] = ...,
        flags: ApplicationFlags = ...,
        inactivity_timeout: int = ...,
        resource_base_path: typing.Optional[str] = ...,
        version: str = ...,
    ) -> None: ...
    def activate(self) -> None: ...
    def add_main_option(
        self,
        long_name: str,
        short_name: int,
        flags: GLib.OptionFlags,
        arg: GLib.OptionArg,
        description: str,
        arg_description: typing.Optional[str] = None,
    ) -> None: ...
    def add_main_option_entries(
        self, entries: typing.Sequence[GLib.OptionEntry]
    ) -> None: ...
    def add_option_group(self, group: GLib.OptionGroup) -> None: ...
    def bind_busy_property(self, object: GObject.Object, property: str) -> None: ...
    def do_activate(self) -> None: ...
    def do_add_platform_data(self, builder: GLib.VariantBuilder) -> None: ...
    def do_after_emit(self, platform_data: GLib.Variant) -> None: ...
    def do_before_emit(self, platform_data: GLib.Variant) -> None: ...
    def do_command_line(self, command_line: ApplicationCommandLine) -> int: ...
    def do_dbus_register(
        self, connection: DBusConnection, object_path: str
    ) -> bool: ...
    def do_dbus_unregister(
        self, connection: DBusConnection, object_path: str
    ) -> None: ...
    def do_handle_local_options(self, options: GLib.VariantDict) -> int: ...
    def do_local_command_line(self) -> typing.Tuple[bool, list[str], int]: ...
    def do_name_lost(self) -> bool: ...
    def do_open(self, files: typing.Sequence[File], hint: str) -> None: ...
    def do_quit_mainloop(self) -> None: ...
    def do_run_mainloop(self) -> None: ...
    def do_shutdown(self) -> None: ...
    def do_startup(self) -> None: ...
    def get_application_id(self) -> typing.Optional[str]: ...
    def get_dbus_connection(self) -> typing.Optional[DBusConnection]: ...
    def get_dbus_object_path(self) -> typing.Optional[str]: ...
    @staticmethod
    def get_default() -> typing.Optional[Application]: ...
    def get_flags(self) -> ApplicationFlags: ...
    def get_inactivity_timeout(self) -> int: ...
    def get_is_busy(self) -> bool: ...
    def get_is_registered(self) -> bool: ...
    def get_is_remote(self) -> bool: ...
    def get_resource_base_path(self) -> typing.Optional[str]: ...
    def get_version(self) -> typing.Optional[str]: ...
    def hold(self) -> None: ...
    @staticmethod
    def id_is_valid(application_id: str) -> bool: ...
    def mark_busy(self) -> None: ...
    @classmethod
    def new(
        cls, application_id: typing.Optional[str], flags: ApplicationFlags
    ) -> Application: ...
    def open(self, files: typing.Sequence[File], hint: str) -> None: ...
    def quit(self) -> None: ...
    def register(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def release(self) -> None: ...
    # override
    def run(self, argv: typing.Optional[list[str]]) -> int: ...
    def send_notification(
        self, id: typing.Optional[str], notification: Notification
    ) -> None: ...
    def set_action_group(
        self, action_group: typing.Optional[ActionGroup] = None
    ) -> None: ...
    def set_application_id(
        self, application_id: typing.Optional[str] = None
    ) -> None: ...
    def set_default(self) -> None: ...
    def set_flags(self, flags: ApplicationFlags) -> None: ...
    def set_inactivity_timeout(self, inactivity_timeout: int) -> None: ...
    def set_option_context_description(
        self, description: typing.Optional[str] = None
    ) -> None: ...
    def set_option_context_parameter_string(
        self, parameter_string: typing.Optional[str] = None
    ) -> None: ...
    def set_option_context_summary(
        self, summary: typing.Optional[str] = None
    ) -> None: ...
    def set_resource_base_path(
        self, resource_path: typing.Optional[str] = None
    ) -> None: ...
    def set_version(self, version: str) -> None: ...
    def unbind_busy_property(self, object: GObject.Object, property: str) -> None: ...
    def unmark_busy(self) -> None: ...
    def withdraw_notification(self, id: str) -> None: ...

class ApplicationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ApplicationClass()
    """

    parent_class: GObject.ObjectClass = ...
    startup: typing.Callable[[Application], None] = ...
    activate: typing.Callable[[Application], None] = ...
    open: typing.Callable[[Application, typing.Sequence[File], str], None] = ...
    command_line: typing.Callable[[Application, ApplicationCommandLine], int] = ...
    local_command_line: typing.Callable[
        [Application], typing.Tuple[bool, list[str], int]
    ] = ...
    before_emit: typing.Callable[[Application, GLib.Variant], None] = ...
    after_emit: typing.Callable[[Application, GLib.Variant], None] = ...
    add_platform_data: typing.Callable[[Application, GLib.VariantBuilder], None] = ...
    quit_mainloop: typing.Callable[[Application], None] = ...
    run_mainloop: typing.Callable[[Application], None] = ...
    shutdown: typing.Callable[[Application], None] = ...
    dbus_register: typing.Callable[[Application, DBusConnection, str], bool] = ...
    dbus_unregister: typing.Callable[[Application, DBusConnection, str], None] = ...
    handle_local_options: typing.Callable[[Application, GLib.VariantDict], int] = ...
    name_lost: typing.Callable[[Application], bool] = ...
    padding: list[None] = ...

class ApplicationCommandLine(GObject.Object):
    """
    :Constructors:

    ::

        ApplicationCommandLine(**properties)

    Object GApplicationCommandLine

    Properties from GApplicationCommandLine:
      arguments -> GVariant: arguments
      options -> GVariant: options
      platform-data -> GVariant: platform-data
      is-remote -> gboolean: is-remote

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        is_remote: bool
        arguments: GLib.Variant
        options: GLib.Variant
        platform_data: GLib.Variant

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: ApplicationCommandLinePrivate = ...
    def __init__(
        self,
        arguments: GLib.Variant = ...,
        options: GLib.Variant = ...,
        platform_data: GLib.Variant = ...,
    ) -> None: ...
    def create_file_for_arg(self, arg: str) -> File: ...
    def do_done(self) -> None: ...
    def do_get_stdin(self) -> typing.Optional[InputStream]: ...
    def do_print_literal(self, message: str) -> None: ...
    def do_printerr_literal(self, message: str) -> None: ...
    def done(self) -> None: ...
    def get_arguments(self) -> list[str]: ...
    def get_cwd(self) -> typing.Optional[str]: ...
    def get_environ(self) -> list[str]: ...
    def get_exit_status(self) -> int: ...
    def get_is_remote(self) -> bool: ...
    def get_options_dict(self) -> GLib.VariantDict: ...
    def get_platform_data(self) -> typing.Optional[GLib.Variant]: ...
    def get_stdin(self) -> typing.Optional[InputStream]: ...
    def getenv(self, name: str) -> typing.Optional[str]: ...
    def print_literal(self, message: str) -> None: ...
    def printerr_literal(self, message: str) -> None: ...
    def set_exit_status(self, exit_status: int) -> None: ...

class ApplicationCommandLineClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ApplicationCommandLineClass()
    """

    parent_class: GObject.ObjectClass = ...
    print_literal: typing.Callable[[ApplicationCommandLine, str], None] = ...
    printerr_literal: typing.Callable[[ApplicationCommandLine, str], None] = ...
    get_stdin: typing.Callable[
        [ApplicationCommandLine], typing.Optional[InputStream]
    ] = ...
    done: typing.Callable[[ApplicationCommandLine], None] = ...
    padding: list[None] = ...

class ApplicationCommandLinePrivate(GObject.GPointer): ...
class ApplicationPrivate(GObject.GPointer): ...

class AsyncInitable(GObject.GInterface):
    """
    Interface GAsyncInitable

    Signals from GObject:
      notify (GParam)
    """

    def init_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def init_finish(self, res: AsyncResult) -> bool: ...
    def new_finish(self, res: AsyncResult) -> GObject.Object: ...
    @staticmethod
    def newv_async(
        object_type: typing.Type[typing.Any],
        n_parameters: int,
        parameters: GObject.Parameter,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...

class AsyncInitableIface(GObject.GPointer):
    """
    :Constructors:

    ::

        AsyncInitableIface()
    """

    g_iface: GObject.TypeInterface = ...
    init_async: typing.Callable[..., None] = ...
    init_finish: typing.Callable[[AsyncInitable, AsyncResult], bool] = ...

class AsyncResult(GObject.GInterface):
    """
    Interface GAsyncResult

    Signals from GObject:
      notify (GParam)
    """

    def get_source_object(self) -> typing.Optional[GObject.Object]: ...
    def get_user_data(self) -> None: ...
    def is_tagged(self, source_tag: None) -> bool: ...
    def legacy_propagate_error(self) -> bool: ...

class AsyncResultIface(GObject.GPointer):
    """
    :Constructors:

    ::

        AsyncResultIface()
    """

    g_iface: GObject.TypeInterface = ...
    get_user_data: typing.Callable[[AsyncResult], None] = ...
    get_source_object: typing.Callable[
        [AsyncResult], typing.Optional[GObject.Object]
    ] = ...
    is_tagged: typing.Callable[[AsyncResult, None], bool] = ...

class BufferedInputStream(FilterInputStream, Seekable):
    """
    :Constructors:

    ::

        BufferedInputStream(**properties)
        new(base_stream:Gio.InputStream) -> Gio.InputStream
        new_sized(base_stream:Gio.InputStream, size:int) -> Gio.InputStream

    Object GBufferedInputStream

    Properties from GBufferedInputStream:
      buffer-size -> guint: buffer-size

    Properties from GFilterInputStream:
      base-stream -> GInputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        buffer_size: int
        base_stream: InputStream
        close_base_stream: bool

    props: Props = ...
    parent_instance: FilterInputStream = ...
    priv: BufferedInputStreamPrivate = ...
    def __init__(
        self,
        buffer_size: int = ...,
        base_stream: InputStream = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def do_fill(
        self, count: int, cancellable: typing.Optional[Cancellable] = None
    ) -> int: ...
    def do_fill_async(
        self,
        count: int,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_fill_finish(self, result: AsyncResult) -> int: ...
    def fill(
        self, count: int, cancellable: typing.Optional[Cancellable] = None
    ) -> int: ...
    def fill_async(
        self,
        count: int,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def fill_finish(self, result: AsyncResult) -> int: ...
    def get_available(self) -> int: ...
    def get_buffer_size(self) -> int: ...
    @classmethod
    def new(cls, base_stream: InputStream) -> BufferedInputStream: ...
    @classmethod
    def new_sized(cls, base_stream: InputStream, size: int) -> BufferedInputStream: ...
    def peek(self, buffer: typing.Sequence[int], offset: int) -> int: ...
    def peek_buffer(self) -> bytes: ...
    def read_byte(self, cancellable: typing.Optional[Cancellable] = None) -> int: ...
    def set_buffer_size(self, size: int) -> None: ...

class BufferedInputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BufferedInputStreamClass()
    """

    parent_class: FilterInputStreamClass = ...
    fill: typing.Callable[
        [BufferedInputStream, int, typing.Optional[Cancellable]], int
    ] = ...
    fill_async: typing.Callable[..., None] = ...
    fill_finish: typing.Callable[[BufferedInputStream, AsyncResult], int] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class BufferedInputStreamPrivate(GObject.GPointer): ...

class BufferedOutputStream(FilterOutputStream, Seekable):
    """
    :Constructors:

    ::

        BufferedOutputStream(**properties)
        new(base_stream:Gio.OutputStream) -> Gio.OutputStream
        new_sized(base_stream:Gio.OutputStream, size:int) -> Gio.OutputStream

    Object GBufferedOutputStream

    Properties from GBufferedOutputStream:
      buffer-size -> guint: buffer-size
      auto-grow -> gboolean: auto-grow

    Properties from GFilterOutputStream:
      base-stream -> GOutputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        auto_grow: bool
        buffer_size: int
        base_stream: OutputStream
        close_base_stream: bool

    props: Props = ...
    parent_instance: FilterOutputStream = ...
    priv: BufferedOutputStreamPrivate = ...
    def __init__(
        self,
        auto_grow: bool = ...,
        buffer_size: int = ...,
        base_stream: OutputStream = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def get_auto_grow(self) -> bool: ...
    def get_buffer_size(self) -> int: ...
    @classmethod
    def new(cls, base_stream: OutputStream) -> BufferedOutputStream: ...
    @classmethod
    def new_sized(
        cls, base_stream: OutputStream, size: int
    ) -> BufferedOutputStream: ...
    def set_auto_grow(self, auto_grow: bool) -> None: ...
    def set_buffer_size(self, size: int) -> None: ...

class BufferedOutputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BufferedOutputStreamClass()
    """

    parent_class: FilterOutputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...

class BufferedOutputStreamPrivate(GObject.GPointer): ...

class BytesIcon(GObject.Object, Icon, LoadableIcon):
    """
    :Constructors:

    ::

        BytesIcon(**properties)
        new(bytes:GLib.Bytes) -> Gio.BytesIcon

    Object GBytesIcon

    Properties from GBytesIcon:
      bytes -> GBytes: bytes

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        bytes: GLib.Bytes

    props: Props = ...
    # override
    def __init__(self, *, bytes: GLib.Bytes = ...) -> None: ...
    def get_bytes(self) -> GLib.Bytes: ...
    @classmethod
    def new(cls, bytes: GLib.Bytes) -> BytesIcon: ...

class Cancellable(GObject.Object):
    """
    :Constructors:

    ::

        Cancellable(**properties)
        new() -> Gio.Cancellable

    Object GCancellable

    Signals from GCancellable:
      cancelled ()

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: CancellablePrivate = ...
    def cancel(self) -> None: ...
    def connect(
        self, callback: typing.Callable[..., None], *data: typing.Any
    ) -> int: ...
    def disconnect(self, handler_id: int) -> None: ...
    def do_cancelled(self) -> None: ...
    @staticmethod
    def get_current() -> typing.Optional[Cancellable]: ...
    def get_fd(self) -> int: ...
    def is_cancelled(self) -> bool: ...
    def make_pollfd(self, pollfd: GLib.PollFD) -> bool: ...
    @classmethod
    def new(cls) -> Cancellable: ...
    def pop_current(self) -> None: ...
    def push_current(self) -> None: ...
    def release_fd(self) -> None: ...
    def reset(self) -> None: ...
    def set_error_if_cancelled(self) -> bool: ...
    def source_new(self) -> GLib.Source: ...

class CancellableClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CancellableClass()
    """

    parent_class: GObject.ObjectClass = ...
    cancelled: typing.Callable[[typing.Optional[Cancellable]], None] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class CancellablePrivate(GObject.GPointer): ...

class CharsetConverter(GObject.Object, Converter, Initable):
    """
    :Constructors:

    ::

        CharsetConverter(**properties)
        new(to_charset:str, from_charset:str) -> Gio.CharsetConverter

    Object GCharsetConverter

    Properties from GCharsetConverter:
      from-charset -> gchararray: from-charset
      to-charset -> gchararray: to-charset
      use-fallback -> gboolean: use-fallback

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        from_charset: str
        to_charset: str
        use_fallback: bool

    props: Props = ...
    def __init__(
        self, from_charset: str = ..., to_charset: str = ..., use_fallback: bool = ...
    ) -> None: ...
    def get_num_fallbacks(self) -> int: ...
    def get_use_fallback(self) -> bool: ...
    @classmethod
    def new(cls, to_charset: str, from_charset: str) -> CharsetConverter: ...
    def set_use_fallback(self, use_fallback: bool) -> None: ...

class CharsetConverterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CharsetConverterClass()
    """

    parent_class: GObject.ObjectClass = ...

class Converter(GObject.GInterface):
    """
    Interface GConverter

    Signals from GObject:
      notify (GParam)
    """

    def convert(
        self,
        inbuf: typing.Sequence[int],
        outbuf: typing.Sequence[int],
        flags: ConverterFlags,
    ) -> typing.Tuple[ConverterResult, int, int]: ...
    def convert_bytes(self, bytes: GLib.Bytes) -> GLib.Bytes: ...
    def reset(self) -> None: ...

class ConverterIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ConverterIface()
    """

    g_iface: GObject.TypeInterface = ...
    convert: typing.Callable[
        [
            Converter,
            typing.Optional[typing.Sequence[int]],
            typing.Sequence[int],
            ConverterFlags,
        ],
        typing.Tuple[ConverterResult, int, int],
    ] = ...
    reset: typing.Callable[[Converter], None] = ...

class ConverterInputStream(FilterInputStream, PollableInputStream):
    """
    :Constructors:

    ::

        ConverterInputStream(**properties)
        new(base_stream:Gio.InputStream, converter:Gio.Converter) -> Gio.InputStream

    Object GConverterInputStream

    Properties from GConverterInputStream:
      converter -> GConverter: converter

    Properties from GFilterInputStream:
      base-stream -> GInputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        converter: Converter
        base_stream: InputStream
        close_base_stream: bool

    props: Props = ...
    parent_instance: FilterInputStream = ...
    priv: ConverterInputStreamPrivate = ...
    def __init__(
        self,
        converter: Converter = ...,
        base_stream: InputStream = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def get_converter(self) -> Converter: ...
    @classmethod
    def new(
        cls, base_stream: InputStream, converter: Converter
    ) -> ConverterInputStream: ...

class ConverterInputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ConverterInputStreamClass()
    """

    parent_class: FilterInputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class ConverterInputStreamPrivate(GObject.GPointer): ...

class ConverterOutputStream(FilterOutputStream, PollableOutputStream):
    """
    :Constructors:

    ::

        ConverterOutputStream(**properties)
        new(base_stream:Gio.OutputStream, converter:Gio.Converter) -> Gio.OutputStream

    Object GConverterOutputStream

    Properties from GConverterOutputStream:
      converter -> GConverter: converter

    Properties from GFilterOutputStream:
      base-stream -> GOutputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        converter: Converter
        base_stream: OutputStream
        close_base_stream: bool

    props: Props = ...
    parent_instance: FilterOutputStream = ...
    priv: ConverterOutputStreamPrivate = ...
    def __init__(
        self,
        converter: Converter = ...,
        base_stream: OutputStream = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def get_converter(self) -> Converter: ...
    @classmethod
    def new(
        cls, base_stream: OutputStream, converter: Converter
    ) -> ConverterOutputStream: ...

class ConverterOutputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ConverterOutputStreamClass()
    """

    parent_class: FilterOutputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class ConverterOutputStreamPrivate(GObject.GPointer): ...

class Credentials(GObject.Object):
    """
    :Constructors:

    ::

        Credentials(**properties)
        new() -> Gio.Credentials

    Object GCredentials

    Signals from GObject:
      notify (GParam)
    """

    def get_unix_pid(self) -> int: ...
    def get_unix_user(self) -> int: ...
    def is_same_user(self, other_credentials: Credentials) -> bool: ...
    @classmethod
    def new(cls) -> Credentials: ...
    def set_native(self, native_type: CredentialsType, native: None) -> None: ...
    def set_unix_user(self, uid: int) -> bool: ...
    def to_string(self) -> str: ...

class CredentialsClass(GObject.GPointer): ...

class DBusActionGroup(GObject.Object, ActionGroup, RemoteActionGroup):
    """
    :Constructors:

    ::

        DBusActionGroup(**properties)

    Object GDBusActionGroup

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def get(
        connection: DBusConnection, bus_name: typing.Optional[str], object_path: str
    ) -> DBusActionGroup: ...

class DBusAnnotationInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusAnnotationInfo()
    """

    ref_count: int = ...
    key: str = ...
    value: str = ...
    annotations: list[DBusAnnotationInfo] = ...
    @staticmethod
    def lookup(
        annotations: typing.Optional[typing.Sequence[DBusAnnotationInfo]], name: str
    ) -> typing.Optional[str]: ...
    def ref(self) -> DBusAnnotationInfo: ...
    def unref(self) -> None: ...

class DBusArgInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusArgInfo()
    """

    ref_count: int = ...
    name: str = ...
    signature: str = ...
    annotations: list[DBusAnnotationInfo] = ...
    def ref(self) -> DBusArgInfo: ...
    def unref(self) -> None: ...

class DBusAuthObserver(GObject.Object):
    """
    :Constructors:

    ::

        DBusAuthObserver(**properties)
        new() -> Gio.DBusAuthObserver

    Object GDBusAuthObserver

    Signals from GDBusAuthObserver:
      authorize-authenticated-peer (GIOStream, GCredentials) -> gboolean
      allow-mechanism (gchararray) -> gboolean

    Signals from GObject:
      notify (GParam)
    """

    def allow_mechanism(self, mechanism: str) -> bool: ...
    def authorize_authenticated_peer(
        self, stream: IOStream, credentials: typing.Optional[Credentials] = None
    ) -> bool: ...
    @classmethod
    def new(cls) -> DBusAuthObserver: ...

class DBusConnection(GObject.Object, AsyncInitable, Initable):
    """
    :Constructors:

    ::

        DBusConnection(**properties)
        new_finish(res:Gio.AsyncResult) -> Gio.DBusConnection
        new_for_address_finish(res:Gio.AsyncResult) -> Gio.DBusConnection
        new_for_address_sync(address:str, flags:Gio.DBusConnectionFlags, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None) -> Gio.DBusConnection
        new_sync(stream:Gio.IOStream, guid:str=None, flags:Gio.DBusConnectionFlags, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None) -> Gio.DBusConnection

    Object GDBusConnection

    Signals from GDBusConnection:
      closed (gboolean, GError)

    Properties from GDBusConnection:
      stream -> GIOStream: stream
      address -> gchararray: address
      flags -> GDBusConnectionFlags: flags
      guid -> gchararray: guid
      unique-name -> gchararray: unique-name
      closed -> gboolean: closed
      exit-on-close -> gboolean: exit-on-close
      capabilities -> GDBusCapabilityFlags: capabilities
      authentication-observer -> GDBusAuthObserver: authentication-observer

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        capabilities: DBusCapabilityFlags
        closed: bool
        exit_on_close: bool
        flags: DBusConnectionFlags
        guid: str
        stream: IOStream
        unique_name: typing.Optional[str]
        address: str
        authentication_observer: DBusAuthObserver

    props: Props = ...
    def __init__(
        self,
        address: str = ...,
        authentication_observer: DBusAuthObserver = ...,
        exit_on_close: bool = ...,
        flags: DBusConnectionFlags = ...,
        guid: str = ...,
        stream: IOStream = ...,
    ) -> None: ...
    def add_filter(
        self,
        filter_function: typing.Callable[..., typing.Optional[DBusMessage]],
        *user_data: typing.Any,
    ) -> int: ...
    def call(
        self,
        bus_name: typing.Optional[str],
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: typing.Optional[GLib.Variant],
        reply_type: typing.Optional[GLib.VariantType],
        flags: DBusCallFlags,
        timeout_msec: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def call_finish(self, res: AsyncResult) -> GLib.Variant: ...
    def call_sync(
        self,
        bus_name: typing.Optional[str],
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: typing.Optional[GLib.Variant],
        reply_type: typing.Optional[GLib.VariantType],
        flags: DBusCallFlags,
        timeout_msec: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> GLib.Variant: ...
    def call_with_unix_fd_list(
        self,
        bus_name: typing.Optional[str],
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: typing.Optional[GLib.Variant],
        reply_type: typing.Optional[GLib.VariantType],
        flags: DBusCallFlags,
        timeout_msec: int,
        fd_list: typing.Optional[UnixFDList] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def call_with_unix_fd_list_finish(
        self, res: AsyncResult
    ) -> typing.Tuple[GLib.Variant, UnixFDList]: ...
    def call_with_unix_fd_list_sync(
        self,
        bus_name: typing.Optional[str],
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: typing.Optional[GLib.Variant],
        reply_type: typing.Optional[GLib.VariantType],
        flags: DBusCallFlags,
        timeout_msec: int,
        fd_list: typing.Optional[UnixFDList] = None,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[GLib.Variant, UnixFDList]: ...
    def close(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def close_finish(self, res: AsyncResult) -> bool: ...
    def close_sync(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def emit_signal(
        self,
        destination_bus_name: typing.Optional[str],
        object_path: str,
        interface_name: str,
        signal_name: str,
        parameters: typing.Optional[GLib.Variant] = None,
    ) -> bool: ...
    def export_action_group(
        self, object_path: str, action_group: ActionGroup
    ) -> int: ...
    def export_menu_model(self, object_path: str, menu: MenuModel) -> int: ...
    def flush(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def flush_finish(self, res: AsyncResult) -> bool: ...
    def flush_sync(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def get_capabilities(self) -> DBusCapabilityFlags: ...
    def get_exit_on_close(self) -> bool: ...
    def get_flags(self) -> DBusConnectionFlags: ...
    def get_guid(self) -> str: ...
    def get_last_serial(self) -> int: ...
    def get_peer_credentials(self) -> typing.Optional[Credentials]: ...
    def get_stream(self) -> IOStream: ...
    def get_unique_name(self) -> typing.Optional[str]: ...
    def is_closed(self) -> bool: ...
    @staticmethod
    def new(
        stream: IOStream,
        guid: typing.Optional[str],
        flags: DBusConnectionFlags,
        observer: typing.Optional[DBusAuthObserver] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: AsyncResult) -> DBusConnection: ...
    @staticmethod
    def new_for_address(
        address: str,
        flags: DBusConnectionFlags,
        observer: typing.Optional[DBusAuthObserver] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_for_address_finish(cls, res: AsyncResult) -> DBusConnection: ...
    @classmethod
    def new_for_address_sync(
        cls,
        address: str,
        flags: DBusConnectionFlags,
        observer: typing.Optional[DBusAuthObserver] = None,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> DBusConnection: ...
    @classmethod
    def new_sync(
        cls,
        stream: IOStream,
        guid: typing.Optional[str],
        flags: DBusConnectionFlags,
        observer: typing.Optional[DBusAuthObserver] = None,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> DBusConnection: ...
    # override
    def register_object(
        self,
        object_path: str,
        interface_info: DBusInterfaceInfo,
        method_call_closure: (
            typing.Callable[
                [
                    DBusConnection,
                    str,
                    str,
                    str,
                    str,
                    GLib.Variant,
                    DBusMethodInvocation,
                ],
                typing.Any,
            ]
            | None
        ) = None,
        get_property_closure: (
            typing.Callable[[DBusConnection, str, str, str, str], typing.Any] | None
        ) = None,
        set_property_closure: typing.Callable[..., typing.Any] | None = None,
    ) -> int: ...
    def register_subtree(
        self,
        object_path: str,
        vtable: DBusSubtreeVTable,
        flags: DBusSubtreeFlags,
        user_data: None,
        user_data_free_func: typing.Callable[[None], None],
    ) -> int: ...
    def remove_filter(self, filter_id: int) -> None: ...
    def send_message(
        self, message: DBusMessage, flags: DBusSendMessageFlags
    ) -> typing.Tuple[bool, int]: ...
    def send_message_with_reply(
        self,
        message: DBusMessage,
        flags: DBusSendMessageFlags,
        timeout_msec: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> int: ...
    def send_message_with_reply_finish(self, res: AsyncResult) -> DBusMessage: ...
    def send_message_with_reply_sync(
        self,
        message: DBusMessage,
        flags: DBusSendMessageFlags,
        timeout_msec: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[DBusMessage, int]: ...
    def set_exit_on_close(self, exit_on_close: bool) -> None: ...
    def signal_subscribe(
        self,
        sender: typing.Optional[str],
        interface_name: typing.Optional[str],
        member: typing.Optional[str],
        object_path: typing.Optional[str],
        arg0: typing.Optional[str],
        flags: DBusSignalFlags,
        callback: typing.Callable[..., None],
        *user_data: typing.Any,
    ) -> int: ...
    def signal_unsubscribe(self, subscription_id: int) -> None: ...
    def start_message_processing(self) -> None: ...
    def unexport_action_group(self, export_id: int) -> None: ...
    def unexport_menu_model(self, export_id: int) -> None: ...
    def unregister_object(self, registration_id: int) -> bool: ...
    def unregister_subtree(self, registration_id: int) -> bool: ...

class DBusErrorEntry(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusErrorEntry()
    """

    error_code: int = ...
    dbus_error_name: str = ...

class DBusInterface(GObject.GInterface):
    """
    Interface GDBusInterface

    Signals from GObject:
      notify (GParam)
    """

    def get_info(self) -> DBusInterfaceInfo: ...
    def get_object(self) -> typing.Optional[DBusObject]: ...
    def set_object(self, object: typing.Optional[DBusObject] = None) -> None: ...

class DBusInterfaceIface(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusInterfaceIface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_info: typing.Callable[[DBusInterface], DBusInterfaceInfo] = ...
    get_object: typing.Callable[[DBusInterface], typing.Optional[DBusObject]] = ...
    set_object: typing.Callable[[DBusInterface, typing.Optional[DBusObject]], None] = (
        ...
    )
    dup_object: typing.Callable[[DBusInterface], typing.Optional[DBusObject]] = ...

class DBusInterfaceInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusInterfaceInfo()
    """

    ref_count: int = ...
    name: str = ...
    methods: list[DBusMethodInfo] = ...
    signals: list[DBusSignalInfo] = ...
    properties: list[DBusPropertyInfo] = ...
    annotations: list[DBusAnnotationInfo] = ...
    def cache_build(self) -> None: ...
    def cache_release(self) -> None: ...
    def generate_xml(self, indent: int, string_builder: GLib.String) -> None: ...
    def lookup_method(self, name: str) -> typing.Optional[DBusMethodInfo]: ...
    def lookup_property(self, name: str) -> typing.Optional[DBusPropertyInfo]: ...
    def lookup_signal(self, name: str) -> typing.Optional[DBusSignalInfo]: ...
    def ref(self) -> DBusInterfaceInfo: ...
    def unref(self) -> None: ...

class DBusInterfaceSkeleton(GObject.Object, DBusInterface):
    """
    :Constructors:

    ::

        DBusInterfaceSkeleton(**properties)

    Object GDBusInterfaceSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_flags: DBusInterfaceSkeletonFlags

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: DBusInterfaceSkeletonPrivate = ...
    def __init__(self, g_flags: DBusInterfaceSkeletonFlags = ...) -> None: ...
    def do_flush(self) -> None: ...
    def do_g_authorize_method(self, invocation: DBusMethodInvocation) -> bool: ...
    def do_get_info(self) -> DBusInterfaceInfo: ...
    def do_get_properties(self) -> GLib.Variant: ...
    def do_get_vtable(self) -> DBusInterfaceVTable: ...
    def export(self, connection: DBusConnection, object_path: str) -> bool: ...
    def flush(self) -> None: ...
    def get_connection(self) -> typing.Optional[DBusConnection]: ...
    def get_connections(self) -> list[DBusConnection]: ...
    def get_flags(self) -> DBusInterfaceSkeletonFlags: ...
    def get_info(self) -> DBusInterfaceInfo: ...
    def get_object_path(self) -> typing.Optional[str]: ...
    def get_properties(self) -> GLib.Variant: ...
    def get_vtable(self) -> DBusInterfaceVTable: ...
    def has_connection(self, connection: DBusConnection) -> bool: ...
    def set_flags(self, flags: DBusInterfaceSkeletonFlags) -> None: ...
    def unexport(self) -> None: ...
    def unexport_from_connection(self, connection: DBusConnection) -> None: ...

class DBusInterfaceSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusInterfaceSkeletonClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_info: typing.Callable[[DBusInterfaceSkeleton], DBusInterfaceInfo] = ...
    get_vtable: typing.Callable[[DBusInterfaceSkeleton], DBusInterfaceVTable] = ...
    get_properties: typing.Callable[[DBusInterfaceSkeleton], GLib.Variant] = ...
    flush: typing.Callable[[DBusInterfaceSkeleton], None] = ...
    vfunc_padding: list[None] = ...
    g_authorize_method: typing.Callable[
        [DBusInterfaceSkeleton, DBusMethodInvocation], bool
    ] = ...
    signal_padding: list[None] = ...

class DBusInterfaceSkeletonPrivate(GObject.GPointer): ...

class DBusInterfaceVTable(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusInterfaceVTable()
    """

    method_call: typing.Callable[..., None] = ...
    get_property: typing.Callable[..., GLib.Variant] = ...
    set_property: typing.Callable[..., bool] = ...
    padding: list[None] = ...

class DBusMenuModel(MenuModel):
    """
    :Constructors:

    ::

        DBusMenuModel(**properties)

    Object GDBusMenuModel

    Signals from GMenuModel:
      items-changed (gint, gint, gint)

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def get(
        connection: DBusConnection, bus_name: typing.Optional[str], object_path: str
    ) -> DBusMenuModel: ...

class DBusMessage(GObject.Object):
    """
    :Constructors:

    ::

        DBusMessage(**properties)
        new() -> Gio.DBusMessage
        new_from_blob(blob:list, capabilities:Gio.DBusCapabilityFlags) -> Gio.DBusMessage
        new_method_call(name:str=None, path:str, interface_:str=None, method:str) -> Gio.DBusMessage
        new_signal(path:str, interface_:str, signal:str) -> Gio.DBusMessage

    Object GDBusMessage

    Properties from GDBusMessage:
      locked -> gboolean: locked

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        locked: bool

    props: Props = ...
    @staticmethod
    def bytes_needed(blob: typing.Sequence[int]) -> int: ...
    def copy(self) -> DBusMessage: ...
    def get_arg0(self) -> typing.Optional[str]: ...
    def get_arg0_path(self) -> typing.Optional[str]: ...
    def get_body(self) -> typing.Optional[GLib.Variant]: ...
    def get_byte_order(self) -> DBusMessageByteOrder: ...
    def get_destination(self) -> typing.Optional[str]: ...
    def get_error_name(self) -> typing.Optional[str]: ...
    def get_flags(self) -> DBusMessageFlags: ...
    def get_header(
        self, header_field: DBusMessageHeaderField
    ) -> typing.Optional[GLib.Variant]: ...
    def get_header_fields(self) -> bytes: ...
    def get_interface(self) -> typing.Optional[str]: ...
    def get_locked(self) -> bool: ...
    def get_member(self) -> typing.Optional[str]: ...
    def get_message_type(self) -> DBusMessageType: ...
    def get_num_unix_fds(self) -> int: ...
    def get_path(self) -> typing.Optional[str]: ...
    def get_reply_serial(self) -> int: ...
    def get_sender(self) -> typing.Optional[str]: ...
    def get_serial(self) -> int: ...
    def get_signature(self) -> str: ...
    def get_unix_fd_list(self) -> typing.Optional[UnixFDList]: ...
    def lock(self) -> None: ...
    @classmethod
    def new(cls) -> DBusMessage: ...
    @classmethod
    def new_from_blob(
        cls, blob: typing.Sequence[int], capabilities: DBusCapabilityFlags
    ) -> DBusMessage: ...
    @classmethod
    def new_method_call(
        cls,
        name: typing.Optional[str],
        path: str,
        interface_: typing.Optional[str],
        method: str,
    ) -> DBusMessage: ...
    def new_method_error_literal(
        self, error_name: str, error_message: str
    ) -> DBusMessage: ...
    def new_method_reply(self) -> DBusMessage: ...
    @classmethod
    def new_signal(cls, path: str, interface_: str, signal: str) -> DBusMessage: ...
    def print_(self, indent: int) -> str: ...
    def set_body(self, body: GLib.Variant) -> None: ...
    def set_byte_order(self, byte_order: DBusMessageByteOrder) -> None: ...
    def set_destination(self, value: typing.Optional[str] = None) -> None: ...
    def set_error_name(self, value: str) -> None: ...
    def set_flags(self, flags: DBusMessageFlags) -> None: ...
    def set_header(
        self,
        header_field: DBusMessageHeaderField,
        value: typing.Optional[GLib.Variant] = None,
    ) -> None: ...
    def set_interface(self, value: typing.Optional[str] = None) -> None: ...
    def set_member(self, value: typing.Optional[str] = None) -> None: ...
    def set_message_type(self, type: DBusMessageType) -> None: ...
    def set_num_unix_fds(self, value: int) -> None: ...
    def set_path(self, value: typing.Optional[str] = None) -> None: ...
    def set_reply_serial(self, value: int) -> None: ...
    def set_sender(self, value: typing.Optional[str] = None) -> None: ...
    def set_serial(self, serial: int) -> None: ...
    def set_signature(self, value: typing.Optional[str] = None) -> None: ...
    def set_unix_fd_list(self, fd_list: typing.Optional[UnixFDList] = None) -> None: ...
    def to_blob(self, capabilities: DBusCapabilityFlags) -> bytes: ...
    def to_gerror(self) -> bool: ...

class DBusMethodInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusMethodInfo()
    """

    ref_count: int = ...
    name: str = ...
    in_args: list[DBusArgInfo] = ...
    out_args: list[DBusArgInfo] = ...
    annotations: list[DBusAnnotationInfo] = ...
    def ref(self) -> DBusMethodInfo: ...
    def unref(self) -> None: ...

class DBusMethodInvocation(GObject.Object):
    """
    :Constructors:

    ::

        DBusMethodInvocation(**properties)

    Object GDBusMethodInvocation

    Signals from GObject:
      notify (GParam)
    """

    def get_connection(self) -> DBusConnection: ...
    def get_interface_name(self) -> str: ...
    def get_message(self) -> DBusMessage: ...
    def get_method_info(self) -> typing.Optional[DBusMethodInfo]: ...
    def get_method_name(self) -> str: ...
    def get_object_path(self) -> str: ...
    def get_parameters(self) -> GLib.Variant: ...
    def get_property_info(self) -> typing.Optional[DBusPropertyInfo]: ...
    def get_sender(self) -> str: ...
    def return_dbus_error(self, error_name: str, error_message: str) -> None: ...
    def return_error_literal(self, domain: int, code: int, message: str) -> None: ...
    def return_gerror(self, error: GLib.Error) -> None: ...
    def return_value(
        self, parameters: typing.Optional[GLib.Variant] = None
    ) -> None: ...
    def return_value_with_unix_fd_list(
        self,
        parameters: typing.Optional[GLib.Variant] = None,
        fd_list: typing.Optional[UnixFDList] = None,
    ) -> None: ...

class DBusNodeInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusNodeInfo()
        new_for_xml(xml_data:str) -> Gio.DBusNodeInfo
    """

    ref_count: int = ...
    path: str = ...
    interfaces: list[DBusInterfaceInfo] = ...
    nodes: list[DBusNodeInfo] = ...
    annotations: list[DBusAnnotationInfo] = ...
    def generate_xml(self, indent: int, string_builder: GLib.String) -> None: ...
    def lookup_interface(self, name: str) -> typing.Optional[DBusInterfaceInfo]: ...
    @classmethod
    def new_for_xml(cls, xml_data: str) -> DBusNodeInfo: ...
    def ref(self) -> DBusNodeInfo: ...
    def unref(self) -> None: ...

class DBusObject(GObject.GInterface):
    """
    Interface GDBusObject

    Signals from GObject:
      notify (GParam)
    """

    def get_interface(self, interface_name: str) -> typing.Optional[DBusInterface]: ...
    def get_interfaces(self) -> list[DBusInterface]: ...
    def get_object_path(self) -> str: ...

class DBusObjectIface(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusObjectIface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_object_path: typing.Callable[[DBusObject], str] = ...
    get_interfaces: typing.Callable[[DBusObject], list[DBusInterface]] = ...
    get_interface: typing.Callable[
        [DBusObject, str], typing.Optional[DBusInterface]
    ] = ...
    interface_added: typing.Callable[[DBusObject, DBusInterface], None] = ...
    interface_removed: typing.Callable[[DBusObject, DBusInterface], None] = ...

class DBusObjectManager(GObject.GInterface):
    """
    Interface GDBusObjectManager

    Signals from GObject:
      notify (GParam)
    """

    def get_interface(
        self, object_path: str, interface_name: str
    ) -> typing.Optional[DBusInterface]: ...
    def get_object(self, object_path: str) -> typing.Optional[DBusObject]: ...
    def get_object_path(self) -> str: ...
    def get_objects(self) -> list[DBusObject]: ...

class DBusObjectManagerClient(
    GObject.Object, AsyncInitable, DBusObjectManager, Initable
):
    """
    :Constructors:

    ::

        DBusObjectManagerClient(**properties)
        new_finish(res:Gio.AsyncResult) -> Gio.DBusObjectManagerClient
        new_for_bus_finish(res:Gio.AsyncResult) -> Gio.DBusObjectManagerClient
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusObjectManagerClientFlags, name:str, object_path:str, get_proxy_type_func:Gio.DBusProxyTypeFunc=None, get_proxy_type_user_data=None, cancellable:Gio.Cancellable=None) -> Gio.DBusObjectManagerClient
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusObjectManagerClientFlags, name:str=None, object_path:str, get_proxy_type_func:Gio.DBusProxyTypeFunc=None, get_proxy_type_user_data=None, cancellable:Gio.Cancellable=None) -> Gio.DBusObjectManagerClient

    Object GDBusObjectManagerClient

    Signals from GDBusObjectManagerClient:
      interface-proxy-signal (GDBusObjectProxy, GDBusProxy, gchararray, gchararray, GVariant)
      interface-proxy-properties-changed (GDBusObjectProxy, GDBusProxy, GVariant, GStrv)

    Properties from GDBusObjectManagerClient:
      bus-type -> GBusType: bus-type
      connection -> GDBusConnection: connection
      flags -> GDBusObjectManagerClientFlags: flags
      object-path -> gchararray: object-path
      name -> gchararray: name
      name-owner -> gchararray: name-owner
      get-proxy-type-func -> gpointer: get-proxy-type-func
      get-proxy-type-user-data -> gpointer: get-proxy-type-user-data
      get-proxy-type-destroy-notify -> gpointer: get-proxy-type-destroy-notify

    Signals from GDBusObjectManager:
      object-added (GDBusObject)
      object-removed (GDBusObject)
      interface-added (GDBusObject, GDBusInterface)
      interface-removed (GDBusObject, GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connection: DBusConnection
        flags: DBusObjectManagerClientFlags
        get_proxy_type_destroy_notify: None
        get_proxy_type_func: None
        get_proxy_type_user_data: None
        name: str
        name_owner: typing.Optional[str]
        object_path: str
        bus_type: BusType

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: DBusObjectManagerClientPrivate = ...
    def __init__(
        self,
        bus_type: BusType = ...,
        connection: DBusConnection = ...,
        flags: DBusObjectManagerClientFlags = ...,
        get_proxy_type_destroy_notify: None = ...,
        get_proxy_type_func: None = ...,
        get_proxy_type_user_data: None = ...,
        name: str = ...,
        object_path: str = ...,
    ) -> None: ...
    def do_interface_proxy_properties_changed(
        self,
        object_proxy: DBusObjectProxy,
        interface_proxy: DBusProxy,
        changed_properties: GLib.Variant,
        invalidated_properties: str,
    ) -> None: ...
    def do_interface_proxy_signal(
        self,
        object_proxy: DBusObjectProxy,
        interface_proxy: DBusProxy,
        sender_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ) -> None: ...
    def get_connection(self) -> DBusConnection: ...
    def get_flags(self) -> DBusObjectManagerClientFlags: ...
    def get_name(self) -> str: ...
    def get_name_owner(self) -> typing.Optional[str]: ...
    @staticmethod
    def new(
        connection: DBusConnection,
        flags: DBusObjectManagerClientFlags,
        name: str,
        object_path: str,
        get_proxy_type_func: typing.Optional[
            typing.Callable[..., typing.Type[typing.Any]]
        ] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: AsyncResult) -> DBusObjectManagerClient: ...
    @staticmethod
    def new_for_bus(
        bus_type: BusType,
        flags: DBusObjectManagerClientFlags,
        name: str,
        object_path: str,
        get_proxy_type_func: typing.Optional[
            typing.Callable[..., typing.Type[typing.Any]]
        ] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: AsyncResult) -> DBusObjectManagerClient: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: BusType,
        flags: DBusObjectManagerClientFlags,
        name: str,
        object_path: str,
        get_proxy_type_func: typing.Optional[
            typing.Callable[..., typing.Type[typing.Any]]
        ] = None,
        cancellable: typing.Optional[Cancellable] = None,
        *get_proxy_type_user_data: typing.Any,
    ) -> DBusObjectManagerClient: ...
    @classmethod
    def new_sync(
        cls,
        connection: DBusConnection,
        flags: DBusObjectManagerClientFlags,
        name: typing.Optional[str],
        object_path: str,
        get_proxy_type_func: typing.Optional[
            typing.Callable[..., typing.Type[typing.Any]]
        ] = None,
        cancellable: typing.Optional[Cancellable] = None,
        *get_proxy_type_user_data: typing.Any,
    ) -> DBusObjectManagerClient: ...

class DBusObjectManagerClientClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusObjectManagerClientClass()
    """

    parent_class: GObject.ObjectClass = ...
    interface_proxy_signal: typing.Callable[
        [DBusObjectManagerClient, DBusObjectProxy, DBusProxy, str, str, GLib.Variant],
        None,
    ] = ...
    interface_proxy_properties_changed: typing.Callable[
        [DBusObjectManagerClient, DBusObjectProxy, DBusProxy, GLib.Variant, str], None
    ] = ...
    padding: list[None] = ...

class DBusObjectManagerClientPrivate(GObject.GPointer): ...

class DBusObjectManagerIface(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusObjectManagerIface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_object_path: typing.Callable[[DBusObjectManager], str] = ...
    get_objects: typing.Callable[[DBusObjectManager], list[DBusObject]] = ...
    get_object: typing.Callable[
        [DBusObjectManager, str], typing.Optional[DBusObject]
    ] = ...
    get_interface: typing.Callable[
        [DBusObjectManager, str, str], typing.Optional[DBusInterface]
    ] = ...
    object_added: typing.Callable[[DBusObjectManager, DBusObject], None] = ...
    object_removed: typing.Callable[[DBusObjectManager, DBusObject], None] = ...
    interface_added: typing.Callable[
        [DBusObjectManager, DBusObject, DBusInterface], None
    ] = ...
    interface_removed: typing.Callable[
        [DBusObjectManager, DBusObject, DBusInterface], None
    ] = ...

class DBusObjectManagerServer(GObject.Object, DBusObjectManager):
    """
    :Constructors:

    ::

        DBusObjectManagerServer(**properties)
        new(object_path:str) -> Gio.DBusObjectManagerServer

    Object GDBusObjectManagerServer

    Properties from GDBusObjectManagerServer:
      connection -> GDBusConnection: connection
      object-path -> gchararray: object-path

    Signals from GDBusObjectManager:
      object-added (GDBusObject)
      object-removed (GDBusObject)
      interface-added (GDBusObject, GDBusInterface)
      interface-removed (GDBusObject, GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connection: typing.Optional[DBusConnection]
        object_path: str

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: DBusObjectManagerServerPrivate = ...
    def __init__(
        self, connection: typing.Optional[DBusConnection] = ..., object_path: str = ...
    ) -> None: ...
    def export(self, object: DBusObjectSkeleton) -> None: ...
    def export_uniquely(self, object: DBusObjectSkeleton) -> None: ...
    def get_connection(self) -> typing.Optional[DBusConnection]: ...
    def is_exported(self, object: DBusObjectSkeleton) -> bool: ...
    @classmethod
    def new(cls, object_path: str) -> DBusObjectManagerServer: ...
    def set_connection(
        self, connection: typing.Optional[DBusConnection] = None
    ) -> None: ...
    def unexport(self, object_path: str) -> bool: ...

class DBusObjectManagerServerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusObjectManagerServerClass()
    """

    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class DBusObjectManagerServerPrivate(GObject.GPointer): ...

class DBusObjectProxy(GObject.Object, DBusObject):
    """
    :Constructors:

    ::

        DBusObjectProxy(**properties)
        new(connection:Gio.DBusConnection, object_path:str) -> Gio.DBusObjectProxy

    Object GDBusObjectProxy

    Properties from GDBusObjectProxy:
      g-object-path -> gchararray: g-object-path
      g-connection -> GDBusConnection: g-connection

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_connection: DBusConnection
        g_object_path: str

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: DBusObjectProxyPrivate = ...
    def __init__(
        self, g_connection: DBusConnection = ..., g_object_path: str = ...
    ) -> None: ...
    def get_connection(self) -> DBusConnection: ...
    @classmethod
    def new(cls, connection: DBusConnection, object_path: str) -> DBusObjectProxy: ...

class DBusObjectProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusObjectProxyClass()
    """

    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class DBusObjectProxyPrivate(GObject.GPointer): ...

class DBusObjectSkeleton(GObject.Object, DBusObject):
    """
    :Constructors:

    ::

        DBusObjectSkeleton(**properties)
        new(object_path:str) -> Gio.DBusObjectSkeleton

    Object GDBusObjectSkeleton

    Signals from GDBusObjectSkeleton:
      authorize-method (GDBusInterfaceSkeleton, GDBusMethodInvocation) -> gboolean

    Properties from GDBusObjectSkeleton:
      g-object-path -> gchararray: g-object-path

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_object_path: str

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: DBusObjectSkeletonPrivate = ...
    def __init__(self, g_object_path: str = ...) -> None: ...
    def add_interface(self, interface_: DBusInterfaceSkeleton) -> None: ...
    def do_authorize_method(
        self, interface_: DBusInterfaceSkeleton, invocation: DBusMethodInvocation
    ) -> bool: ...
    def flush(self) -> None: ...
    @classmethod
    def new(cls, object_path: str) -> DBusObjectSkeleton: ...
    def remove_interface(self, interface_: DBusInterfaceSkeleton) -> None: ...
    def remove_interface_by_name(self, interface_name: str) -> None: ...
    def set_object_path(self, object_path: str) -> None: ...

class DBusObjectSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusObjectSkeletonClass()
    """

    parent_class: GObject.ObjectClass = ...
    authorize_method: typing.Callable[
        [DBusObjectSkeleton, DBusInterfaceSkeleton, DBusMethodInvocation], bool
    ] = ...
    padding: list[None] = ...

class DBusObjectSkeletonPrivate(GObject.GPointer): ...

class DBusPropertyInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusPropertyInfo()
    """

    ref_count: int = ...
    name: str = ...
    signature: str = ...
    flags: DBusPropertyInfoFlags = ...
    annotations: list[DBusAnnotationInfo] = ...
    def ref(self) -> DBusPropertyInfo: ...
    def unref(self) -> None: ...

class DBusProxy(GObject.Object, AsyncInitable, DBusInterface, Initable):
    """
    Provide comfortable and pythonic method calls.

        This marshalls the method arguments into a GVariant, invokes the
        call_sync() method on the DBusProxy object, and unmarshalls the result
        GVariant back into a Python tuple.

        The first argument always needs to be the D-Bus signature tuple of the
        method call. Example:

          proxy = Gio.DBusProxy.new_sync(...)
          result = proxy.MyMethod('(is)', 42, 'hello')

        The exception are methods which take no arguments, like
        proxy.MyMethod('()'). For these you can omit the signature and just write
        proxy.MyMethod().

        Optional keyword arguments:

        - timeout: timeout for the call in milliseconds (default to D-Bus timeout)

        - flags: Combination of Gio.DBusCallFlags.*

        - result_handler: Do an asynchronous method call and invoke
             result_handler(proxy_object, result, user_data) when it finishes.

        - error_handler: If the asynchronous call raises an exception,
          error_handler(proxy_object, exception, user_data) is called when it
          finishes. If error_handler is not given, result_handler is called with
          the exception object as result instead.

        - user_data: Optional user data to pass to result_handler for
          asynchronous calls.

        Example for asynchronous calls:

          def mymethod_done(proxy, result, user_data):
              if isinstance(result, Exception):
                  # handle error
              else:
                  # do something with result

          proxy.MyMethod('(is)', 42, 'hello',
              result_handler=mymethod_done, user_data='data')

    Object GDBusProxy

    Provide comfortable and pythonic method calls.

        This marshalls the method arguments into a GVariant, invokes the
        call_sync() method on the DBusProxy object, and unmarshalls the result
        GVariant back into a Python tuple.

        The first argument always needs to be the D-Bus signature tuple of the
        method call. Example:

          proxy = Gio.DBusProxy.new_sync(...)
          result = proxy.MyMethod('(is)', 42, 'hello')

        The exception are methods which take no arguments, like
        proxy.MyMethod('()'). For these you can omit the signature and just write
        proxy.MyMethod().

        Optional keyword arguments:

        - timeout: timeout for the call in milliseconds (default to D-Bus timeout)

        - flags: Combination of Gio.DBusCallFlags.*

        - result_handler: Do an asynchronous method call and invoke
             result_handler(proxy_object, result, user_data) when it finishes.

        - error_handler: If the asynchronous call raises an exception,
          error_handler(proxy_object, exception, user_data) is called when it
          finishes. If error_handler is not given, result_handler is called with
          the exception object as result instead.

        - user_data: Optional user data to pass to result_handler for
          asynchronous calls.

        Example for asynchronous calls:

          def mymethod_done(proxy, result, user_data):
              if isinstance(result, Exception):
                  # handle error
              else:
                  # do something with result

          proxy.MyMethod('(is)', 42, 'hello',
              result_handler=mymethod_done, user_data='data')


    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
      g-bus-type -> GBusType: g-bus-type
      g-name -> gchararray: g-name
      g-name-owner -> gchararray: g-name-owner
      g-flags -> GDBusProxyFlags: g-flags
      g-object-path -> gchararray: g-object-path
      g-interface-name -> gchararray: g-interface-name
      g-default-timeout -> gint: g-default-timeout
      g-interface-info -> GDBusInterfaceInfo: g-interface-info

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_connection: DBusConnection
        g_default_timeout: int
        g_flags: DBusProxyFlags
        g_interface_info: DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: BusType

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: DBusProxyPrivate = ...
    def __init__(
        self,
        g_bus_type: BusType = ...,
        g_connection: DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: DBusProxyFlags = ...,
        g_interface_info: DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ) -> None: ...
    def call(
        self,
        method_name: str,
        parameters: typing.Optional[GLib.Variant],
        flags: DBusCallFlags,
        timeout_msec: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def call_finish(self, res: AsyncResult) -> GLib.Variant: ...
    def call_sync(
        self,
        method_name: str,
        parameters: typing.Optional[GLib.Variant],
        flags: DBusCallFlags,
        timeout_msec: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> GLib.Variant: ...
    def call_with_unix_fd_list(
        self,
        method_name: str,
        parameters: typing.Optional[GLib.Variant],
        flags: DBusCallFlags,
        timeout_msec: int,
        fd_list: typing.Optional[UnixFDList] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def call_with_unix_fd_list_finish(
        self, res: AsyncResult
    ) -> typing.Tuple[GLib.Variant, UnixFDList]: ...
    def call_with_unix_fd_list_sync(
        self,
        method_name: str,
        parameters: typing.Optional[GLib.Variant],
        flags: DBusCallFlags,
        timeout_msec: int,
        fd_list: typing.Optional[UnixFDList] = None,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[GLib.Variant, UnixFDList]: ...
    def do_g_properties_changed(
        self, changed_properties: GLib.Variant, invalidated_properties: str
    ) -> None: ...
    def do_g_signal(
        self, sender_name: str, signal_name: str, parameters: GLib.Variant
    ) -> None: ...
    def get_cached_property(
        self, property_name: str
    ) -> typing.Optional[GLib.Variant]: ...
    def get_cached_property_names(self) -> typing.Optional[list[str]]: ...
    def get_connection(self) -> DBusConnection: ...
    def get_default_timeout(self) -> int: ...
    def get_flags(self) -> DBusProxyFlags: ...
    def get_interface_info(self) -> typing.Optional[DBusInterfaceInfo]: ...
    def get_interface_name(self) -> str: ...
    def get_name(self) -> typing.Optional[str]: ...
    def get_name_owner(self) -> typing.Optional[str]: ...
    def get_object_path(self) -> str: ...
    @staticmethod
    def new(
        connection: DBusConnection,
        flags: DBusProxyFlags,
        info: typing.Optional[DBusInterfaceInfo],
        name: typing.Optional[str],
        object_path: str,
        interface_name: str,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: AsyncResult) -> DBusProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: BusType,
        flags: DBusProxyFlags,
        info: typing.Optional[DBusInterfaceInfo],
        name: str,
        object_path: str,
        interface_name: str,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: AsyncResult) -> DBusProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: BusType,
        flags: DBusProxyFlags,
        info: typing.Optional[DBusInterfaceInfo],
        name: str,
        object_path: str,
        interface_name: str,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> DBusProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: DBusConnection,
        flags: DBusProxyFlags,
        info: typing.Optional[DBusInterfaceInfo],
        name: typing.Optional[str],
        object_path: str,
        interface_name: str,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> DBusProxy: ...
    def set_cached_property(
        self, property_name: str, value: typing.Optional[GLib.Variant] = None
    ) -> None: ...
    def set_default_timeout(self, timeout_msec: int) -> None: ...
    def set_interface_info(
        self, info: typing.Optional[DBusInterfaceInfo] = None
    ) -> None: ...

class DBusProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusProxyClass()
    """

    parent_class: GObject.ObjectClass = ...
    g_properties_changed: typing.Callable[[DBusProxy, GLib.Variant, str], None] = ...
    g_signal: typing.Callable[[DBusProxy, str, str, GLib.Variant], None] = ...
    padding: list[None] = ...

class DBusProxyPrivate(GObject.GPointer): ...

class DBusServer(GObject.Object, Initable):
    """
    :Constructors:

    ::

        DBusServer(**properties)
        new_sync(address:str, flags:Gio.DBusServerFlags, guid:str, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None) -> Gio.DBusServer

    Object GDBusServer

    Signals from GDBusServer:
      new-connection (GDBusConnection) -> gboolean

    Properties from GDBusServer:
      address -> gchararray: address
      client-address -> gchararray: client-address
      flags -> GDBusServerFlags: flags
      guid -> gchararray: guid
      active -> gboolean: active
      authentication-observer -> GDBusAuthObserver: authentication-observer

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        active: bool
        address: str
        authentication_observer: DBusAuthObserver
        client_address: str
        flags: DBusServerFlags
        guid: str

    props: Props = ...
    def __init__(
        self,
        address: str = ...,
        authentication_observer: DBusAuthObserver = ...,
        flags: DBusServerFlags = ...,
        guid: str = ...,
    ) -> None: ...
    def get_client_address(self) -> str: ...
    def get_flags(self) -> DBusServerFlags: ...
    def get_guid(self) -> str: ...
    def is_active(self) -> bool: ...
    @classmethod
    def new_sync(
        cls,
        address: str,
        flags: DBusServerFlags,
        guid: str,
        observer: typing.Optional[DBusAuthObserver] = None,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> DBusServer: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class DBusSignalInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusSignalInfo()
    """

    ref_count: int = ...
    name: str = ...
    args: list[DBusArgInfo] = ...
    annotations: list[DBusAnnotationInfo] = ...
    def ref(self) -> DBusSignalInfo: ...
    def unref(self) -> None: ...

class DBusSubtreeVTable(GObject.GPointer):
    """
    :Constructors:

    ::

        DBusSubtreeVTable()
    """

    enumerate: typing.Callable[..., list[str]] = ...
    introspect: typing.Callable[..., typing.Optional[list[DBusInterfaceInfo]]] = ...
    dispatch: typing.Callable[..., typing.Optional[DBusInterfaceVTable]] = ...
    padding: list[None] = ...

class DataInputStream(BufferedInputStream, Seekable):
    """
    :Constructors:

    ::

        DataInputStream(**properties)
        new(base_stream:Gio.InputStream) -> Gio.DataInputStream

    Object GDataInputStream

    Properties from GDataInputStream:
      byte-order -> GDataStreamByteOrder: byte-order
      newline-type -> GDataStreamNewlineType: newline-type

    Properties from GBufferedInputStream:
      buffer-size -> guint: buffer-size

    Properties from GFilterInputStream:
      base-stream -> GInputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        byte_order: DataStreamByteOrder
        newline_type: DataStreamNewlineType
        buffer_size: int
        base_stream: InputStream
        close_base_stream: bool

    props: Props = ...
    parent_instance: BufferedInputStream = ...
    priv: DataInputStreamPrivate = ...
    def __init__(
        self,
        byte_order: DataStreamByteOrder = ...,
        newline_type: DataStreamNewlineType = ...,
        buffer_size: int = ...,
        base_stream: InputStream = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def get_byte_order(self) -> DataStreamByteOrder: ...
    def get_newline_type(self) -> DataStreamNewlineType: ...
    @classmethod
    def new(cls, base_stream: InputStream) -> DataInputStream: ...
    def read_byte(self, cancellable: typing.Optional[Cancellable] = None) -> int: ...
    def read_int16(self, cancellable: typing.Optional[Cancellable] = None) -> int: ...
    def read_int32(self, cancellable: typing.Optional[Cancellable] = None) -> int: ...
    def read_int64(self, cancellable: typing.Optional[Cancellable] = None) -> int: ...
    def read_line(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[typing.Optional[bytes], int]: ...
    def read_line_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def read_line_finish(
        self, result: AsyncResult
    ) -> typing.Tuple[typing.Optional[bytes], int]: ...
    def read_line_finish_utf8(
        self, result: AsyncResult
    ) -> typing.Tuple[typing.Optional[str], int]: ...
    def read_line_utf8(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[typing.Optional[str], int]: ...
    def read_uint16(self, cancellable: typing.Optional[Cancellable] = None) -> int: ...
    def read_uint32(self, cancellable: typing.Optional[Cancellable] = None) -> int: ...
    def read_uint64(self, cancellable: typing.Optional[Cancellable] = None) -> int: ...
    def read_until(
        self, stop_chars: str, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[str, int]: ...
    def read_until_async(
        self,
        stop_chars: str,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def read_until_finish(self, result: AsyncResult) -> typing.Tuple[str, int]: ...
    def read_upto(
        self,
        stop_chars: str,
        stop_chars_len: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[str, int]: ...
    def read_upto_async(
        self,
        stop_chars: str,
        stop_chars_len: int,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def read_upto_finish(self, result: AsyncResult) -> typing.Tuple[str, int]: ...
    def set_byte_order(self, order: DataStreamByteOrder) -> None: ...
    def set_newline_type(self, type: DataStreamNewlineType) -> None: ...

class DataInputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DataInputStreamClass()
    """

    parent_class: BufferedInputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class DataInputStreamPrivate(GObject.GPointer): ...

class DataOutputStream(FilterOutputStream, Seekable):
    """
    :Constructors:

    ::

        DataOutputStream(**properties)
        new(base_stream:Gio.OutputStream) -> Gio.DataOutputStream

    Object GDataOutputStream

    Properties from GDataOutputStream:
      byte-order -> GDataStreamByteOrder: byte-order

    Properties from GFilterOutputStream:
      base-stream -> GOutputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        byte_order: DataStreamByteOrder
        base_stream: OutputStream
        close_base_stream: bool

    props: Props = ...
    parent_instance: FilterOutputStream = ...
    priv: DataOutputStreamPrivate = ...
    def __init__(
        self,
        byte_order: DataStreamByteOrder = ...,
        base_stream: OutputStream = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def get_byte_order(self) -> DataStreamByteOrder: ...
    @classmethod
    def new(cls, base_stream: OutputStream) -> DataOutputStream: ...
    def put_byte(
        self, data: int, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def put_int16(
        self, data: int, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def put_int32(
        self, data: int, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def put_int64(
        self, data: int, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def put_string(
        self, str: str, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def put_uint16(
        self, data: int, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def put_uint32(
        self, data: int, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def put_uint64(
        self, data: int, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def set_byte_order(self, order: DataStreamByteOrder) -> None: ...

class DataOutputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DataOutputStreamClass()
    """

    parent_class: FilterOutputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class DataOutputStreamPrivate(GObject.GPointer): ...

class DatagramBased(GObject.GInterface):
    """
    Interface GDatagramBased

    Signals from GObject:
      notify (GParam)
    """

    def condition_check(self, condition: GLib.IOCondition) -> GLib.IOCondition: ...
    def condition_wait(
        self,
        condition: GLib.IOCondition,
        timeout: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def create_source(
        self,
        condition: GLib.IOCondition,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> GLib.Source: ...
    def receive_messages(
        self,
        messages: typing.Sequence[InputMessage],
        flags: int,
        timeout: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def send_messages(
        self,
        messages: typing.Sequence[OutputMessage],
        flags: int,
        timeout: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...

class DatagramBasedInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        DatagramBasedInterface()
    """

    g_iface: GObject.TypeInterface = ...
    receive_messages: typing.Callable[
        [
            DatagramBased,
            typing.Sequence[InputMessage],
            int,
            int,
            typing.Optional[Cancellable],
        ],
        int,
    ] = ...
    send_messages: typing.Callable[
        [
            DatagramBased,
            typing.Sequence[OutputMessage],
            int,
            int,
            typing.Optional[Cancellable],
        ],
        int,
    ] = ...
    create_source: typing.Callable[
        [DatagramBased, GLib.IOCondition, typing.Optional[Cancellable]], GLib.Source
    ] = ...
    condition_check: typing.Callable[
        [DatagramBased, GLib.IOCondition], GLib.IOCondition
    ] = ...
    condition_wait: typing.Callable[
        [DatagramBased, GLib.IOCondition, int, typing.Optional[Cancellable]], bool
    ] = ...

class DebugController(GObject.GInterface):
    """
    Interface GDebugController

    Signals from GObject:
      notify (GParam)
    """

    def get_debug_enabled(self) -> bool: ...
    def set_debug_enabled(self, debug_enabled: bool) -> None: ...

class DebugControllerDBus(GObject.Object, DebugController, Initable):
    """
    :Constructors:

    ::

        DebugControllerDBus(**properties)
        new(connection:Gio.DBusConnection, cancellable:Gio.Cancellable=None) -> Gio.DebugControllerDBus or None

    Object GDebugControllerDBus

    Signals from GDebugControllerDBus:
      authorize (GDBusMethodInvocation) -> gboolean

    Properties from GDebugControllerDBus:
      connection -> GDBusConnection: connection

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connection: DBusConnection
        debug_enabled: bool

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self, connection: DBusConnection = ..., debug_enabled: bool = ...
    ) -> None: ...
    def do_authorize(self, invocation: DBusMethodInvocation) -> bool: ...
    @classmethod
    def new(
        cls,
        connection: DBusConnection,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Optional[DebugControllerDBus]: ...
    def stop(self) -> None: ...

class DebugControllerDBusClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DebugControllerDBusClass()
    """

    parent_class: GObject.ObjectClass = ...
    authorize: typing.Callable[[DebugControllerDBus, DBusMethodInvocation], bool] = ...
    padding: list[None] = ...

class DebugControllerInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        DebugControllerInterface()
    """

    g_iface: GObject.TypeInterface = ...

class DesktopAppInfo(GObject.Object, AppInfo):
    """
    :Constructors:

    ::

        DesktopAppInfo(**properties)
        new(desktop_id:str) -> Gio.DesktopAppInfo or None
        new_from_filename(filename:str) -> Gio.DesktopAppInfo or None
        new_from_keyfile(key_file:GLib.KeyFile) -> Gio.DesktopAppInfo or None

    Object GDesktopAppInfo

    Properties from GDesktopAppInfo:
      filename -> gchararray: filename

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        filename: typing.Optional[str]

    props: Props = ...
    def __init__(self, filename: str = ...) -> None: ...
    def get_action_name(self, action_name: str) -> str: ...
    def get_boolean(self, key: str) -> bool: ...
    def get_categories(self) -> typing.Optional[str]: ...
    def get_filename(self) -> typing.Optional[str]: ...
    def get_generic_name(self) -> typing.Optional[str]: ...
    @staticmethod
    def get_implementations(interface: str) -> list[DesktopAppInfo]: ...
    def get_is_hidden(self) -> bool: ...
    def get_keywords(self) -> list[str]: ...
    def get_locale_string(self, key: str) -> typing.Optional[str]: ...
    def get_nodisplay(self) -> bool: ...
    def get_show_in(self, desktop_env: typing.Optional[str] = None) -> bool: ...
    def get_startup_wm_class(self) -> typing.Optional[str]: ...
    def get_string(self, key: str) -> typing.Optional[str]: ...
    def get_string_list(self, key: str) -> list[str]: ...
    def has_key(self, key: str) -> bool: ...
    def launch_action(
        self, action_name: str, launch_context: typing.Optional[AppLaunchContext] = None
    ) -> None: ...
    def launch_uris_as_manager(
        self,
        uris: list[str],
        launch_context: typing.Optional[AppLaunchContext],
        spawn_flags: GLib.SpawnFlags,
        user_setup: typing.Optional[typing.Callable[..., None]] = None,
        pid_callback: typing.Optional[typing.Callable[..., None]] = None,
        *pid_callback_data: typing.Any,
    ) -> bool: ...
    def launch_uris_as_manager_with_fds(
        self,
        uris: list[str],
        launch_context: typing.Optional[AppLaunchContext],
        spawn_flags: GLib.SpawnFlags,
        user_setup: typing.Optional[typing.Callable[..., None]],
        pid_callback: typing.Optional[typing.Callable[..., None]],
        stdin_fd: int,
        stdout_fd: int,
        stderr_fd: int,
        *pid_callback_data: typing.Any,
    ) -> bool: ...
    def list_actions(self) -> list[str]: ...
    @classmethod
    def new(cls, desktop_id: str) -> typing.Optional[DesktopAppInfo]: ...
    @classmethod
    def new_from_filename(cls, filename: str) -> typing.Optional[DesktopAppInfo]: ...
    @classmethod
    def new_from_keyfile(
        cls, key_file: GLib.KeyFile
    ) -> typing.Optional[DesktopAppInfo]: ...
    @staticmethod
    def search(search_string: str) -> list[typing.Sequence[str]]: ...
    @staticmethod
    def set_desktop_env(desktop_env: str) -> None: ...

class DesktopAppInfoClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DesktopAppInfoClass()
    """

    parent_class: GObject.ObjectClass = ...

class DesktopAppInfoLookup(GObject.GInterface):
    """
    Interface GDesktopAppInfoLookup

    Signals from GObject:
      notify (GParam)
    """

    def get_default_for_uri_scheme(
        self, uri_scheme: str
    ) -> typing.Optional[AppInfo]: ...

class DesktopAppInfoLookupIface(GObject.GPointer):
    """
    :Constructors:

    ::

        DesktopAppInfoLookupIface()
    """

    g_iface: GObject.TypeInterface = ...
    get_default_for_uri_scheme: typing.Callable[
        [DesktopAppInfoLookup, str], typing.Optional[AppInfo]
    ] = ...

class Drive(GObject.GInterface):
    """
    Interface GDrive

    Signals from GObject:
      notify (GParam)
    """

    def can_eject(self) -> bool: ...
    def can_poll_for_media(self) -> bool: ...
    def can_start(self) -> bool: ...
    def can_start_degraded(self) -> bool: ...
    def can_stop(self) -> bool: ...
    def eject(
        self,
        flags: MountUnmountFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def eject_finish(self, result: AsyncResult) -> bool: ...
    def eject_with_operation(
        self,
        flags: MountUnmountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def eject_with_operation_finish(self, result: AsyncResult) -> bool: ...
    def enumerate_identifiers(self) -> list[str]: ...
    def get_icon(self) -> Icon: ...
    def get_identifier(self, kind: str) -> typing.Optional[str]: ...
    def get_name(self) -> str: ...
    def get_sort_key(self) -> typing.Optional[str]: ...
    def get_start_stop_type(self) -> DriveStartStopType: ...
    def get_symbolic_icon(self) -> Icon: ...
    def get_volumes(self) -> list[Volume]: ...
    def has_media(self) -> bool: ...
    def has_volumes(self) -> bool: ...
    def is_media_check_automatic(self) -> bool: ...
    def is_media_removable(self) -> bool: ...
    def is_removable(self) -> bool: ...
    def poll_for_media(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def poll_for_media_finish(self, result: AsyncResult) -> bool: ...
    def start(
        self,
        flags: DriveStartFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def start_finish(self, result: AsyncResult) -> bool: ...
    def stop(
        self,
        flags: MountUnmountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def stop_finish(self, result: AsyncResult) -> bool: ...

class DriveIface(GObject.GPointer):
    """
    :Constructors:

    ::

        DriveIface()
    """

    g_iface: GObject.TypeInterface = ...
    changed: typing.Callable[[Drive], None] = ...
    disconnected: typing.Callable[[Drive], None] = ...
    eject_button: typing.Callable[[Drive], None] = ...
    get_name: typing.Callable[[Drive], str] = ...
    get_icon: typing.Callable[[Drive], Icon] = ...
    has_volumes: typing.Callable[[Drive], bool] = ...
    get_volumes: typing.Callable[[Drive], list[Volume]] = ...
    is_media_removable: typing.Callable[[Drive], bool] = ...
    has_media: typing.Callable[[Drive], bool] = ...
    is_media_check_automatic: typing.Callable[[Drive], bool] = ...
    can_eject: typing.Callable[[Drive], bool] = ...
    can_poll_for_media: typing.Callable[[Drive], bool] = ...
    eject: typing.Callable[..., None] = ...
    eject_finish: typing.Callable[[Drive, AsyncResult], bool] = ...
    poll_for_media: typing.Callable[..., None] = ...
    poll_for_media_finish: typing.Callable[[Drive, AsyncResult], bool] = ...
    get_identifier: typing.Callable[[Drive, str], typing.Optional[str]] = ...
    enumerate_identifiers: typing.Callable[[Drive], list[str]] = ...
    get_start_stop_type: typing.Callable[[Drive], DriveStartStopType] = ...
    can_start: typing.Callable[[Drive], bool] = ...
    can_start_degraded: typing.Callable[[Drive], bool] = ...
    start: typing.Callable[..., None] = ...
    start_finish: typing.Callable[[Drive, AsyncResult], bool] = ...
    can_stop: typing.Callable[[Drive], bool] = ...
    stop: typing.Callable[..., None] = ...
    stop_finish: typing.Callable[[Drive, AsyncResult], bool] = ...
    stop_button: typing.Callable[[Drive], None] = ...
    eject_with_operation: typing.Callable[..., None] = ...
    eject_with_operation_finish: typing.Callable[[Drive, AsyncResult], bool] = ...
    get_sort_key: typing.Callable[[Drive], typing.Optional[str]] = ...
    get_symbolic_icon: typing.Callable[[Drive], Icon] = ...
    is_removable: typing.Callable[[Drive], bool] = ...

class DtlsClientConnection(GObject.GInterface):
    """
    Interface GDtlsClientConnection

    Signals from GObject:
      notify (GParam)
    """

    def get_accepted_cas(self) -> list[typing.Sequence[int]]: ...
    def get_server_identity(self) -> SocketConnectable: ...
    def get_validation_flags(self) -> TlsCertificateFlags: ...
    @staticmethod
    def new(
        base_socket: DatagramBased,
        server_identity: typing.Optional[SocketConnectable] = None,
    ) -> DtlsClientConnection: ...
    def set_server_identity(self, identity: SocketConnectable) -> None: ...
    def set_validation_flags(self, flags: TlsCertificateFlags) -> None: ...

class DtlsClientConnectionInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        DtlsClientConnectionInterface()
    """

    g_iface: GObject.TypeInterface = ...

class DtlsConnection(GObject.GInterface):
    """
    Interface GDtlsConnection

    Signals from GObject:
      notify (GParam)
    """

    def close(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def close_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def close_finish(self, result: AsyncResult) -> bool: ...
    def emit_accept_certificate(
        self, peer_cert: TlsCertificate, errors: TlsCertificateFlags
    ) -> bool: ...
    def get_certificate(self) -> typing.Optional[TlsCertificate]: ...
    def get_channel_binding_data(
        self, type: TlsChannelBindingType
    ) -> typing.Tuple[bool, bytes]: ...
    def get_ciphersuite_name(self) -> typing.Optional[str]: ...
    def get_database(self) -> typing.Optional[TlsDatabase]: ...
    def get_interaction(self) -> typing.Optional[TlsInteraction]: ...
    def get_negotiated_protocol(self) -> typing.Optional[str]: ...
    def get_peer_certificate(self) -> typing.Optional[TlsCertificate]: ...
    def get_peer_certificate_errors(self) -> TlsCertificateFlags: ...
    def get_protocol_version(self) -> TlsProtocolVersion: ...
    def get_rehandshake_mode(self) -> TlsRehandshakeMode: ...
    def get_require_close_notify(self) -> bool: ...
    def handshake(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def handshake_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def handshake_finish(self, result: AsyncResult) -> bool: ...
    def set_advertised_protocols(
        self, protocols: typing.Optional[typing.Sequence[str]] = None
    ) -> None: ...
    def set_certificate(self, certificate: TlsCertificate) -> None: ...
    def set_database(self, database: typing.Optional[TlsDatabase] = None) -> None: ...
    def set_interaction(
        self, interaction: typing.Optional[TlsInteraction] = None
    ) -> None: ...
    def set_rehandshake_mode(self, mode: TlsRehandshakeMode) -> None: ...
    def set_require_close_notify(self, require_close_notify: bool) -> None: ...
    def shutdown(
        self,
        shutdown_read: bool,
        shutdown_write: bool,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def shutdown_async(
        self,
        shutdown_read: bool,
        shutdown_write: bool,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def shutdown_finish(self, result: AsyncResult) -> bool: ...

class DtlsConnectionInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        DtlsConnectionInterface()
    """

    g_iface: GObject.TypeInterface = ...
    accept_certificate: typing.Callable[
        [DtlsConnection, TlsCertificate, TlsCertificateFlags], bool
    ] = ...
    handshake: typing.Callable[[DtlsConnection, typing.Optional[Cancellable]], bool] = (
        ...
    )
    handshake_async: typing.Callable[..., None] = ...
    handshake_finish: typing.Callable[[DtlsConnection, AsyncResult], bool] = ...
    shutdown: typing.Callable[
        [DtlsConnection, bool, bool, typing.Optional[Cancellable]], bool
    ] = ...
    shutdown_async: typing.Callable[..., None] = ...
    shutdown_finish: typing.Callable[[DtlsConnection, AsyncResult], bool] = ...
    set_advertised_protocols: typing.Callable[
        [DtlsConnection, typing.Optional[typing.Sequence[str]]], None
    ] = ...
    get_negotiated_protocol: typing.Callable[[DtlsConnection], typing.Optional[str]] = (
        ...
    )
    get_binding_data: typing.Callable[
        [DtlsConnection, TlsChannelBindingType, typing.Sequence[int]], bool
    ] = ...

class DtlsServerConnection(GObject.GInterface):
    """
    Interface GDtlsServerConnection

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def new(
        base_socket: DatagramBased, certificate: typing.Optional[TlsCertificate] = None
    ) -> DtlsServerConnection: ...

class DtlsServerConnectionInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        DtlsServerConnectionInterface()
    """

    g_iface: GObject.TypeInterface = ...

class Emblem(GObject.Object, Icon):
    """
    :Constructors:

    ::

        Emblem(**properties)
        new(icon:Gio.Icon) -> Gio.Emblem
        new_with_origin(icon:Gio.Icon, origin:Gio.EmblemOrigin) -> Gio.Emblem

    Object GEmblem

    Properties from GEmblem:
      icon -> GObject: icon
      origin -> GEmblemOrigin: origin

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        icon: GObject.Object
        origin: EmblemOrigin

    props: Props = ...
    # override
    def __init__(
        self, *, icon: GObject.Object = ..., origin: EmblemOrigin = ...
    ) -> None: ...
    def get_icon(self) -> Icon: ...
    def get_origin(self) -> EmblemOrigin: ...
    @classmethod
    def new(cls, icon: Icon) -> Emblem: ...
    @classmethod
    def new_with_origin(cls, icon: Icon, origin: EmblemOrigin) -> Emblem: ...

class EmblemClass(GObject.GPointer): ...

class EmblemedIcon(GObject.Object, Icon):
    """
    :Constructors:

    ::

        EmblemedIcon(**properties)
        new(icon:Gio.Icon, emblem:Gio.Emblem=None) -> Gio.EmblemedIcon

    Object GEmblemedIcon

    Properties from GEmblemedIcon:
      gicon -> GIcon: gicon

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        gicon: Icon

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: EmblemedIconPrivate = ...
    # override
    def __init__(self, *, gicon: Icon = ...) -> None: ...
    def add_emblem(self, emblem: Emblem) -> None: ...
    def clear_emblems(self) -> None: ...
    def get_emblems(self) -> list[Emblem]: ...
    def get_icon(self) -> Icon: ...
    @classmethod
    def new(
        cls, icon: Icon, emblem: typing.Optional[Emblem] = None
    ) -> EmblemedIcon: ...

class EmblemedIconClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EmblemedIconClass()
    """

    parent_class: GObject.ObjectClass = ...

class EmblemedIconPrivate(GObject.GPointer): ...

class File(GObject.GInterface):
    """
    Interface GFile

    Signals from GObject:
      notify (GParam)
    """

    def append_to(
        self, flags: FileCreateFlags, cancellable: typing.Optional[Cancellable] = None
    ) -> FileOutputStream: ...
    def append_to_async(
        self,
        flags: FileCreateFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def append_to_finish(self, res: AsyncResult) -> FileOutputStream: ...
    def build_attribute_list_for_copy(
        self, flags: FileCopyFlags, cancellable: typing.Optional[Cancellable] = None
    ) -> str: ...
    def copy(
        self,
        destination: File,
        flags: FileCopyFlags,
        cancellable: typing.Optional[Cancellable] = None,
        progress_callback: typing.Optional[typing.Callable[..., None]] = None,
        *progress_callback_data: typing.Any,
    ) -> bool: ...
    def copy_async(
        self,
        destination: File,
        flags: FileCopyFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable],
        progress_callback_closure: typing.Optional[typing.Callable[..., typing.Any]],
        ready_callback_closure: typing.Callable[..., typing.Any],
    ) -> None: ...
    def copy_attributes(
        self,
        destination: File,
        flags: FileCopyFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def copy_finish(self, res: AsyncResult) -> bool: ...
    def create(
        self, flags: FileCreateFlags, cancellable: typing.Optional[Cancellable] = None
    ) -> FileOutputStream: ...
    def create_async(
        self,
        flags: FileCreateFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def create_finish(self, res: AsyncResult) -> FileOutputStream: ...
    def create_readwrite(
        self, flags: FileCreateFlags, cancellable: typing.Optional[Cancellable] = None
    ) -> FileIOStream: ...
    def create_readwrite_async(
        self,
        flags: FileCreateFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def create_readwrite_finish(self, res: AsyncResult) -> FileIOStream: ...
    def delete(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def delete_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def delete_finish(self, result: AsyncResult) -> bool: ...
    def dup(self) -> File: ...
    def eject_mountable(
        self,
        flags: MountUnmountFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def eject_mountable_finish(self, result: AsyncResult) -> bool: ...
    def eject_mountable_with_operation(
        self,
        flags: MountUnmountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def eject_mountable_with_operation_finish(self, result: AsyncResult) -> bool: ...
    def enumerate_children(
        self,
        attributes: str,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> FileEnumerator: ...
    def enumerate_children_async(
        self,
        attributes: str,
        flags: FileQueryInfoFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def enumerate_children_finish(self, res: AsyncResult) -> FileEnumerator: ...
    def equal(self, file2: File) -> bool: ...
    def find_enclosing_mount(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> Mount: ...
    def find_enclosing_mount_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def find_enclosing_mount_finish(self, res: AsyncResult) -> Mount: ...
    def get_basename(self) -> typing.Optional[str]: ...
    def get_child(self, name: str) -> File: ...
    def get_child_for_display_name(self, display_name: str) -> File: ...
    def get_parent(self) -> typing.Optional[File]: ...
    def get_parse_name(self) -> str: ...
    def get_path(self) -> typing.Optional[str]: ...
    def get_relative_path(self, descendant: File) -> typing.Optional[str]: ...
    def get_uri(self) -> str: ...
    def get_uri_scheme(self) -> typing.Optional[str]: ...
    def has_parent(self, parent: typing.Optional[File] = None) -> bool: ...
    def has_prefix(self, prefix: File) -> bool: ...
    def has_uri_scheme(self, uri_scheme: str) -> bool: ...
    def hash(self) -> int: ...
    def is_native(self) -> bool: ...
    def load_bytes(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[GLib.Bytes, str]: ...
    def load_bytes_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def load_bytes_finish(
        self, result: AsyncResult
    ) -> typing.Tuple[GLib.Bytes, str]: ...
    def load_contents(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[bool, bytes, str]: ...
    def load_contents_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def load_contents_finish(
        self, res: AsyncResult
    ) -> typing.Tuple[bool, bytes, str]: ...
    def load_partial_contents_finish(
        self, res: AsyncResult
    ) -> typing.Tuple[bool, bytes, str]: ...
    def make_directory(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def make_directory_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def make_directory_finish(self, result: AsyncResult) -> bool: ...
    def make_directory_with_parents(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def make_symbolic_link(
        self, symlink_value: str, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def make_symbolic_link_async(
        self,
        symlink_value: str,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def make_symbolic_link_finish(self, result: AsyncResult) -> bool: ...
    def measure_disk_usage(
        self,
        flags: FileMeasureFlags,
        cancellable: typing.Optional[Cancellable] = None,
        progress_callback: typing.Optional[typing.Callable[..., None]] = None,
        *progress_data: typing.Any,
    ) -> typing.Tuple[bool, int, int, int]: ...
    def measure_disk_usage_finish(
        self, result: AsyncResult
    ) -> typing.Tuple[bool, int, int, int]: ...
    def monitor(
        self, flags: FileMonitorFlags, cancellable: typing.Optional[Cancellable] = None
    ) -> FileMonitor: ...
    def monitor_directory(
        self, flags: FileMonitorFlags, cancellable: typing.Optional[Cancellable] = None
    ) -> FileMonitor: ...
    def monitor_file(
        self, flags: FileMonitorFlags, cancellable: typing.Optional[Cancellable] = None
    ) -> FileMonitor: ...
    def mount_enclosing_volume(
        self,
        flags: MountMountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def mount_enclosing_volume_finish(self, result: AsyncResult) -> bool: ...
    def mount_mountable(
        self,
        flags: MountMountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def mount_mountable_finish(self, result: AsyncResult) -> File: ...
    def move(
        self,
        destination: File,
        flags: FileCopyFlags,
        cancellable: typing.Optional[Cancellable] = None,
        progress_callback: typing.Optional[typing.Callable[..., None]] = None,
        *progress_callback_data: typing.Any,
    ) -> bool: ...
    def move_async(
        self,
        destination: File,
        flags: FileCopyFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable],
        progress_callback_closure: typing.Optional[typing.Callable[..., typing.Any]],
        ready_callback_closure: typing.Callable[..., typing.Any],
    ) -> None: ...
    def move_finish(self, result: AsyncResult) -> bool: ...
    @staticmethod
    def new_build_filenamev(args: typing.Sequence[str]) -> File: ...
    @staticmethod
    def new_for_commandline_arg(arg: str) -> File: ...
    @staticmethod
    def new_for_commandline_arg_and_cwd(arg: str, cwd: str) -> File: ...
    @staticmethod
    def new_for_path(path: str) -> File: ...
    @staticmethod
    def new_for_uri(uri: str) -> File: ...
    @staticmethod
    def new_tmp(
        tmpl: typing.Optional[str] = None,
    ) -> typing.Tuple[File, FileIOStream]: ...
    @staticmethod
    def new_tmp_async(
        tmpl: typing.Optional[str],
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @staticmethod
    def new_tmp_dir_async(
        tmpl: typing.Optional[str],
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @staticmethod
    def new_tmp_dir_finish(result: AsyncResult) -> File: ...
    @staticmethod
    def new_tmp_finish(result: AsyncResult) -> typing.Tuple[File, FileIOStream]: ...
    def open_readwrite(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> FileIOStream: ...
    def open_readwrite_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def open_readwrite_finish(self, res: AsyncResult) -> FileIOStream: ...
    @staticmethod
    def parse_name(parse_name: str) -> File: ...
    def peek_path(self) -> typing.Optional[str]: ...
    def poll_mountable(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def poll_mountable_finish(self, result: AsyncResult) -> bool: ...
    def query_default_handler(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> AppInfo: ...
    def query_default_handler_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def query_default_handler_finish(self, result: AsyncResult) -> AppInfo: ...
    def query_exists(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def query_file_type(
        self,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> FileType: ...
    def query_filesystem_info(
        self, attributes: str, cancellable: typing.Optional[Cancellable] = None
    ) -> FileInfo: ...
    def query_filesystem_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def query_filesystem_info_finish(self, res: AsyncResult) -> FileInfo: ...
    def query_info(
        self,
        attributes: str,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> FileInfo: ...
    def query_info_async(
        self,
        attributes: str,
        flags: FileQueryInfoFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def query_info_finish(self, res: AsyncResult) -> FileInfo: ...
    def query_settable_attributes(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> FileAttributeInfoList: ...
    def query_writable_namespaces(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> FileAttributeInfoList: ...
    def read(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> FileInputStream: ...
    def read_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def read_finish(self, res: AsyncResult) -> FileInputStream: ...
    def replace(
        self,
        etag: typing.Optional[str],
        make_backup: bool,
        flags: FileCreateFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> FileOutputStream: ...
    def replace_async(
        self,
        etag: typing.Optional[str],
        make_backup: bool,
        flags: FileCreateFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def replace_contents(
        self,
        contents: typing.Sequence[int],
        etag: typing.Optional[str],
        make_backup: bool,
        flags: FileCreateFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[bool, str]: ...
    def replace_contents_async(
        self,
        contents: typing.Sequence[int],
        etag: typing.Optional[str],
        make_backup: bool,
        flags: FileCreateFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def replace_contents_bytes_async(
        self,
        contents: GLib.Bytes,
        etag: typing.Optional[str],
        make_backup: bool,
        flags: FileCreateFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def replace_contents_finish(self, res: AsyncResult) -> typing.Tuple[bool, str]: ...
    def replace_finish(self, res: AsyncResult) -> FileOutputStream: ...
    def replace_readwrite(
        self,
        etag: typing.Optional[str],
        make_backup: bool,
        flags: FileCreateFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> FileIOStream: ...
    def replace_readwrite_async(
        self,
        etag: typing.Optional[str],
        make_backup: bool,
        flags: FileCreateFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def replace_readwrite_finish(self, res: AsyncResult) -> FileIOStream: ...
    def resolve_relative_path(self, relative_path: str) -> File: ...
    def set_attribute(
        self,
        attribute: str,
        type: FileAttributeType,
        value_p: None,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def set_attribute_byte_string(
        self,
        attribute: str,
        value: str,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def set_attribute_int32(
        self,
        attribute: str,
        value: int,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def set_attribute_int64(
        self,
        attribute: str,
        value: int,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def set_attribute_string(
        self,
        attribute: str,
        value: str,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def set_attribute_uint32(
        self,
        attribute: str,
        value: int,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def set_attribute_uint64(
        self,
        attribute: str,
        value: int,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def set_attributes_async(
        self,
        info: FileInfo,
        flags: FileQueryInfoFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def set_attributes_finish(
        self, result: AsyncResult
    ) -> typing.Tuple[bool, FileInfo]: ...
    def set_attributes_from_info(
        self,
        info: FileInfo,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def set_display_name(
        self, display_name: str, cancellable: typing.Optional[Cancellable] = None
    ) -> File: ...
    def set_display_name_async(
        self,
        display_name: str,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def set_display_name_finish(self, res: AsyncResult) -> File: ...
    def start_mountable(
        self,
        flags: DriveStartFlags,
        start_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def start_mountable_finish(self, result: AsyncResult) -> bool: ...
    def stop_mountable(
        self,
        flags: MountUnmountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def stop_mountable_finish(self, result: AsyncResult) -> bool: ...
    def supports_thread_contexts(self) -> bool: ...
    def trash(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def trash_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def trash_finish(self, result: AsyncResult) -> bool: ...
    def unmount_mountable(
        self,
        flags: MountUnmountFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def unmount_mountable_finish(self, result: AsyncResult) -> bool: ...
    def unmount_mountable_with_operation(
        self,
        flags: MountUnmountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def unmount_mountable_with_operation_finish(self, result: AsyncResult) -> bool: ...

class FileAttributeInfo(GObject.GPointer):
    """
    :Constructors:

    ::

        FileAttributeInfo()
    """

    name: str = ...
    type: FileAttributeType = ...
    flags: FileAttributeInfoFlags = ...

class FileAttributeInfoList(GObject.GBoxed):
    """
    :Constructors:

    ::

        FileAttributeInfoList()
        new() -> Gio.FileAttributeInfoList
    """

    infos: FileAttributeInfo = ...
    n_infos: int = ...
    def add(
        self, name: str, type: FileAttributeType, flags: FileAttributeInfoFlags
    ) -> None: ...
    def dup(self) -> FileAttributeInfoList: ...
    def lookup(self, name: str) -> FileAttributeInfo: ...
    @classmethod
    def new(cls) -> FileAttributeInfoList: ...
    def ref(self) -> FileAttributeInfoList: ...
    def unref(self) -> None: ...

class FileAttributeMatcher(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(attributes:str) -> Gio.FileAttributeMatcher
    """

    def enumerate_namespace(self, ns: str) -> bool: ...
    def enumerate_next(self) -> typing.Optional[str]: ...
    def matches(self, attribute: str) -> bool: ...
    def matches_only(self, attribute: str) -> bool: ...
    @classmethod
    def new(cls, attributes: str) -> FileAttributeMatcher: ...
    def ref(self) -> FileAttributeMatcher: ...
    def subtract(
        self, subtract: typing.Optional[FileAttributeMatcher] = None
    ) -> typing.Optional[FileAttributeMatcher]: ...
    def to_string(self) -> str: ...
    def unref(self) -> None: ...

class FileDescriptorBased(GObject.GInterface):
    """
    Interface GFileDescriptorBased

    Signals from GObject:
      notify (GParam)
    """

    def get_fd(self) -> int: ...

class FileDescriptorBasedIface(GObject.GPointer):
    """
    :Constructors:

    ::

        FileDescriptorBasedIface()
    """

    g_iface: GObject.TypeInterface = ...
    get_fd: typing.Callable[[FileDescriptorBased], int] = ...

class FileEnumerator(GObject.Object):
    """
    :Constructors:

    ::

        FileEnumerator(**properties)

    Object GFileEnumerator

    Properties from GFileEnumerator:
      container -> GFile: container

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        container: File

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: FileEnumeratorPrivate = ...
    def __init__(self, container: File = ...) -> None: ...
    def close(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def close_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_fn(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def do_next_file(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Optional[FileInfo]: ...
    def do_next_files_async(
        self,
        num_files: int,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_next_files_finish(self, result: AsyncResult) -> list[FileInfo]: ...
    def get_child(self, info: FileInfo) -> File: ...
    def get_container(self) -> File: ...
    def has_pending(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def iterate(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[bool, FileInfo, File]: ...
    def next_file(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Optional[FileInfo]: ...
    def next_files_async(
        self,
        num_files: int,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def next_files_finish(self, result: AsyncResult) -> list[FileInfo]: ...
    def set_pending(self, pending: bool) -> None: ...

class FileEnumeratorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileEnumeratorClass()
    """

    parent_class: GObject.ObjectClass = ...
    next_file: typing.Callable[
        [FileEnumerator, typing.Optional[Cancellable]], typing.Optional[FileInfo]
    ] = ...
    close_fn: typing.Callable[[FileEnumerator, typing.Optional[Cancellable]], bool] = (
        ...
    )
    next_files_async: typing.Callable[..., None] = ...
    next_files_finish: typing.Callable[
        [FileEnumerator, AsyncResult], list[FileInfo]
    ] = ...
    close_async: typing.Callable[..., None] = ...
    close_finish: typing.Callable[[FileEnumerator, AsyncResult], bool] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...
    _g_reserved6: None = ...
    _g_reserved7: None = ...

class FileEnumeratorPrivate(GObject.GPointer): ...

class FileIOStream(IOStream, Seekable):
    """
    :Constructors:

    ::

        FileIOStream(**properties)

    Object GFileIOStream

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        closed: bool
        input_stream: InputStream
        output_stream: OutputStream

    props: Props = ...
    parent_instance: IOStream = ...
    priv: FileIOStreamPrivate = ...
    def do_can_seek(self) -> bool: ...
    def do_can_truncate(self) -> bool: ...
    def do_get_etag(self) -> typing.Optional[str]: ...
    def do_query_info(
        self, attributes: str, cancellable: typing.Optional[Cancellable] = None
    ) -> FileInfo: ...
    def do_query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_query_info_finish(self, result: AsyncResult) -> FileInfo: ...
    def do_seek(
        self,
        offset: int,
        type: GLib.SeekType,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def do_tell(self) -> int: ...
    def do_truncate_fn(
        self, size: int, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def get_etag(self) -> typing.Optional[str]: ...
    def query_info(
        self, attributes: str, cancellable: typing.Optional[Cancellable] = None
    ) -> FileInfo: ...
    def query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def query_info_finish(self, result: AsyncResult) -> FileInfo: ...

class FileIOStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileIOStreamClass()
    """

    parent_class: IOStreamClass = ...
    tell: typing.Callable[[FileIOStream], int] = ...
    can_seek: typing.Callable[[FileIOStream], bool] = ...
    seek: typing.Callable[
        [FileIOStream, int, GLib.SeekType, typing.Optional[Cancellable]], bool
    ] = ...
    can_truncate: typing.Callable[[FileIOStream], bool] = ...
    truncate_fn: typing.Callable[
        [FileIOStream, int, typing.Optional[Cancellable]], bool
    ] = ...
    query_info: typing.Callable[
        [FileIOStream, str, typing.Optional[Cancellable]], FileInfo
    ] = ...
    query_info_async: typing.Callable[..., None] = ...
    query_info_finish: typing.Callable[[FileIOStream, AsyncResult], FileInfo] = ...
    get_etag: typing.Callable[[FileIOStream], typing.Optional[str]] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class FileIOStreamPrivate(GObject.GPointer): ...

class FileIcon(GObject.Object, Icon, LoadableIcon):
    """
    :Constructors:

    ::

        FileIcon(**properties)
        new(file:Gio.File) -> Gio.FileIcon

    Object GFileIcon

    Properties from GFileIcon:
      file -> GFile: file

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        file: File

    props: Props = ...
    # override
    def __init__(self, *, file: File = ...) -> None: ...
    def get_file(self) -> File: ...
    @classmethod
    def new(cls, file: File) -> FileIcon: ...

class FileIconClass(GObject.GPointer): ...

class FileIface(GObject.GPointer):
    """
    :Constructors:

    ::

        FileIface()
    """

    g_iface: GObject.TypeInterface = ...
    dup: typing.Callable[[File], File] = ...
    hash: typing.Callable[[File], int] = ...
    equal: typing.Callable[[File, File], bool] = ...
    is_native: typing.Callable[[File], bool] = ...
    has_uri_scheme: typing.Callable[[File, str], bool] = ...
    get_uri_scheme: typing.Callable[[File], typing.Optional[str]] = ...
    get_basename: typing.Callable[[File], typing.Optional[str]] = ...
    get_path: typing.Callable[[File], typing.Optional[str]] = ...
    get_uri: typing.Callable[[File], str] = ...
    get_parse_name: typing.Callable[[File], str] = ...
    get_parent: typing.Callable[[File], typing.Optional[File]] = ...
    prefix_matches: typing.Callable[[File, File], bool] = ...
    get_relative_path: typing.Callable[[File, File], typing.Optional[str]] = ...
    resolve_relative_path: typing.Callable[[File, str], File] = ...
    get_child_for_display_name: typing.Callable[[File, str], File] = ...
    enumerate_children: typing.Callable[
        [File, str, FileQueryInfoFlags, typing.Optional[Cancellable]], FileEnumerator
    ] = ...
    enumerate_children_async: typing.Callable[..., None] = ...
    enumerate_children_finish: typing.Callable[[File, AsyncResult], FileEnumerator] = (
        ...
    )
    query_info: typing.Callable[
        [File, str, FileQueryInfoFlags, typing.Optional[Cancellable]], FileInfo
    ] = ...
    query_info_async: typing.Callable[..., None] = ...
    query_info_finish: typing.Callable[[File, AsyncResult], FileInfo] = ...
    query_filesystem_info: typing.Callable[
        [File, str, typing.Optional[Cancellable]], FileInfo
    ] = ...
    query_filesystem_info_async: typing.Callable[..., None] = ...
    query_filesystem_info_finish: typing.Callable[[File, AsyncResult], FileInfo] = ...
    find_enclosing_mount: typing.Callable[
        [File, typing.Optional[Cancellable]], Mount
    ] = ...
    find_enclosing_mount_async: typing.Callable[..., None] = ...
    find_enclosing_mount_finish: typing.Callable[[File, AsyncResult], Mount] = ...
    set_display_name: typing.Callable[
        [File, str, typing.Optional[Cancellable]], File
    ] = ...
    set_display_name_async: typing.Callable[..., None] = ...
    set_display_name_finish: typing.Callable[[File, AsyncResult], File] = ...
    query_settable_attributes: typing.Callable[
        [File, typing.Optional[Cancellable]], FileAttributeInfoList
    ] = ...
    _query_settable_attributes_async: None = ...
    _query_settable_attributes_finish: None = ...
    query_writable_namespaces: typing.Callable[
        [File, typing.Optional[Cancellable]], FileAttributeInfoList
    ] = ...
    _query_writable_namespaces_async: None = ...
    _query_writable_namespaces_finish: None = ...
    set_attribute: typing.Callable[
        [
            File,
            str,
            FileAttributeType,
            None,
            FileQueryInfoFlags,
            typing.Optional[Cancellable],
        ],
        bool,
    ] = ...
    set_attributes_from_info: typing.Callable[
        [File, FileInfo, FileQueryInfoFlags, typing.Optional[Cancellable]], bool
    ] = ...
    set_attributes_async: typing.Callable[..., None] = ...
    set_attributes_finish: typing.Callable[
        [File, AsyncResult], typing.Tuple[bool, FileInfo]
    ] = ...
    read_fn: typing.Callable[[File, typing.Optional[Cancellable]], FileInputStream] = (
        ...
    )
    read_async: typing.Callable[..., None] = ...
    read_finish: typing.Callable[[File, AsyncResult], FileInputStream] = ...
    append_to: typing.Callable[
        [File, FileCreateFlags, typing.Optional[Cancellable]], FileOutputStream
    ] = ...
    append_to_async: typing.Callable[..., None] = ...
    append_to_finish: typing.Callable[[File, AsyncResult], FileOutputStream] = ...
    create: typing.Callable[
        [File, FileCreateFlags, typing.Optional[Cancellable]], FileOutputStream
    ] = ...
    create_async: typing.Callable[..., None] = ...
    create_finish: typing.Callable[[File, AsyncResult], FileOutputStream] = ...
    replace: typing.Callable[
        [
            File,
            typing.Optional[str],
            bool,
            FileCreateFlags,
            typing.Optional[Cancellable],
        ],
        FileOutputStream,
    ] = ...
    replace_async: typing.Callable[..., None] = ...
    replace_finish: typing.Callable[[File, AsyncResult], FileOutputStream] = ...
    delete_file: typing.Callable[[File, typing.Optional[Cancellable]], bool] = ...
    delete_file_async: typing.Callable[..., None] = ...
    delete_file_finish: typing.Callable[[File, AsyncResult], bool] = ...
    trash: typing.Callable[[File, typing.Optional[Cancellable]], bool] = ...
    trash_async: typing.Callable[..., None] = ...
    trash_finish: typing.Callable[[File, AsyncResult], bool] = ...
    make_directory: typing.Callable[[File, typing.Optional[Cancellable]], bool] = ...
    make_directory_async: typing.Callable[..., None] = ...
    make_directory_finish: typing.Callable[[File, AsyncResult], bool] = ...
    make_symbolic_link: typing.Callable[
        [File, str, typing.Optional[Cancellable]], bool
    ] = ...
    make_symbolic_link_async: typing.Callable[..., None] = ...
    make_symbolic_link_finish: typing.Callable[[File, AsyncResult], bool] = ...
    copy: typing.Callable[..., bool] = ...
    copy_async: typing.Callable[..., None] = ...
    copy_finish: typing.Callable[[File, AsyncResult], bool] = ...
    move: typing.Callable[..., bool] = ...
    move_async: typing.Callable[..., None] = ...
    move_finish: typing.Callable[[File, AsyncResult], bool] = ...
    mount_mountable: typing.Callable[..., None] = ...
    mount_mountable_finish: typing.Callable[[File, AsyncResult], File] = ...
    unmount_mountable: typing.Callable[..., None] = ...
    unmount_mountable_finish: typing.Callable[[File, AsyncResult], bool] = ...
    eject_mountable: typing.Callable[..., None] = ...
    eject_mountable_finish: typing.Callable[[File, AsyncResult], bool] = ...
    mount_enclosing_volume: typing.Callable[..., None] = ...
    mount_enclosing_volume_finish: typing.Callable[[File, AsyncResult], bool] = ...
    monitor_dir: typing.Callable[
        [File, FileMonitorFlags, typing.Optional[Cancellable]], FileMonitor
    ] = ...
    monitor_file: typing.Callable[
        [File, FileMonitorFlags, typing.Optional[Cancellable]], FileMonitor
    ] = ...
    open_readwrite: typing.Callable[
        [File, typing.Optional[Cancellable]], FileIOStream
    ] = ...
    open_readwrite_async: typing.Callable[..., None] = ...
    open_readwrite_finish: typing.Callable[[File, AsyncResult], FileIOStream] = ...
    create_readwrite: typing.Callable[
        [File, FileCreateFlags, typing.Optional[Cancellable]], FileIOStream
    ] = ...
    create_readwrite_async: typing.Callable[..., None] = ...
    create_readwrite_finish: typing.Callable[[File, AsyncResult], FileIOStream] = ...
    replace_readwrite: typing.Callable[
        [
            File,
            typing.Optional[str],
            bool,
            FileCreateFlags,
            typing.Optional[Cancellable],
        ],
        FileIOStream,
    ] = ...
    replace_readwrite_async: typing.Callable[..., None] = ...
    replace_readwrite_finish: typing.Callable[[File, AsyncResult], FileIOStream] = ...
    start_mountable: typing.Callable[..., None] = ...
    start_mountable_finish: typing.Callable[[File, AsyncResult], bool] = ...
    stop_mountable: typing.Callable[..., None] = ...
    stop_mountable_finish: typing.Callable[[File, AsyncResult], bool] = ...
    supports_thread_contexts: bool = ...
    unmount_mountable_with_operation: typing.Callable[..., None] = ...
    unmount_mountable_with_operation_finish: typing.Callable[
        [File, AsyncResult], bool
    ] = ...
    eject_mountable_with_operation: typing.Callable[..., None] = ...
    eject_mountable_with_operation_finish: typing.Callable[
        [File, AsyncResult], bool
    ] = ...
    poll_mountable: typing.Callable[..., None] = ...
    poll_mountable_finish: typing.Callable[[File, AsyncResult], bool] = ...
    measure_disk_usage: typing.Callable[..., typing.Tuple[bool, int, int, int]] = ...
    measure_disk_usage_async: None = ...
    measure_disk_usage_finish: typing.Callable[
        [File, AsyncResult], typing.Tuple[bool, int, int, int]
    ] = ...

class FileInfo(GObject.Object):
    """
    :Constructors:

    ::

        FileInfo(**properties)
        new() -> Gio.FileInfo

    Object GFileInfo

    Signals from GObject:
      notify (GParam)
    """

    def clear_status(self) -> None: ...
    def copy_into(self, dest_info: FileInfo) -> None: ...
    def dup(self) -> FileInfo: ...
    def get_access_date_time(self) -> typing.Optional[GLib.DateTime]: ...
    def get_attribute_as_string(self, attribute: str) -> typing.Optional[str]: ...
    def get_attribute_boolean(self, attribute: str) -> bool: ...
    def get_attribute_byte_string(self, attribute: str) -> typing.Optional[str]: ...
    def get_attribute_data(
        self, attribute: str
    ) -> typing.Tuple[bool, FileAttributeType, None, FileAttributeStatus]: ...
    def get_attribute_file_path(self, attribute: str) -> typing.Optional[str]: ...
    def get_attribute_int32(self, attribute: str) -> int: ...
    def get_attribute_int64(self, attribute: str) -> int: ...
    def get_attribute_object(
        self, attribute: str
    ) -> typing.Optional[GObject.Object]: ...
    def get_attribute_status(self, attribute: str) -> FileAttributeStatus: ...
    def get_attribute_string(self, attribute: str) -> typing.Optional[str]: ...
    def get_attribute_stringv(self, attribute: str) -> typing.Optional[list[str]]: ...
    def get_attribute_type(self, attribute: str) -> FileAttributeType: ...
    def get_attribute_uint32(self, attribute: str) -> int: ...
    def get_attribute_uint64(self, attribute: str) -> int: ...
    def get_content_type(self) -> typing.Optional[str]: ...
    def get_creation_date_time(self) -> typing.Optional[GLib.DateTime]: ...
    def get_deletion_date(self) -> typing.Optional[GLib.DateTime]: ...
    def get_display_name(self) -> str: ...
    def get_edit_name(self) -> str: ...
    def get_etag(self) -> typing.Optional[str]: ...
    def get_file_type(self) -> FileType: ...
    def get_icon(self) -> typing.Optional[Icon]: ...
    def get_is_backup(self) -> bool: ...
    def get_is_hidden(self) -> bool: ...
    def get_is_symlink(self) -> bool: ...
    def get_modification_date_time(self) -> typing.Optional[GLib.DateTime]: ...
    def get_modification_time(self) -> GLib.TimeVal: ...
    def get_name(self) -> str: ...
    def get_size(self) -> int: ...
    def get_sort_order(self) -> int: ...
    def get_symbolic_icon(self) -> typing.Optional[Icon]: ...
    def get_symlink_target(self) -> typing.Optional[str]: ...
    def has_attribute(self, attribute: str) -> bool: ...
    def has_namespace(self, name_space: str) -> bool: ...
    def list_attributes(
        self, name_space: typing.Optional[str] = None
    ) -> typing.Optional[list[str]]: ...
    @classmethod
    def new(cls) -> FileInfo: ...
    def remove_attribute(self, attribute: str) -> None: ...
    def set_access_date_time(self, atime: GLib.DateTime) -> None: ...
    def set_attribute(
        self, attribute: str, type: FileAttributeType, value_p: None
    ) -> None: ...
    def set_attribute_boolean(self, attribute: str, attr_value: bool) -> None: ...
    def set_attribute_byte_string(self, attribute: str, attr_value: str) -> None: ...
    def set_attribute_file_path(self, attribute: str, attr_value: str) -> None: ...
    def set_attribute_int32(self, attribute: str, attr_value: int) -> None: ...
    def set_attribute_int64(self, attribute: str, attr_value: int) -> None: ...
    def set_attribute_mask(self, mask: FileAttributeMatcher) -> None: ...
    def set_attribute_object(
        self, attribute: str, attr_value: GObject.Object
    ) -> None: ...
    def set_attribute_status(
        self, attribute: str, status: FileAttributeStatus
    ) -> bool: ...
    def set_attribute_string(self, attribute: str, attr_value: str) -> None: ...
    def set_attribute_stringv(
        self, attribute: str, attr_value: typing.Sequence[str]
    ) -> None: ...
    def set_attribute_uint32(self, attribute: str, attr_value: int) -> None: ...
    def set_attribute_uint64(self, attribute: str, attr_value: int) -> None: ...
    def set_content_type(self, content_type: str) -> None: ...
    def set_creation_date_time(self, creation_time: GLib.DateTime) -> None: ...
    def set_display_name(self, display_name: str) -> None: ...
    def set_edit_name(self, edit_name: str) -> None: ...
    def set_file_type(self, type: FileType) -> None: ...
    def set_icon(self, icon: Icon) -> None: ...
    def set_is_hidden(self, is_hidden: bool) -> None: ...
    def set_is_symlink(self, is_symlink: bool) -> None: ...
    def set_modification_date_time(self, mtime: GLib.DateTime) -> None: ...
    def set_modification_time(self, mtime: GLib.TimeVal) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_sort_order(self, sort_order: int) -> None: ...
    def set_symbolic_icon(self, icon: Icon) -> None: ...
    def set_symlink_target(self, symlink_target: str) -> None: ...
    def unset_attribute_mask(self) -> None: ...

class FileInfoClass(GObject.GPointer): ...

class FileInputStream(InputStream, Seekable):
    """
    :Constructors:

    ::

        FileInputStream(**properties)

    Object GFileInputStream

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: InputStream = ...
    priv: FileInputStreamPrivate = ...
    def do_can_seek(self) -> bool: ...
    def do_query_info(
        self, attributes: str, cancellable: typing.Optional[Cancellable] = None
    ) -> FileInfo: ...
    def do_query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_query_info_finish(self, result: AsyncResult) -> FileInfo: ...
    def do_seek(
        self,
        offset: int,
        type: GLib.SeekType,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def do_tell(self) -> int: ...
    def query_info(
        self, attributes: str, cancellable: typing.Optional[Cancellable] = None
    ) -> FileInfo: ...
    def query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def query_info_finish(self, result: AsyncResult) -> FileInfo: ...

class FileInputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileInputStreamClass()
    """

    parent_class: InputStreamClass = ...
    tell: typing.Callable[[FileInputStream], int] = ...
    can_seek: typing.Callable[[FileInputStream], bool] = ...
    seek: typing.Callable[
        [FileInputStream, int, GLib.SeekType, typing.Optional[Cancellable]], bool
    ] = ...
    query_info: typing.Callable[
        [FileInputStream, str, typing.Optional[Cancellable]], FileInfo
    ] = ...
    query_info_async: typing.Callable[..., None] = ...
    query_info_finish: typing.Callable[[FileInputStream, AsyncResult], FileInfo] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class FileInputStreamPrivate(GObject.GPointer): ...

class FileMonitor(GObject.Object):
    """
    :Constructors:

    ::

        FileMonitor(**properties)

    Object GFileMonitor

    Signals from GFileMonitor:
      changed (GFile, GFile, GFileMonitorEvent)

    Properties from GFileMonitor:
      rate-limit -> gint: rate-limit
      cancelled -> gboolean: cancelled

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        cancelled: bool
        rate_limit: int

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: FileMonitorPrivate = ...
    def __init__(self, rate_limit: int = ...) -> None: ...
    def cancel(self) -> bool: ...
    def do_cancel(self) -> bool: ...
    def do_changed(
        self, file: File, other_file: File, event_type: FileMonitorEvent
    ) -> None: ...
    def emit_event(
        self, child: File, other_file: File, event_type: FileMonitorEvent
    ) -> None: ...
    def is_cancelled(self) -> bool: ...
    def set_rate_limit(self, limit_msecs: int) -> None: ...

class FileMonitorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileMonitorClass()
    """

    parent_class: GObject.ObjectClass = ...
    changed: typing.Callable[[FileMonitor, File, File, FileMonitorEvent], None] = ...
    cancel: typing.Callable[[FileMonitor], bool] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class FileMonitorPrivate(GObject.GPointer): ...

class FileOutputStream(OutputStream, Seekable):
    """
    :Constructors:

    ::

        FileOutputStream(**properties)

    Object GFileOutputStream

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: OutputStream = ...
    priv: FileOutputStreamPrivate = ...
    def do_can_seek(self) -> bool: ...
    def do_can_truncate(self) -> bool: ...
    def do_get_etag(self) -> typing.Optional[str]: ...
    def do_query_info(
        self, attributes: str, cancellable: typing.Optional[Cancellable] = None
    ) -> FileInfo: ...
    def do_query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_query_info_finish(self, result: AsyncResult) -> FileInfo: ...
    def do_seek(
        self,
        offset: int,
        type: GLib.SeekType,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def do_tell(self) -> int: ...
    def do_truncate_fn(
        self, size: int, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def get_etag(self) -> typing.Optional[str]: ...
    def query_info(
        self, attributes: str, cancellable: typing.Optional[Cancellable] = None
    ) -> FileInfo: ...
    def query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def query_info_finish(self, result: AsyncResult) -> FileInfo: ...

class FileOutputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileOutputStreamClass()
    """

    parent_class: OutputStreamClass = ...
    tell: typing.Callable[[FileOutputStream], int] = ...
    can_seek: typing.Callable[[FileOutputStream], bool] = ...
    seek: typing.Callable[
        [FileOutputStream, int, GLib.SeekType, typing.Optional[Cancellable]], bool
    ] = ...
    can_truncate: typing.Callable[[FileOutputStream], bool] = ...
    truncate_fn: typing.Callable[
        [FileOutputStream, int, typing.Optional[Cancellable]], bool
    ] = ...
    query_info: typing.Callable[
        [FileOutputStream, str, typing.Optional[Cancellable]], FileInfo
    ] = ...
    query_info_async: typing.Callable[..., None] = ...
    query_info_finish: typing.Callable[[FileOutputStream, AsyncResult], FileInfo] = ...
    get_etag: typing.Callable[[FileOutputStream], typing.Optional[str]] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class FileOutputStreamPrivate(GObject.GPointer): ...

class FilenameCompleter(GObject.Object):
    """
    :Constructors:

    ::

        FilenameCompleter(**properties)
        new() -> Gio.FilenameCompleter

    Object GFilenameCompleter

    Signals from GFilenameCompleter:
      got-completion-data ()

    Signals from GObject:
      notify (GParam)
    """

    def do_got_completion_data(self) -> None: ...
    def get_completion_suffix(self, initial_text: str) -> typing.Optional[str]: ...
    def get_completions(self, initial_text: str) -> list[str]: ...
    @classmethod
    def new(cls) -> FilenameCompleter: ...
    def set_dirs_only(self, dirs_only: bool) -> None: ...

class FilenameCompleterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FilenameCompleterClass()
    """

    parent_class: GObject.ObjectClass = ...
    got_completion_data: typing.Callable[[FilenameCompleter], None] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...

class FilterInputStream(InputStream):
    """
    :Constructors:

    ::

        FilterInputStream(**properties)

    Object GFilterInputStream

    Properties from GFilterInputStream:
      base-stream -> GInputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        base_stream: InputStream
        close_base_stream: bool

    props: Props = ...
    parent_instance: InputStream = ...
    base_stream: InputStream = ...
    def __init__(
        self, base_stream: InputStream = ..., close_base_stream: bool = ...
    ) -> None: ...
    def get_base_stream(self) -> InputStream: ...
    def get_close_base_stream(self) -> bool: ...
    def set_close_base_stream(self, close_base: bool) -> None: ...

class FilterInputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FilterInputStreamClass()
    """

    parent_class: InputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...

class FilterOutputStream(OutputStream):
    """
    :Constructors:

    ::

        FilterOutputStream(**properties)

    Object GFilterOutputStream

    Properties from GFilterOutputStream:
      base-stream -> GOutputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        base_stream: OutputStream
        close_base_stream: bool

    props: Props = ...
    parent_instance: OutputStream = ...
    base_stream: OutputStream = ...
    def __init__(
        self, base_stream: OutputStream = ..., close_base_stream: bool = ...
    ) -> None: ...
    def get_base_stream(self) -> OutputStream: ...
    def get_close_base_stream(self) -> bool: ...
    def set_close_base_stream(self, close_base: bool) -> None: ...

class FilterOutputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FilterOutputStreamClass()
    """

    parent_class: OutputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...

class IOExtension(GObject.GPointer):
    def get_name(self) -> str: ...
    def get_priority(self) -> int: ...
    def get_type(self) -> typing.Type[typing.Any]: ...

class IOExtensionPoint(GObject.GPointer):
    def get_extension_by_name(self, name: str) -> IOExtension: ...
    def get_extensions(self) -> list[IOExtension]: ...
    def get_required_type(self) -> typing.Type[typing.Any]: ...
    @staticmethod
    def implement(
        extension_point_name: str,
        type: typing.Type[typing.Any],
        extension_name: str,
        priority: int,
    ) -> IOExtension: ...
    @staticmethod
    def lookup(name: str) -> IOExtensionPoint: ...
    @staticmethod
    def register(name: str) -> IOExtensionPoint: ...
    def set_required_type(self, type: typing.Type[typing.Any]) -> None: ...

class IOModule(GObject.TypeModule, GObject.TypePlugin):
    """
    :Constructors:

    ::

        IOModule(**properties)
        new(filename:str) -> Gio.IOModule

    Object GIOModule

    Signals from GObject:
      notify (GParam)
    """

    @classmethod
    def new(cls, filename: str) -> IOModule: ...
    @staticmethod
    def query() -> list[str]: ...

class IOModuleClass(GObject.GPointer): ...

class IOModuleScope(GObject.GPointer):
    def block(self, basename: str) -> None: ...
    def free(self) -> None: ...

class IOSchedulerJob(GObject.GPointer):
    def send_to_mainloop(
        self, func: typing.Callable[..., bool], *user_data: typing.Any
    ) -> bool: ...
    def send_to_mainloop_async(
        self, func: typing.Callable[..., bool], *user_data: typing.Any
    ) -> None: ...

class IOStream(GObject.Object):
    """
    :Constructors:

    ::

        IOStream(**properties)

    Object GIOStream

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        closed: bool
        input_stream: InputStream
        output_stream: OutputStream

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: IOStreamPrivate = ...
    def clear_pending(self) -> None: ...
    def close(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def close_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_fn(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def do_get_input_stream(self) -> InputStream: ...
    def do_get_output_stream(self) -> OutputStream: ...
    def get_input_stream(self) -> InputStream: ...
    def get_output_stream(self) -> OutputStream: ...
    def has_pending(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def set_pending(self) -> bool: ...
    def splice_async(
        self,
        stream2: IOStream,
        flags: IOStreamSpliceFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @staticmethod
    def splice_finish(result: AsyncResult) -> bool: ...

class IOStreamAdapter(GObject.GPointer): ...

class IOStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        IOStreamClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_input_stream: typing.Callable[[IOStream], InputStream] = ...
    get_output_stream: typing.Callable[[IOStream], OutputStream] = ...
    close_fn: typing.Callable[[IOStream, typing.Optional[Cancellable]], bool] = ...
    close_async: typing.Callable[..., None] = ...
    close_finish: typing.Callable[[IOStream, AsyncResult], bool] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...
    _g_reserved6: None = ...
    _g_reserved7: None = ...
    _g_reserved8: None = ...
    _g_reserved9: None = ...
    _g_reserved10: None = ...

class IOStreamPrivate(GObject.GPointer): ...

class Icon(GObject.GInterface):
    """
    Interface GIcon

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def deserialize(value: GLib.Variant) -> typing.Optional[Icon]: ...
    def equal(self, icon2: typing.Optional[Icon] = None) -> bool: ...
    def hash(self) -> int: ...
    @staticmethod
    def new_for_string(str: str) -> Icon: ...
    def serialize(self) -> typing.Optional[GLib.Variant]: ...
    def to_string(self) -> typing.Optional[str]: ...

class IconIface(GObject.GPointer):
    """
    :Constructors:

    ::

        IconIface()
    """

    g_iface: GObject.TypeInterface = ...
    hash: typing.Callable[[Icon], int] = ...
    equal: typing.Callable[[typing.Optional[Icon], typing.Optional[Icon]], bool] = ...
    to_tokens: typing.Callable[[Icon], typing.Tuple[bool, list[str], int]] = ...
    from_tokens: None = ...
    serialize: typing.Callable[[Icon], typing.Optional[GLib.Variant]] = ...

class InetAddress(GObject.Object):
    """
    :Constructors:

    ::

        InetAddress(**properties)
        new_any(family:Gio.SocketFamily) -> Gio.InetAddress
        new_from_bytes(bytes:list, family:Gio.SocketFamily) -> Gio.InetAddress
        new_from_string(string:str) -> Gio.InetAddress or None
        new_loopback(family:Gio.SocketFamily) -> Gio.InetAddress

    Object GInetAddress

    Properties from GInetAddress:
      family -> GSocketFamily: family
      bytes -> gpointer: bytes
      is-any -> gboolean: is-any
      is-loopback -> gboolean: is-loopback
      is-link-local -> gboolean: is-link-local
      is-site-local -> gboolean: is-site-local
      is-multicast -> gboolean: is-multicast
      is-mc-global -> gboolean: is-mc-global
      is-mc-link-local -> gboolean: is-mc-link-local
      is-mc-node-local -> gboolean: is-mc-node-local
      is-mc-org-local -> gboolean: is-mc-org-local
      is-mc-site-local -> gboolean: is-mc-site-local

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        bytes: None
        family: SocketFamily
        is_any: bool
        is_link_local: bool
        is_loopback: bool
        is_mc_global: bool
        is_mc_link_local: bool
        is_mc_node_local: bool
        is_mc_org_local: bool
        is_mc_site_local: bool
        is_multicast: bool
        is_site_local: bool

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: InetAddressPrivate = ...
    def __init__(self, bytes: None = ..., family: SocketFamily = ...) -> None: ...
    def do_to_string(self) -> str: ...
    def equal(self, other_address: InetAddress) -> bool: ...
    def get_family(self) -> SocketFamily: ...
    def get_is_any(self) -> bool: ...
    def get_is_link_local(self) -> bool: ...
    def get_is_loopback(self) -> bool: ...
    def get_is_mc_global(self) -> bool: ...
    def get_is_mc_link_local(self) -> bool: ...
    def get_is_mc_node_local(self) -> bool: ...
    def get_is_mc_org_local(self) -> bool: ...
    def get_is_mc_site_local(self) -> bool: ...
    def get_is_multicast(self) -> bool: ...
    def get_is_site_local(self) -> bool: ...
    def get_native_size(self) -> int: ...
    @classmethod
    def new_any(cls, family: SocketFamily) -> InetAddress: ...
    @classmethod
    def new_from_bytes(
        cls, bytes: typing.Sequence[int], family: SocketFamily
    ) -> InetAddress: ...
    @classmethod
    def new_from_string(cls, string: str) -> typing.Optional[InetAddress]: ...
    @classmethod
    def new_loopback(cls, family: SocketFamily) -> InetAddress: ...
    def to_string(self) -> str: ...

class InetAddressClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InetAddressClass()
    """

    parent_class: GObject.ObjectClass = ...
    to_string: typing.Callable[[InetAddress], str] = ...
    to_bytes: typing.Callable[[InetAddress], int] = ...

class InetAddressMask(GObject.Object, Initable):
    """
    :Constructors:

    ::

        InetAddressMask(**properties)
        new(addr:Gio.InetAddress, length:int) -> Gio.InetAddressMask
        new_from_string(mask_string:str) -> Gio.InetAddressMask

    Object GInetAddressMask

    Properties from GInetAddressMask:
      family -> GSocketFamily: family
      address -> GInetAddress: address
      length -> guint: length

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        address: InetAddress
        family: SocketFamily
        length: int

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: InetAddressMaskPrivate = ...
    def __init__(self, address: InetAddress = ..., length: int = ...) -> None: ...
    def equal(self, mask2: InetAddressMask) -> bool: ...
    def get_address(self) -> InetAddress: ...
    def get_family(self) -> SocketFamily: ...
    def get_length(self) -> int: ...
    def matches(self, address: InetAddress) -> bool: ...
    @classmethod
    def new(cls, addr: InetAddress, length: int) -> InetAddressMask: ...
    @classmethod
    def new_from_string(cls, mask_string: str) -> InetAddressMask: ...
    def to_string(self) -> str: ...

class InetAddressMaskClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InetAddressMaskClass()
    """

    parent_class: GObject.ObjectClass = ...

class InetAddressMaskPrivate(GObject.GPointer): ...
class InetAddressPrivate(GObject.GPointer): ...

class InetSocketAddress(SocketAddress, SocketConnectable):
    """
    :Constructors:

    ::

        InetSocketAddress(**properties)
        new(address:Gio.InetAddress, port:int) -> Gio.SocketAddress
        new_from_string(address:str, port:int) -> Gio.SocketAddress or None

    Object GInetSocketAddress

    Properties from GInetSocketAddress:
      address -> GInetAddress: address
      port -> guint: port
      flowinfo -> guint: flowinfo
      scope-id -> guint: scope-id

    Properties from GSocketAddress:
      family -> GSocketFamily: family

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        address: InetAddress
        flowinfo: int
        port: int
        scope_id: int
        family: SocketFamily

    props: Props = ...
    parent_instance: SocketAddress = ...
    priv: InetSocketAddressPrivate = ...
    def __init__(
        self,
        address: InetAddress = ...,
        flowinfo: int = ...,
        port: int = ...,
        scope_id: int = ...,
    ) -> None: ...
    def get_address(self) -> InetAddress: ...
    def get_flowinfo(self) -> int: ...
    def get_port(self) -> int: ...
    def get_scope_id(self) -> int: ...
    @classmethod
    def new(cls, address: InetAddress, port: int) -> InetSocketAddress: ...
    @classmethod
    def new_from_string(cls, address: str, port: int) -> InetSocketAddress: ...

class InetSocketAddressClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InetSocketAddressClass()
    """

    parent_class: SocketAddressClass = ...

class InetSocketAddressPrivate(GObject.GPointer): ...

class Initable(GObject.GInterface):
    """
    Interface GInitable

    Signals from GObject:
      notify (GParam)
    """

    def init(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    @staticmethod
    def newv(
        object_type: typing.Type[typing.Any],
        parameters: typing.Sequence[GObject.Parameter],
        cancellable: typing.Optional[Cancellable] = None,
    ) -> GObject.Object: ...

class InitableIface(GObject.GPointer):
    """
    :Constructors:

    ::

        InitableIface()
    """

    g_iface: GObject.TypeInterface = ...
    init: typing.Callable[[Initable, typing.Optional[Cancellable]], bool] = ...

class InputMessage(GObject.GPointer):
    """
    :Constructors:

    ::

        InputMessage()
    """

    address: SocketAddress = ...
    vectors: list[InputVector] = ...
    num_vectors: int = ...
    bytes_received: int = ...
    flags: int = ...
    control_messages: list[SocketControlMessage] = ...
    num_control_messages: int = ...

class InputStream(GObject.Object):
    """
    :Constructors:

    ::

        InputStream(**properties)

    Object GInputStream

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: InputStreamPrivate = ...
    def clear_pending(self) -> None: ...
    def close(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def close_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_fn(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def do_read_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> bytes: ...
    def do_read_finish(self, result: AsyncResult) -> int: ...
    def do_read_fn(
        self, buffer: None, count: int, cancellable: typing.Optional[Cancellable] = None
    ) -> int: ...
    def do_skip(
        self, count: int, cancellable: typing.Optional[Cancellable] = None
    ) -> int: ...
    def do_skip_async(
        self,
        count: int,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_skip_finish(self, result: AsyncResult) -> int: ...
    def has_pending(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def read(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[int, bytes]: ...
    def read_all(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[bool, bytes, int]: ...
    def read_all_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> bytes: ...
    def read_all_finish(self, result: AsyncResult) -> typing.Tuple[bool, int]: ...
    def read_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> bytes: ...
    def read_bytes(
        self, count: int, cancellable: typing.Optional[Cancellable] = None
    ) -> GLib.Bytes: ...
    def read_bytes_async(
        self,
        count: int,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def read_bytes_finish(self, result: AsyncResult) -> GLib.Bytes: ...
    def read_finish(self, result: AsyncResult) -> int: ...
    def set_pending(self) -> bool: ...
    def skip(
        self, count: int, cancellable: typing.Optional[Cancellable] = None
    ) -> int: ...
    def skip_async(
        self,
        count: int,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def skip_finish(self, result: AsyncResult) -> int: ...

class InputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InputStreamClass()
    """

    parent_class: GObject.ObjectClass = ...
    read_fn: typing.Callable[
        [InputStream, None, int, typing.Optional[Cancellable]], int
    ] = ...
    skip: typing.Callable[[InputStream, int, typing.Optional[Cancellable]], int] = ...
    close_fn: typing.Callable[[InputStream, typing.Optional[Cancellable]], bool] = ...
    read_async: typing.Callable[..., bytes] = ...
    read_finish: typing.Callable[[InputStream, AsyncResult], int] = ...
    skip_async: typing.Callable[..., None] = ...
    skip_finish: typing.Callable[[InputStream, AsyncResult], int] = ...
    close_async: typing.Callable[..., None] = ...
    close_finish: typing.Callable[[InputStream, AsyncResult], bool] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class InputStreamPrivate(GObject.GPointer): ...

class InputVector(GObject.GPointer):
    """
    :Constructors:

    ::

        InputVector()
    """

    buffer: None = ...
    size: int = ...

# override
class ListModel(GObject.GInterface):
    def __contains__(self, item: object) -> bool: ...
    def __getitem__(self, position: int) -> GObject.Object: ...
    def __iter__(self) -> typing.Iterator[GObject.Object]: ...
    def __len__(self) -> int: ...
    def get_item(self, position: int) -> typing.Optional[GObject.Object]: ...
    def get_item_type(self) -> typing.Type[typing.Any]: ...
    def get_n_items(self) -> int: ...
    def items_changed(self, position: int, removed: int, added: int) -> None: ...

class ListModelInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        ListModelInterface()
    """

    g_iface: GObject.TypeInterface = ...
    get_item_type: typing.Callable[[ListModel], typing.Type[typing.Any]] = ...
    get_n_items: typing.Callable[[ListModel], int] = ...
    get_item: typing.Callable[[ListModel, int], typing.Optional[GObject.Object]] = ...

class ListStore(GObject.Object, ListModel):
    """
    :Constructors:

    ::

        ListStore(**properties)
        new(item_type:GType) -> Gio.ListStore

    Object GListStore

    Properties from GListStore:
      item-type -> GType: item-type
      n-items -> guint: n-items

    Signals from GListModel:
      items-changed (guint, guint, guint)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        item_type: typing.Type[typing.Any]
        n_items: int

    props: Props = ...
    def __init__(self, item_type: typing.Type[typing.Any] = ...) -> None: ...
    def append(self, item: GObject.Object) -> None: ...
    def find(self, item: GObject.Object) -> typing.Tuple[bool, int]: ...
    def find_with_equal_func(self, item, equal_func, *user_data): ...  # FIXME Function
    def find_with_equal_func_full(
        self,
        item: typing.Optional[GObject.Object],
        equal_func: typing.Callable[..., bool],
        *user_data: typing.Any,
    ) -> typing.Tuple[bool, int]: ...
    def insert(self, position: int, item: GObject.Object) -> None: ...
    def insert_sorted(self, item, compare_func, *user_data): ...  # FIXME Function
    @classmethod
    def new(cls, item_type: typing.Type[typing.Any]) -> ListStore: ...
    def remove(self, position: int) -> None: ...
    def remove_all(self) -> None: ...
    def sort(self, compare_func, *user_data): ...  # FIXME Function
    def splice(
        self, position: int, n_removals: int, additions: typing.Sequence[GObject.Object]
    ) -> None: ...

class ListStoreClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ListStoreClass()
    """

    parent_class: GObject.ObjectClass = ...

class LoadableIcon(GObject.GInterface):
    """
    Interface GLoadableIcon

    Signals from GObject:
      notify (GParam)
    """

    def load(
        self, size: int, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[InputStream, str]: ...
    def load_async(
        self,
        size: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def load_finish(self, res: AsyncResult) -> typing.Tuple[InputStream, str]: ...

class LoadableIconIface(GObject.GPointer):
    """
    :Constructors:

    ::

        LoadableIconIface()
    """

    g_iface: GObject.TypeInterface = ...
    load: typing.Callable[
        [LoadableIcon, int, typing.Optional[Cancellable]],
        typing.Tuple[InputStream, str],
    ] = ...
    load_async: typing.Callable[..., None] = ...
    load_finish: typing.Callable[
        [LoadableIcon, AsyncResult], typing.Tuple[InputStream, str]
    ] = ...

class MemoryInputStream(InputStream, PollableInputStream, Seekable):
    """
    :Constructors:

    ::

        MemoryInputStream(**properties)
        new() -> Gio.InputStream
        new_from_bytes(bytes:GLib.Bytes) -> Gio.InputStream
        new_from_data(data:list, destroy:GLib.DestroyNotify=None) -> Gio.InputStream

    Object GMemoryInputStream

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: InputStream = ...
    priv: MemoryInputStreamPrivate = ...
    def add_bytes(self, bytes: GLib.Bytes) -> None: ...
    def add_data(
        self,
        data: typing.Sequence[int],
        destroy: typing.Optional[typing.Callable[[None], None]] = None,
    ) -> None: ...
    @classmethod
    def new(cls) -> MemoryInputStream: ...
    @classmethod
    def new_from_bytes(cls, bytes: GLib.Bytes) -> MemoryInputStream: ...
    @classmethod
    def new_from_data(
        cls,
        data: typing.Sequence[int],
        destroy: typing.Optional[typing.Callable[[None], None]] = None,
    ) -> MemoryInputStream: ...

class MemoryInputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MemoryInputStreamClass()
    """

    parent_class: InputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class MemoryInputStreamPrivate(GObject.GPointer): ...

class MemoryMonitor(GObject.GInterface):
    """
    Interface GMemoryMonitor

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def dup_default() -> MemoryMonitor: ...

class MemoryMonitorInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        MemoryMonitorInterface()
    """

    g_iface: GObject.TypeInterface = ...
    low_memory_warning: typing.Callable[
        [MemoryMonitor, MemoryMonitorWarningLevel], None
    ] = ...

class MemoryOutputStream(OutputStream, PollableOutputStream, Seekable):
    """
    :Constructors:

    ::

        MemoryOutputStream(**properties)
        new_resizable() -> Gio.OutputStream

    Object GMemoryOutputStream

    Properties from GMemoryOutputStream:
      data -> gpointer: data
      size -> gulong: size
      data-size -> gulong: data-size
      realloc-function -> gpointer: realloc-function
      destroy-function -> gpointer: destroy-function

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        data: typing.Optional[None]
        data_size: int
        size: int

    props: Props = ...
    parent_instance: OutputStream = ...
    priv: MemoryOutputStreamPrivate = ...
    def __init__(self, data: None = ..., size: int = ...) -> None: ...
    def get_data(self) -> None: ...
    def get_data_size(self) -> int: ...
    def get_size(self) -> int: ...
    @classmethod
    def new_resizable(cls) -> MemoryOutputStream: ...
    def steal_as_bytes(self) -> GLib.Bytes: ...
    def steal_data(self) -> None: ...

class MemoryOutputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MemoryOutputStreamClass()
    """

    parent_class: OutputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class MemoryOutputStreamPrivate(GObject.GPointer): ...

class Menu(MenuModel):
    """
    :Constructors:

    ::

        Menu(**properties)
        new() -> Gio.Menu

    Object GMenu

    Signals from GMenuModel:
      items-changed (gint, gint, gint)

    Signals from GObject:
      notify (GParam)
    """

    def append(
        self,
        label: typing.Optional[str] = None,
        detailed_action: typing.Optional[str] = None,
    ) -> None: ...
    def append_item(self, item: MenuItem) -> None: ...
    def append_section(
        self, label: typing.Optional[str], section: MenuModel
    ) -> None: ...
    def append_submenu(
        self, label: typing.Optional[str], submenu: MenuModel
    ) -> None: ...
    def freeze(self) -> None: ...
    def insert(
        self,
        position: int,
        label: typing.Optional[str] = None,
        detailed_action: typing.Optional[str] = None,
    ) -> None: ...
    def insert_item(self, position: int, item: MenuItem) -> None: ...
    def insert_section(
        self, position: int, label: typing.Optional[str], section: MenuModel
    ) -> None: ...
    def insert_submenu(
        self, position: int, label: typing.Optional[str], submenu: MenuModel
    ) -> None: ...
    @classmethod
    def new(cls) -> Menu: ...
    def prepend(
        self,
        label: typing.Optional[str] = None,
        detailed_action: typing.Optional[str] = None,
    ) -> None: ...
    def prepend_item(self, item: MenuItem) -> None: ...
    def prepend_section(
        self, label: typing.Optional[str], section: MenuModel
    ) -> None: ...
    def prepend_submenu(
        self, label: typing.Optional[str], submenu: MenuModel
    ) -> None: ...
    def remove(self, position: int) -> None: ...
    def remove_all(self) -> None: ...

class MenuAttributeIter(GObject.Object):
    """
    :Constructors:

    ::

        MenuAttributeIter(**properties)

    Object GMenuAttributeIter

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: MenuAttributeIterPrivate = ...
    def do_get_next(self) -> typing.Tuple[bool, str, GLib.Variant]: ...
    def get_name(self) -> str: ...
    def get_next(self) -> typing.Tuple[bool, str, GLib.Variant]: ...
    def get_value(self) -> GLib.Variant: ...
    def next(self) -> bool: ...

class MenuAttributeIterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MenuAttributeIterClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_next: typing.Callable[
        [MenuAttributeIter], typing.Tuple[bool, str, GLib.Variant]
    ] = ...

class MenuAttributeIterPrivate(GObject.GPointer): ...

class MenuItem(GObject.Object):
    """
    :Constructors:

    ::

        MenuItem(**properties)
        new(label:str=None, detailed_action:str=None) -> Gio.MenuItem
        new_from_model(model:Gio.MenuModel, item_index:int) -> Gio.MenuItem
        new_section(label:str=None, section:Gio.MenuModel) -> Gio.MenuItem
        new_submenu(label:str=None, submenu:Gio.MenuModel) -> Gio.MenuItem

    Object GMenuItem

    Signals from GObject:
      notify (GParam)
    """

    def get_attribute_value(
        self, attribute: str, expected_type: typing.Optional[GLib.VariantType] = None
    ) -> typing.Optional[GLib.Variant]: ...
    def get_link(self, link: str) -> typing.Optional[MenuModel]: ...
    @classmethod
    def new(
        cls,
        label: typing.Optional[str] = None,
        detailed_action: typing.Optional[str] = None,
    ) -> MenuItem: ...
    @classmethod
    def new_from_model(cls, model: MenuModel, item_index: int) -> MenuItem: ...
    @classmethod
    def new_section(
        cls, label: typing.Optional[str], section: MenuModel
    ) -> MenuItem: ...
    @classmethod
    def new_submenu(
        cls, label: typing.Optional[str], submenu: MenuModel
    ) -> MenuItem: ...
    def set_action_and_target_value(
        self,
        action: typing.Optional[str] = None,
        target_value: typing.Optional[GLib.Variant] = None,
    ) -> None: ...
    # override
    def set_attribute(
        self, attributes: list[typing.Tuple[str, str, typing.Any]]
    ) -> None: ...
    def set_attribute_value(
        self, attribute: str, value: typing.Optional[GLib.Variant] = None
    ) -> None: ...
    def set_detailed_action(self, detailed_action: str) -> None: ...
    def set_icon(self, icon: Icon) -> None: ...
    def set_label(self, label: typing.Optional[str] = None) -> None: ...
    def set_link(self, link: str, model: typing.Optional[MenuModel] = None) -> None: ...
    def set_section(self, section: typing.Optional[MenuModel] = None) -> None: ...
    def set_submenu(self, submenu: typing.Optional[MenuModel] = None) -> None: ...

class MenuLinkIter(GObject.Object):
    """
    :Constructors:

    ::

        MenuLinkIter(**properties)

    Object GMenuLinkIter

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: MenuLinkIterPrivate = ...
    def do_get_next(self) -> typing.Tuple[bool, str, MenuModel]: ...
    def get_name(self) -> str: ...
    def get_next(self) -> typing.Tuple[bool, str, MenuModel]: ...
    def get_value(self) -> MenuModel: ...
    def next(self) -> bool: ...

class MenuLinkIterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MenuLinkIterClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_next: typing.Callable[[MenuLinkIter], typing.Tuple[bool, str, MenuModel]] = ...

class MenuLinkIterPrivate(GObject.GPointer): ...

class MenuModel(GObject.Object):
    """
    :Constructors:

    ::

        MenuModel(**properties)

    Object GMenuModel

    Signals from GMenuModel:
      items-changed (gint, gint, gint)

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: MenuModelPrivate = ...
    def do_get_item_attribute_value(
        self,
        item_index: int,
        attribute: str,
        expected_type: typing.Optional[GLib.VariantType] = None,
    ) -> typing.Optional[GLib.Variant]: ...
    def do_get_item_attributes(self, item_index: int) -> dict[str, GLib.Variant]: ...
    def do_get_item_link(
        self, item_index: int, link: str
    ) -> typing.Optional[MenuModel]: ...
    def do_get_item_links(self, item_index: int) -> dict[str, MenuModel]: ...
    def do_get_n_items(self) -> int: ...
    def do_is_mutable(self) -> bool: ...
    def do_iterate_item_attributes(self, item_index: int) -> MenuAttributeIter: ...
    def do_iterate_item_links(self, item_index: int) -> MenuLinkIter: ...
    def get_item_attribute_value(
        self,
        item_index: int,
        attribute: str,
        expected_type: typing.Optional[GLib.VariantType] = None,
    ) -> typing.Optional[GLib.Variant]: ...
    def get_item_link(
        self, item_index: int, link: str
    ) -> typing.Optional[MenuModel]: ...
    def get_n_items(self) -> int: ...
    def is_mutable(self) -> bool: ...
    def items_changed(self, position: int, removed: int, added: int) -> None: ...
    def iterate_item_attributes(self, item_index: int) -> MenuAttributeIter: ...
    def iterate_item_links(self, item_index: int) -> MenuLinkIter: ...

class MenuModelClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MenuModelClass()
    """

    parent_class: GObject.ObjectClass = ...
    is_mutable: typing.Callable[[MenuModel], bool] = ...
    get_n_items: typing.Callable[[MenuModel], int] = ...
    get_item_attributes: typing.Callable[[MenuModel, int], dict[str, GLib.Variant]] = (
        ...
    )
    iterate_item_attributes: typing.Callable[[MenuModel, int], MenuAttributeIter] = ...
    get_item_attribute_value: typing.Callable[
        [MenuModel, int, str, typing.Optional[GLib.VariantType]],
        typing.Optional[GLib.Variant],
    ] = ...
    get_item_links: typing.Callable[[MenuModel, int], dict[str, MenuModel]] = ...
    iterate_item_links: typing.Callable[[MenuModel, int], MenuLinkIter] = ...
    get_item_link: typing.Callable[
        [MenuModel, int, str], typing.Optional[MenuModel]
    ] = ...

class MenuModelPrivate(GObject.GPointer): ...

class Mount(GObject.GInterface):
    """
    Interface GMount

    Signals from GObject:
      notify (GParam)
    """

    def can_eject(self) -> bool: ...
    def can_unmount(self) -> bool: ...
    def eject(
        self,
        flags: MountUnmountFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def eject_finish(self, result: AsyncResult) -> bool: ...
    def eject_with_operation(
        self,
        flags: MountUnmountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def eject_with_operation_finish(self, result: AsyncResult) -> bool: ...
    def get_default_location(self) -> File: ...
    def get_drive(self) -> typing.Optional[Drive]: ...
    def get_icon(self) -> Icon: ...
    def get_name(self) -> str: ...
    def get_root(self) -> File: ...
    def get_sort_key(self) -> typing.Optional[str]: ...
    def get_symbolic_icon(self) -> Icon: ...
    def get_uuid(self) -> typing.Optional[str]: ...
    def get_volume(self) -> typing.Optional[Volume]: ...
    def guess_content_type(
        self,
        force_rescan: bool,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def guess_content_type_finish(self, result: AsyncResult) -> list[str]: ...
    def guess_content_type_sync(
        self, force_rescan: bool, cancellable: typing.Optional[Cancellable] = None
    ) -> list[str]: ...
    def is_shadowed(self) -> bool: ...
    def remount(
        self,
        flags: MountMountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def remount_finish(self, result: AsyncResult) -> bool: ...
    def shadow(self) -> None: ...
    def unmount(
        self,
        flags: MountUnmountFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def unmount_finish(self, result: AsyncResult) -> bool: ...
    def unmount_with_operation(
        self,
        flags: MountUnmountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def unmount_with_operation_finish(self, result: AsyncResult) -> bool: ...
    def unshadow(self) -> None: ...

class MountIface(GObject.GPointer):
    """
    :Constructors:

    ::

        MountIface()
    """

    g_iface: GObject.TypeInterface = ...
    changed: typing.Callable[[Mount], None] = ...
    unmounted: typing.Callable[[Mount], None] = ...
    get_root: typing.Callable[[Mount], File] = ...
    get_name: typing.Callable[[Mount], str] = ...
    get_icon: typing.Callable[[Mount], Icon] = ...
    get_uuid: typing.Callable[[Mount], typing.Optional[str]] = ...
    get_volume: typing.Callable[[Mount], typing.Optional[Volume]] = ...
    get_drive: typing.Callable[[Mount], typing.Optional[Drive]] = ...
    can_unmount: typing.Callable[[Mount], bool] = ...
    can_eject: typing.Callable[[Mount], bool] = ...
    unmount: typing.Callable[..., None] = ...
    unmount_finish: typing.Callable[[Mount, AsyncResult], bool] = ...
    eject: typing.Callable[..., None] = ...
    eject_finish: typing.Callable[[Mount, AsyncResult], bool] = ...
    remount: typing.Callable[..., None] = ...
    remount_finish: typing.Callable[[Mount, AsyncResult], bool] = ...
    guess_content_type: typing.Callable[..., None] = ...
    guess_content_type_finish: typing.Callable[[Mount, AsyncResult], list[str]] = ...
    guess_content_type_sync: typing.Callable[
        [Mount, bool, typing.Optional[Cancellable]], list[str]
    ] = ...
    pre_unmount: typing.Callable[[Mount], None] = ...
    unmount_with_operation: typing.Callable[..., None] = ...
    unmount_with_operation_finish: typing.Callable[[Mount, AsyncResult], bool] = ...
    eject_with_operation: typing.Callable[..., None] = ...
    eject_with_operation_finish: typing.Callable[[Mount, AsyncResult], bool] = ...
    get_default_location: typing.Callable[[Mount], File] = ...
    get_sort_key: typing.Callable[[Mount], typing.Optional[str]] = ...
    get_symbolic_icon: typing.Callable[[Mount], Icon] = ...

class MountOperation(GObject.Object):
    """
    :Constructors:

    ::

        MountOperation(**properties)
        new() -> Gio.MountOperation

    Object GMountOperation

    Signals from GMountOperation:
      ask-password (gchararray, gchararray, gchararray, GAskPasswordFlags)
      ask-question (gchararray, GStrv)
      reply (GMountOperationResult)
      aborted ()
      show-processes (gchararray, GArray, GStrv)
      show-unmount-progress (gchararray, gint64, gint64)

    Properties from GMountOperation:
      username -> gchararray: username
      password -> gchararray: password
      anonymous -> gboolean: anonymous
      domain -> gchararray: domain
      password-save -> GPasswordSave: password-save
      choice -> gint: choice
      is-tcrypt-hidden-volume -> gboolean: is-tcrypt-hidden-volume
      is-tcrypt-system-volume -> gboolean: is-tcrypt-system-volume
      pim -> guint: pim

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        anonymous: bool
        choice: int
        domain: typing.Optional[str]
        is_tcrypt_hidden_volume: bool
        is_tcrypt_system_volume: bool
        password: typing.Optional[str]
        password_save: PasswordSave
        pim: int
        username: typing.Optional[str]

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: MountOperationPrivate = ...
    def __init__(
        self,
        anonymous: bool = ...,
        choice: int = ...,
        domain: typing.Optional[str] = ...,
        is_tcrypt_hidden_volume: bool = ...,
        is_tcrypt_system_volume: bool = ...,
        password: typing.Optional[str] = ...,
        password_save: PasswordSave = ...,
        pim: int = ...,
        username: typing.Optional[str] = ...,
    ) -> None: ...
    def do_aborted(self) -> None: ...
    def do_ask_password(
        self,
        message: str,
        default_user: str,
        default_domain: str,
        flags: AskPasswordFlags,
    ) -> None: ...
    def do_ask_question(self, message: str, choices: typing.Sequence[str]) -> None: ...
    def do_reply(self, result: MountOperationResult) -> None: ...
    def do_show_processes(
        self,
        message: str,
        processes: typing.Sequence[int],
        choices: typing.Sequence[str],
    ) -> None: ...
    def do_show_unmount_progress(
        self, message: str, time_left: int, bytes_left: int
    ) -> None: ...
    def get_anonymous(self) -> bool: ...
    def get_choice(self) -> int: ...
    def get_domain(self) -> typing.Optional[str]: ...
    def get_is_tcrypt_hidden_volume(self) -> bool: ...
    def get_is_tcrypt_system_volume(self) -> bool: ...
    def get_password(self) -> typing.Optional[str]: ...
    def get_password_save(self) -> PasswordSave: ...
    def get_pim(self) -> int: ...
    def get_username(self) -> typing.Optional[str]: ...
    @classmethod
    def new(cls) -> MountOperation: ...
    def reply(self, result: MountOperationResult) -> None: ...
    def set_anonymous(self, anonymous: bool) -> None: ...
    def set_choice(self, choice: int) -> None: ...
    def set_domain(self, domain: typing.Optional[str] = None) -> None: ...
    def set_is_tcrypt_hidden_volume(self, hidden_volume: bool) -> None: ...
    def set_is_tcrypt_system_volume(self, system_volume: bool) -> None: ...
    def set_password(self, password: typing.Optional[str] = None) -> None: ...
    def set_password_save(self, save: PasswordSave) -> None: ...
    def set_pim(self, pim: int) -> None: ...
    def set_username(self, username: typing.Optional[str] = None) -> None: ...

class MountOperationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MountOperationClass()
    """

    parent_class: GObject.ObjectClass = ...
    ask_password: typing.Callable[
        [MountOperation, str, str, str, AskPasswordFlags], None
    ] = ...
    ask_question: typing.Callable[[MountOperation, str, typing.Sequence[str]], None] = (
        ...
    )
    reply: typing.Callable[[MountOperation, MountOperationResult], None] = ...
    aborted: typing.Callable[[MountOperation], None] = ...
    show_processes: typing.Callable[
        [MountOperation, str, typing.Sequence[int], typing.Sequence[str]], None
    ] = ...
    show_unmount_progress: typing.Callable[[MountOperation, str, int, int], None] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...
    _g_reserved6: None = ...
    _g_reserved7: None = ...
    _g_reserved8: None = ...
    _g_reserved9: None = ...

class MountOperationPrivate(GObject.GPointer): ...

class NativeSocketAddress(SocketAddress, SocketConnectable):
    """
    :Constructors:

    ::

        NativeSocketAddress(**properties)
        new(native=None, len:int) -> Gio.SocketAddress

    Object GNativeSocketAddress

    Properties from GSocketAddress:
      family -> GSocketFamily: family

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        family: SocketFamily

    props: Props = ...
    parent_instance: SocketAddress = ...
    priv: NativeSocketAddressPrivate = ...
    @classmethod
    def new(cls, native: None, len: int) -> NativeSocketAddress: ...

class NativeSocketAddressClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NativeSocketAddressClass()
    """

    parent_class: SocketAddressClass = ...

class NativeSocketAddressPrivate(GObject.GPointer): ...

class NativeVolumeMonitor(VolumeMonitor):
    """
    :Constructors:

    ::

        NativeVolumeMonitor(**properties)

    Object GNativeVolumeMonitor

    Signals from GVolumeMonitor:
      volume-added (GVolume)
      volume-removed (GVolume)
      volume-changed (GVolume)
      mount-added (GMount)
      mount-removed (GMount)
      mount-pre-unmount (GMount)
      mount-changed (GMount)
      drive-connected (GDrive)
      drive-disconnected (GDrive)
      drive-changed (GDrive)
      drive-eject-button (GDrive)
      drive-stop-button (GDrive)

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: VolumeMonitor = ...

class NativeVolumeMonitorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NativeVolumeMonitorClass()
    """

    parent_class: VolumeMonitorClass = ...
    get_mount_for_mount_path: None = ...

class NetworkAddress(GObject.Object, SocketConnectable):
    """
    :Constructors:

    ::

        NetworkAddress(**properties)
        new(hostname:str, port:int) -> Gio.NetworkAddress
        new_loopback(port:int) -> Gio.NetworkAddress

    Object GNetworkAddress

    Properties from GNetworkAddress:
      hostname -> gchararray: hostname
      port -> guint: port
      scheme -> gchararray: scheme

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        hostname: str
        port: int
        scheme: typing.Optional[str]

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: NetworkAddressPrivate = ...
    def __init__(
        self, hostname: str = ..., port: int = ..., scheme: str = ...
    ) -> None: ...
    def get_hostname(self) -> str: ...
    def get_port(self) -> int: ...
    def get_scheme(self) -> typing.Optional[str]: ...
    @classmethod
    def new(cls, hostname: str, port: int) -> NetworkAddress: ...
    @classmethod
    def new_loopback(cls, port: int) -> NetworkAddress: ...
    @staticmethod
    def parse(host_and_port: str, default_port: int) -> NetworkAddress: ...
    @staticmethod
    def parse_uri(uri: str, default_port: int) -> NetworkAddress: ...

class NetworkAddressClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NetworkAddressClass()
    """

    parent_class: GObject.ObjectClass = ...

class NetworkAddressPrivate(GObject.GPointer): ...

class NetworkMonitor(GObject.GInterface):
    """
    Interface GNetworkMonitor

    Signals from GObject:
      notify (GParam)
    """

    def can_reach(
        self,
        connectable: SocketConnectable,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def can_reach_async(
        self,
        connectable: SocketConnectable,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def can_reach_finish(self, result: AsyncResult) -> bool: ...
    def get_connectivity(self) -> NetworkConnectivity: ...
    @staticmethod
    def get_default() -> NetworkMonitor: ...
    def get_network_available(self) -> bool: ...
    def get_network_metered(self) -> bool: ...

class NetworkMonitorInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        NetworkMonitorInterface()
    """

    g_iface: GObject.TypeInterface = ...
    network_changed: typing.Callable[[NetworkMonitor, bool], None] = ...
    can_reach: typing.Callable[
        [NetworkMonitor, SocketConnectable, typing.Optional[Cancellable]], bool
    ] = ...
    can_reach_async: typing.Callable[..., None] = ...
    can_reach_finish: typing.Callable[[NetworkMonitor, AsyncResult], bool] = ...

class NetworkService(GObject.Object, SocketConnectable):
    """
    :Constructors:

    ::

        NetworkService(**properties)
        new(service:str, protocol:str, domain:str) -> Gio.NetworkService

    Object GNetworkService

    Properties from GNetworkService:
      service -> gchararray: service
      protocol -> gchararray: protocol
      domain -> gchararray: domain
      scheme -> gchararray: scheme

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        domain: str
        protocol: str
        scheme: str
        service: str

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: NetworkServicePrivate = ...
    def __init__(
        self,
        domain: str = ...,
        protocol: str = ...,
        scheme: str = ...,
        service: str = ...,
    ) -> None: ...
    def get_domain(self) -> str: ...
    def get_protocol(self) -> str: ...
    def get_scheme(self) -> str: ...
    def get_service(self) -> str: ...
    @classmethod
    def new(cls, service: str, protocol: str, domain: str) -> NetworkService: ...
    def set_scheme(self, scheme: str) -> None: ...

class NetworkServiceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NetworkServiceClass()
    """

    parent_class: GObject.ObjectClass = ...

class NetworkServicePrivate(GObject.GPointer): ...

class Notification(GObject.Object):
    """
    :Constructors:

    ::

        Notification(**properties)
        new(title:str) -> Gio.Notification

    Object GNotification

    Signals from GObject:
      notify (GParam)
    """

    def add_button(self, label: str, detailed_action: str) -> None: ...
    def add_button_with_target(
        self, label: str, action: str, target: typing.Optional[GLib.Variant] = None
    ) -> None: ...
    @classmethod
    def new(cls, title: str) -> Notification: ...
    def set_body(self, body: typing.Optional[str] = None) -> None: ...
    def set_category(self, category: typing.Optional[str] = None) -> None: ...
    def set_default_action(self, detailed_action: str) -> None: ...
    def set_default_action_and_target(
        self, action: str, target: typing.Optional[GLib.Variant] = None
    ) -> None: ...
    def set_icon(self, icon: Icon) -> None: ...
    def set_priority(self, priority: NotificationPriority) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_urgent(self, urgent: bool) -> None: ...

class OutputMessage(GObject.GPointer):
    """
    :Constructors:

    ::

        OutputMessage()
    """

    address: SocketAddress = ...
    vectors: OutputVector = ...
    num_vectors: int = ...
    bytes_sent: int = ...
    control_messages: list[SocketControlMessage] = ...
    num_control_messages: int = ...

class OutputStream(GObject.Object):
    """
    :Constructors:

    ::

        OutputStream(**properties)

    Object GOutputStream

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: OutputStreamPrivate = ...
    def clear_pending(self) -> None: ...
    def close(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def close_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_fn(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def do_flush(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def do_flush_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_flush_finish(self, result: AsyncResult) -> bool: ...
    def do_splice(
        self,
        source: InputStream,
        flags: OutputStreamSpliceFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def do_splice_async(
        self,
        source: InputStream,
        flags: OutputStreamSpliceFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_splice_finish(self, result: AsyncResult) -> int: ...
    def do_write_async(
        self,
        buffer: typing.Optional[typing.Sequence[int]],
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_write_finish(self, result: AsyncResult) -> int: ...
    def do_write_fn(
        self,
        buffer: typing.Optional[typing.Sequence[int]] = None,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def do_writev_async(
        self,
        vectors: typing.Sequence[OutputVector],
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_writev_finish(self, result: AsyncResult) -> typing.Tuple[bool, int]: ...
    def do_writev_fn(
        self,
        vectors: typing.Sequence[OutputVector],
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[bool, int]: ...
    def flush(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def flush_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def flush_finish(self, result: AsyncResult) -> bool: ...
    def has_pending(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def is_closing(self) -> bool: ...
    def set_pending(self) -> bool: ...
    def splice(
        self,
        source: InputStream,
        flags: OutputStreamSpliceFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def splice_async(
        self,
        source: InputStream,
        flags: OutputStreamSpliceFlags,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def splice_finish(self, result: AsyncResult) -> int: ...
    def write(
        self,
        buffer: typing.Sequence[int],
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def write_all(
        self,
        buffer: typing.Sequence[int],
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[bool, int]: ...
    def write_all_async(
        self,
        buffer: typing.Sequence[int],
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def write_all_finish(self, result: AsyncResult) -> typing.Tuple[bool, int]: ...
    def write_async(
        self,
        buffer: typing.Sequence[int],
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def write_bytes(
        self, bytes: GLib.Bytes, cancellable: typing.Optional[Cancellable] = None
    ) -> int: ...
    def write_bytes_async(
        self,
        bytes: GLib.Bytes,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def write_bytes_finish(self, result: AsyncResult) -> int: ...
    def write_finish(self, result: AsyncResult) -> int: ...
    def writev(
        self,
        vectors: typing.Sequence[OutputVector],
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[bool, int]: ...
    def writev_all(
        self,
        vectors: typing.Sequence[OutputVector],
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[bool, int]: ...
    def writev_all_async(
        self,
        vectors: typing.Sequence[OutputVector],
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def writev_all_finish(self, result: AsyncResult) -> typing.Tuple[bool, int]: ...
    def writev_async(
        self,
        vectors: typing.Sequence[OutputVector],
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def writev_finish(self, result: AsyncResult) -> typing.Tuple[bool, int]: ...

class OutputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OutputStreamClass()
    """

    parent_class: GObject.ObjectClass = ...
    write_fn: typing.Callable[
        [
            OutputStream,
            typing.Optional[typing.Sequence[int]],
            typing.Optional[Cancellable],
        ],
        int,
    ] = ...
    splice: typing.Callable[
        [
            OutputStream,
            InputStream,
            OutputStreamSpliceFlags,
            typing.Optional[Cancellable],
        ],
        int,
    ] = ...
    flush: typing.Callable[[OutputStream, typing.Optional[Cancellable]], bool] = ...
    close_fn: typing.Callable[[OutputStream, typing.Optional[Cancellable]], bool] = ...
    write_async: typing.Callable[..., None] = ...
    write_finish: typing.Callable[[OutputStream, AsyncResult], int] = ...
    splice_async: typing.Callable[..., None] = ...
    splice_finish: typing.Callable[[OutputStream, AsyncResult], int] = ...
    flush_async: typing.Callable[..., None] = ...
    flush_finish: typing.Callable[[OutputStream, AsyncResult], bool] = ...
    close_async: typing.Callable[..., None] = ...
    close_finish: typing.Callable[[OutputStream, AsyncResult], bool] = ...
    writev_fn: typing.Callable[
        [OutputStream, typing.Sequence[OutputVector], typing.Optional[Cancellable]],
        typing.Tuple[bool, int],
    ] = ...
    writev_async: typing.Callable[..., None] = ...
    writev_finish: typing.Callable[
        [OutputStream, AsyncResult], typing.Tuple[bool, int]
    ] = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...
    _g_reserved6: None = ...
    _g_reserved7: None = ...
    _g_reserved8: None = ...

class OutputStreamPrivate(GObject.GPointer): ...

class OutputVector(GObject.GPointer):
    """
    :Constructors:

    ::

        OutputVector()
    """

    buffer: None = ...
    size: int = ...

class Permission(GObject.Object):
    """
    :Constructors:

    ::

        Permission(**properties)

    Object GPermission

    Properties from GPermission:
      allowed -> gboolean: allowed
      can-acquire -> gboolean: can-acquire
      can-release -> gboolean: can-release

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        allowed: bool
        can_acquire: bool
        can_release: bool

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: PermissionPrivate = ...
    def acquire(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def acquire_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def acquire_finish(self, result: AsyncResult) -> bool: ...
    def do_acquire(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def do_acquire_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_acquire_finish(self, result: AsyncResult) -> bool: ...
    def do_release(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def do_release_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_release_finish(self, result: AsyncResult) -> bool: ...
    def get_allowed(self) -> bool: ...
    def get_can_acquire(self) -> bool: ...
    def get_can_release(self) -> bool: ...
    def impl_update(
        self, allowed: bool, can_acquire: bool, can_release: bool
    ) -> None: ...
    def release(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def release_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def release_finish(self, result: AsyncResult) -> bool: ...

class PermissionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PermissionClass()
    """

    parent_class: GObject.ObjectClass = ...
    acquire: typing.Callable[[Permission, typing.Optional[Cancellable]], bool] = ...
    acquire_async: typing.Callable[..., None] = ...
    acquire_finish: typing.Callable[[Permission, AsyncResult], bool] = ...
    release: typing.Callable[[Permission, typing.Optional[Cancellable]], bool] = ...
    release_async: typing.Callable[..., None] = ...
    release_finish: typing.Callable[[Permission, AsyncResult], bool] = ...
    reserved: list[None] = ...

class PermissionPrivate(GObject.GPointer): ...

class PollableInputStream(GObject.GInterface):
    """
    Interface GPollableInputStream

    Signals from GObject:
      notify (GParam)
    """

    def can_poll(self) -> bool: ...
    def create_source(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> GLib.Source: ...
    def is_readable(self) -> bool: ...
    def read_nonblocking(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[int, bytes]: ...

class PollableInputStreamInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        PollableInputStreamInterface()
    """

    g_iface: GObject.TypeInterface = ...
    can_poll: typing.Callable[[PollableInputStream], bool] = ...
    is_readable: typing.Callable[[PollableInputStream], bool] = ...
    create_source: typing.Callable[
        [PollableInputStream, typing.Optional[Cancellable]], GLib.Source
    ] = ...
    read_nonblocking: typing.Callable[
        [PollableInputStream], typing.Tuple[int, bytes]
    ] = ...

class PollableOutputStream(GObject.GInterface):
    """
    Interface GPollableOutputStream

    Signals from GObject:
      notify (GParam)
    """

    def can_poll(self) -> bool: ...
    def create_source(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> GLib.Source: ...
    def is_writable(self) -> bool: ...
    def write_nonblocking(
        self,
        buffer: typing.Sequence[int],
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def writev_nonblocking(
        self,
        vectors: typing.Sequence[OutputVector],
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[PollableReturn, int]: ...

class PollableOutputStreamInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        PollableOutputStreamInterface()
    """

    g_iface: GObject.TypeInterface = ...
    can_poll: typing.Callable[[PollableOutputStream], bool] = ...
    is_writable: typing.Callable[[PollableOutputStream], bool] = ...
    create_source: typing.Callable[
        [PollableOutputStream, typing.Optional[Cancellable]], GLib.Source
    ] = ...
    write_nonblocking: typing.Callable[
        [PollableOutputStream, typing.Optional[typing.Sequence[int]]], int
    ] = ...
    writev_nonblocking: typing.Callable[
        [PollableOutputStream, typing.Sequence[OutputVector]],
        typing.Tuple[PollableReturn, int],
    ] = ...

class PowerProfileMonitor(GObject.GInterface):
    """
    Interface GPowerProfileMonitor

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def dup_default() -> PowerProfileMonitor: ...
    def get_power_saver_enabled(self) -> bool: ...

class PowerProfileMonitorInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        PowerProfileMonitorInterface()
    """

    g_iface: GObject.TypeInterface = ...

class PropertyAction(GObject.Object, Action):
    """
    :Constructors:

    ::

        PropertyAction(**properties)
        new(name:str, object:GObject.Object, property_name:str) -> Gio.PropertyAction

    Object GPropertyAction

    Properties from GPropertyAction:
      name -> gchararray: name
      parameter-type -> GVariantType: parameter-type
      enabled -> gboolean: enabled
      state-type -> GVariantType: state-type
      state -> GVariant: state
      object -> GObject: object
      property-name -> gchararray: property-name
      invert-boolean -> gboolean: invert-boolean

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        enabled: bool
        invert_boolean: bool
        name: str
        parameter_type: GLib.VariantType
        state: GLib.Variant
        state_type: GLib.VariantType
        object: GObject.Object
        property_name: str

    props: Props = ...
    def __init__(
        self,
        invert_boolean: bool = ...,
        name: str = ...,
        object: GObject.Object = ...,
        property_name: str = ...,
    ) -> None: ...
    @classmethod
    def new(
        cls, name: str, object: GObject.Object, property_name: str
    ) -> PropertyAction: ...

class Proxy(GObject.GInterface):
    """
    Interface GProxy

    Signals from GObject:
      notify (GParam)
    """

    def connect(
        self,
        connection: IOStream,
        proxy_address: ProxyAddress,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> IOStream: ...
    def connect_async(
        self,
        connection: IOStream,
        proxy_address: ProxyAddress,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def connect_finish(self, result: AsyncResult) -> IOStream: ...
    @staticmethod
    def get_default_for_protocol(protocol: str) -> typing.Optional[Proxy]: ...
    def supports_hostname(self) -> bool: ...

class ProxyAddress(InetSocketAddress, SocketConnectable):
    """
    :Constructors:

    ::

        ProxyAddress(**properties)
        new(inetaddr:Gio.InetAddress, port:int, protocol:str, dest_hostname:str, dest_port:int, username:str=None, password:str=None) -> Gio.SocketAddress

    Object GProxyAddress

    Properties from GProxyAddress:
      protocol -> gchararray: protocol
      destination-protocol -> gchararray: destination-protocol
      destination-hostname -> gchararray: destination-hostname
      destination-port -> guint: destination-port
      username -> gchararray: username
      password -> gchararray: password
      uri -> gchararray: uri

    Properties from GInetSocketAddress:
      address -> GInetAddress: address
      port -> guint: port
      flowinfo -> guint: flowinfo
      scope-id -> guint: scope-id

    Properties from GSocketAddress:
      family -> GSocketFamily: family

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        destination_hostname: str
        destination_port: int
        destination_protocol: str
        password: typing.Optional[str]
        protocol: str
        uri: typing.Optional[str]
        username: typing.Optional[str]
        address: InetAddress
        flowinfo: int
        port: int
        scope_id: int
        family: SocketFamily

    props: Props = ...
    parent_instance: InetSocketAddress = ...
    priv: ProxyAddressPrivate = ...
    def __init__(
        self,
        destination_hostname: str = ...,
        destination_port: int = ...,
        destination_protocol: str = ...,
        password: str = ...,
        protocol: str = ...,
        uri: str = ...,
        username: str = ...,
        address: InetAddress = ...,
        flowinfo: int = ...,
        port: int = ...,
        scope_id: int = ...,
    ) -> None: ...
    def get_destination_hostname(self) -> str: ...
    def get_destination_port(self) -> int: ...
    def get_destination_protocol(self) -> str: ...
    def get_password(self) -> typing.Optional[str]: ...
    def get_protocol(self) -> str: ...
    def get_uri(self) -> typing.Optional[str]: ...
    def get_username(self) -> typing.Optional[str]: ...
    @classmethod
    def new(
        cls,
        inetaddr: InetAddress,
        port: int,
        protocol: str,
        dest_hostname: str,
        dest_port: int,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
    ) -> ProxyAddress: ...

class ProxyAddressClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProxyAddressClass()
    """

    parent_class: InetSocketAddressClass = ...

class ProxyAddressEnumerator(SocketAddressEnumerator):
    """
    :Constructors:

    ::

        ProxyAddressEnumerator(**properties)

    Object GProxyAddressEnumerator

    Properties from GProxyAddressEnumerator:
      uri -> gchararray: uri
      default-port -> guint: default-port
      connectable -> GSocketConnectable: connectable
      proxy-resolver -> GProxyResolver: proxy-resolver

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connectable: SocketConnectable
        default_port: int
        proxy_resolver: ProxyResolver
        uri: str

    props: Props = ...
    parent_instance: SocketAddressEnumerator = ...
    priv: ProxyAddressEnumeratorPrivate = ...
    def __init__(
        self,
        connectable: SocketConnectable = ...,
        default_port: int = ...,
        proxy_resolver: ProxyResolver = ...,
        uri: str = ...,
    ) -> None: ...

class ProxyAddressEnumeratorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProxyAddressEnumeratorClass()
    """

    parent_class: SocketAddressEnumeratorClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...
    _g_reserved6: None = ...
    _g_reserved7: None = ...

class ProxyAddressEnumeratorPrivate(GObject.GPointer): ...
class ProxyAddressPrivate(GObject.GPointer): ...

class ProxyInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        ProxyInterface()
    """

    g_iface: GObject.TypeInterface = ...
    connect: typing.Callable[
        [Proxy, IOStream, ProxyAddress, typing.Optional[Cancellable]], IOStream
    ] = ...
    connect_async: typing.Callable[..., None] = ...
    connect_finish: typing.Callable[[Proxy, AsyncResult], IOStream] = ...
    supports_hostname: typing.Callable[[Proxy], bool] = ...

class ProxyResolver(GObject.GInterface):
    """
    Interface GProxyResolver

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def get_default() -> ProxyResolver: ...
    def is_supported(self) -> bool: ...
    def lookup(
        self, uri: str, cancellable: typing.Optional[Cancellable] = None
    ) -> list[str]: ...
    def lookup_async(
        self,
        uri: str,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def lookup_finish(self, result: AsyncResult) -> list[str]: ...

class ProxyResolverInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        ProxyResolverInterface()
    """

    g_iface: GObject.TypeInterface = ...
    is_supported: typing.Callable[[ProxyResolver], bool] = ...
    lookup: typing.Callable[
        [ProxyResolver, str, typing.Optional[Cancellable]], list[str]
    ] = ...
    lookup_async: typing.Callable[..., None] = ...
    lookup_finish: typing.Callable[[ProxyResolver, AsyncResult], list[str]] = ...

class RemoteActionGroup(GObject.GInterface):
    """
    Interface GRemoteActionGroup

    Signals from GObject:
      notify (GParam)
    """

    def activate_action_full(
        self,
        action_name: str,
        parameter: typing.Optional[GLib.Variant],
        platform_data: GLib.Variant,
    ) -> None: ...
    def change_action_state_full(
        self, action_name: str, value: GLib.Variant, platform_data: GLib.Variant
    ) -> None: ...

class RemoteActionGroupInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        RemoteActionGroupInterface()
    """

    g_iface: GObject.TypeInterface = ...
    activate_action_full: typing.Callable[
        [RemoteActionGroup, str, typing.Optional[GLib.Variant], GLib.Variant], None
    ] = ...
    change_action_state_full: typing.Callable[
        [RemoteActionGroup, str, GLib.Variant, GLib.Variant], None
    ] = ...

class Resolver(GObject.Object):
    """
    :Constructors:

    ::

        Resolver(**properties)

    Object GResolver

    Signals from GResolver:
      reload ()

    Properties from GResolver:
      timeout -> guint: timeout

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        timeout: int

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: ResolverPrivate = ...
    def __init__(self, timeout: int = ...) -> None: ...
    def do_lookup_by_address(
        self, address: InetAddress, cancellable: typing.Optional[Cancellable] = None
    ) -> str: ...
    def do_lookup_by_address_async(
        self,
        address: InetAddress,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_lookup_by_address_finish(self, result: AsyncResult) -> str: ...
    def do_lookup_by_name(
        self, hostname: str, cancellable: typing.Optional[Cancellable] = None
    ) -> list[InetAddress]: ...
    def do_lookup_by_name_async(
        self,
        hostname: str,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_lookup_by_name_finish(self, result: AsyncResult) -> list[InetAddress]: ...
    def do_lookup_by_name_with_flags(
        self,
        hostname: str,
        flags: ResolverNameLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> list[InetAddress]: ...
    def do_lookup_by_name_with_flags_async(
        self,
        hostname: str,
        flags: ResolverNameLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_lookup_by_name_with_flags_finish(
        self, result: AsyncResult
    ) -> list[InetAddress]: ...
    def do_lookup_records(
        self,
        rrname: str,
        record_type: ResolverRecordType,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> list[GLib.Variant]: ...
    def do_lookup_records_async(
        self,
        rrname: str,
        record_type: ResolverRecordType,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_lookup_records_finish(self, result: AsyncResult) -> list[GLib.Variant]: ...
    def do_lookup_service_async(
        self,
        rrname: str,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_lookup_service_finish(self, result: AsyncResult) -> list[SrvTarget]: ...
    def do_reload(self) -> None: ...
    @staticmethod
    def get_default() -> Resolver: ...
    def get_timeout(self) -> int: ...
    def lookup_by_address(
        self, address: InetAddress, cancellable: typing.Optional[Cancellable] = None
    ) -> str: ...
    def lookup_by_address_async(
        self,
        address: InetAddress,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def lookup_by_address_finish(self, result: AsyncResult) -> str: ...
    def lookup_by_name(
        self, hostname: str, cancellable: typing.Optional[Cancellable] = None
    ) -> list[InetAddress]: ...
    def lookup_by_name_async(
        self,
        hostname: str,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def lookup_by_name_finish(self, result: AsyncResult) -> list[InetAddress]: ...
    def lookup_by_name_with_flags(
        self,
        hostname: str,
        flags: ResolverNameLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> list[InetAddress]: ...
    def lookup_by_name_with_flags_async(
        self,
        hostname: str,
        flags: ResolverNameLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def lookup_by_name_with_flags_finish(
        self, result: AsyncResult
    ) -> list[InetAddress]: ...
    def lookup_records(
        self,
        rrname: str,
        record_type: ResolverRecordType,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> list[GLib.Variant]: ...
    def lookup_records_async(
        self,
        rrname: str,
        record_type: ResolverRecordType,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def lookup_records_finish(self, result: AsyncResult) -> list[GLib.Variant]: ...
    def lookup_service(
        self,
        service: str,
        protocol: str,
        domain: str,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> list[SrvTarget]: ...
    def lookup_service_async(
        self,
        service: str,
        protocol: str,
        domain: str,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def lookup_service_finish(self, result: AsyncResult) -> list[SrvTarget]: ...
    def set_default(self) -> None: ...
    def set_timeout(self, timeout_ms: int) -> None: ...

class ResolverClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ResolverClass()
    """

    parent_class: GObject.ObjectClass = ...
    reload: typing.Callable[[Resolver], None] = ...
    lookup_by_name: typing.Callable[
        [Resolver, str, typing.Optional[Cancellable]], list[InetAddress]
    ] = ...
    lookup_by_name_async: typing.Callable[..., None] = ...
    lookup_by_name_finish: typing.Callable[
        [Resolver, AsyncResult], list[InetAddress]
    ] = ...
    lookup_by_address: typing.Callable[
        [Resolver, InetAddress, typing.Optional[Cancellable]], str
    ] = ...
    lookup_by_address_async: typing.Callable[..., None] = ...
    lookup_by_address_finish: typing.Callable[[Resolver, AsyncResult], str] = ...
    lookup_service: None = ...
    lookup_service_async: typing.Callable[..., None] = ...
    lookup_service_finish: typing.Callable[[Resolver, AsyncResult], list[SrvTarget]] = (
        ...
    )
    lookup_records: typing.Callable[
        [Resolver, str, ResolverRecordType, typing.Optional[Cancellable]],
        list[GLib.Variant],
    ] = ...
    lookup_records_async: typing.Callable[..., None] = ...
    lookup_records_finish: typing.Callable[
        [Resolver, AsyncResult], list[GLib.Variant]
    ] = ...
    lookup_by_name_with_flags_async: typing.Callable[..., None] = ...
    lookup_by_name_with_flags_finish: typing.Callable[
        [Resolver, AsyncResult], list[InetAddress]
    ] = ...
    lookup_by_name_with_flags: typing.Callable[
        [Resolver, str, ResolverNameLookupFlags, typing.Optional[Cancellable]],
        list[InetAddress],
    ] = ...

class ResolverPrivate(GObject.GPointer): ...

class Resource(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_from_data(data:GLib.Bytes) -> Gio.Resource
    """

    def enumerate_children(
        self, path: str, lookup_flags: ResourceLookupFlags
    ) -> list[str]: ...
    def get_info(
        self, path: str, lookup_flags: ResourceLookupFlags
    ) -> typing.Tuple[bool, int, int]: ...
    @staticmethod
    def load(filename: str) -> Resource: ...
    def lookup_data(
        self, path: str, lookup_flags: ResourceLookupFlags
    ) -> GLib.Bytes: ...
    @classmethod
    def new_from_data(cls, data: GLib.Bytes) -> Resource: ...
    def open_stream(
        self, path: str, lookup_flags: ResourceLookupFlags
    ) -> InputStream: ...
    def ref(self) -> Resource: ...
    def unref(self) -> None: ...

class Seekable(GObject.GInterface):
    """
    Interface GSeekable

    Signals from GObject:
      notify (GParam)
    """

    def can_seek(self) -> bool: ...
    def can_truncate(self) -> bool: ...
    def seek(
        self,
        offset: int,
        type: GLib.SeekType,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def tell(self) -> int: ...
    def truncate(
        self, offset: int, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...

class SeekableIface(GObject.GPointer):
    """
    :Constructors:

    ::

        SeekableIface()
    """

    g_iface: GObject.TypeInterface = ...
    tell: typing.Callable[[Seekable], int] = ...
    can_seek: typing.Callable[[Seekable], bool] = ...
    seek: typing.Callable[
        [Seekable, int, GLib.SeekType, typing.Optional[Cancellable]], bool
    ] = ...
    can_truncate: typing.Callable[[Seekable], bool] = ...
    truncate_fn: typing.Callable[
        [Seekable, int, typing.Optional[Cancellable]], bool
    ] = ...

class Settings(GObject.Object):
    """
    Provide dictionary-like access to GLib.Settings.

    Object GSettings

    Provide dictionary-like access to GLib.Settings.

    Signals from GSettings:
      changed (gchararray)
      change-event (gpointer, gint) -> gboolean
      writable-changed (gchararray)
      writable-change-event (guint) -> gboolean

    Properties from GSettings:
      settings-schema -> GSettingsSchema: settings-schema
      schema -> gchararray: schema
      schema-id -> gchararray: schema-id
      backend -> GSettingsBackend: backend
      path -> gchararray: path
      has-unapplied -> gboolean: has-unapplied
      delay-apply -> gboolean: delay-apply

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        backend: SettingsBackend
        delay_apply: bool
        has_unapplied: bool
        path: str
        schema: str
        schema_id: str
        settings_schema: SettingsSchema

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: SettingsPrivate = ...
    def __init__(
        self,
        backend: SettingsBackend = ...,
        path: str = ...,
        schema: str = ...,
        schema_id: str = ...,
        settings_schema: SettingsSchema = ...,
    ) -> None: ...
    def apply(self) -> None: ...
    def bind(
        self, key: str, object: GObject.Object, property: str, flags: SettingsBindFlags
    ) -> None: ...
    def bind_with_mapping(
        self,
        key: str,
        object: GObject.Object,
        property: str,
        flags: SettingsBindFlags,
        get_mapping: typing.Optional[typing.Callable[..., typing.Any]] = None,
        set_mapping: typing.Optional[typing.Callable[..., typing.Any]] = None,
    ) -> None: ...
    def bind_writable(
        self, key: str, object: GObject.Object, property: str, inverted: bool
    ) -> None: ...
    def create_action(self, key: str) -> Action: ...
    def delay(self) -> None: ...
    def do_change_event(self, keys: int, n_keys: int) -> bool: ...
    def do_changed(self, key: str) -> None: ...
    def do_writable_change_event(self, key: int) -> bool: ...
    def do_writable_changed(self, key: str) -> None: ...
    def get_boolean(self, key: str) -> bool: ...
    def get_child(self, name: str) -> Settings: ...
    def get_default_value(self, key: str) -> typing.Optional[GLib.Variant]: ...
    def get_double(self, key: str) -> float: ...
    def get_enum(self, key: str) -> int: ...
    def get_flags(self, key: str) -> int: ...
    def get_has_unapplied(self) -> bool: ...
    def get_int(self, key: str) -> int: ...
    def get_int64(self, key: str) -> int: ...
    def get_mapped(
        self,
        key: str,
        mapping: typing.Callable[..., typing.Tuple[bool, None]],
        *user_data: typing.Any,
    ) -> None: ...
    def get_range(self, key: str) -> GLib.Variant: ...
    def get_string(self, key: str) -> str: ...
    def get_strv(self, key: str) -> list[str]: ...
    def get_uint(self, key: str) -> int: ...
    def get_uint64(self, key: str) -> int: ...
    def get_user_value(self, key: str) -> typing.Optional[GLib.Variant]: ...
    def get_value(self, key: str) -> GLib.Variant: ...
    def is_writable(self, name: str) -> bool: ...
    def keys(self): ...  # FIXME Function
    def list_children(self) -> list[str]: ...
    def list_keys(self) -> list[str]: ...
    @staticmethod
    def list_relocatable_schemas() -> list[str]: ...
    @staticmethod
    def list_schemas() -> list[str]: ...
    @classmethod
    def new(cls, schema_id: str) -> Settings: ...
    @classmethod
    def new_full(
        cls,
        schema: SettingsSchema,
        backend: typing.Optional[SettingsBackend] = None,
        path: typing.Optional[str] = None,
    ) -> Settings: ...
    @classmethod
    def new_with_backend(cls, schema_id: str, backend: SettingsBackend) -> Settings: ...
    @classmethod
    def new_with_backend_and_path(
        cls, schema_id: str, backend: SettingsBackend, path: str
    ) -> Settings: ...
    @classmethod
    def new_with_path(cls, schema_id: str, path: str) -> Settings: ...
    def range_check(self, key: str, value: GLib.Variant) -> bool: ...
    def reset(self, key: str) -> None: ...
    def revert(self) -> None: ...
    def set_boolean(self, key: str, value: bool) -> bool: ...
    def set_double(self, key: str, value: float) -> bool: ...
    def set_enum(self, key: str, value: int) -> bool: ...
    def set_flags(self, key: str, value: int) -> bool: ...
    def set_int(self, key: str, value: int) -> bool: ...
    def set_int64(self, key: str, value: int) -> bool: ...
    def set_string(self, key: str, value: str) -> bool: ...
    def set_strv(
        self, key: str, value: typing.Optional[typing.Sequence[str]] = None
    ) -> bool: ...
    def set_uint(self, key: str, value: int) -> bool: ...
    def set_uint64(self, key: str, value: int) -> bool: ...
    def set_value(self, key: str, value: GLib.Variant) -> bool: ...
    @staticmethod
    def sync() -> None: ...
    @staticmethod
    def unbind(object: GObject.Object, property: str) -> None: ...

class SettingsBackend(GObject.Object):
    """
    :Constructors:

    ::

        SettingsBackend(**properties)

    Object GSettingsBackend

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: SettingsBackendPrivate = ...
    def changed(self, key: str, origin_tag: None) -> None: ...
    def changed_tree(self, tree: GLib.Tree, origin_tag: None) -> None: ...
    def do_get_writable(self, key: str) -> bool: ...
    def do_read(
        self, key: str, expected_type: GLib.VariantType, default_value: bool
    ) -> GLib.Variant: ...
    def do_read_user_value(
        self, key: str, expected_type: GLib.VariantType
    ) -> GLib.Variant: ...
    def do_reset(self, key: str, origin_tag: None) -> None: ...
    def do_subscribe(self, name: str) -> None: ...
    def do_sync(self) -> None: ...
    def do_unsubscribe(self, name: str) -> None: ...
    def do_write(self, key: str, value: GLib.Variant, origin_tag: None) -> bool: ...
    def do_write_tree(self, tree: GLib.Tree, origin_tag: None) -> bool: ...
    @staticmethod
    def flatten_tree(
        tree: GLib.Tree,
    ) -> typing.Tuple[str, list[str], list[GLib.Variant]]: ...
    @staticmethod
    def get_default() -> SettingsBackend: ...
    def keys_changed(
        self, path: str, items: typing.Sequence[str], origin_tag: None
    ) -> None: ...
    def path_changed(self, path: str, origin_tag: None) -> None: ...
    def path_writable_changed(self, path: str) -> None: ...
    def writable_changed(self, key: str) -> None: ...

class SettingsBackendClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SettingsBackendClass()
    """

    parent_class: GObject.ObjectClass = ...
    read: typing.Callable[
        [SettingsBackend, str, GLib.VariantType, bool], GLib.Variant
    ] = ...
    get_writable: typing.Callable[[SettingsBackend, str], bool] = ...
    write: typing.Callable[[SettingsBackend, str, GLib.Variant, None], bool] = ...
    write_tree: typing.Callable[[SettingsBackend, GLib.Tree, None], bool] = ...
    reset: typing.Callable[[SettingsBackend, str, None], None] = ...
    subscribe: typing.Callable[[SettingsBackend, str], None] = ...
    unsubscribe: typing.Callable[[SettingsBackend, str], None] = ...
    sync: typing.Callable[[SettingsBackend], None] = ...
    get_permission: None = ...
    read_user_value: typing.Callable[
        [SettingsBackend, str, GLib.VariantType], GLib.Variant
    ] = ...
    padding: list[None] = ...

class SettingsBackendPrivate(GObject.GPointer): ...

class SettingsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SettingsClass()
    """

    parent_class: GObject.ObjectClass = ...
    writable_changed: typing.Callable[[Settings, str], None] = ...
    changed: typing.Callable[[Settings, str], None] = ...
    writable_change_event: typing.Callable[[Settings, int], bool] = ...
    change_event: typing.Callable[[Settings, int, int], bool] = ...
    padding: list[None] = ...

class SettingsPrivate(GObject.GPointer): ...

class SettingsSchema(GObject.GBoxed):
    def get_id(self) -> str: ...
    def get_key(self, name: str) -> SettingsSchemaKey: ...
    def get_path(self) -> typing.Optional[str]: ...
    def has_key(self, name: str) -> bool: ...
    def list_children(self) -> list[str]: ...
    def list_keys(self) -> list[str]: ...
    def ref(self) -> SettingsSchema: ...
    def unref(self) -> None: ...

class SettingsSchemaKey(GObject.GBoxed):
    def get_default_value(self) -> GLib.Variant: ...
    def get_description(self) -> typing.Optional[str]: ...
    def get_name(self) -> str: ...
    def get_range(self) -> GLib.Variant: ...
    def get_summary(self) -> typing.Optional[str]: ...
    def get_value_type(self) -> GLib.VariantType: ...
    def range_check(self, value: GLib.Variant) -> bool: ...
    def ref(self) -> SettingsSchemaKey: ...
    def unref(self) -> None: ...

class SettingsSchemaSource(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_from_directory(directory:str, parent:Gio.SettingsSchemaSource=None, trusted:bool) -> Gio.SettingsSchemaSource
    """

    @staticmethod
    def get_default() -> typing.Optional[SettingsSchemaSource]: ...
    def list_schemas(self, recursive: bool) -> typing.Tuple[list[str], list[str]]: ...
    def lookup(
        self, schema_id: str, recursive: bool
    ) -> typing.Optional[SettingsSchema]: ...
    @classmethod
    def new_from_directory(
        cls,
        directory: str,
        parent: typing.Optional[SettingsSchemaSource],
        trusted: bool,
    ) -> SettingsSchemaSource: ...
    def ref(self) -> SettingsSchemaSource: ...
    def unref(self) -> None: ...

class SimpleAction(GObject.Object, Action):
    """
    :Constructors:

    ::

        SimpleAction(**properties)
        new(name:str, parameter_type:GLib.VariantType=None) -> Gio.SimpleAction
        new_stateful(name:str, parameter_type:GLib.VariantType=None, state:GLib.Variant) -> Gio.SimpleAction

    Object GSimpleAction

    Signals from GSimpleAction:
      activate (GVariant)
      change-state (GVariant)

    Properties from GSimpleAction:
      name -> gchararray: name
      parameter-type -> GVariantType: parameter-type
      enabled -> gboolean: enabled
      state-type -> GVariantType: state-type
      state -> GVariant: state

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        enabled: bool
        name: str
        parameter_type: GLib.VariantType
        state: GLib.Variant
        state_type: GLib.VariantType

    props: Props = ...
    def __init__(
        self,
        enabled: bool = ...,
        name: str = ...,
        parameter_type: GLib.VariantType = ...,
        state: GLib.Variant = ...,
    ) -> None: ...
    @classmethod
    def new(
        cls, name: str, parameter_type: typing.Optional[GLib.VariantType] = None
    ) -> SimpleAction: ...
    @classmethod
    def new_stateful(
        cls,
        name: str,
        parameter_type: typing.Optional[GLib.VariantType],
        state: GLib.Variant,
    ) -> SimpleAction: ...
    def set_enabled(self, enabled: bool) -> None: ...
    def set_state(self, value: GLib.Variant) -> None: ...
    def set_state_hint(
        self, state_hint: typing.Optional[GLib.Variant] = None
    ) -> None: ...

class SimpleActionGroup(GObject.Object, ActionGroup, ActionMap):
    """
    :Constructors:

    ::

        SimpleActionGroup(**properties)
        new() -> Gio.SimpleActionGroup

    Object GSimpleActionGroup

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: SimpleActionGroupPrivate = ...
    def add_entries(
        self, entries: typing.Sequence[ActionEntry], user_data: None
    ) -> None: ...
    def insert(self, action: Action) -> None: ...
    def lookup(self, action_name: str) -> Action: ...
    @classmethod
    def new(cls) -> SimpleActionGroup: ...
    def remove(self, action_name: str) -> None: ...

class SimpleActionGroupClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SimpleActionGroupClass()
    """

    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class SimpleActionGroupPrivate(GObject.GPointer): ...

class SimpleAsyncResult(GObject.Object, AsyncResult):
    """
    :Constructors:

    ::

        SimpleAsyncResult(**properties)
        new(source_object:GObject.Object=None, callback:Gio.AsyncReadyCallback=None, user_data=None, source_tag=None) -> Gio.SimpleAsyncResult
        new_from_error(source_object:GObject.Object=None, callback:Gio.AsyncReadyCallback=None, user_data=None, error:error) -> Gio.SimpleAsyncResult

    Object GSimpleAsyncResult

    Signals from GObject:
      notify (GParam)
    """

    def complete(self) -> None: ...
    def complete_in_idle(self) -> None: ...
    def get_op_res_gboolean(self) -> bool: ...
    def get_op_res_gssize(self) -> int: ...
    @staticmethod
    def is_valid(
        result: AsyncResult, source: typing.Optional[GObject.Object], source_tag: None
    ) -> bool: ...
    @classmethod
    def new(
        cls,
        source_object: typing.Optional[GObject.Object],
        callback: typing.Optional[typing.Callable[..., None]],
        source_tag: None,
        *user_data: typing.Any,
    ) -> SimpleAsyncResult: ...
    @classmethod
    def new_from_error(
        cls,
        source_object: typing.Optional[GObject.Object],
        callback: typing.Optional[typing.Callable[..., None]],
        error: GLib.Error,
        *user_data: typing.Any,
    ) -> SimpleAsyncResult: ...
    def propagate_error(self) -> bool: ...
    def set_check_cancellable(
        self, check_cancellable: typing.Optional[Cancellable] = None
    ) -> None: ...
    def set_from_error(self, error: GLib.Error) -> None: ...
    def set_handle_cancellation(self, handle_cancellation: bool) -> None: ...
    def set_op_res_gboolean(self, op_res: bool) -> None: ...
    def set_op_res_gssize(self, op_res: int) -> None: ...

class SimpleAsyncResultClass(GObject.GPointer): ...

class SimpleIOStream(IOStream):
    """
    :Constructors:

    ::

        SimpleIOStream(**properties)
        new(input_stream:Gio.InputStream, output_stream:Gio.OutputStream) -> Gio.IOStream

    Object GSimpleIOStream

    Properties from GSimpleIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        input_stream: InputStream
        output_stream: OutputStream
        closed: bool

    props: Props = ...
    def __init__(
        self, input_stream: InputStream = ..., output_stream: OutputStream = ...
    ) -> None: ...
    @classmethod
    def new(
        cls, input_stream: InputStream, output_stream: OutputStream
    ) -> SimpleIOStream: ...

class SimplePermission(Permission):
    """
    :Constructors:

    ::

        SimplePermission(**properties)
        new(allowed:bool) -> Gio.Permission

    Object GSimplePermission

    Properties from GPermission:
      allowed -> gboolean: allowed
      can-acquire -> gboolean: can-acquire
      can-release -> gboolean: can-release

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        allowed: bool
        can_acquire: bool
        can_release: bool

    props: Props = ...
    @classmethod
    def new(cls, allowed: bool) -> SimplePermission: ...

class SimpleProxyResolver(GObject.Object, ProxyResolver):
    """
    :Constructors:

    ::

        SimpleProxyResolver(**properties)

    Object GSimpleProxyResolver

    Properties from GSimpleProxyResolver:
      default-proxy -> gchararray: default-proxy
      ignore-hosts -> GStrv: ignore-hosts

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        default_proxy: typing.Optional[str]
        ignore_hosts: list[str]

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: SimpleProxyResolverPrivate = ...
    def __init__(
        self,
        default_proxy: typing.Optional[str] = ...,
        ignore_hosts: typing.Sequence[str] = ...,
    ) -> None: ...
    @staticmethod
    def new(
        default_proxy: typing.Optional[str] = None,
        ignore_hosts: typing.Optional[typing.Sequence[str]] = None,
    ) -> ProxyResolver: ...
    def set_default_proxy(self, default_proxy: typing.Optional[str] = None) -> None: ...
    def set_ignore_hosts(self, ignore_hosts: typing.Sequence[str]) -> None: ...
    def set_uri_proxy(self, uri_scheme: str, proxy: str) -> None: ...

class SimpleProxyResolverClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SimpleProxyResolverClass()
    """

    parent_class: GObject.ObjectClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class SimpleProxyResolverPrivate(GObject.GPointer): ...

class Socket(GObject.Object, DatagramBased, Initable):
    """
    :Constructors:

    ::

        Socket(**properties)
        new(family:Gio.SocketFamily, type:Gio.SocketType, protocol:Gio.SocketProtocol) -> Gio.Socket
        new_from_fd(fd:int) -> Gio.Socket

    Object GSocket

    Properties from GSocket:
      family -> GSocketFamily: family
      type -> GSocketType: type
      protocol -> GSocketProtocol: protocol
      fd -> gint: fd
      blocking -> gboolean: blocking
      listen-backlog -> gint: listen-backlog
      keepalive -> gboolean: keepalive
      local-address -> GSocketAddress: local-address
      remote-address -> GSocketAddress: remote-address
      timeout -> guint: timeout
      ttl -> guint: ttl
      broadcast -> gboolean: broadcast
      multicast-loopback -> gboolean: multicast-loopback
      multicast-ttl -> guint: multicast-ttl

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        blocking: bool
        broadcast: bool
        family: SocketFamily
        fd: int
        keepalive: bool
        listen_backlog: int
        local_address: SocketAddress
        multicast_loopback: bool
        multicast_ttl: int
        protocol: SocketProtocol
        remote_address: SocketAddress
        timeout: int
        ttl: int
        type: SocketType

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: SocketPrivate = ...
    def __init__(
        self,
        blocking: bool = ...,
        broadcast: bool = ...,
        family: SocketFamily = ...,
        fd: int = ...,
        keepalive: bool = ...,
        listen_backlog: int = ...,
        multicast_loopback: bool = ...,
        multicast_ttl: int = ...,
        protocol: SocketProtocol = ...,
        timeout: int = ...,
        ttl: int = ...,
        type: SocketType = ...,
    ) -> None: ...
    def accept(self, cancellable: typing.Optional[Cancellable] = None) -> Socket: ...
    def bind(self, address: SocketAddress, allow_reuse: bool) -> bool: ...
    def check_connect_result(self) -> bool: ...
    def close(self) -> bool: ...
    def condition_check(self, condition: GLib.IOCondition) -> GLib.IOCondition: ...
    def condition_timed_wait(
        self,
        condition: GLib.IOCondition,
        timeout_us: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def condition_wait(
        self,
        condition: GLib.IOCondition,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def connect(
        self, address: SocketAddress, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def connection_factory_create_connection(self) -> SocketConnection: ...
    def get_available_bytes(self) -> int: ...
    def get_blocking(self) -> bool: ...
    def get_broadcast(self) -> bool: ...
    def get_credentials(self) -> Credentials: ...
    def get_family(self) -> SocketFamily: ...
    def get_fd(self) -> int: ...
    def get_keepalive(self) -> bool: ...
    def get_listen_backlog(self) -> int: ...
    def get_local_address(self) -> SocketAddress: ...
    def get_multicast_loopback(self) -> bool: ...
    def get_multicast_ttl(self) -> int: ...
    def get_option(self, level: int, optname: int) -> typing.Tuple[bool, int]: ...
    def get_protocol(self) -> SocketProtocol: ...
    def get_remote_address(self) -> SocketAddress: ...
    def get_socket_type(self) -> SocketType: ...
    def get_timeout(self) -> int: ...
    def get_ttl(self) -> int: ...
    def is_closed(self) -> bool: ...
    def is_connected(self) -> bool: ...
    def join_multicast_group(
        self,
        group: InetAddress,
        source_specific: bool,
        iface: typing.Optional[str] = None,
    ) -> bool: ...
    def join_multicast_group_ssm(
        self,
        group: InetAddress,
        source_specific: typing.Optional[InetAddress] = None,
        iface: typing.Optional[str] = None,
    ) -> bool: ...
    def leave_multicast_group(
        self,
        group: InetAddress,
        source_specific: bool,
        iface: typing.Optional[str] = None,
    ) -> bool: ...
    def leave_multicast_group_ssm(
        self,
        group: InetAddress,
        source_specific: typing.Optional[InetAddress] = None,
        iface: typing.Optional[str] = None,
    ) -> bool: ...
    def listen(self) -> bool: ...
    @classmethod
    def new(
        cls, family: SocketFamily, type: SocketType, protocol: SocketProtocol
    ) -> Socket: ...
    @classmethod
    def new_from_fd(cls, fd: int) -> Socket: ...
    def receive(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[int, bytes]: ...
    def receive_bytes(
        self,
        size: int,
        timeout_us: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> GLib.Bytes: ...
    def receive_bytes_from(
        self,
        size: int,
        timeout_us: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[GLib.Bytes, SocketAddress]: ...
    def receive_from(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[int, SocketAddress, bytes]: ...
    def receive_message(
        self,
        vectors: typing.Sequence[InputVector],
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[int, SocketAddress, list[SocketControlMessage], int]: ...
    def receive_messages(
        self,
        messages: typing.Sequence[InputMessage],
        flags: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def receive_with_blocking(
        self, blocking: bool, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[int, bytes]: ...
    def send(
        self,
        buffer: typing.Sequence[int],
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def send_message(
        self,
        address: typing.Optional[SocketAddress],
        vectors: typing.Sequence[OutputVector],
        messages: typing.Optional[typing.Sequence[SocketControlMessage]],
        flags: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def send_message_with_timeout(
        self,
        address: typing.Optional[SocketAddress],
        vectors: typing.Sequence[OutputVector],
        messages: typing.Optional[typing.Sequence[SocketControlMessage]],
        flags: int,
        timeout_us: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[PollableReturn, int]: ...
    def send_messages(
        self,
        messages: typing.Sequence[OutputMessage],
        flags: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def send_to(
        self,
        address: typing.Optional[SocketAddress],
        buffer: typing.Sequence[int],
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def send_with_blocking(
        self,
        buffer: typing.Sequence[int],
        blocking: bool,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> int: ...
    def set_blocking(self, blocking: bool) -> None: ...
    def set_broadcast(self, broadcast: bool) -> None: ...
    def set_keepalive(self, keepalive: bool) -> None: ...
    def set_listen_backlog(self, backlog: int) -> None: ...
    def set_multicast_loopback(self, loopback: bool) -> None: ...
    def set_multicast_ttl(self, ttl: int) -> None: ...
    def set_option(self, level: int, optname: int, value: int) -> bool: ...
    def set_timeout(self, timeout: int) -> None: ...
    def set_ttl(self, ttl: int) -> None: ...
    def shutdown(self, shutdown_read: bool, shutdown_write: bool) -> bool: ...
    def speaks_ipv4(self) -> bool: ...

class SocketAddress(GObject.Object, SocketConnectable):
    """
    :Constructors:

    ::

        SocketAddress(**properties)
        new_from_native(native, len:int) -> Gio.SocketAddress

    Object GSocketAddress

    Properties from GSocketAddress:
      family -> GSocketFamily: family

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        family: SocketFamily

    props: Props = ...
    parent_instance: GObject.Object = ...
    def do_get_family(self) -> SocketFamily: ...
    def do_get_native_size(self) -> int: ...
    def do_to_native(self, dest: None, destlen: int) -> bool: ...
    def get_family(self) -> SocketFamily: ...
    def get_native_size(self) -> int: ...
    @classmethod
    def new_from_native(cls, native: None, len: int) -> SocketAddress: ...
    def to_native(self, dest: None, destlen: int) -> bool: ...

class SocketAddressClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SocketAddressClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_family: typing.Callable[[SocketAddress], SocketFamily] = ...
    get_native_size: typing.Callable[[SocketAddress], int] = ...
    to_native: typing.Callable[[SocketAddress, None, int], bool] = ...

class SocketAddressEnumerator(GObject.Object):
    """
    :Constructors:

    ::

        SocketAddressEnumerator(**properties)

    Object GSocketAddressEnumerator

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def do_next(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Optional[SocketAddress]: ...
    def do_next_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_next_finish(self, result: AsyncResult) -> typing.Optional[SocketAddress]: ...
    def next(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Optional[SocketAddress]: ...
    def next_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def next_finish(self, result: AsyncResult) -> typing.Optional[SocketAddress]: ...

class SocketAddressEnumeratorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SocketAddressEnumeratorClass()
    """

    parent_class: GObject.ObjectClass = ...
    next: typing.Callable[
        [SocketAddressEnumerator, typing.Optional[Cancellable]],
        typing.Optional[SocketAddress],
    ] = ...
    next_async: typing.Callable[..., None] = ...
    next_finish: typing.Callable[
        [SocketAddressEnumerator, AsyncResult], typing.Optional[SocketAddress]
    ] = ...

class SocketClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SocketClass()
    """

    parent_class: GObject.ObjectClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...
    _g_reserved6: None = ...
    _g_reserved7: None = ...
    _g_reserved8: None = ...
    _g_reserved9: None = ...
    _g_reserved10: None = ...

class SocketClient(GObject.Object):
    """
    :Constructors:

    ::

        SocketClient(**properties)
        new() -> Gio.SocketClient

    Object GSocketClient

    Signals from GSocketClient:
      event (GSocketClientEvent, GSocketConnectable, GIOStream)

    Properties from GSocketClient:
      family -> GSocketFamily: family
      type -> GSocketType: type
      protocol -> GSocketProtocol: protocol
      local-address -> GSocketAddress: local-address
      timeout -> guint: timeout
      enable-proxy -> gboolean: enable-proxy
      tls -> gboolean: tls
      tls-validation-flags -> GTlsCertificateFlags: tls-validation-flags
      proxy-resolver -> GProxyResolver: proxy-resolver

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        enable_proxy: bool
        family: SocketFamily
        local_address: typing.Optional[SocketAddress]
        protocol: SocketProtocol
        proxy_resolver: ProxyResolver
        timeout: int
        tls: bool
        tls_validation_flags: TlsCertificateFlags
        type: SocketType

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: SocketClientPrivate = ...
    def __init__(
        self,
        enable_proxy: bool = ...,
        family: SocketFamily = ...,
        local_address: typing.Optional[SocketAddress] = ...,
        protocol: SocketProtocol = ...,
        proxy_resolver: typing.Optional[ProxyResolver] = ...,
        timeout: int = ...,
        tls: bool = ...,
        tls_validation_flags: TlsCertificateFlags = ...,
        type: SocketType = ...,
    ) -> None: ...
    def add_application_proxy(self, protocol: str) -> None: ...
    def connect(
        self,
        connectable: SocketConnectable,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> SocketConnection: ...
    def connect_async(
        self,
        connectable: SocketConnectable,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def connect_finish(self, result: AsyncResult) -> SocketConnection: ...
    def connect_to_host(
        self,
        host_and_port: str,
        default_port: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> SocketConnection: ...
    def connect_to_host_async(
        self,
        host_and_port: str,
        default_port: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def connect_to_host_finish(self, result: AsyncResult) -> SocketConnection: ...
    def connect_to_service(
        self,
        domain: str,
        service: str,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> SocketConnection: ...
    def connect_to_service_async(
        self,
        domain: str,
        service: str,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def connect_to_service_finish(self, result: AsyncResult) -> SocketConnection: ...
    def connect_to_uri(
        self,
        uri: str,
        default_port: int,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> SocketConnection: ...
    def connect_to_uri_async(
        self,
        uri: str,
        default_port: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def connect_to_uri_finish(self, result: AsyncResult) -> SocketConnection: ...
    def do_event(
        self,
        event: SocketClientEvent,
        connectable: SocketConnectable,
        connection: IOStream,
    ) -> None: ...
    def get_enable_proxy(self) -> bool: ...
    def get_family(self) -> SocketFamily: ...
    def get_local_address(self) -> typing.Optional[SocketAddress]: ...
    def get_protocol(self) -> SocketProtocol: ...
    def get_proxy_resolver(self) -> ProxyResolver: ...
    def get_socket_type(self) -> SocketType: ...
    def get_timeout(self) -> int: ...
    def get_tls(self) -> bool: ...
    def get_tls_validation_flags(self) -> TlsCertificateFlags: ...
    @classmethod
    def new(cls) -> SocketClient: ...
    def set_enable_proxy(self, enable: bool) -> None: ...
    def set_family(self, family: SocketFamily) -> None: ...
    def set_local_address(
        self, address: typing.Optional[SocketAddress] = None
    ) -> None: ...
    def set_protocol(self, protocol: SocketProtocol) -> None: ...
    def set_proxy_resolver(
        self, proxy_resolver: typing.Optional[ProxyResolver] = None
    ) -> None: ...
    def set_socket_type(self, type: SocketType) -> None: ...
    def set_timeout(self, timeout: int) -> None: ...
    def set_tls(self, tls: bool) -> None: ...
    def set_tls_validation_flags(self, flags: TlsCertificateFlags) -> None: ...

class SocketClientClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SocketClientClass()
    """

    parent_class: GObject.ObjectClass = ...
    event: typing.Callable[
        [SocketClient, SocketClientEvent, SocketConnectable, IOStream], None
    ] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...

class SocketClientPrivate(GObject.GPointer): ...

class SocketConnectable(GObject.GInterface):
    """
    Interface GSocketConnectable

    Signals from GObject:
      notify (GParam)
    """

    def enumerate(self) -> SocketAddressEnumerator: ...
    def proxy_enumerate(self) -> SocketAddressEnumerator: ...
    def to_string(self) -> str: ...

class SocketConnectableIface(GObject.GPointer):
    """
    :Constructors:

    ::

        SocketConnectableIface()
    """

    g_iface: GObject.TypeInterface = ...
    enumerate: typing.Callable[[SocketConnectable], SocketAddressEnumerator] = ...
    proxy_enumerate: typing.Callable[[SocketConnectable], SocketAddressEnumerator] = ...
    to_string: typing.Callable[[SocketConnectable], str] = ...

class SocketConnection(IOStream):
    """
    :Constructors:

    ::

        SocketConnection(**properties)

    Object GSocketConnection

    Properties from GSocketConnection:
      socket -> GSocket: socket

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        socket: Socket
        closed: bool
        input_stream: InputStream
        output_stream: OutputStream

    props: Props = ...
    parent_instance: IOStream = ...
    priv: SocketConnectionPrivate = ...
    def __init__(self, socket: Socket = ...) -> None: ...
    def connect(
        self, address: SocketAddress, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def connect_async(
        self,
        address: SocketAddress,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def connect_finish(self, result: AsyncResult) -> bool: ...
    @staticmethod
    def factory_lookup_type(
        family: SocketFamily, type: SocketType, protocol_id: int
    ) -> typing.Type[typing.Any]: ...
    @staticmethod
    def factory_register_type(
        g_type: typing.Type[typing.Any],
        family: SocketFamily,
        type: SocketType,
        protocol: int,
    ) -> None: ...
    def get_local_address(self) -> SocketAddress: ...
    def get_remote_address(self) -> SocketAddress: ...
    def get_socket(self) -> Socket: ...
    def is_connected(self) -> bool: ...

class SocketConnectionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SocketConnectionClass()
    """

    parent_class: IOStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...
    _g_reserved6: None = ...

class SocketConnectionPrivate(GObject.GPointer): ...

class SocketControlMessage(GObject.Object):
    """
    :Constructors:

    ::

        SocketControlMessage(**properties)

    Object GSocketControlMessage

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: SocketControlMessagePrivate = ...
    @staticmethod
    def deserialize(
        level: int, type: int, data: typing.Sequence[int]
    ) -> typing.Optional[SocketControlMessage]: ...
    def do_get_level(self) -> int: ...
    def do_get_size(self) -> int: ...
    def do_get_type(self) -> int: ...
    def do_serialize(self, data: None) -> None: ...
    def get_level(self) -> int: ...
    def get_msg_type(self) -> int: ...
    def get_size(self) -> int: ...
    def serialize(self, data: None) -> None: ...

class SocketControlMessageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SocketControlMessageClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_size: typing.Callable[[SocketControlMessage], int] = ...
    get_level: typing.Callable[[SocketControlMessage], int] = ...
    get_type: typing.Callable[[SocketControlMessage], int] = ...
    serialize: typing.Callable[[SocketControlMessage, None], None] = ...
    deserialize: None = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class SocketControlMessagePrivate(GObject.GPointer): ...

class SocketListener(GObject.Object):
    """
    :Constructors:

    ::

        SocketListener(**properties)
        new() -> Gio.SocketListener

    Object GSocketListener

    Signals from GSocketListener:
      event (GSocketListenerEvent, GSocket)

    Properties from GSocketListener:
      listen-backlog -> gint: listen-backlog

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        listen_backlog: int

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: SocketListenerPrivate = ...
    def __init__(self, listen_backlog: int = ...) -> None: ...
    def accept(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[SocketConnection, GObject.Object]: ...
    def accept_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def accept_finish(
        self, result: AsyncResult
    ) -> typing.Tuple[SocketConnection, GObject.Object]: ...
    def accept_socket(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> typing.Tuple[Socket, GObject.Object]: ...
    def accept_socket_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def accept_socket_finish(
        self, result: AsyncResult
    ) -> typing.Tuple[Socket, GObject.Object]: ...
    def add_address(
        self,
        address: SocketAddress,
        type: SocketType,
        protocol: SocketProtocol,
        source_object: typing.Optional[GObject.Object] = None,
    ) -> typing.Tuple[bool, SocketAddress]: ...
    def add_any_inet_port(
        self, source_object: typing.Optional[GObject.Object] = None
    ) -> int: ...
    def add_inet_port(
        self, port: int, source_object: typing.Optional[GObject.Object] = None
    ) -> bool: ...
    def add_socket(
        self, socket: Socket, source_object: typing.Optional[GObject.Object] = None
    ) -> bool: ...
    def close(self) -> None: ...
    def do_changed(self) -> None: ...
    def do_event(self, event: SocketListenerEvent, socket: Socket) -> None: ...
    @classmethod
    def new(cls) -> SocketListener: ...
    def set_backlog(self, listen_backlog: int) -> None: ...

class SocketListenerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SocketListenerClass()
    """

    parent_class: GObject.ObjectClass = ...
    changed: typing.Callable[[SocketListener], None] = ...
    event: typing.Callable[[SocketListener, SocketListenerEvent, Socket], None] = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...
    _g_reserved6: None = ...

class SocketListenerPrivate(GObject.GPointer): ...
class SocketPrivate(GObject.GPointer): ...

class SocketService(SocketListener):
    """
    :Constructors:

    ::

        SocketService(**properties)
        new() -> Gio.SocketService

    Object GSocketService

    Signals from GSocketService:
      incoming (GSocketConnection, GObject) -> gboolean

    Properties from GSocketService:
      active -> gboolean: active

    Signals from GSocketListener:
      event (GSocketListenerEvent, GSocket)

    Properties from GSocketListener:
      listen-backlog -> gint: listen-backlog

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        active: bool
        listen_backlog: int

    props: Props = ...
    parent_instance: SocketListener = ...
    priv: SocketServicePrivate = ...
    def __init__(self, active: bool = ..., listen_backlog: int = ...) -> None: ...
    def do_incoming(
        self, connection: SocketConnection, source_object: GObject.Object
    ) -> bool: ...
    def is_active(self) -> bool: ...
    @classmethod
    def new(cls) -> SocketService: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class SocketServiceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SocketServiceClass()
    """

    parent_class: SocketListenerClass = ...
    incoming: typing.Callable[
        [SocketService, SocketConnection, GObject.Object], bool
    ] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...
    _g_reserved6: None = ...

class SocketServicePrivate(GObject.GPointer): ...

class SrvTarget(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(hostname:str, port:int, priority:int, weight:int) -> Gio.SrvTarget
    """

    def copy(self) -> SrvTarget: ...
    def free(self) -> None: ...
    def get_hostname(self) -> str: ...
    def get_port(self) -> int: ...
    def get_priority(self) -> int: ...
    def get_weight(self) -> int: ...
    @classmethod
    def new(cls, hostname: str, port: int, priority: int, weight: int) -> SrvTarget: ...

class StaticResource(GObject.GPointer):
    """
    :Constructors:

    ::

        StaticResource()
    """

    data: int = ...
    data_len: int = ...
    resource: Resource = ...
    next: StaticResource = ...
    padding: None = ...
    def fini(self) -> None: ...
    def get_resource(self) -> Resource: ...
    def init(self) -> None: ...

class Subprocess(GObject.Object, Initable):
    """
    :Constructors:

    ::

        Subprocess(**properties)
        new(argv:list, flags:Gio.SubprocessFlags) -> Gio.Subprocess

    Object GSubprocess

    Properties from GSubprocess:
      flags -> GSubprocessFlags: flags
      argv -> GStrv: argv

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        argv: list[str]
        flags: SubprocessFlags

    props: Props = ...
    def __init__(
        self, argv: typing.Sequence[str] = ..., flags: SubprocessFlags = ...
    ) -> None: ...
    def communicate(
        self,
        stdin_buf: typing.Optional[GLib.Bytes] = None,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[bool, GLib.Bytes, GLib.Bytes]: ...
    def communicate_async(
        self,
        stdin_buf: typing.Optional[GLib.Bytes] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def communicate_finish(
        self, result: AsyncResult
    ) -> typing.Tuple[bool, GLib.Bytes, GLib.Bytes]: ...
    def communicate_utf8(
        self,
        stdin_buf: typing.Optional[str] = None,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Tuple[bool, str, str]: ...
    def communicate_utf8_async(
        self,
        stdin_buf: typing.Optional[str] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def communicate_utf8_finish(
        self, result: AsyncResult
    ) -> typing.Tuple[bool, str, str]: ...
    def force_exit(self) -> None: ...
    def get_exit_status(self) -> int: ...
    def get_identifier(self) -> typing.Optional[str]: ...
    def get_if_exited(self) -> bool: ...
    def get_if_signaled(self) -> bool: ...
    def get_status(self) -> int: ...
    def get_stderr_pipe(self) -> typing.Optional[InputStream]: ...
    def get_stdin_pipe(self) -> typing.Optional[OutputStream]: ...
    def get_stdout_pipe(self) -> typing.Optional[InputStream]: ...
    def get_successful(self) -> bool: ...
    def get_term_sig(self) -> int: ...
    @classmethod
    def new(cls, argv: typing.Sequence[str], flags: SubprocessFlags) -> Subprocess: ...
    def send_signal(self, signal_num: int) -> None: ...
    def wait(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def wait_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def wait_check(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def wait_check_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def wait_check_finish(self, result: AsyncResult) -> bool: ...
    def wait_finish(self, result: AsyncResult) -> bool: ...

class SubprocessLauncher(GObject.Object):
    """
    :Constructors:

    ::

        SubprocessLauncher(**properties)
        new(flags:Gio.SubprocessFlags) -> Gio.SubprocessLauncher

    Object GSubprocessLauncher

    Properties from GSubprocessLauncher:
      flags -> GSubprocessFlags: flags

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        flags: SubprocessFlags

    props: Props = ...
    def __init__(self, flags: SubprocessFlags = ...) -> None: ...
    def close(self) -> None: ...
    def getenv(self, variable: str) -> typing.Optional[str]: ...
    @classmethod
    def new(cls, flags: SubprocessFlags) -> SubprocessLauncher: ...
    def set_cwd(self, cwd: str) -> None: ...
    def set_environ(self, env: typing.Sequence[str]) -> None: ...
    def set_flags(self, flags: SubprocessFlags) -> None: ...
    def set_stderr_file_path(self, path: typing.Optional[str] = None) -> None: ...
    def set_stdin_file_path(self, path: typing.Optional[str] = None) -> None: ...
    def set_stdout_file_path(self, path: typing.Optional[str] = None) -> None: ...
    def setenv(self, variable: str, value: str, overwrite: bool) -> None: ...
    def spawnv(self, argv: typing.Sequence[str]) -> Subprocess: ...
    def take_fd(self, source_fd: int, target_fd: int) -> None: ...
    def take_stderr_fd(self, fd: int) -> None: ...
    def take_stdin_fd(self, fd: int) -> None: ...
    def take_stdout_fd(self, fd: int) -> None: ...
    def unsetenv(self, variable: str) -> None: ...

class Task(GObject.Object, AsyncResult):
    """
    :Constructors:

    ::

        Task(**properties)
        new(source_object:GObject.Object=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, callback_data=None) -> Gio.Task

    Object GTask

    Properties from GTask:
      completed -> gboolean: completed

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        completed: bool

    props: Props = ...
    def get_cancellable(self) -> typing.Optional[Cancellable]: ...
    def get_check_cancellable(self) -> bool: ...
    def get_completed(self) -> bool: ...
    def get_context(self) -> GLib.MainContext: ...
    def get_name(self) -> typing.Optional[str]: ...
    def get_priority(self) -> int: ...
    def get_return_on_cancel(self) -> bool: ...
    def get_source_object(self) -> typing.Optional[GObject.Object]: ...
    def get_source_tag(self) -> None: ...
    def get_task_data(self) -> None: ...
    def had_error(self) -> bool: ...
    @staticmethod
    def is_valid(
        result: AsyncResult, source_object: typing.Optional[GObject.Object] = None
    ) -> bool: ...
    @classmethod
    def new(
        cls,
        source_object: typing.Optional[GObject.Object] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *callback_data: typing.Any,
    ) -> Task: ...
    def propagate_boolean(self) -> bool: ...
    def propagate_int(self) -> int: ...
    def propagate_pointer(self) -> None: ...
    def propagate_value(self) -> typing.Tuple[bool, typing.Any]: ...
    @staticmethod
    def report_error(
        source_object: typing.Optional[GObject.Object],
        callback: typing.Optional[typing.Callable[..., None]],
        source_tag: None,
        error: GLib.Error,
        *callback_data: typing.Any,
    ) -> None: ...
    def return_boolean(self, result: bool) -> None: ...
    def return_error(self, error: GLib.Error) -> None: ...
    def return_error_if_cancelled(self) -> bool: ...
    def return_int(self, result: int) -> None: ...
    def return_new_error_literal(
        self, domain: int, code: int, message: str
    ) -> None: ...
    def return_pointer(
        self,
        result: None,
        result_destroy: typing.Optional[typing.Callable[[None], None]] = None,
    ) -> None: ...
    def return_value(self, result: typing.Optional[typing.Any] = None) -> None: ...
    def run_in_thread(
        self,
        task_func: typing.Callable[
            [Task, GObject.Object, None, typing.Optional[Cancellable]], None
        ],
    ) -> None: ...
    def run_in_thread_sync(
        self,
        task_func: typing.Callable[
            [Task, GObject.Object, None, typing.Optional[Cancellable]], None
        ],
    ) -> None: ...
    def set_check_cancellable(self, check_cancellable: bool) -> None: ...
    def set_name(self, name: typing.Optional[str] = None) -> None: ...
    def set_priority(self, priority: int) -> None: ...
    def set_return_on_cancel(self, return_on_cancel: bool) -> bool: ...
    def set_source_tag(self, source_tag: None) -> None: ...
    def set_static_name(self, name: typing.Optional[str] = None) -> None: ...
    def set_task_data(
        self,
        task_data: None,
        task_data_destroy: typing.Optional[typing.Callable[[None], None]] = None,
    ) -> None: ...

class TaskClass(GObject.GPointer): ...

class TcpConnection(SocketConnection):
    """
    :Constructors:

    ::

        TcpConnection(**properties)

    Object GTcpConnection

    Properties from GTcpConnection:
      graceful-disconnect -> gboolean: graceful-disconnect

    Properties from GSocketConnection:
      socket -> GSocket: socket

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        graceful_disconnect: bool
        socket: Socket
        closed: bool
        input_stream: InputStream
        output_stream: OutputStream

    props: Props = ...
    parent_instance: SocketConnection = ...
    priv: TcpConnectionPrivate = ...
    def __init__(
        self, graceful_disconnect: bool = ..., socket: Socket = ...
    ) -> None: ...
    def get_graceful_disconnect(self) -> bool: ...
    def set_graceful_disconnect(self, graceful_disconnect: bool) -> None: ...

class TcpConnectionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TcpConnectionClass()
    """

    parent_class: SocketConnectionClass = ...

class TcpConnectionPrivate(GObject.GPointer): ...

class TcpWrapperConnection(TcpConnection):
    """
    :Constructors:

    ::

        TcpWrapperConnection(**properties)
        new(base_io_stream:Gio.IOStream, socket:Gio.Socket) -> Gio.SocketConnection

    Object GTcpWrapperConnection

    Properties from GTcpWrapperConnection:
      base-io-stream -> GIOStream: base-io-stream

    Properties from GTcpConnection:
      graceful-disconnect -> gboolean: graceful-disconnect

    Properties from GSocketConnection:
      socket -> GSocket: socket

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        base_io_stream: IOStream
        graceful_disconnect: bool
        socket: Socket
        closed: bool
        input_stream: InputStream
        output_stream: OutputStream

    props: Props = ...
    parent_instance: TcpConnection = ...
    priv: TcpWrapperConnectionPrivate = ...
    def __init__(
        self,
        base_io_stream: IOStream = ...,
        graceful_disconnect: bool = ...,
        socket: Socket = ...,
    ) -> None: ...
    def get_base_io_stream(self) -> IOStream: ...
    @classmethod
    def new(cls, base_io_stream: IOStream, socket: Socket) -> TcpWrapperConnection: ...

class TcpWrapperConnectionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TcpWrapperConnectionClass()
    """

    parent_class: TcpConnectionClass = ...

class TcpWrapperConnectionPrivate(GObject.GPointer): ...

class TestDBus(GObject.Object):
    """
    :Constructors:

    ::

        TestDBus(**properties)
        new(flags:Gio.TestDBusFlags) -> Gio.TestDBus

    Object GTestDBus

    Properties from GTestDBus:
      flags -> GTestDBusFlags: flags

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        flags: TestDBusFlags

    props: Props = ...
    def __init__(self, flags: TestDBusFlags = ...) -> None: ...
    def add_service_dir(self, path: str) -> None: ...
    def down(self) -> None: ...
    def get_bus_address(self) -> typing.Optional[str]: ...
    def get_flags(self) -> TestDBusFlags: ...
    @classmethod
    def new(cls, flags: TestDBusFlags) -> TestDBus: ...
    def stop(self) -> None: ...
    @staticmethod
    def unset() -> None: ...
    def up(self) -> None: ...

class ThemedIcon(GObject.Object, Icon):
    """
    :Constructors:

    ::

        ThemedIcon(**properties)
        new(iconname:str) -> Gio.ThemedIcon
        new_from_names(iconnames:list) -> Gio.ThemedIcon
        new_with_default_fallbacks(iconname:str) -> Gio.ThemedIcon

    Object GThemedIcon

    Properties from GThemedIcon:
      name -> gchararray: name
      names -> GStrv: names
      use-default-fallbacks -> gboolean: use-default-fallbacks

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        names: list[str]
        use_default_fallbacks: bool
        name: str

    props: Props = ...
    # override
    def __init__(
        self,
        *,
        name: str = ...,
        names: typing.Sequence[str] = ...,
        use_default_fallbacks: bool = ...,
    ) -> None: ...
    def append_name(self, iconname: str) -> None: ...
    def get_names(self) -> list[str]: ...
    @classmethod
    def new(cls, iconname: str) -> ThemedIcon: ...
    @classmethod
    def new_from_names(cls, iconnames: typing.Sequence[str]) -> ThemedIcon: ...
    @classmethod
    def new_with_default_fallbacks(cls, iconname: str) -> ThemedIcon: ...
    def prepend_name(self, iconname: str) -> None: ...

class ThemedIconClass(GObject.GPointer): ...

class ThreadedResolver(Resolver):
    """
    :Constructors:

    ::

        ThreadedResolver(**properties)

    Object GThreadedResolver

    Signals from GResolver:
      reload ()

    Properties from GResolver:
      timeout -> guint: timeout

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        timeout: int

    props: Props = ...
    def __init__(self, timeout: int = ...) -> None: ...

class ThreadedResolverClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ThreadedResolverClass()
    """

    parent_class: ResolverClass = ...

class ThreadedSocketService(SocketService):
    """
    :Constructors:

    ::

        ThreadedSocketService(**properties)
        new(max_threads:int) -> Gio.SocketService

    Object GThreadedSocketService

    Signals from GThreadedSocketService:
      run (GSocketConnection, GObject) -> gboolean

    Properties from GThreadedSocketService:
      max-threads -> gint: max-threads

    Signals from GSocketService:
      incoming (GSocketConnection, GObject) -> gboolean

    Properties from GSocketService:
      active -> gboolean: active

    Signals from GSocketListener:
      event (GSocketListenerEvent, GSocket)

    Properties from GSocketListener:
      listen-backlog -> gint: listen-backlog

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        max_threads: int
        active: bool
        listen_backlog: int

    props: Props = ...
    parent_instance: SocketService = ...
    priv: ThreadedSocketServicePrivate = ...
    def __init__(
        self, max_threads: int = ..., active: bool = ..., listen_backlog: int = ...
    ) -> None: ...
    def do_run(
        self, connection: SocketConnection, source_object: GObject.Object
    ) -> bool: ...
    @classmethod
    def new(cls, max_threads: int) -> ThreadedSocketService: ...

class ThreadedSocketServiceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ThreadedSocketServiceClass()
    """

    parent_class: SocketServiceClass = ...
    run: typing.Callable[
        [ThreadedSocketService, SocketConnection, GObject.Object], bool
    ] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class ThreadedSocketServicePrivate(GObject.GPointer): ...

class TlsBackend(GObject.GInterface):
    """
    Interface GTlsBackend

    Signals from GObject:
      notify (GParam)
    """

    def get_certificate_type(self) -> typing.Type[typing.Any]: ...
    def get_client_connection_type(self) -> typing.Type[typing.Any]: ...
    @staticmethod
    def get_default() -> TlsBackend: ...
    def get_default_database(self) -> TlsDatabase: ...
    def get_dtls_client_connection_type(self) -> typing.Type[typing.Any]: ...
    def get_dtls_server_connection_type(self) -> typing.Type[typing.Any]: ...
    def get_file_database_type(self) -> typing.Type[typing.Any]: ...
    def get_server_connection_type(self) -> typing.Type[typing.Any]: ...
    def set_default_database(
        self, database: typing.Optional[TlsDatabase] = None
    ) -> None: ...
    def supports_dtls(self) -> bool: ...
    def supports_tls(self) -> bool: ...

class TlsBackendInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        TlsBackendInterface()
    """

    g_iface: GObject.TypeInterface = ...
    supports_tls: typing.Callable[[TlsBackend], bool] = ...
    get_certificate_type: typing.Callable[[], typing.Type[typing.Any]] = ...
    get_client_connection_type: typing.Callable[[], typing.Type[typing.Any]] = ...
    get_server_connection_type: typing.Callable[[], typing.Type[typing.Any]] = ...
    get_file_database_type: typing.Callable[[], typing.Type[typing.Any]] = ...
    get_default_database: typing.Callable[[TlsBackend], TlsDatabase] = ...
    supports_dtls: typing.Callable[[TlsBackend], bool] = ...
    get_dtls_client_connection_type: typing.Callable[[], typing.Type[typing.Any]] = ...
    get_dtls_server_connection_type: typing.Callable[[], typing.Type[typing.Any]] = ...

class TlsCertificate(GObject.Object):
    """
    :Constructors:

    ::

        TlsCertificate(**properties)
        new_from_file(file:str) -> Gio.TlsCertificate
        new_from_file_with_password(file:str, password:str) -> Gio.TlsCertificate
        new_from_files(cert_file:str, key_file:str) -> Gio.TlsCertificate
        new_from_pem(data:str, length:int) -> Gio.TlsCertificate
        new_from_pkcs11_uris(pkcs11_uri:str, private_key_pkcs11_uri:str=None) -> Gio.TlsCertificate
        new_from_pkcs12(data:list, password:str=None) -> Gio.TlsCertificate

    Object GTlsCertificate

    Properties from GTlsCertificate:
      certificate -> GByteArray: certificate
      certificate-pem -> gchararray: certificate-pem
      private-key -> GByteArray: private-key
      private-key-pem -> gchararray: private-key-pem
      issuer -> GTlsCertificate: issuer
      pkcs11-uri -> gchararray: pkcs11-uri
      private-key-pkcs11-uri -> gchararray: private-key-pkcs11-uri
      not-valid-before -> GDateTime: not-valid-before
      not-valid-after -> GDateTime: not-valid-after
      subject-name -> gchararray: subject-name
      issuer-name -> gchararray: issuer-name
      dns-names -> GPtrArray: dns-names
      ip-addresses -> GPtrArray: ip-addresses
      pkcs12-data -> GByteArray: pkcs12-data
      password -> gchararray: password

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        certificate: bytes
        certificate_pem: str
        dns_names: typing.Optional[list[None]]
        ip_addresses: typing.Optional[list[None]]
        issuer: typing.Optional[TlsCertificate]
        issuer_name: typing.Optional[str]
        not_valid_after: typing.Optional[GLib.DateTime]
        not_valid_before: typing.Optional[GLib.DateTime]
        pkcs11_uri: str
        private_key: bytes
        private_key_pem: str
        private_key_pkcs11_uri: str
        subject_name: typing.Optional[str]
        password: str
        pkcs12_data: bytes

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: TlsCertificatePrivate = ...
    def __init__(
        self,
        certificate: typing.Sequence[int] = ...,
        certificate_pem: str = ...,
        issuer: TlsCertificate = ...,
        password: str = ...,
        pkcs11_uri: str = ...,
        pkcs12_data: typing.Sequence[int] = ...,
        private_key: typing.Sequence[int] = ...,
        private_key_pem: str = ...,
        private_key_pkcs11_uri: str = ...,
    ) -> None: ...
    def do_verify(
        self,
        identity: typing.Optional[SocketConnectable] = None,
        trusted_ca: typing.Optional[TlsCertificate] = None,
    ) -> TlsCertificateFlags: ...
    def get_dns_names(self) -> typing.Optional[list[GLib.Bytes]]: ...
    def get_ip_addresses(self) -> typing.Optional[list[InetAddress]]: ...
    def get_issuer(self) -> typing.Optional[TlsCertificate]: ...
    def get_issuer_name(self) -> typing.Optional[str]: ...
    def get_not_valid_after(self) -> typing.Optional[GLib.DateTime]: ...
    def get_not_valid_before(self) -> typing.Optional[GLib.DateTime]: ...
    def get_subject_name(self) -> typing.Optional[str]: ...
    def is_same(self, cert_two: TlsCertificate) -> bool: ...
    @staticmethod
    def list_new_from_file(file: str) -> list[TlsCertificate]: ...
    @classmethod
    def new_from_file(cls, file: str) -> TlsCertificate: ...
    @classmethod
    def new_from_file_with_password(
        cls, file: str, password: str
    ) -> TlsCertificate: ...
    @classmethod
    def new_from_files(cls, cert_file: str, key_file: str) -> TlsCertificate: ...
    @classmethod
    def new_from_pem(cls, data: str, length: int) -> TlsCertificate: ...
    @classmethod
    def new_from_pkcs11_uris(
        cls, pkcs11_uri: str, private_key_pkcs11_uri: typing.Optional[str] = None
    ) -> TlsCertificate: ...
    @classmethod
    def new_from_pkcs12(
        cls, data: typing.Sequence[int], password: typing.Optional[str] = None
    ) -> TlsCertificate: ...
    def verify(
        self,
        identity: typing.Optional[SocketConnectable] = None,
        trusted_ca: typing.Optional[TlsCertificate] = None,
    ) -> TlsCertificateFlags: ...

class TlsCertificateClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TlsCertificateClass()
    """

    parent_class: GObject.ObjectClass = ...
    verify: typing.Callable[
        [
            TlsCertificate,
            typing.Optional[SocketConnectable],
            typing.Optional[TlsCertificate],
        ],
        TlsCertificateFlags,
    ] = ...
    padding: list[None] = ...

class TlsCertificatePrivate(GObject.GPointer): ...

class TlsClientConnection(GObject.GInterface):
    """
    Interface GTlsClientConnection

    Signals from GObject:
      notify (GParam)
    """

    def copy_session_state(self, source: TlsClientConnection) -> None: ...
    def get_accepted_cas(self) -> list[typing.Sequence[int]]: ...
    def get_server_identity(self) -> typing.Optional[SocketConnectable]: ...
    def get_use_ssl3(self) -> bool: ...
    def get_validation_flags(self) -> TlsCertificateFlags: ...
    @staticmethod
    def new(
        base_io_stream: IOStream,
        server_identity: typing.Optional[SocketConnectable] = None,
    ) -> TlsClientConnection: ...
    def set_server_identity(self, identity: SocketConnectable) -> None: ...
    def set_use_ssl3(self, use_ssl3: bool) -> None: ...
    def set_validation_flags(self, flags: TlsCertificateFlags) -> None: ...

class TlsClientConnectionInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        TlsClientConnectionInterface()
    """

    g_iface: GObject.TypeInterface = ...
    copy_session_state: typing.Callable[
        [TlsClientConnection, TlsClientConnection], None
    ] = ...

class TlsConnection(IOStream):
    """
    :Constructors:

    ::

        TlsConnection(**properties)

    Object GTlsConnection

    Signals from GTlsConnection:
      accept-certificate (GTlsCertificate, GTlsCertificateFlags) -> gboolean

    Properties from GTlsConnection:
      base-io-stream -> GIOStream: base-io-stream
      require-close-notify -> gboolean: require-close-notify
      rehandshake-mode -> GTlsRehandshakeMode: rehandshake-mode
      use-system-certdb -> gboolean: use-system-certdb
      database -> GTlsDatabase: database
      interaction -> GTlsInteraction: interaction
      certificate -> GTlsCertificate: certificate
      peer-certificate -> GTlsCertificate: peer-certificate
      peer-certificate-errors -> GTlsCertificateFlags: peer-certificate-errors
      advertised-protocols -> GStrv: advertised-protocols
      negotiated-protocol -> gchararray: negotiated-protocol
      protocol-version -> GTlsProtocolVersion: protocol-version
      ciphersuite-name -> gchararray: ciphersuite-name

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        advertised_protocols: typing.Optional[list[str]]
        base_io_stream: IOStream
        certificate: typing.Optional[TlsCertificate]
        ciphersuite_name: typing.Optional[str]
        database: typing.Optional[TlsDatabase]
        interaction: typing.Optional[TlsInteraction]
        negotiated_protocol: typing.Optional[str]
        peer_certificate: typing.Optional[TlsCertificate]
        peer_certificate_errors: TlsCertificateFlags
        protocol_version: TlsProtocolVersion
        rehandshake_mode: TlsRehandshakeMode
        require_close_notify: bool
        use_system_certdb: bool
        closed: bool
        input_stream: InputStream
        output_stream: OutputStream

    props: Props = ...
    parent_instance: IOStream = ...
    priv: TlsConnectionPrivate = ...
    def __init__(
        self,
        advertised_protocols: typing.Optional[typing.Sequence[str]] = ...,
        base_io_stream: IOStream = ...,
        certificate: TlsCertificate = ...,
        database: typing.Optional[TlsDatabase] = ...,
        interaction: typing.Optional[TlsInteraction] = ...,
        rehandshake_mode: TlsRehandshakeMode = ...,
        require_close_notify: bool = ...,
        use_system_certdb: bool = ...,
    ) -> None: ...
    def do_accept_certificate(
        self, peer_cert: TlsCertificate, errors: TlsCertificateFlags
    ) -> bool: ...
    def do_get_binding_data(
        self, type: TlsChannelBindingType, data: typing.Sequence[int]
    ) -> bool: ...
    def do_get_negotiated_protocol(self) -> typing.Optional[str]: ...
    def do_handshake(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def do_handshake_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_handshake_finish(self, result: AsyncResult) -> bool: ...
    def emit_accept_certificate(
        self, peer_cert: TlsCertificate, errors: TlsCertificateFlags
    ) -> bool: ...
    def get_certificate(self) -> typing.Optional[TlsCertificate]: ...
    def get_channel_binding_data(
        self, type: TlsChannelBindingType
    ) -> typing.Tuple[bool, bytes]: ...
    def get_ciphersuite_name(self) -> typing.Optional[str]: ...
    def get_database(self) -> typing.Optional[TlsDatabase]: ...
    def get_interaction(self) -> typing.Optional[TlsInteraction]: ...
    def get_negotiated_protocol(self) -> typing.Optional[str]: ...
    def get_peer_certificate(self) -> typing.Optional[TlsCertificate]: ...
    def get_peer_certificate_errors(self) -> TlsCertificateFlags: ...
    def get_protocol_version(self) -> TlsProtocolVersion: ...
    def get_rehandshake_mode(self) -> TlsRehandshakeMode: ...
    def get_require_close_notify(self) -> bool: ...
    def get_use_system_certdb(self) -> bool: ...
    def handshake(self, cancellable: typing.Optional[Cancellable] = None) -> bool: ...
    def handshake_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def handshake_finish(self, result: AsyncResult) -> bool: ...
    def set_advertised_protocols(
        self, protocols: typing.Optional[typing.Sequence[str]] = None
    ) -> None: ...
    def set_certificate(self, certificate: TlsCertificate) -> None: ...
    def set_database(self, database: typing.Optional[TlsDatabase] = None) -> None: ...
    def set_interaction(
        self, interaction: typing.Optional[TlsInteraction] = None
    ) -> None: ...
    def set_rehandshake_mode(self, mode: TlsRehandshakeMode) -> None: ...
    def set_require_close_notify(self, require_close_notify: bool) -> None: ...
    def set_use_system_certdb(self, use_system_certdb: bool) -> None: ...

class TlsConnectionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TlsConnectionClass()
    """

    parent_class: IOStreamClass = ...
    accept_certificate: typing.Callable[
        [TlsConnection, TlsCertificate, TlsCertificateFlags], bool
    ] = ...
    handshake: typing.Callable[[TlsConnection, typing.Optional[Cancellable]], bool] = (
        ...
    )
    handshake_async: typing.Callable[..., None] = ...
    handshake_finish: typing.Callable[[TlsConnection, AsyncResult], bool] = ...
    get_binding_data: typing.Callable[
        [TlsConnection, TlsChannelBindingType, typing.Sequence[int]], bool
    ] = ...
    get_negotiated_protocol: typing.Callable[[TlsConnection], typing.Optional[str]] = (
        ...
    )
    padding: list[None] = ...

class TlsConnectionPrivate(GObject.GPointer): ...

class TlsDatabase(GObject.Object):
    """
    :Constructors:

    ::

        TlsDatabase(**properties)

    Object GTlsDatabase

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: TlsDatabasePrivate = ...
    def create_certificate_handle(
        self, certificate: TlsCertificate
    ) -> typing.Optional[str]: ...
    def do_create_certificate_handle(
        self, certificate: TlsCertificate
    ) -> typing.Optional[str]: ...
    def do_lookup_certificate_for_handle(
        self,
        handle: str,
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Optional[TlsCertificate]: ...
    def do_lookup_certificate_for_handle_async(
        self,
        handle: str,
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_lookup_certificate_for_handle_finish(
        self, result: AsyncResult
    ) -> TlsCertificate: ...
    def do_lookup_certificate_issuer(
        self,
        certificate: TlsCertificate,
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> TlsCertificate: ...
    def do_lookup_certificate_issuer_async(
        self,
        certificate: TlsCertificate,
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_lookup_certificate_issuer_finish(
        self, result: AsyncResult
    ) -> TlsCertificate: ...
    def do_lookup_certificates_issued_by(
        self,
        issuer_raw_dn: typing.Sequence[int],
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> list[TlsCertificate]: ...
    def do_lookup_certificates_issued_by_async(
        self,
        issuer_raw_dn: typing.Sequence[int],
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_lookup_certificates_issued_by_finish(
        self, result: AsyncResult
    ) -> list[TlsCertificate]: ...
    def do_verify_chain(
        self,
        chain: TlsCertificate,
        purpose: str,
        identity: typing.Optional[SocketConnectable],
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseVerifyFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> TlsCertificateFlags: ...
    def do_verify_chain_async(
        self,
        chain: TlsCertificate,
        purpose: str,
        identity: typing.Optional[SocketConnectable],
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseVerifyFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_verify_chain_finish(self, result: AsyncResult) -> TlsCertificateFlags: ...
    def lookup_certificate_for_handle(
        self,
        handle: str,
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> typing.Optional[TlsCertificate]: ...
    def lookup_certificate_for_handle_async(
        self,
        handle: str,
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def lookup_certificate_for_handle_finish(
        self, result: AsyncResult
    ) -> TlsCertificate: ...
    def lookup_certificate_issuer(
        self,
        certificate: TlsCertificate,
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> TlsCertificate: ...
    def lookup_certificate_issuer_async(
        self,
        certificate: TlsCertificate,
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def lookup_certificate_issuer_finish(
        self, result: AsyncResult
    ) -> TlsCertificate: ...
    def lookup_certificates_issued_by(
        self,
        issuer_raw_dn: typing.Sequence[int],
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> list[TlsCertificate]: ...
    def lookup_certificates_issued_by_async(
        self,
        issuer_raw_dn: typing.Sequence[int],
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseLookupFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def lookup_certificates_issued_by_finish(
        self, result: AsyncResult
    ) -> list[TlsCertificate]: ...
    def verify_chain(
        self,
        chain: TlsCertificate,
        purpose: str,
        identity: typing.Optional[SocketConnectable],
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseVerifyFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> TlsCertificateFlags: ...
    def verify_chain_async(
        self,
        chain: TlsCertificate,
        purpose: str,
        identity: typing.Optional[SocketConnectable],
        interaction: typing.Optional[TlsInteraction],
        flags: TlsDatabaseVerifyFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def verify_chain_finish(self, result: AsyncResult) -> TlsCertificateFlags: ...

class TlsDatabaseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TlsDatabaseClass()
    """

    parent_class: GObject.ObjectClass = ...
    verify_chain: typing.Callable[
        [
            TlsDatabase,
            TlsCertificate,
            str,
            typing.Optional[SocketConnectable],
            typing.Optional[TlsInteraction],
            TlsDatabaseVerifyFlags,
            typing.Optional[Cancellable],
        ],
        TlsCertificateFlags,
    ] = ...
    verify_chain_async: typing.Callable[..., None] = ...
    verify_chain_finish: typing.Callable[
        [TlsDatabase, AsyncResult], TlsCertificateFlags
    ] = ...
    create_certificate_handle: typing.Callable[
        [TlsDatabase, TlsCertificate], typing.Optional[str]
    ] = ...
    lookup_certificate_for_handle: typing.Callable[
        [
            TlsDatabase,
            str,
            typing.Optional[TlsInteraction],
            TlsDatabaseLookupFlags,
            typing.Optional[Cancellable],
        ],
        typing.Optional[TlsCertificate],
    ] = ...
    lookup_certificate_for_handle_async: typing.Callable[..., None] = ...
    lookup_certificate_for_handle_finish: typing.Callable[
        [TlsDatabase, AsyncResult], TlsCertificate
    ] = ...
    lookup_certificate_issuer: typing.Callable[
        [
            TlsDatabase,
            TlsCertificate,
            typing.Optional[TlsInteraction],
            TlsDatabaseLookupFlags,
            typing.Optional[Cancellable],
        ],
        TlsCertificate,
    ] = ...
    lookup_certificate_issuer_async: typing.Callable[..., None] = ...
    lookup_certificate_issuer_finish: typing.Callable[
        [TlsDatabase, AsyncResult], TlsCertificate
    ] = ...
    lookup_certificates_issued_by: typing.Callable[
        [
            TlsDatabase,
            typing.Sequence[int],
            typing.Optional[TlsInteraction],
            TlsDatabaseLookupFlags,
            typing.Optional[Cancellable],
        ],
        list[TlsCertificate],
    ] = ...
    lookup_certificates_issued_by_async: typing.Callable[..., None] = ...
    lookup_certificates_issued_by_finish: typing.Callable[
        [TlsDatabase, AsyncResult], list[TlsCertificate]
    ] = ...
    padding: list[None] = ...

class TlsDatabasePrivate(GObject.GPointer): ...

class TlsFileDatabase(GObject.GInterface):
    """
    Interface GTlsFileDatabase

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def new(anchors: str) -> TlsFileDatabase: ...

class TlsFileDatabaseInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        TlsFileDatabaseInterface()
    """

    g_iface: GObject.TypeInterface = ...
    padding: list[None] = ...

class TlsInteraction(GObject.Object):
    """
    :Constructors:

    ::

        TlsInteraction(**properties)

    Object GTlsInteraction

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: TlsInteractionPrivate = ...
    def ask_password(
        self, password: TlsPassword, cancellable: typing.Optional[Cancellable] = None
    ) -> TlsInteractionResult: ...
    def ask_password_async(
        self,
        password: TlsPassword,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def ask_password_finish(self, result: AsyncResult) -> TlsInteractionResult: ...
    def do_ask_password(
        self, password: TlsPassword, cancellable: typing.Optional[Cancellable] = None
    ) -> TlsInteractionResult: ...
    def do_ask_password_async(
        self,
        password: TlsPassword,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_ask_password_finish(self, result: AsyncResult) -> TlsInteractionResult: ...
    def do_request_certificate(
        self,
        connection: TlsConnection,
        flags: TlsCertificateRequestFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> TlsInteractionResult: ...
    def do_request_certificate_async(
        self,
        connection: TlsConnection,
        flags: TlsCertificateRequestFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_request_certificate_finish(
        self, result: AsyncResult
    ) -> TlsInteractionResult: ...
    def invoke_ask_password(
        self, password: TlsPassword, cancellable: typing.Optional[Cancellable] = None
    ) -> TlsInteractionResult: ...
    def invoke_request_certificate(
        self,
        connection: TlsConnection,
        flags: TlsCertificateRequestFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> TlsInteractionResult: ...
    def request_certificate(
        self,
        connection: TlsConnection,
        flags: TlsCertificateRequestFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> TlsInteractionResult: ...
    def request_certificate_async(
        self,
        connection: TlsConnection,
        flags: TlsCertificateRequestFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def request_certificate_finish(
        self, result: AsyncResult
    ) -> TlsInteractionResult: ...

class TlsInteractionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TlsInteractionClass()
    """

    parent_class: GObject.ObjectClass = ...
    ask_password: typing.Callable[
        [TlsInteraction, TlsPassword, typing.Optional[Cancellable]],
        TlsInteractionResult,
    ] = ...
    ask_password_async: typing.Callable[..., None] = ...
    ask_password_finish: typing.Callable[
        [TlsInteraction, AsyncResult], TlsInteractionResult
    ] = ...
    request_certificate: typing.Callable[
        [
            TlsInteraction,
            TlsConnection,
            TlsCertificateRequestFlags,
            typing.Optional[Cancellable],
        ],
        TlsInteractionResult,
    ] = ...
    request_certificate_async: typing.Callable[..., None] = ...
    request_certificate_finish: typing.Callable[
        [TlsInteraction, AsyncResult], TlsInteractionResult
    ] = ...
    padding: list[None] = ...

class TlsInteractionPrivate(GObject.GPointer): ...

class TlsPassword(GObject.Object):
    """
    :Constructors:

    ::

        TlsPassword(**properties)
        new(flags:Gio.TlsPasswordFlags, description:str) -> Gio.TlsPassword

    Object GTlsPassword

    Properties from GTlsPassword:
      flags -> GTlsPasswordFlags: flags
      description -> gchararray: description
      warning -> gchararray: warning

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        description: str
        flags: TlsPasswordFlags
        warning: str

    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: TlsPasswordPrivate = ...
    def __init__(
        self, description: str = ..., flags: TlsPasswordFlags = ..., warning: str = ...
    ) -> None: ...
    def do_get_default_warning(self) -> str: ...
    def do_get_value(self) -> bytes: ...
    def do_set_value(
        self,
        value: typing.Sequence[int],
        destroy: typing.Optional[typing.Callable[[None], None]] = None,
    ) -> None: ...
    def get_description(self) -> str: ...
    def get_flags(self) -> TlsPasswordFlags: ...
    def get_value(self) -> bytes: ...
    def get_warning(self) -> str: ...
    @classmethod
    def new(cls, flags: TlsPasswordFlags, description: str) -> TlsPassword: ...
    def set_description(self, description: str) -> None: ...
    def set_flags(self, flags: TlsPasswordFlags) -> None: ...
    def set_value(self, value: typing.Sequence[int]) -> None: ...
    def set_value_full(
        self,
        value: typing.Sequence[int],
        destroy: typing.Optional[typing.Callable[[None], None]] = None,
    ) -> None: ...
    def set_warning(self, warning: str) -> None: ...

class TlsPasswordClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TlsPasswordClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_value: typing.Callable[[TlsPassword], bytes] = ...
    set_value: typing.Callable[
        [
            TlsPassword,
            typing.Sequence[int],
            typing.Optional[typing.Callable[[None], None]],
        ],
        None,
    ] = ...
    get_default_warning: typing.Callable[[TlsPassword], str] = ...
    padding: list[None] = ...

class TlsPasswordPrivate(GObject.GPointer): ...

class TlsServerConnection(GObject.GInterface):
    """
    Interface GTlsServerConnection

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def new(
        base_io_stream: IOStream, certificate: typing.Optional[TlsCertificate] = None
    ) -> TlsServerConnection: ...

class TlsServerConnectionInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        TlsServerConnectionInterface()
    """

    g_iface: GObject.TypeInterface = ...

class UnixConnection(SocketConnection):
    """
    :Constructors:

    ::

        UnixConnection(**properties)

    Object GUnixConnection

    Properties from GSocketConnection:
      socket -> GSocket: socket

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        socket: Socket
        closed: bool
        input_stream: InputStream
        output_stream: OutputStream

    props: Props = ...
    parent_instance: SocketConnection = ...
    priv: UnixConnectionPrivate = ...
    def __init__(self, socket: Socket = ...) -> None: ...
    def receive_credentials(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> Credentials: ...
    def receive_credentials_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def receive_credentials_finish(self, result: AsyncResult) -> Credentials: ...
    def receive_fd(self, cancellable: typing.Optional[Cancellable] = None) -> int: ...
    def send_credentials(
        self, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...
    def send_credentials_async(
        self,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def send_credentials_finish(self, result: AsyncResult) -> bool: ...
    def send_fd(
        self, fd: int, cancellable: typing.Optional[Cancellable] = None
    ) -> bool: ...

class UnixConnectionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnixConnectionClass()
    """

    parent_class: SocketConnectionClass = ...

class UnixConnectionPrivate(GObject.GPointer): ...

class UnixCredentialsMessage(SocketControlMessage):
    """
    :Constructors:

    ::

        UnixCredentialsMessage(**properties)
        new() -> Gio.SocketControlMessage
        new_with_credentials(credentials:Gio.Credentials) -> Gio.SocketControlMessage

    Object GUnixCredentialsMessage

    Properties from GUnixCredentialsMessage:
      credentials -> GCredentials: credentials

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        credentials: Credentials

    props: Props = ...
    parent_instance: SocketControlMessage = ...
    priv: UnixCredentialsMessagePrivate = ...
    def __init__(self, credentials: Credentials = ...) -> None: ...
    def get_credentials(self) -> Credentials: ...
    @staticmethod
    def is_supported() -> bool: ...
    @classmethod
    def new(cls) -> UnixCredentialsMessage: ...
    @classmethod
    def new_with_credentials(
        cls, credentials: Credentials
    ) -> UnixCredentialsMessage: ...

class UnixCredentialsMessageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnixCredentialsMessageClass()
    """

    parent_class: SocketControlMessageClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...

class UnixCredentialsMessagePrivate(GObject.GPointer): ...

class UnixFDList(GObject.Object):
    """
    :Constructors:

    ::

        UnixFDList(**properties)
        new() -> Gio.UnixFDList
        new_from_array(fds:list) -> Gio.UnixFDList

    Object GUnixFDList

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: UnixFDListPrivate = ...
    def append(self, fd: int) -> int: ...
    def get(self, index_: int) -> int: ...
    def get_length(self) -> int: ...
    @classmethod
    def new(cls) -> UnixFDList: ...
    @classmethod
    def new_from_array(cls, fds: typing.Sequence[int]) -> UnixFDList: ...
    def peek_fds(self) -> list[int]: ...
    def steal_fds(self) -> list[int]: ...

class UnixFDListClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnixFDListClass()
    """

    parent_class: GObject.ObjectClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class UnixFDListPrivate(GObject.GPointer): ...

class UnixFDMessage(SocketControlMessage):
    """
    :Constructors:

    ::

        UnixFDMessage(**properties)
        new() -> Gio.SocketControlMessage
        new_with_fd_list(fd_list:Gio.UnixFDList) -> Gio.SocketControlMessage

    Object GUnixFDMessage

    Properties from GUnixFDMessage:
      fd-list -> GUnixFDList: fd-list

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        fd_list: UnixFDList

    props: Props = ...
    parent_instance: SocketControlMessage = ...
    priv: UnixFDMessagePrivate = ...
    def __init__(self, fd_list: UnixFDList = ...) -> None: ...
    def append_fd(self, fd: int) -> bool: ...
    def get_fd_list(self) -> UnixFDList: ...
    @classmethod
    def new(cls) -> UnixFDMessage: ...
    @classmethod
    def new_with_fd_list(cls, fd_list: UnixFDList) -> UnixFDMessage: ...
    def steal_fds(self) -> list[int]: ...

class UnixFDMessageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnixFDMessageClass()
    """

    parent_class: SocketControlMessageClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...

class UnixFDMessagePrivate(GObject.GPointer): ...

class UnixInputStream(InputStream, FileDescriptorBased, PollableInputStream):
    """
    :Constructors:

    ::

        UnixInputStream(**properties)
        new(fd:int, close_fd:bool) -> Gio.InputStream

    Object GUnixInputStream

    Properties from GUnixInputStream:
      fd -> gint: fd
      close-fd -> gboolean: close-fd

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        close_fd: bool
        fd: int

    props: Props = ...
    parent_instance: InputStream = ...
    priv: UnixInputStreamPrivate = ...
    def __init__(self, close_fd: bool = ..., fd: int = ...) -> None: ...
    def get_close_fd(self) -> bool: ...
    def get_fd(self) -> int: ...
    @classmethod
    def new(cls, fd: int, close_fd: bool) -> UnixInputStream: ...
    def set_close_fd(self, close_fd: bool) -> None: ...

class UnixInputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnixInputStreamClass()
    """

    parent_class: InputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class UnixInputStreamPrivate(GObject.GPointer): ...
class UnixMountEntry(GObject.GBoxed): ...

class UnixMountMonitor(GObject.Object):
    """
    :Constructors:

    ::

        UnixMountMonitor(**properties)
        new() -> Gio.UnixMountMonitor

    Object GUnixMountMonitor

    Signals from GUnixMountMonitor:
      mounts-changed ()
      mountpoints-changed ()

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def get() -> UnixMountMonitor: ...
    @classmethod
    def new(cls) -> UnixMountMonitor: ...
    def set_rate_limit(self, limit_msec: int) -> None: ...

class UnixMountMonitorClass(GObject.GPointer): ...

class UnixMountPoint(GObject.GBoxed):
    @staticmethod
    def at(mount_path: str) -> typing.Tuple[typing.Optional[UnixMountPoint], int]: ...
    def compare(self, mount2: UnixMountPoint) -> int: ...
    def copy(self) -> UnixMountPoint: ...
    def free(self) -> None: ...
    def get_device_path(self) -> str: ...
    def get_fs_type(self) -> str: ...
    def get_mount_path(self) -> str: ...
    def get_options(self) -> typing.Optional[str]: ...
    def guess_can_eject(self) -> bool: ...
    def guess_icon(self) -> Icon: ...
    def guess_name(self) -> str: ...
    def guess_symbolic_icon(self) -> Icon: ...
    def is_loopback(self) -> bool: ...
    def is_readonly(self) -> bool: ...
    def is_user_mountable(self) -> bool: ...

class UnixOutputStream(OutputStream, FileDescriptorBased, PollableOutputStream):
    """
    :Constructors:

    ::

        UnixOutputStream(**properties)
        new(fd:int, close_fd:bool) -> Gio.OutputStream

    Object GUnixOutputStream

    Properties from GUnixOutputStream:
      fd -> gint: fd
      close-fd -> gboolean: close-fd

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        close_fd: bool
        fd: int

    props: Props = ...
    parent_instance: OutputStream = ...
    priv: UnixOutputStreamPrivate = ...
    def __init__(self, close_fd: bool = ..., fd: int = ...) -> None: ...
    def get_close_fd(self) -> bool: ...
    def get_fd(self) -> int: ...
    @classmethod
    def new(cls, fd: int, close_fd: bool) -> UnixOutputStream: ...
    def set_close_fd(self, close_fd: bool) -> None: ...

class UnixOutputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnixOutputStreamClass()
    """

    parent_class: OutputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class UnixOutputStreamPrivate(GObject.GPointer): ...

class UnixSocketAddress(SocketAddress, SocketConnectable):
    """
    :Constructors:

    ::

        UnixSocketAddress(**properties)
        new(path:str) -> Gio.SocketAddress
        new_abstract(path:list) -> Gio.SocketAddress
        new_with_type(path:list, type:Gio.UnixSocketAddressType) -> Gio.SocketAddress

    Object GUnixSocketAddress

    Properties from GUnixSocketAddress:
      path -> gchararray: path
      path-as-array -> GByteArray: path-as-array
      abstract -> gboolean: abstract
      address-type -> GUnixSocketAddressType: address-type

    Properties from GSocketAddress:
      family -> GSocketFamily: family

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        abstract: bool
        address_type: UnixSocketAddressType
        path: str
        path_as_array: bytes
        family: SocketFamily

    props: Props = ...
    parent_instance: SocketAddress = ...
    priv: UnixSocketAddressPrivate = ...
    def __init__(
        self,
        abstract: bool = ...,
        address_type: UnixSocketAddressType = ...,
        path: str = ...,
        path_as_array: typing.Sequence[int] = ...,
    ) -> None: ...
    @staticmethod
    def abstract_names_supported() -> bool: ...
    def get_address_type(self) -> UnixSocketAddressType: ...
    def get_is_abstract(self) -> bool: ...
    def get_path(self) -> str: ...
    def get_path_len(self) -> int: ...
    @classmethod
    def new(cls, path: str) -> UnixSocketAddress: ...
    @classmethod
    def new_abstract(cls, path: typing.Sequence[int]) -> UnixSocketAddress: ...
    @classmethod
    def new_with_type(
        cls, path: typing.Sequence[int], type: UnixSocketAddressType
    ) -> UnixSocketAddress: ...

class UnixSocketAddressClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnixSocketAddressClass()
    """

    parent_class: SocketAddressClass = ...

class UnixSocketAddressPrivate(GObject.GPointer): ...

class Vfs(GObject.Object):
    """
    :Constructors:

    ::

        Vfs(**properties)

    Object GVfs

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def do_add_writable_namespaces(self, list: FileAttributeInfoList) -> None: ...
    def do_get_file_for_path(self, path: str) -> File: ...
    def do_get_file_for_uri(self, uri: str) -> File: ...
    def do_get_supported_uri_schemes(self) -> list[str]: ...
    def do_is_active(self) -> bool: ...
    def do_local_file_add_info(
        self,
        filename: str,
        device: int,
        attribute_matcher: FileAttributeMatcher,
        info: FileInfo,
        cancellable: typing.Optional[Cancellable],
        extra_data: None,
        free_extra_data: typing.Callable[[None], None],
    ) -> None: ...
    def do_local_file_moved(self, source: str, dest: str) -> None: ...
    def do_local_file_removed(self, filename: str) -> None: ...
    def do_local_file_set_attributes(
        self,
        filename: str,
        info: FileInfo,
        flags: FileQueryInfoFlags,
        cancellable: typing.Optional[Cancellable] = None,
    ) -> bool: ...
    def do_parse_name(self, parse_name: str) -> File: ...
    @staticmethod
    def get_default() -> Vfs: ...
    def get_file_for_path(self, path: str) -> File: ...
    def get_file_for_uri(self, uri: str) -> File: ...
    @staticmethod
    def get_local() -> Vfs: ...
    def get_supported_uri_schemes(self) -> list[str]: ...
    def is_active(self) -> bool: ...
    def parse_name(self, parse_name: str) -> File: ...
    def register_uri_scheme(
        self,
        scheme: str,
        uri_func: typing.Optional[typing.Callable[..., File]] = None,
        parse_name_func: typing.Optional[typing.Callable[..., File]] = None,
        *parse_name_data: typing.Any,
    ) -> bool: ...
    def unregister_uri_scheme(self, scheme: str) -> bool: ...

class VfsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VfsClass()
    """

    parent_class: GObject.ObjectClass = ...
    is_active: typing.Callable[[Vfs], bool] = ...
    get_file_for_path: typing.Callable[[Vfs, str], File] = ...
    get_file_for_uri: typing.Callable[[Vfs, str], File] = ...
    get_supported_uri_schemes: typing.Callable[[Vfs], list[str]] = ...
    parse_name: typing.Callable[[Vfs, str], File] = ...
    local_file_add_info: typing.Callable[
        [
            Vfs,
            str,
            int,
            FileAttributeMatcher,
            FileInfo,
            typing.Optional[Cancellable],
            None,
            typing.Callable[[None], None],
        ],
        None,
    ] = ...
    add_writable_namespaces: typing.Callable[[Vfs, FileAttributeInfoList], None] = ...
    local_file_set_attributes: typing.Callable[
        [Vfs, str, FileInfo, FileQueryInfoFlags, typing.Optional[Cancellable]], bool
    ] = ...
    local_file_removed: typing.Callable[[Vfs, str], None] = ...
    local_file_moved: typing.Callable[[Vfs, str, str], None] = ...
    deserialize_icon: None = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...
    _g_reserved6: None = ...

class Volume(GObject.GInterface):
    """
    Interface GVolume

    Signals from GObject:
      notify (GParam)
    """

    def can_eject(self) -> bool: ...
    def can_mount(self) -> bool: ...
    def eject(
        self,
        flags: MountUnmountFlags,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def eject_finish(self, result: AsyncResult) -> bool: ...
    def eject_with_operation(
        self,
        flags: MountUnmountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def eject_with_operation_finish(self, result: AsyncResult) -> bool: ...
    def enumerate_identifiers(self) -> list[str]: ...
    def get_activation_root(self) -> typing.Optional[File]: ...
    def get_drive(self) -> typing.Optional[Drive]: ...
    def get_icon(self) -> Icon: ...
    def get_identifier(self, kind: str) -> typing.Optional[str]: ...
    def get_mount(self) -> typing.Optional[Mount]: ...
    def get_name(self) -> str: ...
    def get_sort_key(self) -> typing.Optional[str]: ...
    def get_symbolic_icon(self) -> Icon: ...
    def get_uuid(self) -> typing.Optional[str]: ...
    def mount(
        self,
        flags: MountMountFlags,
        mount_operation: typing.Optional[MountOperation] = None,
        cancellable: typing.Optional[Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def mount_finish(self, result: AsyncResult) -> bool: ...
    def should_automount(self) -> bool: ...

class VolumeIface(GObject.GPointer):
    """
    :Constructors:

    ::

        VolumeIface()
    """

    g_iface: GObject.TypeInterface = ...
    changed: typing.Callable[[Volume], None] = ...
    removed: typing.Callable[[Volume], None] = ...
    get_name: typing.Callable[[Volume], str] = ...
    get_icon: typing.Callable[[Volume], Icon] = ...
    get_uuid: typing.Callable[[Volume], typing.Optional[str]] = ...
    get_drive: typing.Callable[[Volume], typing.Optional[Drive]] = ...
    get_mount: typing.Callable[[Volume], typing.Optional[Mount]] = ...
    can_mount: typing.Callable[[Volume], bool] = ...
    can_eject: typing.Callable[[Volume], bool] = ...
    mount_fn: typing.Callable[..., None] = ...
    mount_finish: typing.Callable[[Volume, AsyncResult], bool] = ...
    eject: typing.Callable[..., None] = ...
    eject_finish: typing.Callable[[Volume, AsyncResult], bool] = ...
    get_identifier: typing.Callable[[Volume, str], typing.Optional[str]] = ...
    enumerate_identifiers: typing.Callable[[Volume], list[str]] = ...
    should_automount: typing.Callable[[Volume], bool] = ...
    get_activation_root: typing.Callable[[Volume], typing.Optional[File]] = ...
    eject_with_operation: typing.Callable[..., None] = ...
    eject_with_operation_finish: typing.Callable[[Volume, AsyncResult], bool] = ...
    get_sort_key: typing.Callable[[Volume], typing.Optional[str]] = ...
    get_symbolic_icon: typing.Callable[[Volume], Icon] = ...

class VolumeMonitor(GObject.Object):
    """
    :Constructors:

    ::

        VolumeMonitor(**properties)

    Object GVolumeMonitor

    Signals from GVolumeMonitor:
      volume-added (GVolume)
      volume-removed (GVolume)
      volume-changed (GVolume)
      mount-added (GMount)
      mount-removed (GMount)
      mount-pre-unmount (GMount)
      mount-changed (GMount)
      drive-connected (GDrive)
      drive-disconnected (GDrive)
      drive-changed (GDrive)
      drive-eject-button (GDrive)
      drive-stop-button (GDrive)

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: None = ...
    @staticmethod
    def adopt_orphan_mount(mount: Mount) -> Volume: ...
    def do_drive_changed(self, drive: Drive) -> None: ...
    def do_drive_connected(self, drive: Drive) -> None: ...
    def do_drive_disconnected(self, drive: Drive) -> None: ...
    def do_drive_eject_button(self, drive: Drive) -> None: ...
    def do_drive_stop_button(self, drive: Drive) -> None: ...
    def do_get_connected_drives(self) -> list[Drive]: ...
    def do_get_mount_for_uuid(self, uuid: str) -> typing.Optional[Mount]: ...
    def do_get_mounts(self) -> list[Mount]: ...
    def do_get_volume_for_uuid(self, uuid: str) -> typing.Optional[Volume]: ...
    def do_get_volumes(self) -> list[Volume]: ...
    def do_mount_added(self, mount: Mount) -> None: ...
    def do_mount_changed(self, mount: Mount) -> None: ...
    def do_mount_pre_unmount(self, mount: Mount) -> None: ...
    def do_mount_removed(self, mount: Mount) -> None: ...
    def do_volume_added(self, volume: Volume) -> None: ...
    def do_volume_changed(self, volume: Volume) -> None: ...
    def do_volume_removed(self, volume: Volume) -> None: ...
    @staticmethod
    def get() -> VolumeMonitor: ...
    def get_connected_drives(self) -> list[Drive]: ...
    def get_mount_for_uuid(self, uuid: str) -> typing.Optional[Mount]: ...
    def get_mounts(self) -> list[Mount]: ...
    def get_volume_for_uuid(self, uuid: str) -> typing.Optional[Volume]: ...
    def get_volumes(self) -> list[Volume]: ...

class VolumeMonitorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VolumeMonitorClass()
    """

    parent_class: GObject.ObjectClass = ...
    volume_added: typing.Callable[[VolumeMonitor, Volume], None] = ...
    volume_removed: typing.Callable[[VolumeMonitor, Volume], None] = ...
    volume_changed: typing.Callable[[VolumeMonitor, Volume], None] = ...
    mount_added: typing.Callable[[VolumeMonitor, Mount], None] = ...
    mount_removed: typing.Callable[[VolumeMonitor, Mount], None] = ...
    mount_pre_unmount: typing.Callable[[VolumeMonitor, Mount], None] = ...
    mount_changed: typing.Callable[[VolumeMonitor, Mount], None] = ...
    drive_connected: typing.Callable[[VolumeMonitor, Drive], None] = ...
    drive_disconnected: typing.Callable[[VolumeMonitor, Drive], None] = ...
    drive_changed: typing.Callable[[VolumeMonitor, Drive], None] = ...
    is_supported: typing.Callable[[], bool] = ...
    get_connected_drives: typing.Callable[[VolumeMonitor], list[Drive]] = ...
    get_volumes: typing.Callable[[VolumeMonitor], list[Volume]] = ...
    get_mounts: typing.Callable[[VolumeMonitor], list[Mount]] = ...
    get_volume_for_uuid: typing.Callable[
        [VolumeMonitor, str], typing.Optional[Volume]
    ] = ...
    get_mount_for_uuid: typing.Callable[
        [VolumeMonitor, str], typing.Optional[Mount]
    ] = ...
    adopt_orphan_mount: None = ...
    drive_eject_button: typing.Callable[[VolumeMonitor, Drive], None] = ...
    drive_stop_button: typing.Callable[[VolumeMonitor, Drive], None] = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...
    _g_reserved6: None = ...

class ZlibCompressor(GObject.Object, Converter):
    """
    :Constructors:

    ::

        ZlibCompressor(**properties)
        new(format:Gio.ZlibCompressorFormat, level:int) -> Gio.ZlibCompressor

    Object GZlibCompressor

    Properties from GZlibCompressor:
      format -> GZlibCompressorFormat: format
      level -> gint: level
      file-info -> GFileInfo: file-info

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        file_info: typing.Optional[FileInfo]
        format: ZlibCompressorFormat
        level: int

    props: Props = ...
    def __init__(
        self,
        file_info: typing.Optional[FileInfo] = ...,
        format: ZlibCompressorFormat = ...,
        level: int = ...,
    ) -> None: ...
    def get_file_info(self) -> typing.Optional[FileInfo]: ...
    @classmethod
    def new(cls, format: ZlibCompressorFormat, level: int) -> ZlibCompressor: ...
    def set_file_info(self, file_info: typing.Optional[FileInfo] = None) -> None: ...

class ZlibCompressorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ZlibCompressorClass()
    """

    parent_class: GObject.ObjectClass = ...

class ZlibDecompressor(GObject.Object, Converter):
    """
    :Constructors:

    ::

        ZlibDecompressor(**properties)
        new(format:Gio.ZlibCompressorFormat) -> Gio.ZlibDecompressor

    Object GZlibDecompressor

    Properties from GZlibDecompressor:
      format -> GZlibCompressorFormat: format
      file-info -> GFileInfo: file-info

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        file_info: typing.Optional[FileInfo]
        format: ZlibCompressorFormat

    props: Props = ...
    def __init__(self, format: ZlibCompressorFormat = ...) -> None: ...
    def get_file_info(self) -> typing.Optional[FileInfo]: ...
    @classmethod
    def new(cls, format: ZlibCompressorFormat) -> ZlibDecompressor: ...

class ZlibDecompressorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ZlibDecompressorClass()
    """

    parent_class: GObject.ObjectClass = ...

class AppInfoCreateFlags(GObject.GFlags):
    NEEDS_TERMINAL = 1
    NONE = 0
    SUPPORTS_STARTUP_NOTIFICATION = 4
    SUPPORTS_URIS = 2

class ApplicationFlags(GObject.GFlags):
    ALLOW_REPLACEMENT = 128
    CAN_OVERRIDE_APP_ID = 64
    DEFAULT_FLAGS = 0
    FLAGS_NONE = 0
    HANDLES_COMMAND_LINE = 8
    HANDLES_OPEN = 4
    IS_LAUNCHER = 2
    IS_SERVICE = 1
    NON_UNIQUE = 32
    REPLACE = 256
    SEND_ENVIRONMENT = 16

class AskPasswordFlags(GObject.GFlags):
    ANONYMOUS_SUPPORTED = 16
    NEED_DOMAIN = 4
    NEED_PASSWORD = 1
    NEED_USERNAME = 2
    SAVING_SUPPORTED = 8
    TCRYPT = 32

class BusNameOwnerFlags(GObject.GFlags):
    ALLOW_REPLACEMENT = 1
    DO_NOT_QUEUE = 4
    NONE = 0
    REPLACE = 2

class BusNameWatcherFlags(GObject.GFlags):
    AUTO_START = 1
    NONE = 0

class ConverterFlags(GObject.GFlags):
    FLUSH = 2
    INPUT_AT_END = 1
    NONE = 0

class DBusCallFlags(GObject.GFlags):
    ALLOW_INTERACTIVE_AUTHORIZATION = 2
    NONE = 0
    NO_AUTO_START = 1

class DBusCapabilityFlags(GObject.GFlags):
    NONE = 0
    UNIX_FD_PASSING = 1

class DBusConnectionFlags(GObject.GFlags):
    AUTHENTICATION_ALLOW_ANONYMOUS = 4
    AUTHENTICATION_CLIENT = 1
    AUTHENTICATION_REQUIRE_SAME_USER = 32
    AUTHENTICATION_SERVER = 2
    CROSS_NAMESPACE = 64
    DELAY_MESSAGE_PROCESSING = 16
    MESSAGE_BUS_CONNECTION = 8
    NONE = 0

class DBusInterfaceSkeletonFlags(GObject.GFlags):
    HANDLE_METHOD_INVOCATIONS_IN_THREAD = 1
    NONE = 0

class DBusMessageFlags(GObject.GFlags):
    ALLOW_INTERACTIVE_AUTHORIZATION = 4
    NONE = 0
    NO_AUTO_START = 2
    NO_REPLY_EXPECTED = 1

class DBusObjectManagerClientFlags(GObject.GFlags):
    DO_NOT_AUTO_START = 1
    NONE = 0

class DBusPropertyInfoFlags(GObject.GFlags):
    NONE = 0
    READABLE = 1
    WRITABLE = 2

class DBusProxyFlags(GObject.GFlags):
    DO_NOT_AUTO_START = 4
    DO_NOT_AUTO_START_AT_CONSTRUCTION = 16
    DO_NOT_CONNECT_SIGNALS = 2
    DO_NOT_LOAD_PROPERTIES = 1
    GET_INVALIDATED_PROPERTIES = 8
    NONE = 0
    NO_MATCH_RULE = 32

class DBusSendMessageFlags(GObject.GFlags):
    NONE = 0
    PRESERVE_SERIAL = 1

class DBusServerFlags(GObject.GFlags):
    AUTHENTICATION_ALLOW_ANONYMOUS = 2
    AUTHENTICATION_REQUIRE_SAME_USER = 4
    NONE = 0
    RUN_IN_THREAD = 1

class DBusSignalFlags(GObject.GFlags):
    MATCH_ARG0_NAMESPACE = 2
    MATCH_ARG0_PATH = 4
    NONE = 0
    NO_MATCH_RULE = 1

class DBusSubtreeFlags(GObject.GFlags):
    DISPATCH_TO_UNENUMERATED_NODES = 1
    NONE = 0

class DriveStartFlags(GObject.GFlags):
    NONE = 0

class FileAttributeInfoFlags(GObject.GFlags):
    COPY_WHEN_MOVED = 2
    COPY_WITH_FILE = 1
    NONE = 0

class FileCopyFlags(GObject.GFlags):
    ALL_METADATA = 8
    BACKUP = 2
    NOFOLLOW_SYMLINKS = 4
    NONE = 0
    NO_FALLBACK_FOR_MOVE = 16
    OVERWRITE = 1
    TARGET_DEFAULT_MODIFIED_TIME = 64
    TARGET_DEFAULT_PERMS = 32

class FileCreateFlags(GObject.GFlags):
    NONE = 0
    PRIVATE = 1
    REPLACE_DESTINATION = 2

class FileMeasureFlags(GObject.GFlags):
    APPARENT_SIZE = 4
    NONE = 0
    NO_XDEV = 8
    REPORT_ANY_ERROR = 2

class FileMonitorFlags(GObject.GFlags):
    NONE = 0
    SEND_MOVED = 2
    WATCH_HARD_LINKS = 4
    WATCH_MOUNTS = 1
    WATCH_MOVES = 8

class FileQueryInfoFlags(GObject.GFlags):
    NOFOLLOW_SYMLINKS = 1
    NONE = 0

class IOStreamSpliceFlags(GObject.GFlags):
    CLOSE_STREAM1 = 1
    CLOSE_STREAM2 = 2
    NONE = 0
    WAIT_FOR_BOTH = 4

class MountMountFlags(GObject.GFlags):
    NONE = 0

class MountUnmountFlags(GObject.GFlags):
    FORCE = 1
    NONE = 0

class OutputStreamSpliceFlags(GObject.GFlags):
    CLOSE_SOURCE = 1
    CLOSE_TARGET = 2
    NONE = 0

class ResolverNameLookupFlags(GObject.GFlags):
    DEFAULT = 0
    IPV4_ONLY = 1
    IPV6_ONLY = 2

class ResourceFlags(GObject.GFlags):
    COMPRESSED = 1
    NONE = 0

class ResourceLookupFlags(GObject.GFlags):
    NONE = 0

class SettingsBindFlags(GObject.GFlags):
    DEFAULT = 0
    GET = 1
    GET_NO_CHANGES = 8
    INVERT_BOOLEAN = 16
    NO_SENSITIVITY = 4
    SET = 2

class SocketMsgFlags(GObject.GFlags):
    DONTROUTE = 4
    NONE = 0
    OOB = 1
    PEEK = 2

class SubprocessFlags(GObject.GFlags):
    INHERIT_FDS = 128
    NONE = 0
    SEARCH_PATH_FROM_ENVP = 256
    STDERR_MERGE = 64
    STDERR_PIPE = 16
    STDERR_SILENCE = 32
    STDIN_INHERIT = 2
    STDIN_PIPE = 1
    STDOUT_PIPE = 4
    STDOUT_SILENCE = 8

class TestDBusFlags(GObject.GFlags):
    NONE = 0

class TlsCertificateFlags(GObject.GFlags):
    BAD_IDENTITY = 2
    EXPIRED = 8
    GENERIC_ERROR = 64
    INSECURE = 32
    NOT_ACTIVATED = 4
    NO_FLAGS = 0
    REVOKED = 16
    UNKNOWN_CA = 1
    VALIDATE_ALL = 127

class TlsDatabaseVerifyFlags(GObject.GFlags):
    NONE = 0

class TlsPasswordFlags(GObject.GFlags):
    FINAL_TRY = 8
    MANY_TRIES = 4
    NONE = 0
    PKCS11_CONTEXT_SPECIFIC = 64
    PKCS11_SECURITY_OFFICER = 32
    PKCS11_USER = 16
    RETRY = 2

class BusType(GObject.GEnum):
    NONE = 0
    SESSION = 2
    STARTER = -1
    SYSTEM = 1

class ConverterResult(GObject.GEnum):
    CONVERTED = 1
    ERROR = 0
    FINISHED = 2
    FLUSHED = 3

class CredentialsType(GObject.GEnum):
    APPLE_XUCRED = 6
    FREEBSD_CMSGCRED = 2
    INVALID = 0
    LINUX_UCRED = 1
    NETBSD_UNPCBID = 5
    OPENBSD_SOCKPEERCRED = 3
    SOLARIS_UCRED = 4
    WIN32_PID = 7

class DBusError(GObject.GEnum):
    ACCESS_DENIED = 9
    ADDRESS_IN_USE = 14
    ADT_AUDIT_DATA_UNKNOWN = 39
    AUTH_FAILED = 10
    BAD_ADDRESS = 6
    DISCONNECTED = 15
    FAILED = 0
    FILE_EXISTS = 18
    FILE_NOT_FOUND = 17
    INVALID_ARGS = 16
    INVALID_FILE_CONTENT = 37
    INVALID_SIGNATURE = 36
    IO_ERROR = 5
    LIMITS_EXCEEDED = 8
    MATCH_RULE_INVALID = 22
    MATCH_RULE_NOT_FOUND = 21
    NAME_HAS_NO_OWNER = 3
    NOT_SUPPORTED = 7
    NO_MEMORY = 1
    NO_NETWORK = 13
    NO_REPLY = 4
    NO_SERVER = 11
    OBJECT_PATH_IN_USE = 40
    PROPERTY_READ_ONLY = 44
    SELINUX_SECURITY_CONTEXT_UNKNOWN = 38
    SERVICE_UNKNOWN = 2
    SPAWN_CHILD_EXITED = 25
    SPAWN_CHILD_SIGNALED = 26
    SPAWN_CONFIG_INVALID = 29
    SPAWN_EXEC_FAILED = 23
    SPAWN_FAILED = 27
    SPAWN_FILE_INVALID = 33
    SPAWN_FORK_FAILED = 24
    SPAWN_NO_MEMORY = 34
    SPAWN_PERMISSIONS_INVALID = 32
    SPAWN_SERVICE_INVALID = 30
    SPAWN_SERVICE_NOT_FOUND = 31
    SPAWN_SETUP_FAILED = 28
    TIMED_OUT = 20
    TIMEOUT = 12
    UNIX_PROCESS_ID_UNKNOWN = 35
    UNKNOWN_INTERFACE = 42
    UNKNOWN_METHOD = 19
    UNKNOWN_OBJECT = 41
    UNKNOWN_PROPERTY = 43
    @staticmethod
    def encode_gerror(error: GLib.Error) -> str: ...
    @staticmethod
    def get_remote_error(error: GLib.Error) -> typing.Optional[str]: ...
    @staticmethod
    def is_remote_error(error: GLib.Error) -> bool: ...
    @staticmethod
    def new_for_dbus_error(
        dbus_error_name: str, dbus_error_message: str
    ) -> GLib.Error: ...
    @staticmethod
    def quark() -> int: ...
    @staticmethod
    def register_error(
        error_domain: int, error_code: int, dbus_error_name: str
    ) -> bool: ...
    @staticmethod
    def register_error_domain(
        error_domain_quark_name: str,
        quark_volatile: int,
        entries: typing.Sequence[DBusErrorEntry],
    ) -> None: ...
    @staticmethod
    def strip_remote_error(error: GLib.Error) -> bool: ...
    @staticmethod
    def unregister_error(
        error_domain: int, error_code: int, dbus_error_name: str
    ) -> bool: ...

class DBusMessageByteOrder(GObject.GEnum):
    BIG_ENDIAN = 66
    LITTLE_ENDIAN = 108

class DBusMessageHeaderField(GObject.GEnum):
    DESTINATION = 6
    ERROR_NAME = 4
    INTERFACE = 2
    INVALID = 0
    MEMBER = 3
    NUM_UNIX_FDS = 9
    PATH = 1
    REPLY_SERIAL = 5
    SENDER = 7
    SIGNATURE = 8

class DBusMessageType(GObject.GEnum):
    ERROR = 3
    INVALID = 0
    METHOD_CALL = 1
    METHOD_RETURN = 2
    SIGNAL = 4

class DataStreamByteOrder(GObject.GEnum):
    BIG_ENDIAN = 0
    HOST_ENDIAN = 2
    LITTLE_ENDIAN = 1

class DataStreamNewlineType(GObject.GEnum):
    ANY = 3
    CR = 1
    CR_LF = 2
    LF = 0

class DriveStartStopType(GObject.GEnum):
    MULTIDISK = 3
    NETWORK = 2
    PASSWORD = 4
    SHUTDOWN = 1
    UNKNOWN = 0

class EmblemOrigin(GObject.GEnum):
    DEVICE = 1
    LIVEMETADATA = 2
    TAG = 3
    UNKNOWN = 0

class FileAttributeStatus(GObject.GEnum):
    ERROR_SETTING = 2
    SET = 1
    UNSET = 0

class FileAttributeType(GObject.GEnum):
    BOOLEAN = 3
    BYTE_STRING = 2
    INT32 = 5
    INT64 = 7
    INVALID = 0
    OBJECT = 8
    STRING = 1
    STRINGV = 9
    UINT32 = 4
    UINT64 = 6

class FileMonitorEvent(GObject.GEnum):
    ATTRIBUTE_CHANGED = 4
    CHANGED = 0
    CHANGES_DONE_HINT = 1
    CREATED = 3
    DELETED = 2
    MOVED = 7
    MOVED_IN = 9
    MOVED_OUT = 10
    PRE_UNMOUNT = 5
    RENAMED = 8
    UNMOUNTED = 6

class FileType(GObject.GEnum):
    DIRECTORY = 2
    MOUNTABLE = 6
    REGULAR = 1
    SHORTCUT = 5
    SPECIAL = 4
    SYMBOLIC_LINK = 3
    UNKNOWN = 0

class FilesystemPreviewType(GObject.GEnum):
    IF_ALWAYS = 0
    IF_LOCAL = 1
    NEVER = 2

class IOErrorEnum(GObject.GEnum):
    ADDRESS_IN_USE = 33
    ALREADY_MOUNTED = 17
    BROKEN_PIPE = 44
    BUSY = 26
    CANCELLED = 19
    CANT_CREATE_BACKUP = 22
    CLOSED = 18
    CONNECTION_CLOSED = 44
    CONNECTION_REFUSED = 39
    DBUS_ERROR = 36
    DESTINATION_UNSET = 48
    EXISTS = 2
    FAILED = 0
    FAILED_HANDLED = 30
    FILENAME_TOO_LONG = 9
    HOST_NOT_FOUND = 28
    HOST_UNREACHABLE = 37
    INVALID_ARGUMENT = 13
    INVALID_DATA = 35
    INVALID_FILENAME = 10
    IS_DIRECTORY = 3
    MESSAGE_TOO_LARGE = 46
    NETWORK_UNREACHABLE = 38
    NOT_CONNECTED = 45
    NOT_DIRECTORY = 4
    NOT_EMPTY = 5
    NOT_FOUND = 1
    NOT_INITIALIZED = 32
    NOT_MOUNTABLE_FILE = 8
    NOT_MOUNTED = 16
    NOT_REGULAR_FILE = 6
    NOT_SUPPORTED = 15
    NOT_SYMBOLIC_LINK = 7
    NO_SPACE = 12
    NO_SUCH_DEVICE = 47
    PARTIAL_INPUT = 34
    PENDING = 20
    PERMISSION_DENIED = 14
    PROXY_AUTH_FAILED = 41
    PROXY_FAILED = 40
    PROXY_NEED_AUTH = 42
    PROXY_NOT_ALLOWED = 43
    READ_ONLY = 21
    TIMED_OUT = 24
    TOO_MANY_LINKS = 11
    TOO_MANY_OPEN_FILES = 31
    WOULD_BLOCK = 27
    WOULD_MERGE = 29
    WOULD_RECURSE = 25
    WRONG_ETAG = 23

class IOModuleScopeFlags(GObject.GEnum):
    BLOCK_DUPLICATES = 1
    NONE = 0

class MemoryMonitorWarningLevel(GObject.GEnum):
    CRITICAL = 255
    LOW = 50
    MEDIUM = 100

class MountOperationResult(GObject.GEnum):
    ABORTED = 1
    HANDLED = 0
    UNHANDLED = 2

class NetworkConnectivity(GObject.GEnum):
    FULL = 4
    LIMITED = 2
    LOCAL = 1
    PORTAL = 3

class NotificationPriority(GObject.GEnum):
    HIGH = 2
    LOW = 1
    NORMAL = 0
    URGENT = 3

class PasswordSave(GObject.GEnum):
    FOR_SESSION = 1
    NEVER = 0
    PERMANENTLY = 2

class PollableReturn(GObject.GEnum):
    FAILED = 0
    OK = 1
    WOULD_BLOCK = -27

class ResolverError(GObject.GEnum):
    INTERNAL = 2
    NOT_FOUND = 0
    TEMPORARY_FAILURE = 1
    @staticmethod
    def quark() -> int: ...

class ResolverRecordType(GObject.GEnum):
    MX = 2
    NS = 5
    SOA = 4
    SRV = 1
    TXT = 3

class ResourceError(GObject.GEnum):
    INTERNAL = 1
    NOT_FOUND = 0
    @staticmethod
    def quark() -> int: ...

class SocketClientEvent(GObject.GEnum):
    COMPLETE = 8
    CONNECTED = 3
    CONNECTING = 2
    PROXY_NEGOTIATED = 5
    PROXY_NEGOTIATING = 4
    RESOLVED = 1
    RESOLVING = 0
    TLS_HANDSHAKED = 7
    TLS_HANDSHAKING = 6

class SocketFamily(GObject.GEnum):
    INVALID = 0
    IPV4 = 2
    IPV6 = 10
    UNIX = 1

class SocketListenerEvent(GObject.GEnum):
    BINDING = 0
    BOUND = 1
    LISTENED = 3
    LISTENING = 2

class SocketProtocol(GObject.GEnum):
    DEFAULT = 0
    SCTP = 132
    TCP = 6
    UDP = 17
    UNKNOWN = -1

class SocketType(GObject.GEnum):
    DATAGRAM = 2
    INVALID = 0
    SEQPACKET = 3
    STREAM = 1

class TlsAuthenticationMode(GObject.GEnum):
    NONE = 0
    REQUESTED = 1
    REQUIRED = 2

class TlsCertificateRequestFlags(GObject.GEnum):
    NONE = 0

class TlsChannelBindingError(GObject.GEnum):
    GENERAL_ERROR = 4
    INVALID_STATE = 1
    NOT_AVAILABLE = 2
    NOT_IMPLEMENTED = 0
    NOT_SUPPORTED = 3
    @staticmethod
    def quark() -> int: ...

class TlsChannelBindingType(GObject.GEnum):
    EXPORTER = 2
    SERVER_END_POINT = 1
    UNIQUE = 0

class TlsDatabaseLookupFlags(GObject.GEnum):
    KEYPAIR = 1
    NONE = 0

class TlsError(GObject.GEnum):
    BAD_CERTIFICATE = 2
    BAD_CERTIFICATE_PASSWORD = 8
    CERTIFICATE_REQUIRED = 5
    EOF = 6
    HANDSHAKE = 4
    INAPPROPRIATE_FALLBACK = 7
    MISC = 1
    NOT_TLS = 3
    UNAVAILABLE = 0
    @staticmethod
    def quark() -> int: ...

class TlsInteractionResult(GObject.GEnum):
    FAILED = 2
    HANDLED = 1
    UNHANDLED = 0

class TlsProtocolVersion(GObject.GEnum):
    DTLS_1_0 = 201
    DTLS_1_2 = 202
    SSL_3_0 = 1
    TLS_1_0 = 2
    TLS_1_1 = 3
    TLS_1_2 = 4
    TLS_1_3 = 5
    UNKNOWN = 0

class TlsRehandshakeMode(GObject.GEnum):
    NEVER = 0
    SAFELY = 1
    UNSAFELY = 2

class UnixSocketAddressType(GObject.GEnum):
    ABSTRACT = 3
    ABSTRACT_PADDED = 4
    ANONYMOUS = 1
    INVALID = 0
    PATH = 2

class ZlibCompressorFormat(GObject.GEnum):
    GZIP = 1
    RAW = 2
    ZLIB = 0
