from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import Gio
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import GtkSource

_lock = ...  # FIXME Constant
_namespace: str = "Spelling"
_version: str = "1"

def init() -> None: ...

class Checker(GObject.Object):
    """
    :Constructors:

    ::

        Checker(**properties)
        new(provider:Spelling.Provider, language:str) -> Spelling.Checker

    Object SpellingChecker

    Properties from SpellingChecker:
      language -> gchararray: Language
        The language code
      provider -> SpellingProvider: Provider
        The spell check provider

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        language: Optional[str]
        provider: Provider

    props: Props = ...
    def __init__(self, language: str = ..., provider: Provider = ...): ...
    def add_word(self, word: str) -> None: ...
    def check_word(self, word: str, word_len: int) -> bool: ...
    @staticmethod
    def get_default() -> Checker: ...
    def get_extra_word_chars(self) -> str: ...
    def get_language(self) -> Optional[str]: ...
    def get_provider(self) -> Provider: ...
    def ignore_word(self, word: str) -> None: ...
    def list_corrections(self, word: str) -> Optional[list[str]]: ...
    @classmethod
    def new(cls, provider: Provider, language: str) -> Checker: ...
    def set_language(self, language: str) -> None: ...

class CheckerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CheckerClass()
    """

    parent_class: GObject.ObjectClass = ...

class Language(GObject.Object):
    """
    :Constructors:

    ::

        Language(**properties)

    Object SpellingLanguage

    Properties from SpellingLanguage:
      code -> gchararray: Code
        The language code

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        code: str

    props: Props = ...
    def __init__(self, code: str = ...): ...
    def add_word(self, word: str) -> None: ...
    def contains_word(self, word: str, word_len: int) -> bool: ...
    def get_code(self) -> str: ...
    def get_extra_word_chars(self) -> str: ...
    def ignore_word(self, word: str) -> None: ...
    def list_corrections(self, word: str, word_len: int) -> Optional[list[str]]: ...

class LanguageClass(GObject.GPointer): ...

class LanguageInfo(GObject.Object):
    """
    :Constructors:

    ::

        LanguageInfo(**properties)

    Object SpellingLanguageInfo

    Properties from SpellingLanguageInfo:
      code -> gchararray: Code
        The language code
      group -> gchararray: Group
        A group for sorting, usually the country name
      name -> gchararray: Name
        The name of the language

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        code: str
        group: str
        name: str

    props: Props = ...
    def __init__(self, code: str = ..., group: str = ..., name: str = ...): ...
    def get_code(self) -> str: ...
    def get_group(self) -> str: ...
    def get_name(self) -> str: ...

class LanguageInfoClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LanguageInfoClass()
    """

    parent_class: GObject.ObjectClass = ...

class Provider(GObject.Object):
    """
    :Constructors:

    ::

        Provider(**properties)

    Object SpellingProvider

    Properties from SpellingProvider:
      display-name -> gchararray: Display Name
        Display Name

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        display_name: str

    props: Props = ...
    def __init__(self, display_name: str = ...): ...
    @staticmethod
    def get_default() -> Provider: ...
    def get_default_code(self) -> str: ...
    def get_display_name(self) -> str: ...
    def get_language(self, language: str) -> Optional[Language]: ...
    def list_languages(self) -> list[LanguageInfo]: ...
    def supports_language(self, language: str) -> bool: ...

class ProviderClass(GObject.GPointer): ...

class TextBufferAdapter(GObject.Object, Gio.ActionGroup):
    """
    :Constructors:

    ::

        TextBufferAdapter(**properties)
        new(buffer:GtkSource.Buffer, checker:Spelling.Checker) -> Spelling.TextBufferAdapter

    Object SpellingTextBufferAdapter

    Properties from SpellingTextBufferAdapter:
      buffer -> GtkSourceBuffer: Buffer
        Buffer
      checker -> SpellingChecker: Checker
        Checker
      enabled -> gboolean: Enabled
        If spellcheck is enabled
      language -> gchararray: Language
        The language code such as en_US

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        buffer: Optional[GtkSource.Buffer]
        checker: Optional[Checker]
        enabled: bool
        language: str

    props: Props = ...
    def __init__(
        self,
        buffer: GtkSource.Buffer = ...,
        checker: Checker = ...,
        enabled: bool = ...,
        language: str = ...,
    ): ...
    def get_buffer(self) -> Optional[GtkSource.Buffer]: ...
    def get_checker(self) -> Optional[Checker]: ...
    def get_enabled(self) -> bool: ...
    def get_language(self) -> str: ...
    def get_menu_model(self) -> Gio.MenuModel: ...
    def get_tag(self) -> Optional[Gtk.TextTag]: ...
    def invalidate_all(self) -> None: ...
    @classmethod
    def new(cls, buffer: GtkSource.Buffer, checker: Checker) -> TextBufferAdapter: ...
    def set_checker(self, checker: Checker) -> None: ...
    def set_enabled(self, enabled: bool) -> None: ...
    def set_language(self, language: str) -> None: ...

class TextBufferAdapterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TextBufferAdapterClass()
    """

    parent_class: GObject.ObjectClass = ...
