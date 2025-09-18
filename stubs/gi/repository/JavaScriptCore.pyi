from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import GLib
from gi.repository import GObject

MAJOR_VERSION: int = 2
MICRO_VERSION: int = 3
MINOR_VERSION: int = 42
OPTIONS_USE_DFG: str = "useDFGJIT"
OPTIONS_USE_FTL: str = "useFTLJIT"
OPTIONS_USE_JIT: str = "useJIT"
OPTIONS_USE_LLINT: str = "useLLInt"
_lock = ...  # FIXME Constant
_namespace: str = "JavaScriptCore"
_version: str = "6.0"

def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def options_foreach(function: Callable[..., bool], *user_data: Any) -> None: ...
def options_get_boolean(option: str) -> Tuple[bool, bool]: ...
def options_get_double(option: str) -> Tuple[bool, float]: ...
def options_get_int(option: str) -> Tuple[bool, int]: ...
def options_get_option_group() -> GLib.OptionGroup: ...
def options_get_range_string(option: str) -> Tuple[bool, str]: ...
def options_get_size(option: str) -> Tuple[bool, int]: ...
def options_get_string(option: str) -> Tuple[bool, str]: ...
def options_get_uint(option: str) -> Tuple[bool, int]: ...
def options_set_boolean(option: str, value: bool) -> bool: ...
def options_set_double(option: str, value: float) -> bool: ...
def options_set_int(option: str, value: int) -> bool: ...
def options_set_range_string(option: str, value: str) -> bool: ...
def options_set_size(option: str, value: int) -> bool: ...
def options_set_string(option: str, value: str) -> bool: ...
def options_set_uint(option: str, value: int) -> bool: ...

class Class(GObject.Object):
    """
    :Constructors:

    ::

        Class(**properties)

    Object JSCClass

    Properties from JSCClass:
      context -> JSCContext: context
      name -> gchararray: name
      parent -> JSCClass: parent

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        name: str
        parent: Class
        context: Context

    props: Props = ...
    def __init__(
        self, context: Context = ..., name: str = ..., parent: Class = ...
    ): ...
    def add_constructor(
        self,
        name: Optional[str],
        callback: Callable[..., None],
        return_type: Type,
        parameter_types: Optional[Sequence[Type]] = None,
        *user_data: Any,
    ) -> Value: ...
    def add_constructor_variadic(
        self,
        name: Optional[str],
        callback: Callable[..., None],
        return_type: Type,
        *user_data: Any,
    ) -> Value: ...
    def add_method(
        self,
        name: str,
        callback: Callable[..., None],
        return_type: Type,
        parameter_types: Optional[Sequence[Type]] = None,
        *user_data: Any,
    ) -> None: ...
    def add_method_variadic(
        self,
        name: str,
        callback: Callable[..., None],
        return_type: Type,
        *user_data: Any,
    ) -> None: ...
    def add_property(
        self,
        name: str,
        property_type: Type,
        getter: Optional[Callable[[], None]] = None,
        setter: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def get_name(self) -> str: ...
    def get_parent(self) -> Class: ...

class ClassClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClassClass()
    """

    parent_class: GObject.ObjectClass = ...

class ClassVTable(GObject.GPointer):
    """
    :Constructors:

    ::

        ClassVTable()
    """

    get_property: Callable[[Class, Context, None, str], Optional[Value]] = ...
    set_property: Callable[[Class, Context, None, str, Value], bool] = ...
    has_property: Callable[[Class, Context, None, str], bool] = ...
    delete_property: Callable[[Class, Context, None, str], bool] = ...
    enumerate_properties: Callable[[Class, Context, None], Optional[list[str]]] = ...
    _jsc_reserved0: None = ...
    _jsc_reserved1: None = ...
    _jsc_reserved2: None = ...
    _jsc_reserved3: None = ...
    _jsc_reserved4: None = ...
    _jsc_reserved5: None = ...
    _jsc_reserved6: None = ...
    _jsc_reserved7: None = ...

class Context(GObject.Object):
    """
    :Constructors:

    ::

        Context(**properties)
        new() -> JavaScriptCore.Context
        new_with_virtual_machine(vm:JavaScriptCore.VirtualMachine) -> JavaScriptCore.Context

    Object JSCContext

    Properties from JSCContext:
      virtual-machine -> JSCVirtualMachine: virtual-machine

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        virtual_machine: VirtualMachine

    props: Props = ...
    def __init__(self, virtual_machine: VirtualMachine = ...): ...
    def check_syntax(
        self, code: str, length: int, mode: CheckSyntaxMode, uri: str, line_number: int
    ) -> Tuple[CheckSyntaxResult, Exception]: ...
    def clear_exception(self) -> None: ...
    def evaluate(self, code: str, length: int) -> Value: ...
    def evaluate_in_object(
        self,
        code: str,
        length: int,
        object_instance: None,
        object_class: Optional[Class],
        uri: str,
        line_number: int,
    ) -> Tuple[Value, Value]: ...
    def evaluate_with_source_uri(
        self, code: str, length: int, uri: str, line_number: int
    ) -> Value: ...
    @staticmethod
    def get_current() -> Optional[Context]: ...
    def get_exception(self) -> Optional[Exception]: ...
    def get_global_object(self) -> Value: ...
    def get_value(self, name: str) -> Value: ...
    def get_virtual_machine(self) -> VirtualMachine: ...
    @classmethod
    def new(cls) -> Context: ...
    @classmethod
    def new_with_virtual_machine(cls, vm: VirtualMachine) -> Context: ...
    def pop_exception_handler(self) -> None: ...
    def push_exception_handler(
        self, handler: Callable[..., None], *user_data: Any
    ) -> None: ...
    def register_class(
        self,
        name: str,
        parent_class: Optional[Class] = None,
        vtable: Optional[ClassVTable] = None,
        destroy_notify: Optional[Callable[[None], None]] = None,
    ) -> Class: ...
    def set_value(self, name: str, value: Value) -> None: ...
    def throw(self, error_message: str) -> None: ...
    def throw_exception(self, exception: Exception) -> None: ...
    def throw_with_name(self, error_name: str, error_message: str) -> None: ...

class ContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContextClass()
    """

    parent_class: GObject.ObjectClass = ...

class Exception(GObject.Object):
    """
    :Constructors:

    ::

        Exception(**properties)
        new(context:JavaScriptCore.Context, message:str) -> JavaScriptCore.Exception
        new_with_name(context:JavaScriptCore.Context, name:str, message:str) -> JavaScriptCore.Exception

    Object JSCException

    Signals from GObject:
      notify (GParam)
    """

    def get_backtrace_string(self) -> Optional[str]: ...
    def get_column_number(self) -> int: ...
    def get_line_number(self) -> int: ...
    def get_message(self) -> str: ...
    def get_name(self) -> str: ...
    def get_source_uri(self) -> Optional[str]: ...
    @classmethod
    def new(cls, context: Context, message: str) -> Exception: ...
    @classmethod
    def new_with_name(cls, context: Context, name: str, message: str) -> Exception: ...
    def report(self) -> str: ...
    def to_string(self) -> str: ...

class ExceptionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ExceptionClass()
    """

    parent_class: GObject.ObjectClass = ...

class Value(GObject.Object):
    """
    :Constructors:

    ::

        Value(**properties)
        new_array_buffer(context:JavaScriptCore.Context, data=None, size:int, destroy_notify:GLib.DestroyNotify=None, user_data=None) -> JavaScriptCore.Value or None
        new_array_from_garray(context:JavaScriptCore.Context, array:list=None) -> JavaScriptCore.Value
        new_array_from_strv(context:JavaScriptCore.Context, strv:list) -> JavaScriptCore.Value
        new_boolean(context:JavaScriptCore.Context, value:bool) -> JavaScriptCore.Value
        new_from_json(context:JavaScriptCore.Context, json:str) -> JavaScriptCore.Value
        new_function_variadic(context:JavaScriptCore.Context, name:str=None, callback:GObject.Callback, user_data=None, return_type:GType) -> JavaScriptCore.Value
        new_function(context:JavaScriptCore.Context, name:str=None, callback:GObject.Callback, user_data=None, return_type:GType, parameter_types:list=None) -> JavaScriptCore.Value
        new_null(context:JavaScriptCore.Context) -> JavaScriptCore.Value
        new_number(context:JavaScriptCore.Context, number:float) -> JavaScriptCore.Value
        new_object(context:JavaScriptCore.Context, instance=None, jsc_class:JavaScriptCore.Class=None) -> JavaScriptCore.Value
        new_string(context:JavaScriptCore.Context, string:str=None) -> JavaScriptCore.Value
        new_string_from_bytes(context:JavaScriptCore.Context, bytes:GLib.Bytes=None) -> JavaScriptCore.Value
        new_typed_array(context:JavaScriptCore.Context, type:JavaScriptCore.TypedArrayType, length:int) -> JavaScriptCore.Value
        new_undefined(context:JavaScriptCore.Context) -> JavaScriptCore.Value

    Object JSCValue

    Properties from JSCValue:
      context -> JSCContext: context

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        context: Context

    props: Props = ...
    def __init__(self, context: Context = ...): ...
    def array_buffer_get_data(self, size: Optional[int] = None) -> None: ...
    def array_buffer_get_size(self) -> int: ...
    def constructor_call(
        self, parameters: Optional[Sequence[Value]] = None
    ) -> Value: ...
    def function_call(self, parameters: Optional[Sequence[Value]] = None) -> Value: ...
    def get_context(self) -> Context: ...
    def is_array(self) -> bool: ...
    def is_array_buffer(self) -> bool: ...
    def is_boolean(self) -> bool: ...
    def is_constructor(self) -> bool: ...
    def is_function(self) -> bool: ...
    def is_null(self) -> bool: ...
    def is_number(self) -> bool: ...
    def is_object(self) -> bool: ...
    def is_string(self) -> bool: ...
    def is_typed_array(self) -> bool: ...
    def is_undefined(self) -> bool: ...
    @classmethod
    def new_array_buffer(
        cls,
        context: Context,
        data: None,
        size: int,
        destroy_notify: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> Optional[Value]: ...
    @classmethod
    def new_array_from_garray(
        cls, context: Context, array: Optional[Sequence[Value]] = None
    ) -> Value: ...
    @classmethod
    def new_array_from_strv(cls, context: Context, strv: Sequence[str]) -> Value: ...
    @classmethod
    def new_boolean(cls, context: Context, value: bool) -> Value: ...
    @classmethod
    def new_from_json(cls, context: Context, json: str) -> Value: ...
    @classmethod
    def new_function(
        cls,
        context: Context,
        name: Optional[str],
        callback: Callable[..., None],
        return_type: Type,
        parameter_types: Optional[Sequence[Type]] = None,
        *user_data: Any,
    ) -> Value: ...
    @classmethod
    def new_function_variadic(
        cls,
        context: Context,
        name: Optional[str],
        callback: Callable[..., None],
        return_type: Type,
        *user_data: Any,
    ) -> Value: ...
    @classmethod
    def new_null(cls, context: Context) -> Value: ...
    @classmethod
    def new_number(cls, context: Context, number: float) -> Value: ...
    @classmethod
    def new_object(
        cls, context: Context, instance: None, jsc_class: Optional[Class] = None
    ) -> Value: ...
    @classmethod
    def new_string(cls, context: Context, string: Optional[str] = None) -> Value: ...
    @classmethod
    def new_string_from_bytes(
        cls, context: Context, bytes: Optional[GLib.Bytes] = None
    ) -> Value: ...
    @classmethod
    def new_typed_array(
        cls, context: Context, type: TypedArrayType, length: int
    ) -> Value: ...
    def new_typed_array_with_buffer(
        self, type: TypedArrayType, offset: int, length: int
    ) -> Value: ...
    @classmethod
    def new_undefined(cls, context: Context) -> Value: ...
    def object_define_property_accessor(
        self,
        property_name: str,
        flags: ValuePropertyFlags,
        property_type: Type,
        getter: Optional[Callable[..., None]] = None,
        setter: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def object_define_property_data(
        self,
        property_name: str,
        flags: ValuePropertyFlags,
        property_value: Optional[Value] = None,
    ) -> None: ...
    def object_delete_property(self, name: str) -> bool: ...
    def object_enumerate_properties(self) -> Optional[list[str]]: ...
    def object_get_property(self, name: str) -> Value: ...
    def object_get_property_at_index(self, index: int) -> Value: ...
    def object_has_property(self, name: str) -> bool: ...
    def object_invoke_method(
        self, name: str, parameters: Optional[Sequence[Value]] = None
    ) -> Value: ...
    def object_is_instance_of(self, name: str) -> bool: ...
    def object_set_property(self, name: str, property: Value) -> None: ...
    def object_set_property_at_index(self, index: int, property: Value) -> None: ...
    def to_boolean(self) -> bool: ...
    def to_double(self) -> float: ...
    def to_int32(self) -> int: ...
    def to_json(self, indent: int) -> str: ...
    def to_string(self) -> str: ...
    def to_string_as_bytes(self) -> GLib.Bytes: ...
    def typed_array_get_buffer(self) -> Value: ...
    def typed_array_get_data(self) -> int: ...
    def typed_array_get_length(self) -> int: ...
    def typed_array_get_offset(self) -> int: ...
    def typed_array_get_size(self) -> int: ...
    def typed_array_get_type(self) -> TypedArrayType: ...

class ValueClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ValueClass()
    """

    parent_class: GObject.ObjectClass = ...

class VirtualMachine(GObject.Object):
    """
    :Constructors:

    ::

        VirtualMachine(**properties)
        new() -> JavaScriptCore.VirtualMachine

    Object JSCVirtualMachine

    Signals from GObject:
      notify (GParam)
    """

    @classmethod
    def new(cls) -> VirtualMachine: ...

class VirtualMachineClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VirtualMachineClass()
    """

    parent_class: GObject.ObjectClass = ...

class WeakValue(GObject.Object):
    """
    :Constructors:

    ::

        WeakValue(**properties)
        new(value:JavaScriptCore.Value) -> JavaScriptCore.WeakValue

    Object JSCWeakValue

    Signals from JSCWeakValue:
      cleared ()

    Properties from JSCWeakValue:
      value -> JSCValue: value

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        value: Value

    props: Props = ...
    def __init__(self, value: Value = ...): ...
    def get_value(self) -> Value: ...
    @classmethod
    def new(cls, value: Value) -> WeakValue: ...

class WeakValueClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WeakValueClass()
    """

    parent_class: GObject.ObjectClass = ...

class ValuePropertyFlags(GObject.GFlags):
    CONFIGURABLE = 1
    ENUMERABLE = 2
    WRITABLE = 4

class CheckSyntaxMode(GObject.GEnum):
    MODULE = 1
    SCRIPT = 0

class CheckSyntaxResult(GObject.GEnum):
    IRRECOVERABLE_ERROR = 2
    OUT_OF_MEMORY_ERROR = 4
    RECOVERABLE_ERROR = 1
    STACK_OVERFLOW_ERROR = 5
    SUCCESS = 0
    UNTERMINATED_LITERAL_ERROR = 3

class OptionType(GObject.GEnum):
    BOOLEAN = 0
    DOUBLE = 4
    INT = 1
    RANGE_STRING = 6
    SIZE = 3
    STRING = 5
    UINT = 2

class TypedArrayType(GObject.GEnum):
    FLOAT32 = 10
    FLOAT64 = 11
    INT16 = 2
    INT32 = 3
    INT64 = 4
    INT8 = 1
    NONE = 0
    UINT16 = 7
    UINT32 = 8
    UINT64 = 9
    UINT8 = 5
    UINT8_CLAMPED = 6
