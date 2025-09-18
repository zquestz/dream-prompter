from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Pango

MAJOR_VERSION: int = 5
MICRO_VERSION: int = 1
MINOR_VERSION: int = 12
_lock = ...  # FIXME Constant
_namespace: str = "GtkSource"
_version: str = "5"

def check_version(major: int, minor: int, micro: int) -> bool: ...
def encoding_get_all() -> list[Encoding]: ...
def encoding_get_current() -> Encoding: ...
def encoding_get_default_candidates() -> list[Encoding]: ...
def encoding_get_from_charset(charset: str) -> Optional[Encoding]: ...
def encoding_get_utf8() -> Encoding: ...
def file_loader_error_quark() -> int: ...
def file_saver_error_quark() -> int: ...
def finalize() -> None: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def init() -> None: ...
def scheduler_add(callback: Callable[..., bool], *user_data: Any) -> int: ...
def scheduler_add_full(callback: Callable[..., bool], *user_data: Any) -> int: ...
def scheduler_remove(handler_id: int) -> None: ...
def utils_escape_search_text(text: str) -> str: ...
def utils_unescape_search_text(text: str) -> str: ...

class Buffer(Gtk.TextBuffer):
    """
    :Constructors:

    ::

        Buffer(**properties)
        new(table:Gtk.TextTagTable=None) -> GtkSource.Buffer
        new_with_language(language:GtkSource.Language) -> GtkSource.Buffer

    Object GtkSourceBuffer

    Signals from GtkSourceBuffer:
      cursor-moved ()
      highlight-updated (GtkTextIter, GtkTextIter)
      source-mark-updated (GtkTextMark)
      bracket-matched (GtkTextIter, GtkSourceBracketMatchType)

    Properties from GtkSourceBuffer:
      highlight-matching-brackets -> gboolean: Highlight Matching Brackets
        Whether to highlight matching brackets
      highlight-syntax -> gboolean: Highlight Syntax
        Whether to highlight syntax in the buffer
      implicit-trailing-newline -> gboolean: Implicit trailing newline

      language -> GtkSourceLanguage: Language
        Language object to get highlighting patterns from
      loading -> gboolean: Loading
        If a GtkSourceFileLoader is loading the buffer
      style-scheme -> GtkSourceStyleScheme: Style scheme
        Style scheme

    Signals from GtkTextBuffer:
      changed ()
      insert-text (GtkTextIter, gchararray, gint)
      insert-paintable (GtkTextIter, GdkPaintable)
      insert-child-anchor (GtkTextIter, GtkTextChildAnchor)
      delete-range (GtkTextIter, GtkTextIter)
      modified-changed ()
      mark-set (GtkTextIter, GtkTextMark)
      mark-deleted (GtkTextMark)
      apply-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      remove-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      begin-user-action ()
      end-user-action ()
      paste-done (GdkClipboard)
      redo ()
      undo ()

    Properties from GtkTextBuffer:
      tag-table -> GtkTextTagTable: tag-table
      text -> gchararray: text
      has-selection -> gboolean: has-selection
      cursor-position -> gint: cursor-position
      can-undo -> gboolean: can-undo
      can-redo -> gboolean: can-redo
      enable-undo -> gboolean: enable-undo

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        highlight_matching_brackets: bool
        highlight_syntax: bool
        implicit_trailing_newline: bool
        language: Optional[Language]
        loading: bool
        style_scheme: Optional[StyleScheme]
        can_redo: bool
        can_undo: bool
        cursor_position: int
        enable_undo: bool
        has_selection: bool
        tag_table: Gtk.TextTagTable
        text: str

    props: Props = ...
    parent_instance: Gtk.TextBuffer = ...
    def __init__(
        self,
        highlight_matching_brackets: bool = ...,
        highlight_syntax: bool = ...,
        implicit_trailing_newline: bool = ...,
        language: Optional[Language] = ...,
        style_scheme: Optional[StyleScheme] = ...,
        enable_undo: bool = ...,
        tag_table: Gtk.TextTagTable = ...,
        text: str = ...,
    ): ...
    def backward_iter_to_source_mark(
        self, category: Optional[str] = None
    ) -> Tuple[bool, Gtk.TextIter]: ...
    def change_case(
        self, case_type: ChangeCaseType, start: Gtk.TextIter, end: Gtk.TextIter
    ) -> None: ...
    def create_source_mark(
        self, name: Optional[str], category: str, where: Gtk.TextIter
    ) -> Mark: ...
    def do_bracket_matched(
        self, iter: Gtk.TextIter, state: BracketMatchType
    ) -> None: ...
    def ensure_highlight(self, start: Gtk.TextIter, end: Gtk.TextIter) -> None: ...
    def forward_iter_to_source_mark(
        self, category: Optional[str] = None
    ) -> Tuple[bool, Gtk.TextIter]: ...
    def get_context_classes_at_iter(self, iter: Gtk.TextIter) -> list[str]: ...
    def get_highlight_matching_brackets(self) -> bool: ...
    def get_highlight_syntax(self) -> bool: ...
    def get_implicit_trailing_newline(self) -> bool: ...
    def get_language(self) -> Optional[Language]: ...
    def get_loading(self) -> bool: ...
    def get_source_marks_at_iter(
        self, iter: Gtk.TextIter, category: Optional[str] = None
    ) -> list[Mark]: ...
    def get_source_marks_at_line(
        self, line: int, category: Optional[str] = None
    ) -> list[Mark]: ...
    def get_style_scheme(self) -> Optional[StyleScheme]: ...
    def iter_backward_to_context_class_toggle(
        self, context_class: str
    ) -> Tuple[bool, Gtk.TextIter]: ...
    def iter_forward_to_context_class_toggle(
        self, context_class: str
    ) -> Tuple[bool, Gtk.TextIter]: ...
    def iter_has_context_class(
        self, iter: Gtk.TextIter, context_class: str
    ) -> bool: ...
    def join_lines(self, start: Gtk.TextIter, end: Gtk.TextIter) -> None: ...
    @classmethod
    def new(cls, table: Optional[Gtk.TextTagTable] = None) -> Buffer: ...
    @classmethod
    def new_with_language(cls, language: Language) -> Buffer: ...
    def remove_source_marks(
        self, start: Gtk.TextIter, end: Gtk.TextIter, category: Optional[str] = None
    ) -> None: ...
    def set_highlight_matching_brackets(self, highlight: bool) -> None: ...
    def set_highlight_syntax(self, highlight: bool) -> None: ...
    def set_implicit_trailing_newline(
        self, implicit_trailing_newline: bool
    ) -> None: ...
    def set_language(self, language: Optional[Language] = None) -> None: ...
    def set_style_scheme(self, scheme: Optional[StyleScheme] = None) -> None: ...
    def sort_lines(
        self, start: Gtk.TextIter, end: Gtk.TextIter, flags: SortFlags, column: int
    ) -> None: ...

class BufferClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BufferClass()
    """

    parent_class: Gtk.TextBufferClass = ...
    bracket_matched: Callable[[Buffer, Gtk.TextIter, BracketMatchType], None] = ...
    _reserved: list[None] = ...

class Completion(GObject.Object):
    """
    :Constructors:

    ::

        Completion(**properties)

    Object GtkSourceCompletion

    Signals from GtkSourceCompletion:
      provider-added (GtkSourceCompletionProvider)
      provider-removed (GtkSourceCompletionProvider)
      hide ()
      show ()

    Properties from GtkSourceCompletion:
      buffer -> GtkTextView: Buffer
        The buffer for the view
      page-size -> guint: Number of Rows
        Number of rows to display to the user
      remember-info-visibility -> gboolean: Remember Info Visibility
        Remember Info Visibility
      select-on-show -> gboolean: Select on Show
        Select on Show
      show-icons -> gboolean: Show Icons
        If icons should be shown in the completion results
      view -> GtkSourceView: View
        The text view for which to provide completion

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        buffer: Gtk.TextView
        page_size: int
        remember_info_visibility: bool
        select_on_show: bool
        show_icons: bool
        view: View

    props: Props = ...
    def __init__(
        self,
        page_size: int = ...,
        remember_info_visibility: bool = ...,
        select_on_show: bool = ...,
        show_icons: bool = ...,
        view: View = ...,
    ): ...
    def add_provider(self, provider: CompletionProvider) -> None: ...
    def block_interactive(self) -> None: ...
    @staticmethod
    def fuzzy_highlight(
        haystack: str, casefold_query: str
    ) -> Optional[Pango.AttrList]: ...
    @staticmethod
    def fuzzy_match(
        haystack: Optional[str], casefold_needle: str
    ) -> Tuple[bool, int]: ...
    def get_buffer(self) -> Buffer: ...
    def get_page_size(self) -> int: ...
    def get_view(self) -> View: ...
    def hide(self) -> None: ...
    def remove_provider(self, provider: CompletionProvider) -> None: ...
    def set_page_size(self, page_size: int) -> None: ...
    def show(self) -> None: ...
    def unblock_interactive(self) -> None: ...

class CompletionCell(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        CompletionCell(**properties)

    Object GtkSourceCompletionCell

    Properties from GtkSourceCompletionCell:
      column -> GtkSourceCompletionColumn: Column
        Column
      markup -> gchararray: Markup
        Markup
      paintable -> GdkPaintable: Paintable
        Paintable
      text -> gchararray: Text
        Text
      widget -> GtkWidget: Widget
        Widget

    Signals from GtkWidget:
      hide ()
      show ()
      destroy ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
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
        column: CompletionColumn
        markup: str
        paintable: Gdk.Paintable
        text: Optional[str]
        widget: Optional[Gtk.Widget]
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
        column: CompletionColumn = ...,
        markup: str = ...,
        paintable: Gdk.Paintable = ...,
        text: Optional[str] = ...,
        widget: Gtk.Widget = ...,
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
    def get_column(self) -> CompletionColumn: ...
    def get_widget(self) -> Optional[Gtk.Widget]: ...
    def set_gicon(self, gicon: Gio.Icon) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_markup(self, markup: str) -> None: ...
    def set_paintable(self, paintable: Gdk.Paintable) -> None: ...
    def set_text(self, text: Optional[str] = None) -> None: ...
    def set_text_with_attributes(self, text: str, attrs: Pango.AttrList) -> None: ...
    def set_widget(self, child: Gtk.Widget) -> None: ...

class CompletionCellClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionCellClass()
    """

    parent_class: Gtk.WidgetClass = ...

class CompletionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionClass()
    """

    parent_class: GObject.ObjectClass = ...

class CompletionContext(GObject.Object, Gio.ListModel):
    """
    :Constructors:

    ::

        CompletionContext(**properties)

    Object GtkSourceCompletionContext

    Signals from GtkSourceCompletionContext:
      provider-model-changed (GtkSourceCompletionProvider, GListModel)

    Properties from GtkSourceCompletionContext:
      busy -> gboolean: Busy
        Is the completion context busy populating
      completion -> GtkSourceCompletion: Completion
        Completion
      empty -> gboolean: Empty
        If the context has no results

    Signals from GListModel:
      items-changed (guint, guint, guint)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        busy: bool
        completion: Optional[Completion]
        empty: bool

    props: Props = ...
    def __init__(self, completion: Completion = ...): ...
    def get_activation(self) -> CompletionActivation: ...
    def get_bounds(self) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter]: ...
    def get_buffer(self) -> Optional[Buffer]: ...
    def get_busy(self) -> bool: ...
    def get_completion(self) -> Optional[Completion]: ...
    def get_empty(self) -> bool: ...
    def get_language(self) -> Optional[Language]: ...
    def get_proposals_for_provider(
        self, provider: CompletionProvider
    ) -> Optional[Gio.ListModel]: ...
    def get_view(self) -> Optional[View]: ...
    def get_word(self) -> str: ...
    def list_providers(self) -> Gio.ListModel: ...
    def set_proposals_for_provider(
        self, provider: CompletionProvider, results: Optional[Gio.ListModel] = None
    ) -> None: ...

class CompletionContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionContextClass()
    """

    parent_class: GObject.ObjectClass = ...

class CompletionProposal(GObject.GInterface):
    """
    Interface GtkSourceCompletionProposal

    Signals from GObject:
      notify (GParam)
    """

    def get_typed_text(self) -> Optional[str]: ...

class CompletionProposalInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionProposalInterface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_typed_text: Callable[[CompletionProposal], Optional[str]] = ...

class CompletionProvider(GObject.GInterface):
    """
    Interface GtkSourceCompletionProvider

    Signals from GObject:
      notify (GParam)
    """

    def activate(
        self, context: CompletionContext, proposal: CompletionProposal
    ) -> None: ...
    def display(
        self,
        context: CompletionContext,
        proposal: CompletionProposal,
        cell: CompletionCell,
    ) -> None: ...
    def get_priority(self, context: CompletionContext) -> int: ...
    def get_title(self) -> Optional[str]: ...
    def is_trigger(self, iter: Gtk.TextIter, ch: str) -> bool: ...
    def key_activates(
        self,
        context: CompletionContext,
        proposal: CompletionProposal,
        keyval: int,
        state: Gdk.ModifierType,
    ) -> bool: ...
    def list_alternates(
        self, context: CompletionContext, proposal: CompletionProposal
    ) -> Optional[list[CompletionProposal]]: ...
    def populate_async(
        self,
        context: CompletionContext,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def populate_finish(self, result: Gio.AsyncResult) -> Gio.ListModel: ...
    def refilter(self, context: CompletionContext, model: Gio.ListModel) -> None: ...

class CompletionProviderInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionProviderInterface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_title: Callable[[CompletionProvider], Optional[str]] = ...
    get_priority: Callable[[CompletionProvider, CompletionContext], int] = ...
    is_trigger: Callable[[CompletionProvider, Gtk.TextIter, str], bool] = ...
    key_activates: Callable[
        [
            CompletionProvider,
            CompletionContext,
            CompletionProposal,
            int,
            Gdk.ModifierType,
        ],
        bool,
    ] = ...
    populate: None = ...
    populate_async: Callable[..., None] = ...
    populate_finish: Callable[[CompletionProvider, Gio.AsyncResult], Gio.ListModel] = (
        ...
    )
    refilter: Callable[[CompletionProvider, CompletionContext, Gio.ListModel], None] = (
        ...
    )
    display: Callable[
        [CompletionProvider, CompletionContext, CompletionProposal, CompletionCell],
        None,
    ] = ...
    activate: Callable[
        [CompletionProvider, CompletionContext, CompletionProposal], None
    ] = ...
    list_alternates: Callable[
        [CompletionProvider, CompletionContext, CompletionProposal],
        Optional[list[CompletionProposal]],
    ] = ...

class CompletionSnippets(GObject.Object, CompletionProvider):
    """
    :Constructors:

    ::

        CompletionSnippets(**properties)
        new() -> GtkSource.CompletionSnippets

    Object GtkSourceCompletionSnippets

    Properties from GtkSourceCompletionSnippets:
      title -> gchararray: Title
        The provider title
      priority -> gint: Priority
        Provider priority

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        priority: int
        title: str

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, priority: int = ..., title: str = ...): ...
    @classmethod
    def new(cls) -> CompletionSnippets: ...

class CompletionSnippetsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionSnippetsClass()
    """

    parent_class: GObject.ObjectClass = ...
    _reserved: list[None] = ...

class CompletionWords(GObject.Object, CompletionProvider):
    """
    :Constructors:

    ::

        CompletionWords(**properties)
        new(title:str=None) -> GtkSource.CompletionWords

    Object GtkSourceCompletionWords

    Properties from GtkSourceCompletionWords:
      title -> gchararray: Title
        The provider title
      proposals-batch-size -> guint: Proposals Batch Size
        Number of proposals added in one batch
      scan-batch-size -> guint: Scan Batch Size
        Number of lines scanned in one batch
      minimum-word-size -> guint: Minimum Word Size
        The minimum word size to complete
      priority -> gint: Priority
        Provider priority

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        minimum_word_size: int
        priority: int
        proposals_batch_size: int
        scan_batch_size: int
        title: str

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self,
        minimum_word_size: int = ...,
        priority: int = ...,
        proposals_batch_size: int = ...,
        scan_batch_size: int = ...,
        title: str = ...,
    ): ...
    @classmethod
    def new(cls, title: Optional[str] = None) -> CompletionWords: ...
    def register(self, buffer: Gtk.TextBuffer) -> None: ...
    def unregister(self, buffer: Gtk.TextBuffer) -> None: ...

class CompletionWordsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CompletionWordsClass()
    """

    parent_class: GObject.ObjectClass = ...
    _reserved: list[None] = ...

class Encoding(GObject.GBoxed):
    def copy(self) -> Encoding: ...
    def free(self) -> None: ...
    @staticmethod
    def get_all() -> list[Encoding]: ...
    def get_charset(self) -> str: ...
    @staticmethod
    def get_current() -> Encoding: ...
    @staticmethod
    def get_default_candidates() -> list[Encoding]: ...
    @staticmethod
    def get_from_charset(charset: str) -> Optional[Encoding]: ...
    def get_name(self) -> str: ...
    @staticmethod
    def get_utf8() -> Encoding: ...
    def to_string(self) -> str: ...

class File(GObject.Object):
    """
    :Constructors:

    ::

        File(**properties)
        new() -> GtkSource.File

    Object GtkSourceFile

    Properties from GtkSourceFile:
      location -> GFile: Location

      encoding -> GtkSourceEncoding: Encoding

      newline-type -> GtkSourceNewlineType: Newline type

      compression-type -> GtkSourceCompressionType: Compression type

      read-only -> gboolean: Read Only


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        compression_type: CompressionType
        encoding: Encoding
        location: Gio.File
        newline_type: NewlineType
        read_only: bool

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, location: Optional[Gio.File] = ...): ...
    def check_file_on_disk(self) -> None: ...
    def get_compression_type(self) -> CompressionType: ...
    def get_encoding(self) -> Encoding: ...
    def get_location(self) -> Gio.File: ...
    def get_newline_type(self) -> NewlineType: ...
    def is_deleted(self) -> bool: ...
    def is_externally_modified(self) -> bool: ...
    def is_local(self) -> bool: ...
    def is_readonly(self) -> bool: ...
    @classmethod
    def new(cls) -> File: ...
    def set_location(self, location: Optional[Gio.File] = None) -> None: ...

class FileClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileClass()
    """

    parent_class: GObject.ObjectClass = ...
    _reserved: list[None] = ...

class FileLoader(GObject.Object):
    """
    :Constructors:

    ::

        FileLoader(**properties)
        new(buffer:GtkSource.Buffer, file:GtkSource.File) -> GtkSource.FileLoader
        new_from_stream(buffer:GtkSource.Buffer, file:GtkSource.File, stream:Gio.InputStream) -> GtkSource.FileLoader

    Object GtkSourceFileLoader

    Properties from GtkSourceFileLoader:
      buffer -> GtkSourceBuffer: GtkSourceBuffer

      file -> GtkSourceFile: GtkSourceFile

      location -> GFile: Location

      input-stream -> GInputStream: Input stream


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        buffer: Buffer
        file: File
        input_stream: Optional[Gio.InputStream]
        location: Optional[Gio.File]

    props: Props = ...
    def __init__(
        self,
        buffer: Buffer = ...,
        file: File = ...,
        input_stream: Gio.InputStream = ...,
        location: Gio.File = ...,
    ): ...
    def get_buffer(self) -> Buffer: ...
    def get_compression_type(self) -> CompressionType: ...
    def get_encoding(self) -> Encoding: ...
    def get_file(self) -> File: ...
    def get_input_stream(self) -> Optional[Gio.InputStream]: ...
    def get_location(self) -> Optional[Gio.File]: ...
    def get_newline_type(self) -> NewlineType: ...
    def load_async(
        self,
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        progress_callback: Optional[Callable[..., None]] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def load_finish(self, result: Gio.AsyncResult) -> bool: ...
    @classmethod
    def new(cls, buffer: Buffer, file: File) -> FileLoader: ...
    @classmethod
    def new_from_stream(
        cls, buffer: Buffer, file: File, stream: Gio.InputStream
    ) -> FileLoader: ...
    def set_candidate_encodings(self, candidate_encodings: list[Encoding]) -> None: ...

class FileLoaderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileLoaderClass()
    """

    parent_class: GObject.ObjectClass = ...

class FileSaver(GObject.Object):
    """
    :Constructors:

    ::

        FileSaver(**properties)
        new(buffer:GtkSource.Buffer, file:GtkSource.File) -> GtkSource.FileSaver
        new_with_target(buffer:GtkSource.Buffer, file:GtkSource.File, target_location:Gio.File) -> GtkSource.FileSaver

    Object GtkSourceFileSaver

    Properties from GtkSourceFileSaver:
      buffer -> GtkSourceBuffer: GtkSourceBuffer

      file -> GtkSourceFile: GtkSourceFile

      location -> GFile: Location

      encoding -> GtkSourceEncoding: Encoding

      newline-type -> GtkSourceNewlineType: Newline type

      compression-type -> GtkSourceCompressionType: Compression type

      flags -> GtkSourceFileSaverFlags: Flags


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        buffer: Buffer
        compression_type: CompressionType
        encoding: Encoding
        file: File
        flags: FileSaverFlags
        location: Gio.File
        newline_type: NewlineType

    props: Props = ...
    def __init__(
        self,
        buffer: Buffer = ...,
        compression_type: CompressionType = ...,
        encoding: Optional[Encoding] = ...,
        file: File = ...,
        flags: FileSaverFlags = ...,
        location: Gio.File = ...,
        newline_type: NewlineType = ...,
    ): ...
    def get_buffer(self) -> Buffer: ...
    def get_compression_type(self) -> CompressionType: ...
    def get_encoding(self) -> Encoding: ...
    def get_file(self) -> File: ...
    def get_flags(self) -> FileSaverFlags: ...
    def get_location(self) -> Gio.File: ...
    def get_newline_type(self) -> NewlineType: ...
    @classmethod
    def new(cls, buffer: Buffer, file: File) -> FileSaver: ...
    @classmethod
    def new_with_target(
        cls, buffer: Buffer, file: File, target_location: Gio.File
    ) -> FileSaver: ...
    def save_async(
        self,
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        progress_callback: Optional[Callable[..., None]] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def save_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_compression_type(self, compression_type: CompressionType) -> None: ...
    def set_encoding(self, encoding: Optional[Encoding] = None) -> None: ...
    def set_flags(self, flags: FileSaverFlags) -> None: ...
    def set_newline_type(self, newline_type: NewlineType) -> None: ...

class FileSaverClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileSaverClass()
    """

    parent_class: GObject.ObjectClass = ...

class Gutter(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Gutter(**properties)

    Object GtkSourceGutter

    Properties from GtkSourceGutter:
      view -> GtkSourceView: View

      window-type -> GtkTextWindowType: Window Type
        The gutters' text window type

    Signals from GtkWidget:
      hide ()
      show ()
      destroy ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
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
        view: View
        window_type: Gtk.TextWindowType
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
        view: View = ...,
        window_type: Gtk.TextWindowType = ...,
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
    def get_view(self) -> View: ...
    def insert(self, renderer: GutterRenderer, position: int) -> bool: ...
    def remove(self, renderer: GutterRenderer) -> None: ...
    def reorder(self, renderer: GutterRenderer, position: int) -> None: ...

class GutterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GutterClass()
    """

    parent_class: Gtk.WidgetClass = ...

class GutterLines(GObject.Object):
    """
    :Constructors:

    ::

        GutterLines(**properties)

    Object GtkSourceGutterLines

    Signals from GObject:
      notify (GParam)
    """

    def add_class(self, line: int, name: str) -> None: ...
    def add_qclass(self, line: int, qname: int) -> None: ...
    def get_buffer(self) -> Gtk.TextBuffer: ...
    def get_first(self) -> int: ...
    def get_iter_at_line(self, line: int) -> Gtk.TextIter: ...
    def get_last(self) -> int: ...
    def get_line_yrange(
        self, line: int, mode: GutterRendererAlignmentMode
    ) -> Tuple[int, int]: ...
    def get_view(self) -> Gtk.TextView: ...
    def has_any_class(self, line: int) -> bool: ...
    def has_class(self, line: int, name: str) -> bool: ...
    def has_qclass(self, line: int, qname: int) -> bool: ...
    def is_cursor(self, line: int) -> bool: ...
    def is_prelit(self, line: int) -> bool: ...
    def is_selected(self, line: int) -> bool: ...
    def remove_class(self, line: int, name: str) -> None: ...
    def remove_qclass(self, line: int, qname: int) -> None: ...

class GutterLinesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GutterLinesClass()
    """

    parent_class: GObject.ObjectClass = ...

class GutterRenderer(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        GutterRenderer(**properties)

    Object GtkSourceGutterRenderer

    Signals from GtkSourceGutterRenderer:
      activate (GtkTextIter, GdkRectangle, guint, GdkModifierType, gint)
      query-activatable (GtkTextIter, GdkRectangle) -> gboolean
      query-data (GObject, guint)

    Properties from GtkSourceGutterRenderer:
      alignment-mode -> GtkSourceGutterRendererAlignmentMode: Alignment Mode
        The alignment mode
      lines -> GtkSourceGutterLines: Lines
        Information about the lines to render
      view -> GtkTextView: The View
        The view
      xalign -> gfloat: X Alignment
        The x-alignment
      xpad -> gint: X Padding
        The x-padding
      yalign -> gfloat: Y Alignment
        The y-alignment
      ypad -> gint: Y Padding
        The y-padding

    Signals from GtkWidget:
      hide ()
      show ()
      destroy ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
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
        alignment_mode: GutterRendererAlignmentMode
        lines: GutterLines
        view: Gtk.TextView
        xalign: float
        xpad: int
        yalign: float
        ypad: int
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
        alignment_mode: GutterRendererAlignmentMode = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
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
    def activate(
        self,
        iter: Gtk.TextIter,
        area: Gdk.Rectangle,
        button: int,
        state: Gdk.ModifierType,
        n_presses: int,
    ) -> None: ...
    def align_cell(
        self, line: int, width: float, height: float
    ) -> Tuple[float, float]: ...
    def do_activate(
        self,
        iter: Gtk.TextIter,
        area: Gdk.Rectangle,
        button: int,
        state: Gdk.ModifierType,
        n_presses: int,
    ) -> None: ...
    def do_begin(self, lines: GutterLines) -> None: ...
    def do_change_buffer(self, old_buffer: Optional[Buffer] = None) -> None: ...
    def do_change_view(self, old_view: Optional[View] = None) -> None: ...
    def do_end(self) -> None: ...
    def do_query_activatable(self, iter: Gtk.TextIter, area: Gdk.Rectangle) -> bool: ...
    def do_query_data(self, lines: GutterLines, line: int) -> None: ...
    def do_snapshot_line(
        self, snapshot: Gtk.Snapshot, lines: GutterLines, line: int
    ) -> None: ...
    def get_alignment_mode(self) -> GutterRendererAlignmentMode: ...
    def get_buffer(self) -> Optional[Buffer]: ...
    def get_view(self) -> View: ...
    def get_xalign(self) -> float: ...
    def get_xpad(self) -> int: ...
    def get_yalign(self) -> float: ...
    def get_ypad(self) -> int: ...
    def query_activatable(self, iter: Gtk.TextIter, area: Gdk.Rectangle) -> bool: ...
    def set_alignment_mode(self, mode: GutterRendererAlignmentMode) -> None: ...
    def set_xalign(self, xalign: float) -> None: ...
    def set_xpad(self, xpad: int) -> None: ...
    def set_yalign(self, yalign: float) -> None: ...
    def set_ypad(self, ypad: int) -> None: ...

class GutterRendererClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GutterRendererClass()
    """

    parent_class: Gtk.WidgetClass = ...
    query_data: Callable[[GutterRenderer, GutterLines, int], None] = ...
    begin: Callable[[GutterRenderer, GutterLines], None] = ...
    snapshot_line: Callable[[GutterRenderer, Gtk.Snapshot, GutterLines, int], None] = (
        ...
    )
    end: Callable[[GutterRenderer], None] = ...
    change_view: Callable[[GutterRenderer, Optional[View]], None] = ...
    change_buffer: Callable[[GutterRenderer, Optional[Buffer]], None] = ...
    query_activatable: Callable[[GutterRenderer, Gtk.TextIter, Gdk.Rectangle], bool] = (
        ...
    )
    activate: Callable[
        [GutterRenderer, Gtk.TextIter, Gdk.Rectangle, int, Gdk.ModifierType, int], None
    ] = ...
    _reserved: list[None] = ...

class GutterRendererPixbuf(
    GutterRenderer, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        GutterRendererPixbuf(**properties)
        new() -> GtkSource.GutterRenderer

    Object GtkSourceGutterRendererPixbuf

    Properties from GtkSourceGutterRendererPixbuf:
      pixbuf -> GdkPixbuf: Pixbuf
        The pixbuf
      icon-name -> gchararray: Icon Name
        The icon name
      gicon -> GIcon: GIcon
        The gicon
      paintable -> GdkPaintable: Paintable
        The paintable

    Signals from GtkSourceGutterRenderer:
      activate (GtkTextIter, GdkRectangle, guint, GdkModifierType, gint)
      query-activatable (GtkTextIter, GdkRectangle) -> gboolean
      query-data (GObject, guint)

    Properties from GtkSourceGutterRenderer:
      alignment-mode -> GtkSourceGutterRendererAlignmentMode: Alignment Mode
        The alignment mode
      lines -> GtkSourceGutterLines: Lines
        Information about the lines to render
      view -> GtkTextView: The View
        The view
      xalign -> gfloat: X Alignment
        The x-alignment
      xpad -> gint: X Padding
        The x-padding
      yalign -> gfloat: Y Alignment
        The y-alignment
      ypad -> gint: Y Padding
        The y-padding

    Signals from GtkWidget:
      hide ()
      show ()
      destroy ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
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
        gicon: Gio.Icon
        icon_name: str
        paintable: Optional[Gdk.Paintable]
        pixbuf: GdkPixbuf.Pixbuf
        alignment_mode: GutterRendererAlignmentMode
        lines: GutterLines
        view: Gtk.TextView
        xalign: float
        xpad: int
        yalign: float
        ypad: int
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
    parent_instance: GutterRenderer = ...
    def __init__(
        self,
        gicon: Optional[Gio.Icon] = ...,
        icon_name: Optional[str] = ...,
        paintable: Optional[Gdk.Paintable] = ...,
        pixbuf: Optional[GdkPixbuf.Pixbuf] = ...,
        alignment_mode: GutterRendererAlignmentMode = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
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
    def get_gicon(self) -> Gio.Icon: ...
    def get_icon_name(self) -> str: ...
    def get_paintable(self) -> Optional[Gdk.Paintable]: ...
    def get_pixbuf(self) -> GdkPixbuf.Pixbuf: ...
    @classmethod
    def new(cls) -> GutterRendererPixbuf: ...
    def overlay_paintable(self, paintable: Gdk.Paintable) -> None: ...
    def set_gicon(self, icon: Optional[Gio.Icon] = None) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_paintable(self, paintable: Optional[Gdk.Paintable] = None) -> None: ...
    def set_pixbuf(self, pixbuf: Optional[GdkPixbuf.Pixbuf] = None) -> None: ...

class GutterRendererPixbufClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GutterRendererPixbufClass()
    """

    parent_class: GutterRendererClass = ...
    _reserved: list[None] = ...

class GutterRendererText(
    GutterRenderer, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        GutterRendererText(**properties)
        new() -> GtkSource.GutterRenderer

    Object GtkSourceGutterRendererText

    Properties from GtkSourceGutterRendererText:
      markup -> gchararray: Markup
        The markup
      text -> gchararray: Text
        The text

    Signals from GtkSourceGutterRenderer:
      activate (GtkTextIter, GdkRectangle, guint, GdkModifierType, gint)
      query-activatable (GtkTextIter, GdkRectangle) -> gboolean
      query-data (GObject, guint)

    Properties from GtkSourceGutterRenderer:
      alignment-mode -> GtkSourceGutterRendererAlignmentMode: Alignment Mode
        The alignment mode
      lines -> GtkSourceGutterLines: Lines
        Information about the lines to render
      view -> GtkTextView: The View
        The view
      xalign -> gfloat: X Alignment
        The x-alignment
      xpad -> gint: X Padding
        The x-padding
      yalign -> gfloat: Y Alignment
        The y-alignment
      ypad -> gint: Y Padding
        The y-padding

    Signals from GtkWidget:
      hide ()
      show ()
      destroy ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
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
        markup: str
        text: str
        alignment_mode: GutterRendererAlignmentMode
        lines: GutterLines
        view: Gtk.TextView
        xalign: float
        xpad: int
        yalign: float
        ypad: int
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
    parent_instance: GutterRenderer = ...
    def __init__(
        self,
        markup: str = ...,
        text: str = ...,
        alignment_mode: GutterRendererAlignmentMode = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
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
    def measure(self, text: str) -> Tuple[int, int]: ...
    def measure_markup(self, markup: str) -> Tuple[int, int]: ...
    @classmethod
    def new(cls) -> GutterRendererText: ...
    def set_markup(self, markup: str, length: int) -> None: ...
    def set_text(self, text: str, length: int) -> None: ...

class GutterRendererTextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GutterRendererTextClass()
    """

    parent_class: GutterRendererClass = ...
    _reserved: list[None] = ...

class Hover(GObject.Object):
    """
    :Constructors:

    ::

        Hover(**properties)

    Object GtkSourceHover

    Properties from GtkSourceHover:
      hover-delay -> guint: Hover Delay
        Number of milliseconds to delay before showing assistant

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        hover_delay: int

    props: Props = ...
    def __init__(self, hover_delay: int = ...): ...
    def add_provider(self, provider: HoverProvider) -> None: ...
    def remove_provider(self, provider: HoverProvider) -> None: ...

class HoverClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HoverClass()
    """

    parent_class: GObject.ObjectClass = ...

class HoverContext(GObject.Object):
    """
    :Constructors:

    ::

        HoverContext(**properties)

    Object GtkSourceHoverContext

    Signals from GObject:
      notify (GParam)
    """

    def get_bounds(self) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter]: ...
    def get_buffer(self) -> Buffer: ...
    def get_iter(self, iter: Gtk.TextIter) -> bool: ...
    def get_view(self) -> View: ...

class HoverContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HoverContextClass()
    """

    parent_class: GObject.ObjectClass = ...

class HoverDisplay(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        HoverDisplay(**properties)

    Object GtkSourceHoverDisplay

    Signals from GtkWidget:
      hide ()
      show ()
      destroy ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
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
    def append(self, child: Gtk.Widget) -> None: ...
    def insert_after(self, child: Gtk.Widget, sibling: Gtk.Widget) -> None: ...
    def prepend(self, child: Gtk.Widget) -> None: ...
    def remove(self, child: Gtk.Widget) -> None: ...

class HoverDisplayClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HoverDisplayClass()
    """

    parent_class: Gtk.WidgetClass = ...

class HoverProvider(GObject.GInterface):
    """
    Interface GtkSourceHoverProvider

    Signals from GObject:
      notify (GParam)
    """

    def populate_async(
        self,
        context: HoverContext,
        display: HoverDisplay,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def populate_finish(self, result: Gio.AsyncResult) -> bool: ...

class HoverProviderInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        HoverProviderInterface()
    """

    parent_iface: GObject.TypeInterface = ...
    populate: Callable[[HoverProvider, HoverContext, HoverDisplay], bool] = ...
    populate_async: Callable[..., None] = ...
    populate_finish: Callable[[HoverProvider, Gio.AsyncResult], bool] = ...

class Indenter(GObject.GInterface):
    """
    Interface GtkSourceIndenter

    Signals from GObject:
      notify (GParam)
    """

    def indent(self, view: View) -> Gtk.TextIter: ...
    def is_trigger(
        self, view: View, location: Gtk.TextIter, state: Gdk.ModifierType, keyval: int
    ) -> bool: ...

class IndenterInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        IndenterInterface()
    """

    parent_iface: GObject.TypeInterface = ...
    is_trigger: Callable[
        [Indenter, View, Gtk.TextIter, Gdk.ModifierType, int], bool
    ] = ...
    indent: Callable[[Indenter, View], Gtk.TextIter] = ...

class Language(GObject.Object):
    """
    :Constructors:

    ::

        Language(**properties)

    Object GtkSourceLanguage

    Properties from GtkSourceLanguage:
      id -> gchararray: Language id
        Language id
      name -> gchararray: Language name
        Language name
      section -> gchararray: Language section
        Language section
      hidden -> gboolean: Hidden
        Whether the language should be hidden from the user

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        hidden: bool
        id: str
        name: str
        section: str

    props: Props = ...
    def get_globs(self) -> Optional[list[str]]: ...
    def get_hidden(self) -> bool: ...
    def get_id(self) -> str: ...
    def get_metadata(self, name: str) -> Optional[str]: ...
    def get_mime_types(self) -> Optional[list[str]]: ...
    def get_name(self) -> str: ...
    def get_section(self) -> str: ...
    def get_style_fallback(self, style_id: str) -> Optional[str]: ...
    def get_style_ids(self) -> Optional[list[str]]: ...
    def get_style_name(self, style_id: str) -> Optional[str]: ...

class LanguageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LanguageClass()
    """

    parent_class: GObject.ObjectClass = ...

class LanguageManager(GObject.Object):
    """
    :Constructors:

    ::

        LanguageManager(**properties)
        new() -> GtkSource.LanguageManager

    Object GtkSourceLanguageManager

    Properties from GtkSourceLanguageManager:
      search-path -> GStrv: Language specification directories
        List of directories where the language specification files (.lang) are located
      language-ids -> GStrv: Language ids
        List of the ids of the available languages

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        language_ids: Optional[list[str]]
        search_path: list[str]

    props: Props = ...
    def __init__(self, search_path: Optional[Sequence[str]] = ...): ...
    def append_search_path(self, path: str) -> None: ...
    @staticmethod
    def get_default() -> LanguageManager: ...
    def get_language(self, id: str) -> Optional[Language]: ...
    def get_language_ids(self) -> Optional[list[str]]: ...
    def get_search_path(self) -> list[str]: ...
    def guess_language(
        self, filename: Optional[str] = None, content_type: Optional[str] = None
    ) -> Optional[Language]: ...
    @classmethod
    def new(cls) -> LanguageManager: ...
    def prepend_search_path(self, path: str) -> None: ...
    def set_search_path(self, dirs: Optional[Sequence[str]] = None) -> None: ...

class LanguageManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LanguageManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class Map(
    View,
    Gtk.Accessible,
    Gtk.AccessibleText,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Scrollable,
):
    """
    :Constructors:

    ::

        Map(**properties)
        new() -> Gtk.Widget

    Object GtkSourceMap

    Properties from GtkSourceMap:
      view -> GtkSourceView: View
        The view this widget is mapping.
      font-desc -> PangoFontDescription: Font Description
        The Pango font description to use.

    Signals from GtkSourceView:
      smart-home-end (GtkTextIter, gint)
      show-completion ()
      line-mark-activated (GtkTextIter, guint, GdkModifierType, gint)
      move-lines (gboolean)
      move-words (gint)
      push-snippet (GtkSourceSnippet, GtkTextIter)
      move-to-matching-bracket (gboolean)
      change-number (gint)
      change-case (GtkSourceChangeCaseType)
      join-lines ()

    Properties from GtkSourceView:
      auto-indent -> gboolean: Auto Indentation
        Whether to enable auto indentation
      background-pattern -> GtkSourceBackgroundPatternType: Background pattern
        Draw a specific background pattern on the view
      completion -> GtkSourceCompletion: Completion
        The completion object associated with the view
      enable-snippets -> gboolean: Enable Snippets
        Whether to enable snippet expansion
      highlight-current-line -> gboolean: Highlight current line
        Whether to highlight the current line
      indent-on-tab -> gboolean: Indent on tab
        Whether to indent the selected text when the tab key is pressed
      indent-width -> gint: Indent Width
        Number of spaces to use for each step of indent
      indenter -> GtkSourceIndenter: Indenter
        A indenter to use to indent typed text
      insert-spaces-instead-of-tabs -> gboolean: Insert Spaces Instead of Tabs
        Whether to insert spaces instead of tabs
      right-margin-position -> guint: Right Margin Position
        Position of the right margin
      show-line-marks -> gboolean: Show Line Marks
        Whether to display line mark pixbufs
      show-line-numbers -> gboolean: Show Line Numbers
        Whether to display line numbers
      show-right-margin -> gboolean: Show Right Margin
        Whether to display the right margin
      smart-backspace -> gboolean: Smart Backspace

      smart-home-end -> GtkSourceSmartHomeEndType: Smart Home/End
        HOME and END keys move to first/last non whitespace characters on line before going to the start/end of the line
      space-drawer -> GtkSourceSpaceDrawer: Space Drawer

      tab-width -> guint: Tab Width
        Width of a tab character expressed in spaces

    Signals from GtkTextView:
      move-cursor (GtkMovementStep, gint, gboolean)
      move-viewport (GtkScrollStep, gint)
      set-anchor ()
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      select-all (gboolean)
      toggle-cursor-visible ()
      preedit-changed (gchararray)
      extend-selection (GtkTextExtendSelection, GtkTextIter, GtkTextIter, GtkTextIter) -> gboolean
      insert-emoji ()

    Properties from GtkTextView:
      pixels-above-lines -> gint: pixels-above-lines
      pixels-below-lines -> gint: pixels-below-lines
      pixels-inside-wrap -> gint: pixels-inside-wrap
      editable -> gboolean: editable
      wrap-mode -> GtkWrapMode: wrap-mode
      justification -> GtkJustification: justification
      left-margin -> gint: left-margin
      right-margin -> gint: right-margin
      top-margin -> gint: top-margin
      bottom-margin -> gint: bottom-margin
      indent -> gint: indent
      tabs -> PangoTabArray: tabs
      cursor-visible -> gboolean: cursor-visible
      buffer -> GtkTextBuffer: buffer
      overwrite -> gboolean: overwrite
      accepts-tab -> gboolean: accepts-tab
      im-module -> gchararray: im-module
      input-purpose -> GtkInputPurpose: input-purpose
      input-hints -> GtkInputHints: input-hints
      monospace -> gboolean: monospace
      extra-menu -> GMenuModel: extra-menu

    Signals from GtkWidget:
      hide ()
      show ()
      destroy ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
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
        font_desc: Pango.FontDescription
        view: Optional[View]
        auto_indent: bool
        background_pattern: BackgroundPatternType
        completion: Completion
        enable_snippets: bool
        highlight_current_line: bool
        indent_on_tab: bool
        indent_width: int
        indenter: Optional[Indenter]
        insert_spaces_instead_of_tabs: bool
        right_margin_position: int
        show_line_marks: bool
        show_line_numbers: bool
        show_right_margin: bool
        smart_backspace: bool
        smart_home_end: SmartHomeEndType
        space_drawer: SpaceDrawer
        tab_width: int
        accepts_tab: bool
        bottom_margin: int
        buffer: Gtk.TextBuffer
        cursor_visible: bool
        editable: bool
        extra_menu: Gio.MenuModel
        im_module: str
        indent: int
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        justification: Gtk.Justification
        left_margin: int
        monospace: bool
        overwrite: bool
        pixels_above_lines: int
        pixels_below_lines: int
        pixels_inside_wrap: int
        right_margin: int
        tabs: Optional[Pango.TabArray]
        top_margin: int
        wrap_mode: Gtk.WrapMode
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
        hadjustment: Optional[Gtk.Adjustment]
        hscroll_policy: Gtk.ScrollablePolicy
        vadjustment: Optional[Gtk.Adjustment]
        vscroll_policy: Gtk.ScrollablePolicy

    props: Props = ...
    parent_instance: View = ...
    def __init__(
        self,
        font_desc: Pango.FontDescription = ...,
        view: View = ...,
        auto_indent: bool = ...,
        background_pattern: BackgroundPatternType = ...,
        enable_snippets: bool = ...,
        highlight_current_line: bool = ...,
        indent_on_tab: bool = ...,
        indent_width: int = ...,
        indenter: Optional[Indenter] = ...,
        insert_spaces_instead_of_tabs: bool = ...,
        right_margin_position: int = ...,
        show_line_marks: bool = ...,
        show_line_numbers: bool = ...,
        show_right_margin: bool = ...,
        smart_backspace: bool = ...,
        smart_home_end: SmartHomeEndType = ...,
        tab_width: int = ...,
        accepts_tab: bool = ...,
        bottom_margin: int = ...,
        buffer: Optional[Gtk.TextBuffer] = ...,
        cursor_visible: bool = ...,
        editable: bool = ...,
        extra_menu: Optional[Gio.MenuModel] = ...,
        im_module: str = ...,
        indent: int = ...,
        input_hints: Gtk.InputHints = ...,
        input_purpose: Gtk.InputPurpose = ...,
        justification: Gtk.Justification = ...,
        left_margin: int = ...,
        monospace: bool = ...,
        overwrite: bool = ...,
        pixels_above_lines: int = ...,
        pixels_below_lines: int = ...,
        pixels_inside_wrap: int = ...,
        right_margin: int = ...,
        tabs: Pango.TabArray = ...,
        top_margin: int = ...,
        wrap_mode: Gtk.WrapMode = ...,
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
        hadjustment: Optional[Gtk.Adjustment] = ...,
        hscroll_policy: Gtk.ScrollablePolicy = ...,
        vadjustment: Optional[Gtk.Adjustment] = ...,
        vscroll_policy: Gtk.ScrollablePolicy = ...,
    ): ...
    def get_view(self) -> Optional[View]: ...
    @classmethod
    def new(cls) -> Map: ...
    def set_view(self, view: View) -> None: ...

class MapClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MapClass()
    """

    parent_class: ViewClass = ...
    _reserved: list[None] = ...

class Mark(Gtk.TextMark):
    """
    :Constructors:

    ::

        Mark(**properties)
        new(name:str=None, category:str) -> GtkSource.Mark

    Object GtkSourceMark

    Properties from GtkSourceMark:
      category -> gchararray: Category
        The mark category

    Properties from GtkTextMark:
      name -> gchararray: name
      left-gravity -> gboolean: left-gravity

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        category: str
        left_gravity: bool
        name: Optional[str]

    props: Props = ...
    parent_instance: Gtk.TextMark = ...
    def __init__(
        self, category: str = ..., left_gravity: bool = ..., name: str = ...
    ): ...
    def get_category(self) -> str: ...
    @classmethod
    def new(cls, name: Optional[str], category: str) -> Mark: ...
    def next(self, category: Optional[str] = None) -> Optional[Mark]: ...
    def prev(self, category: Optional[str] = None) -> Optional[Mark]: ...

class MarkAttributes(GObject.Object):
    """
    :Constructors:

    ::

        MarkAttributes(**properties)
        new() -> GtkSource.MarkAttributes

    Object GtkSourceMarkAttributes

    Signals from GtkSourceMarkAttributes:
      query-tooltip-text (GtkSourceMark) -> gchararray
      query-tooltip-markup (GtkSourceMark) -> gchararray

    Properties from GtkSourceMarkAttributes:
      background -> GdkRGBA: Background
        The background
      pixbuf -> GdkPixbuf: Pixbuf
        The pixbuf
      icon-name -> gchararray: Icon Name
        The icon name
      gicon -> GIcon: GIcon
        The GIcon

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        background: Gdk.RGBA
        gicon: Gio.Icon
        icon_name: str
        pixbuf: GdkPixbuf.Pixbuf

    props: Props = ...
    def __init__(
        self,
        background: Gdk.RGBA = ...,
        gicon: Gio.Icon = ...,
        icon_name: str = ...,
        pixbuf: GdkPixbuf.Pixbuf = ...,
    ): ...
    def get_background(self) -> Tuple[bool, Gdk.RGBA]: ...
    def get_gicon(self) -> Gio.Icon: ...
    def get_icon_name(self) -> str: ...
    def get_pixbuf(self) -> GdkPixbuf.Pixbuf: ...
    def get_tooltip_markup(self, mark: Mark) -> str: ...
    def get_tooltip_text(self, mark: Mark) -> str: ...
    @classmethod
    def new(cls) -> MarkAttributes: ...
    def render_icon(self, widget: Gtk.Widget, size: int) -> Gdk.Paintable: ...
    def set_background(self, background: Gdk.RGBA) -> None: ...
    def set_gicon(self, gicon: Gio.Icon) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_pixbuf(self, pixbuf: GdkPixbuf.Pixbuf) -> None: ...

class MarkAttributesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MarkAttributesClass()
    """

    parent_class: GObject.ObjectClass = ...

class MarkClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MarkClass()
    """

    parent_class: Gtk.TextMarkClass = ...
    _reserved: list[None] = ...

class PrintCompositor(GObject.Object):
    """
    :Constructors:

    ::

        PrintCompositor(**properties)
        new(buffer:GtkSource.Buffer) -> GtkSource.PrintCompositor
        new_from_view(view:GtkSource.View) -> GtkSource.PrintCompositor

    Object GtkSourcePrintCompositor

    Properties from GtkSourcePrintCompositor:
      buffer -> GtkSourceBuffer: Source Buffer
        The GtkSourceBuffer object to print
      tab-width -> guint: Tab Width
        Width of a tab character expressed in spaces
      wrap-mode -> GtkWrapMode: Wrap Mode

      highlight-syntax -> gboolean: Highlight Syntax

      print-line-numbers -> guint: Print Line Numbers

      print-header -> gboolean: Print Header

      print-footer -> gboolean: Print Footer

      body-font-name -> gchararray: Body Font Name

      line-numbers-font-name -> gchararray: Line Numbers Font Name

      header-font-name -> gchararray: Header Font Name

      footer-font-name -> gchararray: Footer Font Name

      n-pages -> gint: Number of pages


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        body_font_name: str
        buffer: Buffer
        footer_font_name: str
        header_font_name: str
        highlight_syntax: bool
        line_numbers_font_name: str
        n_pages: int
        print_footer: bool
        print_header: bool
        print_line_numbers: int
        tab_width: int
        wrap_mode: Gtk.WrapMode

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self,
        body_font_name: str = ...,
        buffer: Buffer = ...,
        footer_font_name: Optional[str] = ...,
        header_font_name: Optional[str] = ...,
        highlight_syntax: bool = ...,
        line_numbers_font_name: Optional[str] = ...,
        print_footer: bool = ...,
        print_header: bool = ...,
        print_line_numbers: int = ...,
        tab_width: int = ...,
        wrap_mode: Gtk.WrapMode = ...,
    ): ...
    def draw_page(self, context: Gtk.PrintContext, page_nr: int) -> None: ...
    def get_body_font_name(self) -> str: ...
    def get_bottom_margin(self, unit: Gtk.Unit) -> float: ...
    def get_buffer(self) -> Buffer: ...
    def get_footer_font_name(self) -> str: ...
    def get_header_font_name(self) -> str: ...
    def get_highlight_syntax(self) -> bool: ...
    def get_left_margin(self, unit: Gtk.Unit) -> float: ...
    def get_line_numbers_font_name(self) -> str: ...
    def get_n_pages(self) -> int: ...
    def get_pagination_progress(self) -> float: ...
    def get_print_footer(self) -> bool: ...
    def get_print_header(self) -> bool: ...
    def get_print_line_numbers(self) -> int: ...
    def get_right_margin(self, unit: Gtk.Unit) -> float: ...
    def get_tab_width(self) -> int: ...
    def get_top_margin(self, unit: Gtk.Unit) -> float: ...
    def get_wrap_mode(self) -> Gtk.WrapMode: ...
    def ignore_tag(self, tag: Gtk.TextTag) -> None: ...
    @classmethod
    def new(cls, buffer: Buffer) -> PrintCompositor: ...
    @classmethod
    def new_from_view(cls, view: View) -> PrintCompositor: ...
    def paginate(self, context: Gtk.PrintContext) -> bool: ...
    def set_body_font_name(self, font_name: str) -> None: ...
    def set_bottom_margin(self, margin: float, unit: Gtk.Unit) -> None: ...
    def set_footer_font_name(self, font_name: Optional[str] = None) -> None: ...
    def set_footer_format(
        self,
        separator: bool,
        left: Optional[str] = None,
        center: Optional[str] = None,
        right: Optional[str] = None,
    ) -> None: ...
    def set_header_font_name(self, font_name: Optional[str] = None) -> None: ...
    def set_header_format(
        self,
        separator: bool,
        left: Optional[str] = None,
        center: Optional[str] = None,
        right: Optional[str] = None,
    ) -> None: ...
    def set_highlight_syntax(self, highlight: bool) -> None: ...
    def set_left_margin(self, margin: float, unit: Gtk.Unit) -> None: ...
    def set_line_numbers_font_name(self, font_name: Optional[str] = None) -> None: ...
    def set_print_footer(self, print_: bool) -> None: ...
    def set_print_header(self, print_: bool) -> None: ...
    def set_print_line_numbers(self, interval: int) -> None: ...
    def set_right_margin(self, margin: float, unit: Gtk.Unit) -> None: ...
    def set_tab_width(self, width: int) -> None: ...
    def set_top_margin(self, margin: float, unit: Gtk.Unit) -> None: ...
    def set_wrap_mode(self, wrap_mode: Gtk.WrapMode) -> None: ...

class PrintCompositorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PrintCompositorClass()
    """

    parent_class: GObject.ObjectClass = ...
    _reserved: list[None] = ...

class Region(GObject.Object):
    """
    :Constructors:

    ::

        Region(**properties)
        new(buffer:Gtk.TextBuffer) -> GtkSource.Region

    Object GtkSourceRegion

    Properties from GtkSourceRegion:
      buffer -> GtkTextBuffer: Buffer


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        buffer: Optional[Gtk.TextBuffer]

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, buffer: Gtk.TextBuffer = ...): ...
    def add_region(self, region_to_add: Optional[Region] = None) -> None: ...
    def add_subregion(self, _start: Gtk.TextIter, _end: Gtk.TextIter) -> None: ...
    def get_bounds(self) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter]: ...
    def get_buffer(self) -> Optional[Gtk.TextBuffer]: ...
    def get_start_region_iter(self) -> RegionIter: ...
    def intersect_region(
        self, region2: Optional[Region] = None
    ) -> Optional[Region]: ...
    def intersect_subregion(
        self, _start: Gtk.TextIter, _end: Gtk.TextIter
    ) -> Optional[Region]: ...
    def is_empty(self) -> bool: ...
    @classmethod
    def new(cls, buffer: Gtk.TextBuffer) -> Region: ...
    def subtract_region(self, region_to_subtract: Optional[Region] = None) -> None: ...
    def subtract_subregion(self, _start: Gtk.TextIter, _end: Gtk.TextIter) -> None: ...
    def to_string(self) -> Optional[str]: ...

class RegionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RegionClass()
    """

    parent_class: GObject.ObjectClass = ...
    _reserved: list[None] = ...

class RegionIter(GObject.GPointer):
    """
    :Constructors:

    ::

        RegionIter()
    """

    dummy1: None = ...
    dummy2: int = ...
    dummy3: None = ...
    def get_subregion(self) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter]: ...
    def is_end(self) -> bool: ...
    def next(self) -> bool: ...

class SearchContext(GObject.Object):
    """
    :Constructors:

    ::

        SearchContext(**properties)
        new(buffer:GtkSource.Buffer, settings:GtkSource.SearchSettings=None) -> GtkSource.SearchContext

    Object GtkSourceSearchContext

    Properties from GtkSourceSearchContext:
      buffer -> GtkSourceBuffer: Buffer
        The associated GtkSourceBuffer
      settings -> GtkSourceSearchSettings: Settings
        The associated GtkSourceSearchSettings
      highlight -> gboolean: Highlight
        Highlight search occurrences
      match-style -> GtkSourceStyle: Match style
        The text style for matches
      occurrences-count -> gint: Occurrences count
        Total number of search occurrences
      regex-error -> GError: Regex error
        Regular expression error

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        buffer: Buffer
        highlight: bool
        match_style: Style
        occurrences_count: int
        regex_error: Optional[GLib.Error]
        settings: SearchSettings

    props: Props = ...
    def __init__(
        self,
        buffer: Buffer = ...,
        highlight: bool = ...,
        match_style: Optional[Style] = ...,
        settings: SearchSettings = ...,
    ): ...
    def backward(
        self, iter: Gtk.TextIter
    ) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter, bool]: ...
    def backward_async(
        self,
        iter: Gtk.TextIter,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def backward_finish(
        self, result: Gio.AsyncResult
    ) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter, bool]: ...
    def forward(
        self, iter: Gtk.TextIter
    ) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter, bool]: ...
    def forward_async(
        self,
        iter: Gtk.TextIter,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def forward_finish(
        self, result: Gio.AsyncResult
    ) -> Tuple[bool, Gtk.TextIter, Gtk.TextIter, bool]: ...
    def get_buffer(self) -> Buffer: ...
    def get_highlight(self) -> bool: ...
    def get_match_style(self) -> Style: ...
    def get_occurrence_position(
        self, match_start: Gtk.TextIter, match_end: Gtk.TextIter
    ) -> int: ...
    def get_occurrences_count(self) -> int: ...
    def get_regex_error(self) -> Optional[GLib.Error]: ...
    def get_settings(self) -> SearchSettings: ...
    @classmethod
    def new(
        cls, buffer: Buffer, settings: Optional[SearchSettings] = None
    ) -> SearchContext: ...
    def replace(
        self,
        match_start: Gtk.TextIter,
        match_end: Gtk.TextIter,
        replace: str,
        replace_length: int,
    ) -> bool: ...
    def replace_all(self, replace: str, replace_length: int) -> int: ...
    def set_highlight(self, highlight: bool) -> None: ...
    def set_match_style(self, match_style: Optional[Style] = None) -> None: ...

class SearchContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SearchContextClass()
    """

    parent_class: GObject.ObjectClass = ...

class SearchSettings(GObject.Object):
    """
    :Constructors:

    ::

        SearchSettings(**properties)
        new() -> GtkSource.SearchSettings

    Object GtkSourceSearchSettings

    Properties from GtkSourceSearchSettings:
      search-text -> gchararray: Search text
        The text to search
      case-sensitive -> gboolean: Case sensitive
        Case sensitive
      at-word-boundaries -> gboolean: At word boundaries
        Search at word boundaries
      wrap-around -> gboolean: Wrap around
        Wrap around
      regex-enabled -> gboolean: Regex enabled
        Whether to search by regular expression
      visible-only -> gboolean: Visible only
        Whether to exclude invisible text from the search

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        at_word_boundaries: bool
        case_sensitive: bool
        regex_enabled: bool
        search_text: Optional[str]
        visible_only: bool
        wrap_around: bool

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self,
        at_word_boundaries: bool = ...,
        case_sensitive: bool = ...,
        regex_enabled: bool = ...,
        search_text: Optional[str] = ...,
        visible_only: bool = ...,
        wrap_around: bool = ...,
    ): ...
    def get_at_word_boundaries(self) -> bool: ...
    def get_case_sensitive(self) -> bool: ...
    def get_regex_enabled(self) -> bool: ...
    def get_search_text(self) -> Optional[str]: ...
    def get_visible_only(self) -> bool: ...
    def get_wrap_around(self) -> bool: ...
    @classmethod
    def new(cls) -> SearchSettings: ...
    def set_at_word_boundaries(self, at_word_boundaries: bool) -> None: ...
    def set_case_sensitive(self, case_sensitive: bool) -> None: ...
    def set_regex_enabled(self, regex_enabled: bool) -> None: ...
    def set_search_text(self, search_text: Optional[str] = None) -> None: ...
    def set_visible_only(self, visible_only: bool) -> None: ...
    def set_wrap_around(self, wrap_around: bool) -> None: ...

class SearchSettingsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SearchSettingsClass()
    """

    parent_class: GObject.ObjectClass = ...
    _reserved: list[None] = ...

class Snippet(GObject.Object):
    """
    :Constructors:

    ::

        Snippet(**properties)
        new(trigger:str=None, language_id:str=None) -> GtkSource.Snippet
        new_parsed(text:str) -> GtkSource.Snippet

    Object GtkSourceSnippet

    Properties from GtkSourceSnippet:
      buffer -> GtkTextBuffer: Buffer
        The GtkTextBuffer for the snippet
      description -> gchararray: Description
        The description for the snippet
      focus-position -> gint: Focus Position
        The currently focused chunk
      language-id -> gchararray: Language Id
        The language-id for the snippet
      name -> gchararray: Name
        The name for the snippet
      trigger -> gchararray: Trigger
        The trigger for the snippet

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        buffer: Gtk.TextBuffer
        description: str
        focus_position: int
        language_id: str
        name: str
        trigger: Optional[str]

    props: Props = ...
    def __init__(
        self,
        description: str = ...,
        language_id: str = ...,
        name: str = ...,
        trigger: str = ...,
    ): ...
    def add_chunk(self, chunk: SnippetChunk) -> None: ...
    def copy(self) -> Snippet: ...
    def get_context(self) -> Optional[SnippetContext]: ...
    def get_description(self) -> str: ...
    def get_focus_position(self) -> int: ...
    def get_language_id(self) -> str: ...
    def get_n_chunks(self) -> int: ...
    def get_name(self) -> str: ...
    def get_nth_chunk(self, nth: int) -> SnippetChunk: ...
    def get_trigger(self) -> Optional[str]: ...
    @classmethod
    def new(
        cls, trigger: Optional[str] = None, language_id: Optional[str] = None
    ) -> Snippet: ...
    @classmethod
    def new_parsed(cls, text: str) -> Snippet: ...
    def set_description(self, description: str) -> None: ...
    def set_language_id(self, language_id: str) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_trigger(self, trigger: str) -> None: ...

class SnippetChunk(GObject.InitiallyUnowned):
    """
    :Constructors:

    ::

        SnippetChunk(**properties)
        new() -> GtkSource.SnippetChunk

    Object GtkSourceSnippetChunk

    Properties from GtkSourceSnippetChunk:
      context -> GtkSourceSnippetContext: Context
        The snippet context.
      spec -> gchararray: Spec
        The specification to expand using the context.
      focus-position -> gint: Focus Position
        The focus position for the chunk.
      text -> gchararray: Text
        The text for the chunk.
      text-set -> gboolean: If text property is set
        If the text property has been manually set.
      tooltip-text -> gchararray: Tooltip Text
        The tooltip text for the chunk.

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        context: SnippetContext
        focus_position: int
        spec: Optional[str]
        text: str
        text_set: bool
        tooltip_text: str

    props: Props = ...
    def __init__(
        self,
        context: SnippetContext = ...,
        focus_position: int = ...,
        spec: str = ...,
        text: str = ...,
        text_set: bool = ...,
        tooltip_text: str = ...,
    ): ...
    def copy(self) -> SnippetChunk: ...
    def get_context(self) -> SnippetContext: ...
    def get_focus_position(self) -> int: ...
    def get_spec(self) -> Optional[str]: ...
    def get_text(self) -> str: ...
    def get_text_set(self) -> bool: ...
    def get_tooltip_text(self) -> str: ...
    @classmethod
    def new(cls) -> SnippetChunk: ...
    def set_context(self, context: SnippetContext) -> None: ...
    def set_focus_position(self, focus_position: int) -> None: ...
    def set_spec(self, spec: str) -> None: ...
    def set_text(self, text: str) -> None: ...
    def set_text_set(self, text_set: bool) -> None: ...
    def set_tooltip_text(self, tooltip_text: str) -> None: ...

class SnippetChunkClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SnippetChunkClass()
    """

    parent_class: GObject.InitiallyUnownedClass = ...

class SnippetClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SnippetClass()
    """

    parent_class: GObject.ObjectClass = ...

class SnippetContext(GObject.Object):
    """
    :Constructors:

    ::

        SnippetContext(**properties)
        new() -> GtkSource.SnippetContext

    Object GtkSourceSnippetContext

    Signals from GtkSourceSnippetContext:
      changed ()

    Signals from GObject:
      notify (GParam)
    """

    def clear_variables(self) -> None: ...
    def expand(self, input: str) -> str: ...
    def get_variable(self, key: str) -> Optional[str]: ...
    @classmethod
    def new(cls) -> SnippetContext: ...
    def set_constant(self, key: str, value: str) -> None: ...
    def set_line_prefix(self, line_prefix: str) -> None: ...
    def set_tab_width(self, tab_width: int) -> None: ...
    def set_use_spaces(self, use_spaces: bool) -> None: ...
    def set_variable(self, key: str, value: str) -> None: ...

class SnippetContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SnippetContextClass()
    """

    parent_class: GObject.ObjectClass = ...

class SnippetManager(GObject.Object):
    """
    :Constructors:

    ::

        SnippetManager(**properties)

    Object GtkSourceSnippetManager

    Properties from GtkSourceSnippetManager:
      search-path -> GStrv: Snippet directories
        List of directories with snippet definitions (*.snippets)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        search_path: list[str]

    props: Props = ...
    def __init__(self, search_path: Optional[Sequence[str]] = ...): ...
    @staticmethod
    def get_default() -> SnippetManager: ...
    def get_search_path(self) -> list[str]: ...
    def get_snippet(
        self, group: Optional[str], language_id: Optional[str], trigger: str
    ) -> Optional[Snippet]: ...
    def list_all(self) -> Gio.ListModel: ...
    def list_groups(self) -> list[str]: ...
    def list_matching(
        self,
        group: Optional[str] = None,
        language_id: Optional[str] = None,
        trigger_prefix: Optional[str] = None,
    ) -> Gio.ListModel: ...
    def set_search_path(self, dirs: Optional[Sequence[str]] = None) -> None: ...

class SnippetManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SnippetManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class SpaceDrawer(GObject.Object):
    """
    :Constructors:

    ::

        SpaceDrawer(**properties)
        new() -> GtkSource.SpaceDrawer

    Object GtkSourceSpaceDrawer

    Properties from GtkSourceSpaceDrawer:
      enable-matrix -> gboolean: Enable Matrix

      matrix -> GVariant: Matrix


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        enable_matrix: bool
        matrix: GLib.Variant

    props: Props = ...
    def __init__(
        self, enable_matrix: bool = ..., matrix: Optional[GLib.Variant] = ...
    ): ...
    def bind_matrix_setting(
        self, settings: Gio.Settings, key: str, flags: Gio.SettingsBindFlags
    ) -> None: ...
    def get_enable_matrix(self) -> bool: ...
    def get_matrix(self) -> GLib.Variant: ...
    def get_types_for_locations(
        self, locations: SpaceLocationFlags
    ) -> SpaceTypeFlags: ...
    @classmethod
    def new(cls) -> SpaceDrawer: ...
    def set_enable_matrix(self, enable_matrix: bool) -> None: ...
    def set_matrix(self, matrix: Optional[GLib.Variant] = None) -> None: ...
    def set_types_for_locations(
        self, locations: SpaceLocationFlags, types: SpaceTypeFlags
    ) -> None: ...

class SpaceDrawerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SpaceDrawerClass()
    """

    parent_class: GObject.ObjectClass = ...

class Style(GObject.Object):
    """
    :Constructors:

    ::

        Style(**properties)

    Object GtkSourceStyle

    Properties from GtkSourceStyle:
      line-background -> gchararray: Line background
        Line background color
      line-background-set -> gboolean: Line background set
        Whether line background color is set
      background -> gchararray: Background
        Background color
      background-set -> gboolean: Background set
        Whether background color is set
      foreground -> gchararray: Foreground
        Foreground color
      foreground-set -> gboolean: Foreground set
        Whether foreground color is set
      bold -> gboolean: Bold
        Bold
      bold-set -> gboolean: Bold set
        Whether bold attribute is set
      italic -> gboolean: Italic
        Italic
      italic-set -> gboolean: Italic set
        Whether italic attribute is set
      pango-underline -> PangoUnderline: Pango Underline
        Pango Underline
      underline-set -> gboolean: Underline set
        Whether underline attribute is set
      strikethrough -> gboolean: Strikethrough
        Strikethrough
      strikethrough-set -> gboolean: Strikethrough set
        Whether strikethrough attribute is set
      scale -> gchararray: Scale
        Text scale factor
      scale-set -> gboolean: Scale set
        Whether scale attribute is set
      underline-color -> gchararray: Underline Color
        Underline color
      underline-color-set -> gboolean: Underline color set
        Whether underline color attribute is set
      weight -> PangoWeight: Weight
        Text weight
      weight-set -> gboolean: Weight set
        Whether weight attribute is set

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        background: str
        background_set: bool
        bold: bool
        bold_set: bool
        foreground: str
        foreground_set: bool
        italic: bool
        italic_set: bool
        line_background: str
        line_background_set: bool
        pango_underline: Pango.Underline
        scale: str
        scale_set: bool
        strikethrough: bool
        strikethrough_set: bool
        underline_color: str
        underline_color_set: bool
        underline_set: bool
        weight: Pango.Weight
        weight_set: bool

    props: Props = ...
    def __init__(
        self,
        background: str = ...,
        background_set: bool = ...,
        bold: bool = ...,
        bold_set: bool = ...,
        foreground: str = ...,
        foreground_set: bool = ...,
        italic: bool = ...,
        italic_set: bool = ...,
        line_background: str = ...,
        line_background_set: bool = ...,
        pango_underline: Pango.Underline = ...,
        scale: str = ...,
        scale_set: bool = ...,
        strikethrough: bool = ...,
        strikethrough_set: bool = ...,
        underline_color: str = ...,
        underline_color_set: bool = ...,
        underline_set: bool = ...,
        weight: Pango.Weight = ...,
        weight_set: bool = ...,
    ): ...
    def apply(self, tag: Gtk.TextTag) -> None: ...
    def copy(self) -> Style: ...

class StyleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleClass()
    """

    parent_class: GObject.ObjectClass = ...

class StyleScheme(GObject.Object):
    """
    :Constructors:

    ::

        StyleScheme(**properties)

    Object GtkSourceStyleScheme

    Properties from GtkSourceStyleScheme:
      id -> gchararray: Style scheme id
        Style scheme id
      name -> gchararray: Style scheme name
        Style scheme name
      description -> gchararray: Style scheme description
        Style scheme description
      filename -> gchararray: Style scheme filename
        Style scheme filename

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        description: Optional[str]
        filename: Optional[str]
        id: str
        name: str

    props: Props = ...
    def __init__(self, id: str = ...): ...
    def get_authors(self) -> Optional[list[str]]: ...
    def get_description(self) -> Optional[str]: ...
    def get_filename(self) -> Optional[str]: ...
    def get_id(self) -> str: ...
    def get_metadata(self, name: str) -> Optional[str]: ...
    def get_name(self) -> str: ...
    def get_style(self, style_id: str) -> Optional[Style]: ...

class StyleSchemeChooser(GObject.GInterface):
    """
    Interface GtkSourceStyleSchemeChooser

    Signals from GObject:
      notify (GParam)
    """

    def get_style_scheme(self) -> StyleScheme: ...
    def set_style_scheme(self, scheme: StyleScheme) -> None: ...

class StyleSchemeChooserButton(
    Gtk.Button,
    Gtk.Accessible,
    Gtk.Actionable,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    StyleSchemeChooser,
):
    """
    :Constructors:

    ::

        StyleSchemeChooserButton(**properties)
        new() -> Gtk.Widget

    Object GtkSourceStyleSchemeChooserButton

    Signals from GtkButton:
      activate ()
      clicked ()

    Properties from GtkButton:
      label -> gchararray: label
      has-frame -> gboolean: has-frame
      use-underline -> gboolean: use-underline
      icon-name -> gchararray: icon-name
      child -> GtkWidget: child
      can-shrink -> gboolean: can-shrink

    Signals from GtkWidget:
      hide ()
      show ()
      destroy ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
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
        can_shrink: bool
        child: Optional[Gtk.Widget]
        has_frame: bool
        icon_name: Optional[str]
        label: Optional[str]
        use_underline: bool
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
        style_scheme: StyleScheme

    props: Props = ...
    parent_instance: Gtk.Button = ...
    def __init__(
        self,
        can_shrink: bool = ...,
        child: Optional[Gtk.Widget] = ...,
        has_frame: bool = ...,
        icon_name: str = ...,
        label: str = ...,
        use_underline: bool = ...,
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
        style_scheme: StyleScheme = ...,
    ): ...
    @classmethod
    def new(cls) -> StyleSchemeChooserButton: ...

class StyleSchemeChooserButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleSchemeChooserButtonClass()
    """

    parent: Gtk.ButtonClass = ...
    _reserved: list[None] = ...

class StyleSchemeChooserInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleSchemeChooserInterface()
    """

    base_interface: GObject.TypeInterface = ...
    get_style_scheme: Callable[[StyleSchemeChooser], StyleScheme] = ...
    set_style_scheme: Callable[[StyleSchemeChooser, StyleScheme], None] = ...
    _reserved: list[None] = ...

class StyleSchemeChooserWidget(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, StyleSchemeChooser
):
    """
    :Constructors:

    ::

        StyleSchemeChooserWidget(**properties)
        new() -> Gtk.Widget

    Object GtkSourceStyleSchemeChooserWidget

    Signals from GtkWidget:
      hide ()
      show ()
      destroy ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
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
        style_scheme: StyleScheme

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
        style_scheme: StyleScheme = ...,
    ): ...
    @classmethod
    def new(cls) -> StyleSchemeChooserWidget: ...

class StyleSchemeChooserWidgetClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleSchemeChooserWidgetClass()
    """

    parent: Gtk.WidgetClass = ...
    _reserved: list[None] = ...

class StyleSchemeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleSchemeClass()
    """

    parent_class: GObject.ObjectClass = ...

class StyleSchemeManager(GObject.Object):
    """
    :Constructors:

    ::

        StyleSchemeManager(**properties)
        new() -> GtkSource.StyleSchemeManager

    Object GtkSourceStyleSchemeManager

    Properties from GtkSourceStyleSchemeManager:
      search-path -> GStrv: Style scheme search path
        List of directories and files where the style schemes are located
      scheme-ids -> GStrv: Scheme ids
        List of the ids of the available style schemes

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        scheme_ids: Optional[list[str]]
        search_path: list[str]

    props: Props = ...
    def __init__(self, search_path: Optional[Sequence[str]] = ...): ...
    def append_search_path(self, path: str) -> None: ...
    def force_rescan(self) -> None: ...
    @staticmethod
    def get_default() -> StyleSchemeManager: ...
    def get_scheme(self, scheme_id: str) -> Optional[StyleScheme]: ...
    def get_scheme_ids(self) -> Optional[list[str]]: ...
    def get_search_path(self) -> list[str]: ...
    @classmethod
    def new(cls) -> StyleSchemeManager: ...
    def prepend_search_path(self, path: str) -> None: ...
    def set_search_path(self, path: Optional[Sequence[str]] = None) -> None: ...

class StyleSchemeManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleSchemeManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class StyleSchemePreview(
    Gtk.Widget, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        StyleSchemePreview(**properties)
        new(scheme:GtkSource.StyleScheme) -> Gtk.Widget

    Object GtkSourceStyleSchemePreview

    Signals from GtkSourceStyleSchemePreview:
      activate ()

    Properties from GtkSourceStyleSchemePreview:
      scheme -> GtkSourceStyleScheme: Scheme
        The style scheme to preview
      selected -> gboolean: Selected
        If the preview should have the selected state

    Signals from GtkWidget:
      hide ()
      show ()
      destroy ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
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
        scheme: StyleScheme
        selected: bool
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
    def __init__(
        self,
        scheme: StyleScheme = ...,
        selected: bool = ...,
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
    def get_scheme(self) -> StyleScheme: ...
    def get_selected(self) -> bool: ...
    @classmethod
    def new(cls, scheme: StyleScheme) -> StyleSchemePreview: ...
    def set_selected(self, selected: bool) -> None: ...

class StyleSchemePreviewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleSchemePreviewClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Tag(Gtk.TextTag):
    """
    :Constructors:

    ::

        Tag(**properties)
        new(name:str=None) -> Gtk.TextTag

    Object GtkSourceTag

    Properties from GtkSourceTag:
      draw-spaces -> gboolean: Draw Spaces

      draw-spaces-set -> gboolean: Draw Spaces Set


    Properties from GtkTextTag:
      name -> gchararray: name
      background -> gchararray: background
      foreground -> gchararray: foreground
      background-rgba -> GdkRGBA: background-rgba
      foreground-rgba -> GdkRGBA: foreground-rgba
      font -> gchararray: font
      font-desc -> PangoFontDescription: font-desc
      family -> gchararray: family
      style -> PangoStyle: style
      variant -> PangoVariant: variant
      weight -> gint: weight
      stretch -> PangoStretch: stretch
      size -> gint: size
      size-points -> gdouble: size-points
      scale -> gdouble: scale
      pixels-above-lines -> gint: pixels-above-lines
      pixels-below-lines -> gint: pixels-below-lines
      pixels-inside-wrap -> gint: pixels-inside-wrap
      line-height -> gfloat: line-height
      editable -> gboolean: editable
      wrap-mode -> GtkWrapMode: wrap-mode
      justification -> GtkJustification: justification
      direction -> GtkTextDirection: direction
      left-margin -> gint: left-margin
      indent -> gint: indent
      strikethrough -> gboolean: strikethrough
      strikethrough-rgba -> GdkRGBA: strikethrough-rgba
      right-margin -> gint: right-margin
      underline -> PangoUnderline: underline
      underline-rgba -> GdkRGBA: underline-rgba
      overline -> PangoOverline: overline
      overline-rgba -> GdkRGBA: overline-rgba
      rise -> gint: rise
      background-full-height -> gboolean: background-full-height
      language -> gchararray: language
      tabs -> PangoTabArray: tabs
      invisible -> gboolean: invisible
      paragraph-background -> gchararray: paragraph-background
      paragraph-background-rgba -> GdkRGBA: paragraph-background-rgba
      fallback -> gboolean: fallback
      letter-spacing -> gint: letter-spacing
      font-features -> gchararray: font-features
      allow-breaks -> gboolean: allow-breaks
      show-spaces -> PangoShowFlags: show-spaces
      insert-hyphens -> gboolean: insert-hyphens
      text-transform -> PangoTextTransform: text-transform
      word -> gboolean: word
      sentence -> gboolean: sentence
      accumulative-margin -> gboolean: accumulative-margin
      background-set -> gboolean: background-set
      foreground-set -> gboolean: foreground-set
      family-set -> gboolean: family-set
      style-set -> gboolean: style-set
      variant-set -> gboolean: variant-set
      weight-set -> gboolean: weight-set
      stretch-set -> gboolean: stretch-set
      size-set -> gboolean: size-set
      scale-set -> gboolean: scale-set
      pixels-above-lines-set -> gboolean: pixels-above-lines-set
      pixels-below-lines-set -> gboolean: pixels-below-lines-set
      pixels-inside-wrap-set -> gboolean: pixels-inside-wrap-set
      line-height-set -> gboolean: line-height-set
      editable-set -> gboolean: editable-set
      wrap-mode-set -> gboolean: wrap-mode-set
      justification-set -> gboolean: justification-set
      left-margin-set -> gboolean: left-margin-set
      indent-set -> gboolean: indent-set
      strikethrough-set -> gboolean: strikethrough-set
      strikethrough-rgba-set -> gboolean: strikethrough-rgba-set
      right-margin-set -> gboolean: right-margin-set
      underline-set -> gboolean: underline-set
      underline-rgba-set -> gboolean: underline-rgba-set
      overline-set -> gboolean: overline-set
      overline-rgba-set -> gboolean: overline-rgba-set
      rise-set -> gboolean: rise-set
      background-full-height-set -> gboolean: background-full-height-set
      language-set -> gboolean: language-set
      tabs-set -> gboolean: tabs-set
      invisible-set -> gboolean: invisible-set
      paragraph-background-set -> gboolean: paragraph-background-set
      fallback-set -> gboolean: fallback-set
      letter-spacing-set -> gboolean: letter-spacing-set
      font-features-set -> gboolean: font-features-set
      allow-breaks-set -> gboolean: allow-breaks-set
      show-spaces-set -> gboolean: show-spaces-set
      insert-hyphens-set -> gboolean: insert-hyphens-set
      text-transform-set -> gboolean: text-transform-set
      sentence-set -> gboolean: sentence-set
      word-set -> gboolean: word-set

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        draw_spaces: bool
        draw_spaces_set: bool
        accumulative_margin: bool
        allow_breaks: bool
        allow_breaks_set: bool
        background_full_height: bool
        background_full_height_set: bool
        background_rgba: Gdk.RGBA
        background_set: bool
        direction: Gtk.TextDirection
        editable: bool
        editable_set: bool
        fallback: bool
        fallback_set: bool
        family: str
        family_set: bool
        font: str
        font_desc: Pango.FontDescription
        font_features: str
        font_features_set: bool
        foreground_rgba: Gdk.RGBA
        foreground_set: bool
        indent: int
        indent_set: bool
        insert_hyphens: bool
        insert_hyphens_set: bool
        invisible: bool
        invisible_set: bool
        justification: Gtk.Justification
        justification_set: bool
        language: str
        language_set: bool
        left_margin: int
        left_margin_set: bool
        letter_spacing: int
        letter_spacing_set: bool
        line_height: float
        line_height_set: bool
        name: str
        overline: Pango.Overline
        overline_rgba: Gdk.RGBA
        overline_rgba_set: bool
        overline_set: bool
        paragraph_background_rgba: Gdk.RGBA
        paragraph_background_set: bool
        pixels_above_lines: int
        pixels_above_lines_set: bool
        pixels_below_lines: int
        pixels_below_lines_set: bool
        pixels_inside_wrap: int
        pixels_inside_wrap_set: bool
        right_margin: int
        right_margin_set: bool
        rise: int
        rise_set: bool
        scale: float
        scale_set: bool
        sentence: bool
        sentence_set: bool
        show_spaces: Pango.ShowFlags
        show_spaces_set: bool
        size: int
        size_points: float
        size_set: bool
        stretch: Pango.Stretch
        stretch_set: bool
        strikethrough: bool
        strikethrough_rgba: Gdk.RGBA
        strikethrough_rgba_set: bool
        strikethrough_set: bool
        style: Pango.Style
        style_set: bool
        tabs: Pango.TabArray
        tabs_set: bool
        text_transform: Pango.TextTransform
        text_transform_set: bool
        underline: Pango.Underline
        underline_rgba: Gdk.RGBA
        underline_rgba_set: bool
        underline_set: bool
        variant: Pango.Variant
        variant_set: bool
        weight: int
        weight_set: bool
        word: bool
        word_set: bool
        wrap_mode: Gtk.WrapMode
        wrap_mode_set: bool
        background: str
        foreground: str
        paragraph_background: str

    props: Props = ...
    parent_instance: Gtk.TextTag = ...
    def __init__(
        self,
        draw_spaces: bool = ...,
        draw_spaces_set: bool = ...,
        accumulative_margin: bool = ...,
        allow_breaks: bool = ...,
        allow_breaks_set: bool = ...,
        background: str = ...,
        background_full_height: bool = ...,
        background_full_height_set: bool = ...,
        background_rgba: Gdk.RGBA = ...,
        background_set: bool = ...,
        direction: Gtk.TextDirection = ...,
        editable: bool = ...,
        editable_set: bool = ...,
        fallback: bool = ...,
        fallback_set: bool = ...,
        family: str = ...,
        family_set: bool = ...,
        font: str = ...,
        font_desc: Pango.FontDescription = ...,
        font_features: str = ...,
        font_features_set: bool = ...,
        foreground: str = ...,
        foreground_rgba: Gdk.RGBA = ...,
        foreground_set: bool = ...,
        indent: int = ...,
        indent_set: bool = ...,
        insert_hyphens: bool = ...,
        insert_hyphens_set: bool = ...,
        invisible: bool = ...,
        invisible_set: bool = ...,
        justification: Gtk.Justification = ...,
        justification_set: bool = ...,
        language: str = ...,
        language_set: bool = ...,
        left_margin: int = ...,
        left_margin_set: bool = ...,
        letter_spacing: int = ...,
        letter_spacing_set: bool = ...,
        line_height: float = ...,
        line_height_set: bool = ...,
        name: str = ...,
        overline: Pango.Overline = ...,
        overline_rgba: Gdk.RGBA = ...,
        overline_rgba_set: bool = ...,
        overline_set: bool = ...,
        paragraph_background: str = ...,
        paragraph_background_rgba: Gdk.RGBA = ...,
        paragraph_background_set: bool = ...,
        pixels_above_lines: int = ...,
        pixels_above_lines_set: bool = ...,
        pixels_below_lines: int = ...,
        pixels_below_lines_set: bool = ...,
        pixels_inside_wrap: int = ...,
        pixels_inside_wrap_set: bool = ...,
        right_margin: int = ...,
        right_margin_set: bool = ...,
        rise: int = ...,
        rise_set: bool = ...,
        scale: float = ...,
        scale_set: bool = ...,
        sentence: bool = ...,
        sentence_set: bool = ...,
        show_spaces: Pango.ShowFlags = ...,
        show_spaces_set: bool = ...,
        size: int = ...,
        size_points: float = ...,
        size_set: bool = ...,
        stretch: Pango.Stretch = ...,
        stretch_set: bool = ...,
        strikethrough: bool = ...,
        strikethrough_rgba: Gdk.RGBA = ...,
        strikethrough_rgba_set: bool = ...,
        strikethrough_set: bool = ...,
        style: Pango.Style = ...,
        style_set: bool = ...,
        tabs: Pango.TabArray = ...,
        tabs_set: bool = ...,
        text_transform: Pango.TextTransform = ...,
        text_transform_set: bool = ...,
        underline: Pango.Underline = ...,
        underline_rgba: Gdk.RGBA = ...,
        underline_rgba_set: bool = ...,
        underline_set: bool = ...,
        variant: Pango.Variant = ...,
        variant_set: bool = ...,
        weight: int = ...,
        weight_set: bool = ...,
        word: bool = ...,
        word_set: bool = ...,
        wrap_mode: Gtk.WrapMode = ...,
        wrap_mode_set: bool = ...,
    ): ...
    @classmethod
    def new(cls, name: Optional[str] = None) -> Tag: ...

class TagClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TagClass()
    """

    parent_class: Gtk.TextTagClass = ...
    _reserved: list[None] = ...

# override
class View(
    Gtk.TextView,
    Gtk.Accessible,
    Gtk.AccessibleText,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Scrollable,
):
    """
    :Constructors:

    ::

        View(**properties)
        new() -> Gtk.Widget
        new_with_buffer(buffer:GtkSource.Buffer) -> Gtk.Widget

    Object GtkSourceView

    Signals from GtkSourceView:
      smart-home-end (GtkTextIter, gint)
      show-completion ()
      line-mark-activated (GtkTextIter, guint, GdkModifierType, gint)
      move-lines (gboolean)
      move-words (gint)
      push-snippet (GtkSourceSnippet, GtkTextIter)
      move-to-matching-bracket (gboolean)
      change-number (gint)
      change-case (GtkSourceChangeCaseType)
      join-lines ()

    Properties from GtkSourceView:
      auto-indent -> gboolean: Auto Indentation
        Whether to enable auto indentation
      background-pattern -> GtkSourceBackgroundPatternType: Background pattern
        Draw a specific background pattern on the view
      completion -> GtkSourceCompletion: Completion
        The completion object associated with the view
      enable-snippets -> gboolean: Enable Snippets
        Whether to enable snippet expansion
      highlight-current-line -> gboolean: Highlight current line
        Whether to highlight the current line
      indent-on-tab -> gboolean: Indent on tab
        Whether to indent the selected text when the tab key is pressed
      indent-width -> gint: Indent Width
        Number of spaces to use for each step of indent
      indenter -> GtkSourceIndenter: Indenter
        A indenter to use to indent typed text
      insert-spaces-instead-of-tabs -> gboolean: Insert Spaces Instead of Tabs
        Whether to insert spaces instead of tabs
      right-margin-position -> guint: Right Margin Position
        Position of the right margin
      show-line-marks -> gboolean: Show Line Marks
        Whether to display line mark pixbufs
      show-line-numbers -> gboolean: Show Line Numbers
        Whether to display line numbers
      show-right-margin -> gboolean: Show Right Margin
        Whether to display the right margin
      smart-backspace -> gboolean: Smart Backspace

      smart-home-end -> GtkSourceSmartHomeEndType: Smart Home/End
        HOME and END keys move to first/last non whitespace characters on line before going to the start/end of the line
      space-drawer -> GtkSourceSpaceDrawer: Space Drawer

      tab-width -> guint: Tab Width
        Width of a tab character expressed in spaces

    Signals from GtkTextView:
      move-cursor (GtkMovementStep, gint, gboolean)
      move-viewport (GtkScrollStep, gint)
      set-anchor ()
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      select-all (gboolean)
      toggle-cursor-visible ()
      preedit-changed (gchararray)
      extend-selection (GtkTextExtendSelection, GtkTextIter, GtkTextIter, GtkTextIter) -> gboolean
      insert-emoji ()

    Properties from GtkTextView:
      pixels-above-lines -> gint: pixels-above-lines
      pixels-below-lines -> gint: pixels-below-lines
      pixels-inside-wrap -> gint: pixels-inside-wrap
      editable -> gboolean: editable
      wrap-mode -> GtkWrapMode: wrap-mode
      justification -> GtkJustification: justification
      left-margin -> gint: left-margin
      right-margin -> gint: right-margin
      top-margin -> gint: top-margin
      bottom-margin -> gint: bottom-margin
      indent -> gint: indent
      tabs -> PangoTabArray: tabs
      cursor-visible -> gboolean: cursor-visible
      overwrite -> gboolean: overwrite
      accepts-tab -> gboolean: accepts-tab
      im-module -> gchararray: im-module
      input-purpose -> GtkInputPurpose: input-purpose
      input-hints -> GtkInputHints: input-hints
      monospace -> gboolean: monospace
      extra-menu -> GMenuModel: extra-menu

    Signals from GtkWidget:
      hide ()
      show ()
      destroy ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
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
        auto_indent: bool
        background_pattern: BackgroundPatternType
        completion: Completion
        enable_snippets: bool
        highlight_current_line: bool
        indent_on_tab: bool
        indent_width: int
        indenter: Optional[Indenter]
        insert_spaces_instead_of_tabs: bool
        right_margin_position: int
        show_line_marks: bool
        show_line_numbers: bool
        show_right_margin: bool
        smart_backspace: bool
        smart_home_end: SmartHomeEndType
        space_drawer: SpaceDrawer
        tab_width: int
        accepts_tab: bool
        bottom_margin: int
        buffer: Buffer
        cursor_visible: bool
        editable: bool
        extra_menu: Gio.MenuModel
        im_module: str
        indent: int
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        justification: Gtk.Justification
        left_margin: int
        monospace: bool
        overwrite: bool
        pixels_above_lines: int
        pixels_below_lines: int
        pixels_inside_wrap: int
        right_margin: int
        tabs: Optional[Pango.TabArray]
        top_margin: int
        wrap_mode: Gtk.WrapMode
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
        hadjustment: Optional[Gtk.Adjustment]
        hscroll_policy: Gtk.ScrollablePolicy
        vadjustment: Optional[Gtk.Adjustment]
        vscroll_policy: Gtk.ScrollablePolicy

    props: Props = ...
    parent_instance: Gtk.TextView = ...

    def __init__(
        self,
        auto_indent: bool = ...,
        background_pattern: BackgroundPatternType = ...,
        enable_snippets: bool = ...,
        highlight_current_line: bool = ...,
        indent_on_tab: bool = ...,
        indent_width: int = ...,
        indenter: Optional[Indenter] = ...,
        insert_spaces_instead_of_tabs: bool = ...,
        right_margin_position: int = ...,
        show_line_marks: bool = ...,
        show_line_numbers: bool = ...,
        show_right_margin: bool = ...,
        smart_backspace: bool = ...,
        smart_home_end: SmartHomeEndType = ...,
        tab_width: int = ...,
        accepts_tab: bool = ...,
        bottom_margin: int = ...,
        buffer: Optional[Gtk.TextBuffer] = ...,
        cursor_visible: bool = ...,
        editable: bool = ...,
        extra_menu: Optional[Gio.MenuModel] = ...,
        im_module: str = ...,
        indent: int = ...,
        input_hints: Gtk.InputHints = ...,
        input_purpose: Gtk.InputPurpose = ...,
        justification: Gtk.Justification = ...,
        left_margin: int = ...,
        monospace: bool = ...,
        overwrite: bool = ...,
        pixels_above_lines: int = ...,
        pixels_below_lines: int = ...,
        pixels_inside_wrap: int = ...,
        right_margin: int = ...,
        tabs: Pango.TabArray = ...,
        top_margin: int = ...,
        wrap_mode: Gtk.WrapMode = ...,
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
        hadjustment: Optional[Gtk.Adjustment] = ...,
        hscroll_policy: Gtk.ScrollablePolicy = ...,
        vadjustment: Optional[Gtk.Adjustment] = ...,
        vscroll_policy: Gtk.ScrollablePolicy = ...,
    ): ...
    def do_line_mark_activated(
        self, iter: Gtk.TextIter, button: int, state: Gdk.ModifierType, n_presses: int
    ) -> None: ...
    def do_move_lines(self, down: bool) -> None: ...
    def do_move_words(self, step: int) -> None: ...
    def do_push_snippet(
        self, snippet: Snippet, location: Optional[Gtk.TextIter] = None
    ) -> None: ...
    def do_show_completion(self) -> None: ...
    def get_auto_indent(self) -> bool: ...
    def get_background_pattern(self) -> BackgroundPatternType: ...
    def get_buffer(self) -> Buffer: ...
    def get_completion(self) -> Completion: ...
    def get_enable_snippets(self) -> bool: ...
    def get_gutter(self, window_type: Gtk.TextWindowType) -> Gutter: ...
    def get_highlight_current_line(self) -> bool: ...
    def get_hover(self) -> Hover: ...
    def get_indent_on_tab(self) -> bool: ...
    def get_indent_width(self) -> int: ...
    def get_indenter(self) -> Optional[Indenter]: ...
    def get_insert_spaces_instead_of_tabs(self) -> bool: ...
    def get_mark_attributes(self, category: str, priority: int) -> MarkAttributes: ...
    def get_right_margin_position(self) -> int: ...
    def get_show_line_marks(self) -> bool: ...
    def get_show_line_numbers(self) -> bool: ...
    def get_show_right_margin(self) -> bool: ...
    def get_smart_backspace(self) -> bool: ...
    def get_smart_home_end(self) -> SmartHomeEndType: ...
    def get_space_drawer(self) -> SpaceDrawer: ...
    def get_tab_width(self) -> int: ...
    def get_visual_column(self, iter: Gtk.TextIter) -> int: ...
    def indent_lines(self, start: Gtk.TextIter, end: Gtk.TextIter) -> None: ...
    @classmethod
    def new(cls) -> View: ...
    @classmethod
    def new_with_buffer(cls, buffer: Buffer) -> View: ...
    def push_snippet(
        self, snippet: Snippet, location: Optional[Gtk.TextIter] = None
    ) -> None: ...
    def set_auto_indent(self, enable: bool) -> None: ...
    def set_background_pattern(
        self, background_pattern: BackgroundPatternType
    ) -> None: ...
    def set_enable_snippets(self, enable_snippets: bool) -> None: ...
    def set_highlight_current_line(self, highlight: bool) -> None: ...
    def set_indent_on_tab(self, enable: bool) -> None: ...
    def set_indent_width(self, width: int) -> None: ...
    def set_indenter(self, indenter: Optional[Indenter] = None) -> None: ...
    def set_insert_spaces_instead_of_tabs(self, enable: bool) -> None: ...
    def set_mark_attributes(
        self, category: str, attributes: MarkAttributes, priority: int
    ) -> None: ...
    def set_right_margin_position(self, pos: int) -> None: ...
    def set_show_line_marks(self, show: bool) -> None: ...
    def set_show_line_numbers(self, show: bool) -> None: ...
    def set_show_right_margin(self, show: bool) -> None: ...
    def set_smart_backspace(self, smart_backspace: bool) -> None: ...
    def set_smart_home_end(self, smart_home_end: SmartHomeEndType) -> None: ...
    def set_tab_width(self, width: int) -> None: ...
    def unindent_lines(self, start: Gtk.TextIter, end: Gtk.TextIter) -> None: ...

class ViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewClass()
    """

    parent_class: Gtk.TextViewClass = ...
    line_mark_activated: Callable[
        [View, Gtk.TextIter, int, Gdk.ModifierType, int], None
    ] = ...
    show_completion: Callable[[View], None] = ...
    move_lines: Callable[[View, bool], None] = ...
    move_words: Callable[[View, int], None] = ...
    push_snippet: Callable[[View, Snippet, Optional[Gtk.TextIter]], None] = ...
    _reserved: list[None] = ...

class VimIMContext(Gtk.IMContext):
    """
    :Constructors:

    ::

        VimIMContext(**properties)
        new() -> Gtk.IMContext

    Object GtkSourceVimIMContext

    Signals from GtkSourceVimIMContext:
      execute-command (gchararray) -> gboolean
      format-text (GtkTextIter, GtkTextIter)
      write (GtkSourceView, gchararray)
      edit (GtkSourceView, gchararray)

    Properties from GtkSourceVimIMContext:
      command-bar-text -> gchararray: Command Bar Text
        The text for the command bar
      command-text -> gchararray: Command Text
        The text for the current command

    Signals from GtkIMContext:
      preedit-changed ()
      preedit-start ()
      preedit-end ()
      commit (gchararray)
      retrieve-surrounding () -> gboolean
      delete-surrounding (gint, gint) -> gboolean

    Properties from GtkIMContext:
      input-purpose -> GtkInputPurpose: input-purpose
      input-hints -> GtkInputHints: input-hints

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        command_bar_text: str
        command_text: str
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose

    props: Props = ...
    def __init__(
        self, input_hints: Gtk.InputHints = ..., input_purpose: Gtk.InputPurpose = ...
    ): ...
    def execute_command(self, command: str) -> None: ...
    def get_command_bar_text(self) -> str: ...
    def get_command_text(self) -> str: ...
    @classmethod
    def new(cls) -> VimIMContext: ...

class VimIMContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VimIMContextClass()
    """

    parent_class: Gtk.IMContextClass = ...

class FileSaverFlags(GObject.GFlags):
    CREATE_BACKUP = 4
    IGNORE_INVALID_CHARS = 1
    IGNORE_MODIFICATION_TIME = 2
    NONE = 0

class SortFlags(GObject.GFlags):
    CASE_SENSITIVE = 1
    NONE = 0
    REMOVE_DUPLICATES = 4
    REVERSE_ORDER = 2

class SpaceLocationFlags(GObject.GFlags):
    ALL = 7
    INSIDE_TEXT = 2
    LEADING = 1
    NONE = 0
    TRAILING = 4

class SpaceTypeFlags(GObject.GFlags):
    ALL = 15
    NBSP = 8
    NEWLINE = 4
    NONE = 0
    SPACE = 1
    TAB = 2

class BackgroundPatternType(GObject.GEnum):
    GRID = 1
    NONE = 0

class BracketMatchType(GObject.GEnum):
    FOUND = 3
    NONE = 0
    NOT_FOUND = 2
    OUT_OF_RANGE = 1

class ChangeCaseType(GObject.GEnum):
    LOWER = 0
    TITLE = 3
    TOGGLE = 2
    UPPER = 1

class CompletionActivation(GObject.GEnum):
    INTERACTIVE = 1
    NONE = 0
    USER_REQUESTED = 2

class CompletionColumn(GObject.GEnum):
    AFTER = 3
    BEFORE = 1
    COMMENT = 4
    DETAILS = 5
    ICON = 0
    TYPED_TEXT = 2

class CompressionType(GObject.GEnum):
    GZIP = 1
    NONE = 0

class FileLoaderError(GObject.GEnum):
    CONVERSION_FALLBACK = 2
    ENCODING_AUTO_DETECTION_FAILED = 1
    TOO_BIG = 0
    @staticmethod
    def quark() -> int: ...

class FileSaverError(GObject.GEnum):
    EXTERNALLY_MODIFIED = 1
    INVALID_CHARS = 0
    @staticmethod
    def quark() -> int: ...

class GutterRendererAlignmentMode(GObject.GEnum):
    CELL = 0
    FIRST = 1
    LAST = 2

class NewlineType(GObject.GEnum):
    CR = 1
    CR_LF = 2
    LF = 0

class SmartHomeEndType(GObject.GEnum):
    AFTER = 2
    ALWAYS = 3
    BEFORE = 1
    DISABLED = 0

class ViewGutterPosition(GObject.GEnum):
    LINES = -30
    MARKS = -20
