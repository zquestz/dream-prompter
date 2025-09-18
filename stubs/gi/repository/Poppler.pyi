from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

import cairo
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

_SomeSurface = TypeVar("_SomeSurface", bound=cairo.Surface)

ANNOT_TEXT_ICON_CIRCLE: str = "Circle"
ANNOT_TEXT_ICON_COMMENT: str = "Comment"
ANNOT_TEXT_ICON_CROSS: str = "Cross"
ANNOT_TEXT_ICON_HELP: str = "Help"
ANNOT_TEXT_ICON_INSERT: str = "Insert"
ANNOT_TEXT_ICON_KEY: str = "Key"
ANNOT_TEXT_ICON_NEW_PARAGRAPH: str = "NewParagraph"
ANNOT_TEXT_ICON_NOTE: str = "Note"
ANNOT_TEXT_ICON_PARAGRAPH: str = "Paragraph"
HAS_CAIRO: int = 1
MAJOR_VERSION: int = 23
MICRO_VERSION: int = 0
MINOR_VERSION: int = 8
_lock = ...  # FIXME Constant
_namespace: str = "Poppler"
_version: str = "0.18"

def date_parse(date: str, timet: int) -> bool: ...
def error_quark() -> int: ...
def get_available_signing_certificates() -> list[CertificateInfo]: ...
def get_backend() -> Backend: ...
def get_certificate_info_by_id(id: str) -> CertificateInfo: ...
def get_nss_dir() -> str: ...
def get_version() -> str: ...
def named_dest_from_bytestring(data: Sequence[int]) -> str: ...
def named_dest_to_bytestring(name: str) -> Optional[bytes]: ...
def set_nss_dir(path: str) -> None: ...
def set_nss_password_callback(func: Callable[[str], str]) -> None: ...

# override
class Action(GObject.GBoxed):
    any: ActionAny = ...
    goto_dest: ActionGotoDest = ...
    goto_remote: ActionGotoRemote = ...
    javascript: ActionJavascript = ...
    launch: ActionLaunch = ...
    movie: ActionMovie = ...
    named: ActionNamed = ...
    ocg_state: ActionOCGState = ...
    rendition: ActionRendition = ...
    reset_form: ActionResetForm = ...
    type: ActionType = ...
    uri: ActionUri = ...

    def free(self) -> None: ...

class ActionAny(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionAny()
    """

    type: ActionType = ...
    title: str = ...

class ActionGotoDest(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionGotoDest()
    """

    type: ActionType = ...
    title: str = ...
    dest: Dest = ...

class ActionGotoRemote(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionGotoRemote()
    """

    type: ActionType = ...
    title: str = ...
    file_name: str = ...
    dest: Dest = ...

class ActionJavascript(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionJavascript()
    """

    type: ActionType = ...
    title: str = ...
    script: str = ...

class ActionLaunch(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionLaunch()
    """

    type: ActionType = ...
    title: str = ...
    file_name: str = ...
    params: str = ...

class ActionLayer(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionLayer()
    """

    action: ActionLayerAction = ...
    layers: list[Layer] = ...

class ActionMovie(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionMovie()
    """

    type: ActionType = ...
    title: str = ...
    operation: ActionMovieOperation = ...
    movie: Movie = ...

class ActionNamed(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionNamed()
    """

    type: ActionType = ...
    title: str = ...
    named_dest: str = ...

class ActionOCGState(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionOCGState()
    """

    type: ActionType = ...
    title: str = ...
    state_list: list[ActionLayer] = ...

class ActionRendition(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionRendition()
    """

    type: ActionType = ...
    title: str = ...
    op: int = ...
    media: Media = ...

class ActionResetForm(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionResetForm()
    """

    type: ActionType = ...
    title: str = ...
    fields: list[str] = ...
    exclude: bool = ...

class ActionUri(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionUri()
    """

    type: ActionType = ...
    title: str = ...
    uri: str = ...

class Annot(GObject.Object):
    """
    :Constructors:

    ::

        Annot(**properties)

    Object PopplerAnnot

    Signals from GObject:
      notify (GParam)
    """

    def get_annot_type(self) -> AnnotType: ...
    def get_color(self) -> Color: ...
    def get_contents(self) -> str: ...
    def get_flags(self) -> AnnotFlag: ...
    def get_modified(self) -> str: ...
    def get_name(self) -> str: ...
    def get_page_index(self) -> int: ...
    def get_rectangle(self) -> Rectangle: ...
    def set_color(self, poppler_color: Optional[Color] = None) -> None: ...
    def set_contents(self, contents: str) -> None: ...
    def set_flags(self, flags: AnnotFlag) -> None: ...
    def set_rectangle(self, poppler_rect: Rectangle) -> None: ...

class AnnotCalloutLine(GObject.GBoxed):
    """
    :Constructors:

    ::

        AnnotCalloutLine()
        new() -> Poppler.AnnotCalloutLine
    """

    multiline: bool = ...
    x1: float = ...
    y1: float = ...
    x2: float = ...
    y2: float = ...
    x3: float = ...
    y3: float = ...
    def copy(self) -> AnnotCalloutLine: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> AnnotCalloutLine: ...

class AnnotCircle(AnnotMarkup):
    """
    :Constructors:

    ::

        AnnotCircle(**properties)
        new(doc:Poppler.Document, rect:Poppler.Rectangle) -> Poppler.Annot

    Object PopplerAnnotCircle

    Signals from GObject:
      notify (GParam)
    """

    def get_interior_color(self) -> Color: ...
    @classmethod
    def new(cls, doc: Document, rect: Rectangle) -> AnnotCircle: ...
    def set_interior_color(self, poppler_color: Optional[Color] = None) -> None: ...

class AnnotFileAttachment(AnnotMarkup):
    """
    :Constructors:

    ::

        AnnotFileAttachment(**properties)

    Object PopplerAnnotFileAttachment

    Signals from GObject:
      notify (GParam)
    """

    def get_attachment(self) -> Attachment: ...
    def get_name(self) -> str: ...

class AnnotFreeText(AnnotMarkup):
    """
    :Constructors:

    ::

        AnnotFreeText(**properties)

    Object PopplerAnnotFreeText

    Signals from GObject:
      notify (GParam)
    """

    def get_callout_line(self) -> AnnotCalloutLine: ...
    def get_quadding(self) -> AnnotFreeTextQuadding: ...

class AnnotLine(AnnotMarkup):
    """
    :Constructors:

    ::

        AnnotLine(**properties)
        new(doc:Poppler.Document, rect:Poppler.Rectangle, start:Poppler.Point, end:Poppler.Point) -> Poppler.Annot

    Object PopplerAnnotLine

    Signals from GObject:
      notify (GParam)
    """

    @classmethod
    def new(
        cls, doc: Document, rect: Rectangle, start: Point, end: Point
    ) -> AnnotLine: ...
    def set_vertices(self, start: Point, end: Point) -> None: ...

class AnnotMapping(GObject.GBoxed):
    """
    :Constructors:

    ::

        AnnotMapping()
        new() -> Poppler.AnnotMapping
    """

    area: Rectangle = ...
    annot: Annot = ...
    def copy(self) -> AnnotMapping: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> AnnotMapping: ...

class AnnotMarkup(Annot):
    """
    :Constructors:

    ::

        AnnotMarkup(**properties)

    Object PopplerAnnotMarkup

    Signals from GObject:
      notify (GParam)
    """

    def get_date(self) -> GLib.Date: ...
    def get_external_data(self) -> AnnotExternalDataType: ...
    def get_label(self) -> str: ...
    def get_opacity(self) -> float: ...
    def get_popup_is_open(self) -> bool: ...
    def get_popup_rectangle(self) -> Tuple[bool, Rectangle]: ...
    def get_reply_to(self) -> AnnotMarkupReplyType: ...
    def get_subject(self) -> str: ...
    def has_popup(self) -> bool: ...
    def set_label(self, label: Optional[str] = None) -> None: ...
    def set_opacity(self, opacity: float) -> None: ...
    def set_popup(self, popup_rect: Rectangle) -> None: ...
    def set_popup_is_open(self, is_open: bool) -> None: ...
    def set_popup_rectangle(self, poppler_rect: Rectangle) -> None: ...

class AnnotMovie(Annot):
    """
    :Constructors:

    ::

        AnnotMovie(**properties)

    Object PopplerAnnotMovie

    Signals from GObject:
      notify (GParam)
    """

    def get_movie(self) -> Movie: ...
    def get_title(self) -> str: ...

class AnnotScreen(Annot):
    """
    :Constructors:

    ::

        AnnotScreen(**properties)

    Object PopplerAnnotScreen

    Signals from GObject:
      notify (GParam)
    """

    def get_action(self) -> Action: ...

class AnnotSquare(AnnotMarkup):
    """
    :Constructors:

    ::

        AnnotSquare(**properties)
        new(doc:Poppler.Document, rect:Poppler.Rectangle) -> Poppler.Annot

    Object PopplerAnnotSquare

    Signals from GObject:
      notify (GParam)
    """

    def get_interior_color(self) -> Color: ...
    @classmethod
    def new(cls, doc: Document, rect: Rectangle) -> AnnotSquare: ...
    def set_interior_color(self, poppler_color: Optional[Color] = None) -> None: ...

class AnnotStamp(Annot):
    """
    :Constructors:

    ::

        AnnotStamp(**properties)
        new(doc:Poppler.Document, rect:Poppler.Rectangle) -> Poppler.Annot

    Object PopplerAnnotStamp

    Signals from GObject:
      notify (GParam)
    """

    def get_icon(self) -> AnnotStampIcon: ...
    @classmethod
    def new(cls, doc: Document, rect: Rectangle) -> AnnotStamp: ...
    def set_custom_image(self, image: cairo.Surface) -> bool: ...
    def set_icon(self, icon: AnnotStampIcon) -> None: ...

class AnnotText(AnnotMarkup):
    """
    :Constructors:

    ::

        AnnotText(**properties)
        new(doc:Poppler.Document, rect:Poppler.Rectangle) -> Poppler.Annot

    Object PopplerAnnotText

    Signals from GObject:
      notify (GParam)
    """

    def get_icon(self) -> str: ...
    def get_is_open(self) -> bool: ...
    def get_state(self) -> AnnotTextState: ...
    @classmethod
    def new(cls, doc: Document, rect: Rectangle) -> AnnotText: ...
    def set_icon(self, icon: str) -> None: ...
    def set_is_open(self, is_open: bool) -> None: ...

class AnnotTextMarkup(AnnotMarkup):
    """
    :Constructors:

    ::

        AnnotTextMarkup(**properties)
        new_highlight(doc:Poppler.Document, rect:Poppler.Rectangle, quadrilaterals:list) -> Poppler.Annot
        new_squiggly(doc:Poppler.Document, rect:Poppler.Rectangle, quadrilaterals:list) -> Poppler.Annot
        new_strikeout(doc:Poppler.Document, rect:Poppler.Rectangle, quadrilaterals:list) -> Poppler.Annot
        new_underline(doc:Poppler.Document, rect:Poppler.Rectangle, quadrilaterals:list) -> Poppler.Annot

    Object PopplerAnnotTextMarkup

    Signals from GObject:
      notify (GParam)
    """

    def get_quadrilaterals(self) -> list[Quadrilateral]: ...
    @classmethod
    def new_highlight(
        cls, doc: Document, rect: Rectangle, quadrilaterals: Sequence[Quadrilateral]
    ) -> AnnotTextMarkup: ...
    @classmethod
    def new_squiggly(
        cls, doc: Document, rect: Rectangle, quadrilaterals: Sequence[Quadrilateral]
    ) -> AnnotTextMarkup: ...
    @classmethod
    def new_strikeout(
        cls, doc: Document, rect: Rectangle, quadrilaterals: Sequence[Quadrilateral]
    ) -> AnnotTextMarkup: ...
    @classmethod
    def new_underline(
        cls, doc: Document, rect: Rectangle, quadrilaterals: Sequence[Quadrilateral]
    ) -> AnnotTextMarkup: ...
    def set_quadrilaterals(self, quadrilaterals: Sequence[Quadrilateral]) -> None: ...

class Attachment(GObject.Object):
    """
    :Constructors:

    ::

        Attachment(**properties)

    Object PopplerAttachment

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    name: str = ...
    description: str = ...
    size: int = ...
    mtime: int = ...
    ctime: int = ...
    checksum: GLib.String = ...
    def get_checksum(self) -> GLib.String: ...
    def get_ctime(self) -> Optional[GLib.DateTime]: ...
    def get_description(self) -> str: ...
    def get_mtime(self) -> Optional[GLib.DateTime]: ...
    def get_name(self) -> str: ...
    def get_size(self) -> int: ...
    def save(self, filename: str) -> bool: ...
    def save_to_callback(
        self, save_func: Callable[..., bool], *user_data: Any
    ) -> bool: ...
    def save_to_fd(self, fd: int) -> bool: ...

class AttachmentClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AttachmentClass()
    """

    parent_class: GObject.ObjectClass = ...

class CertificateInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Poppler.CertificateInfo
    """

    def copy(self) -> CertificateInfo: ...
    def free(self) -> None: ...
    def get_expiration_time(self) -> GLib.DateTime: ...
    def get_id(self) -> str: ...
    def get_issuance_time(self) -> GLib.DateTime: ...
    def get_issuer_common_name(self) -> str: ...
    def get_issuer_email(self) -> str: ...
    def get_issuer_organization(self) -> str: ...
    def get_subject_common_name(self) -> str: ...
    def get_subject_email(self) -> str: ...
    def get_subject_organization(self) -> str: ...
    @classmethod
    def new(cls) -> CertificateInfo: ...

class Color(GObject.GBoxed):
    """
    :Constructors:

    ::

        Color()
        new() -> Poppler.Color
    """

    red: int = ...
    green: int = ...
    blue: int = ...
    def copy(self) -> Color: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> Color: ...

class Dest(GObject.GBoxed):
    """
    :Constructors:

    ::

        Dest()
    """

    type: DestType = ...
    page_num: int = ...
    left: float = ...
    bottom: float = ...
    right: float = ...
    top: float = ...
    zoom: float = ...
    named_dest: str = ...
    change_left: int = ...
    change_top: int = ...
    change_zoom: int = ...
    def copy(self) -> Dest: ...
    def free(self) -> None: ...

class Document(GObject.Object):
    """
    :Constructors:

    ::

        Document(**properties)
        new_from_bytes(bytes:GLib.Bytes, password:str=None) -> Poppler.Document
        new_from_data(data:list, password:str=None) -> Poppler.Document
        new_from_fd(fd:int, password:str=None) -> Poppler.Document
        new_from_file(uri:str, password:str=None) -> Poppler.Document
        new_from_gfile(file:Gio.File, password:str=None, cancellable:Gio.Cancellable=None) -> Poppler.Document
        new_from_stream(stream:Gio.InputStream, length:int, password:str=None, cancellable:Gio.Cancellable=None) -> Poppler.Document

    Object PopplerDocument

    Properties from PopplerDocument:
      title -> gchararray: Document Title
        The title of the document
      format -> gchararray: PDF Format
        The PDF version of the document
      format-major -> guint: PDF Format Major
        The PDF major version number of the document
      format-minor -> guint: PDF Format Minor
        The PDF minor version number of the document
      subtype -> PopplerPDFSubtype: PDF Format Subtype Type
        The PDF subtype of the document
      subtype-string -> gchararray: PDF Format Subtype
        The PDF subtype of the document
      subtype-part -> PopplerPDFPart: PDF Format Subtype Part
        The part of PDF conformance
      subtype-conformance -> PopplerPDFConformance: PDF Format Subtype Conformance
        The conformance level of PDF subtype
      author -> gchararray: Author
        The author of the document
      subject -> gchararray: Subject
        Subjects the document touches
      keywords -> gchararray: Keywords
        Keywords
      creator -> gchararray: Creator
        The software that created the document
      producer -> gchararray: Producer
        The software that converted the document
      creation-date -> gint: Creation Date
        The date and time the document was created
      mod-date -> gint: Modification Date
        The date and time the document was modified
      linearized -> gboolean: Fast Web View Enabled
        Is the document optimized for web viewing?
      page-layout -> PopplerPageLayout: Page Layout
        Initial Page Layout
      page-mode -> PopplerPageMode: Page Mode
        Page Mode
      viewer-preferences -> PopplerViewerPreferences: Viewer Preferences
        Viewer Preferences
      permissions -> PopplerPermissions: Permissions
        Permissions
      metadata -> gchararray: XML Metadata
        Embedded XML metadata
      print-scaling -> PopplerPrintScaling: Print Scaling
        Print Scaling Viewer Preference
      print-duplex -> PopplerPrintDuplex: Print Duplex
        Duplex Viewer Preference
      print-n-copies -> gint: Number of Copies to Print
        Number of Copies Viewer Preference
      creation-datetime -> GDateTime: Creation DateTime
        The date and time the document was created
      mod-datetime -> GDateTime: Modification DateTime
        The date and time the document was modified

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        author: str
        creation_date: int
        creation_datetime: GLib.DateTime
        creator: str
        format: str
        format_major: int
        format_minor: int
        keywords: str
        linearized: bool
        metadata: str
        mod_date: int
        mod_datetime: GLib.DateTime
        page_layout: PageLayout
        page_mode: PageMode
        permissions: Permissions
        print_duplex: PrintDuplex
        print_n_copies: int
        print_scaling: PrintScaling
        producer: str
        subject: str
        subtype: PDFSubtype
        subtype_conformance: PDFConformance
        subtype_part: PDFPart
        subtype_string: str
        title: str
        viewer_preferences: ViewerPreferences

    props: Props = ...
    def __init__(
        self,
        author: str = ...,
        creation_date: int = ...,
        creation_datetime: GLib.DateTime = ...,
        creator: str = ...,
        keywords: str = ...,
        mod_date: int = ...,
        mod_datetime: GLib.DateTime = ...,
        producer: str = ...,
        subject: str = ...,
        title: str = ...,
    ): ...
    def create_dests_tree(self) -> Optional[GLib.Tree]: ...
    def find_dest(self, link_name: str) -> Dest: ...
    def get_attachments(self) -> list[Attachment]: ...
    def get_author(self) -> str: ...
    def get_creation_date(self) -> int: ...
    def get_creation_date_time(self) -> Optional[GLib.DateTime]: ...
    def get_creator(self) -> str: ...
    def get_form_field(self, id: int) -> FormField: ...
    def get_id(self) -> Tuple[bool, str, str]: ...
    def get_keywords(self) -> str: ...
    def get_metadata(self) -> str: ...
    def get_modification_date(self) -> int: ...
    def get_modification_date_time(self) -> Optional[GLib.DateTime]: ...
    def get_n_attachments(self) -> int: ...
    def get_n_pages(self) -> int: ...
    def get_n_signatures(self) -> int: ...
    def get_page(self, index: int) -> Page: ...
    def get_page_by_label(self, label: str) -> Page: ...
    def get_page_layout(self) -> PageLayout: ...
    def get_page_mode(self) -> PageMode: ...
    def get_pdf_conformance(self) -> PDFConformance: ...
    def get_pdf_part(self) -> PDFPart: ...
    def get_pdf_subtype(self) -> PDFSubtype: ...
    def get_pdf_subtype_string(self) -> Optional[str]: ...
    def get_pdf_version(self) -> Tuple[int, int]: ...
    def get_pdf_version_string(self) -> str: ...
    def get_permissions(self) -> Permissions: ...
    def get_print_duplex(self) -> PrintDuplex: ...
    def get_print_n_copies(self) -> int: ...
    def get_print_page_ranges(self) -> list[PageRange]: ...
    def get_print_scaling(self) -> PrintScaling: ...
    def get_producer(self) -> str: ...
    def get_signature_fields(self) -> list[FormField]: ...
    def get_subject(self) -> str: ...
    def get_title(self) -> str: ...
    def has_attachments(self) -> bool: ...
    def has_javascript(self) -> bool: ...
    def is_linearized(self) -> bool: ...
    @classmethod
    def new_from_bytes(
        cls, bytes: GLib.Bytes, password: Optional[str] = None
    ) -> Document: ...
    @classmethod
    def new_from_data(
        cls, data: Sequence[int], password: Optional[str] = None
    ) -> Document: ...
    @classmethod
    def new_from_fd(cls, fd: int, password: Optional[str] = None) -> Document: ...
    @classmethod
    def new_from_file(cls, uri: str, password: Optional[str] = None) -> Document: ...
    @classmethod
    def new_from_gfile(
        cls,
        file: Gio.File,
        password: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Document: ...
    @classmethod
    def new_from_stream(
        cls,
        stream: Gio.InputStream,
        length: int,
        password: Optional[str] = None,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Document: ...
    def reset_form(self, fields: Optional[list[str]], exclude_fields: bool) -> None: ...
    def save(self, uri: str) -> bool: ...
    def save_a_copy(self, uri: str) -> bool: ...
    def save_to_fd(self, fd: int, include_changes: bool) -> bool: ...
    def set_author(self, author: str) -> None: ...
    def set_creation_date(self, creation_date: int) -> None: ...
    def set_creation_date_time(
        self, creation_datetime: Optional[GLib.DateTime] = None
    ) -> None: ...
    def set_creator(self, creator: str) -> None: ...
    def set_keywords(self, keywords: str) -> None: ...
    def set_modification_date(self, modification_date: int) -> None: ...
    def set_modification_date_time(
        self, modification_datetime: Optional[GLib.DateTime] = None
    ) -> None: ...
    def set_producer(self, producer: str) -> None: ...
    def set_subject(self, subject: str) -> None: ...
    def set_title(self, title: str) -> None: ...
    def sign(
        self,
        signing_data: SigningData,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def sign_finish(self, result: Gio.AsyncResult) -> bool: ...

class FontInfo(GObject.Object):
    """
    :Constructors:

    ::

        FontInfo(**properties)
        new(document:Poppler.Document) -> Poppler.FontInfo

    Object PopplerFontInfo

    Signals from GObject:
      notify (GParam)
    """

    def free(self) -> None: ...
    @classmethod
    def new(cls, document: Document) -> FontInfo: ...
    def scan(self, n_pages: int) -> Tuple[bool, FontsIter]: ...

class FontsIter(GObject.GBoxed):
    def copy(self) -> FontsIter: ...
    def free(self) -> None: ...
    def get_encoding(self) -> str: ...
    def get_file_name(self) -> str: ...
    def get_font_type(self) -> FontType: ...
    def get_full_name(self) -> str: ...
    def get_name(self) -> str: ...
    def get_substitute_name(self) -> str: ...
    def is_embedded(self) -> bool: ...
    def is_subset(self) -> bool: ...
    def next(self) -> bool: ...

class FormField(GObject.Object):
    """
    :Constructors:

    ::

        FormField(**properties)

    Object PopplerFormField

    Signals from GObject:
      notify (GParam)
    """

    def button_get_button_type(self) -> FormButtonType: ...
    def button_get_state(self) -> bool: ...
    def button_set_state(self, state: bool) -> None: ...
    def choice_can_select_multiple(self) -> bool: ...
    def choice_commit_on_change(self) -> bool: ...
    def choice_do_spell_check(self) -> bool: ...
    def choice_get_choice_type(self) -> FormChoiceType: ...
    def choice_get_item(self, index: int) -> str: ...
    def choice_get_n_items(self) -> int: ...
    def choice_get_text(self) -> str: ...
    def choice_is_editable(self) -> bool: ...
    def choice_is_item_selected(self, index: int) -> bool: ...
    def choice_select_item(self, index: int) -> None: ...
    def choice_set_text(self, text: str) -> None: ...
    def choice_toggle_item(self, index: int) -> None: ...
    def choice_unselect_all(self) -> None: ...
    def get_action(self) -> Action: ...
    def get_additional_action(self, type: AdditionalActionType) -> Action: ...
    def get_alternate_ui_name(self) -> str: ...
    def get_field_type(self) -> FormFieldType: ...
    def get_font_size(self) -> float: ...
    def get_id(self) -> int: ...
    def get_mapping_name(self) -> str: ...
    def get_name(self) -> str: ...
    def get_partial_name(self) -> str: ...
    def is_read_only(self) -> bool: ...
    def signature_validate_async(
        self,
        flags: SignatureValidationFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def signature_validate_finish(self, result: Gio.AsyncResult) -> SignatureInfo: ...
    def signature_validate_sync(
        self,
        flags: SignatureValidationFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> SignatureInfo: ...
    def text_do_scroll(self) -> bool: ...
    def text_do_spell_check(self) -> bool: ...
    def text_get_max_len(self) -> int: ...
    def text_get_text(self) -> str: ...
    def text_get_text_type(self) -> FormTextType: ...
    def text_is_password(self) -> bool: ...
    def text_is_rich_text(self) -> bool: ...
    def text_set_text(self, text: str) -> None: ...

class FormFieldMapping(GObject.GBoxed):
    """
    :Constructors:

    ::

        FormFieldMapping()
        new() -> Poppler.FormFieldMapping
    """

    area: Rectangle = ...
    field: FormField = ...
    def copy(self) -> FormFieldMapping: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> FormFieldMapping: ...

class ImageMapping(GObject.GBoxed):
    """
    :Constructors:

    ::

        ImageMapping()
        new() -> Poppler.ImageMapping
    """

    area: Rectangle = ...
    image_id: int = ...
    def copy(self) -> ImageMapping: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> ImageMapping: ...

class IndexIter(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(document:Poppler.Document) -> Poppler.IndexIter
    """

    def copy(self) -> IndexIter: ...
    def free(self) -> None: ...
    def get_action(self) -> Action: ...
    def get_child(self) -> IndexIter: ...
    def is_open(self) -> bool: ...
    @classmethod
    def new(cls, document: Document) -> IndexIter: ...
    def next(self) -> bool: ...

class Layer(GObject.Object):
    """
    :Constructors:

    ::

        Layer(**properties)

    Object PopplerLayer

    Signals from GObject:
      notify (GParam)
    """

    def get_radio_button_group_id(self) -> int: ...
    def get_title(self) -> str: ...
    def hide(self) -> None: ...
    def is_parent(self) -> bool: ...
    def is_visible(self) -> bool: ...
    def show(self) -> None: ...

class LayersIter(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(document:Poppler.Document) -> Poppler.LayersIter
    """

    def copy(self) -> LayersIter: ...
    def free(self) -> None: ...
    def get_child(self) -> LayersIter: ...
    def get_layer(self) -> Layer: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(cls, document: Document) -> LayersIter: ...
    def next(self) -> bool: ...

class LinkMapping(GObject.GBoxed):
    """
    :Constructors:

    ::

        LinkMapping()
        new() -> Poppler.LinkMapping
    """

    area: Rectangle = ...
    action: Action = ...
    def copy(self) -> LinkMapping: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> LinkMapping: ...

class Media(GObject.Object):
    """
    :Constructors:

    ::

        Media(**properties)

    Object PopplerMedia

    Signals from GObject:
      notify (GParam)
    """

    def get_auto_play(self) -> bool: ...
    def get_filename(self) -> str: ...
    def get_mime_type(self) -> str: ...
    def get_repeat_count(self) -> float: ...
    def get_show_controls(self) -> bool: ...
    def is_embedded(self) -> bool: ...
    def save(self, filename: str) -> bool: ...
    def save_to_callback(
        self, save_func: Callable[..., bool], *user_data: Any
    ) -> bool: ...
    def save_to_fd(self, fd: int) -> bool: ...

class Movie(GObject.Object):
    """
    :Constructors:

    ::

        Movie(**properties)

    Object PopplerMovie

    Signals from GObject:
      notify (GParam)
    """

    def get_aspect(self, width: int, height: int) -> None: ...
    def get_duration(self) -> int: ...
    def get_filename(self) -> str: ...
    def get_play_mode(self) -> MoviePlayMode: ...
    def get_rate(self) -> float: ...
    def get_rotation_angle(self) -> int: ...
    def get_start(self) -> int: ...
    def get_volume(self) -> float: ...
    def is_synchronous(self) -> bool: ...
    def need_poster(self) -> bool: ...
    def show_controls(self) -> bool: ...

class PSFile(GObject.Object):
    """
    :Constructors:

    ::

        PSFile(**properties)
        new(document:Poppler.Document, filename:str, first_page:int, n_pages:int) -> Poppler.PSFile
        new_fd(document:Poppler.Document, fd:int, first_page:int, n_pages:int) -> Poppler.PSFile

    Object PopplerPSFile

    Signals from GObject:
      notify (GParam)
    """

    def free(self) -> None: ...
    @classmethod
    def new(
        cls, document: Document, filename: str, first_page: int, n_pages: int
    ) -> PSFile: ...
    @classmethod
    def new_fd(
        cls, document: Document, fd: int, first_page: int, n_pages: int
    ) -> PSFile: ...
    def set_duplex(self, duplex: bool) -> None: ...
    def set_paper_size(self, width: float, height: float) -> None: ...

class Size(Tuple[float, float]):
    width: float
    height: float

class Page(GObject.Object):
    """
    :Constructors:

    ::

        Page(**properties)

    Object PopplerPage

    Properties from PopplerPage:
      label -> gchararray: Page Label
        The label of the page

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        label: str

    props: Props = ...
    def add_annot(self, annot: Annot) -> None: ...
    def find_text(self, text: str) -> list[Rectangle]: ...
    def find_text_with_options(
        self, text: str, options: FindFlags
    ) -> list[Rectangle]: ...
    @staticmethod
    def free_annot_mapping(list: list[AnnotMapping]) -> None: ...
    @staticmethod
    def free_form_field_mapping(list: list[FormFieldMapping]) -> None: ...
    @staticmethod
    def free_image_mapping(list: list[ImageMapping]) -> None: ...
    @staticmethod
    def free_link_mapping(list: list[LinkMapping]) -> None: ...
    @staticmethod
    def free_text_attributes(list: list[TextAttributes]) -> None: ...
    def get_annot_mapping(self) -> list[AnnotMapping]: ...
    def get_bounding_box(self, rect: Rectangle) -> bool: ...
    def get_crop_box(self) -> Rectangle: ...
    def get_duration(self) -> float: ...
    def get_form_field_mapping(self) -> list[FormFieldMapping]: ...
    def get_image(self, image_id: int) -> cairo.Surface: ...
    def get_image_mapping(self) -> list[ImageMapping]: ...
    def get_index(self) -> int: ...
    def get_label(self) -> str: ...
    def get_link_mapping(self) -> list[LinkMapping]: ...
    def get_selected_region(
        self, scale: float, style: SelectionStyle, selection: Rectangle
    ) -> cairo.Region: ...
    def get_selected_text(self, style: SelectionStyle, selection: Rectangle) -> str: ...
    def get_selection_region(
        self, scale: float, style: SelectionStyle, selection: Rectangle
    ) -> list[Rectangle]: ...
    # override
    def get_size(self) -> Size: ...
    def get_text(self) -> str: ...
    def get_text_attributes(self) -> list[TextAttributes]: ...
    def get_text_attributes_for_area(self, area: Rectangle) -> list[TextAttributes]: ...
    def get_text_for_area(self, area: Rectangle) -> str: ...
    def get_text_layout(self) -> Tuple[bool, list[Rectangle]]: ...
    def get_text_layout_for_area(
        self, area: Rectangle
    ) -> Tuple[bool, list[Rectangle]]: ...
    def get_thumbnail(self) -> cairo.Surface: ...
    def get_thumbnail_size(self) -> Tuple[bool, int, int]: ...
    def get_transition(self) -> PageTransition: ...
    def remove_annot(self, annot: Annot) -> None: ...
    def render(self, cairo: cairo.Context[_SomeSurface]) -> None: ...
    def render_for_printing(self, cairo: cairo.Context[_SomeSurface]) -> None: ...
    def render_for_printing_with_options(
        self, cairo: cairo.Context[_SomeSurface], options: PrintFlags
    ) -> None: ...
    def render_selection(
        self,
        cairo: cairo.Context[_SomeSurface],
        selection: Rectangle,
        old_selection: Rectangle,
        style: SelectionStyle,
        glyph_color: Color,
        background_color: Color,
    ) -> None: ...
    def render_to_ps(self, ps_file: PSFile) -> None: ...
    @staticmethod
    def selection_region_free(region: list[Rectangle]) -> None: ...

class PageRange(GObject.GPointer):
    """
    :Constructors:

    ::

        PageRange()
    """

    start_page: int = ...
    end_page: int = ...

class PageTransition(GObject.GBoxed):
    """
    :Constructors:

    ::

        PageTransition()
        new() -> Poppler.PageTransition
    """

    type: PageTransitionType = ...
    alignment: PageTransitionAlignment = ...
    direction: PageTransitionDirection = ...
    duration: int = ...
    angle: int = ...
    scale: float = ...
    rectangular: bool = ...
    duration_real: float = ...
    def copy(self) -> PageTransition: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> PageTransition: ...

class Point(GObject.GBoxed):
    """
    :Constructors:

    ::

        Point()
        new() -> Poppler.Point
    """

    x: float = ...
    y: float = ...
    def copy(self) -> Point: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> Point: ...

class Quadrilateral(GObject.GBoxed):
    """
    :Constructors:

    ::

        Quadrilateral()
        new() -> Poppler.Quadrilateral
    """

    p1: Point = ...
    p2: Point = ...
    p3: Point = ...
    p4: Point = ...
    def copy(self) -> Quadrilateral: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> Quadrilateral: ...

class Rectangle(GObject.GBoxed):
    """
    :Constructors:

    ::

        Rectangle()
        new() -> Poppler.Rectangle
    """

    x1: float = ...
    y1: float = ...
    x2: float = ...
    y2: float = ...
    def copy(self) -> Rectangle: ...
    def find_get_ignored_hyphen(self) -> bool: ...
    def find_get_match_continued(self) -> bool: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> Rectangle: ...

class SignatureInfo(GObject.GBoxed):
    def copy(self) -> SignatureInfo: ...
    def free(self) -> None: ...
    def get_certificate_info(self) -> CertificateInfo: ...
    def get_certificate_status(self) -> CertificateStatus: ...
    def get_local_signing_time(self) -> GLib.DateTime: ...
    def get_signature_status(self) -> SignatureStatus: ...
    def get_signer_name(self) -> str: ...

class SigningData(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Poppler.SigningData
    """

    def copy(self) -> SigningData: ...
    def free(self) -> None: ...
    def get_background_color(self) -> Color: ...
    def get_border_color(self) -> Color: ...
    def get_border_width(self) -> float: ...
    def get_certificate_info(self) -> CertificateInfo: ...
    def get_destination_filename(self) -> str: ...
    def get_document_owner_password(self) -> str: ...
    def get_document_user_password(self) -> str: ...
    def get_field_partial_name(self) -> str: ...
    def get_font_color(self) -> Color: ...
    def get_font_size(self) -> float: ...
    def get_image_path(self) -> str: ...
    def get_left_font_size(self) -> float: ...
    def get_location(self) -> str: ...
    def get_page(self) -> int: ...
    def get_password(self) -> str: ...
    def get_reason(self) -> str: ...
    def get_signature_rectangle(self) -> Rectangle: ...
    def get_signature_text(self) -> str: ...
    def get_signature_text_left(self) -> str: ...
    @classmethod
    def new(cls) -> SigningData: ...
    def set_background_color(self, background_color: Color) -> None: ...
    def set_border_color(self, border_color: Color) -> None: ...
    def set_border_width(self, border_width: float) -> None: ...
    def set_certificate_info(self, certificate_info: CertificateInfo) -> None: ...
    def set_destination_filename(self, filename: str) -> None: ...
    def set_document_owner_password(self, document_owner_password: str) -> None: ...
    def set_document_user_password(self, document_user_password: str) -> None: ...
    def set_field_partial_name(self, field_partial_name: str) -> None: ...
    def set_font_color(self, font_color: Color) -> None: ...
    def set_font_size(self, font_size: float) -> None: ...
    def set_image_path(self, image_path: str) -> None: ...
    def set_left_font_size(self, font_size: float) -> None: ...
    def set_location(self, location: str) -> None: ...
    def set_page(self, page: int) -> None: ...
    def set_password(self, password: str) -> None: ...
    def set_reason(self, reason: str) -> None: ...
    def set_signature_rectangle(self, signature_rect: Rectangle) -> None: ...
    def set_signature_text(self, signature_text: str) -> None: ...
    def set_signature_text_left(self, signature_text_left: str) -> None: ...

class StructureElement(GObject.Object):
    """
    :Constructors:

    ::

        StructureElement(**properties)

    Object PopplerStructureElement

    Signals from GObject:
      notify (GParam)
    """

    def get_abbreviation(self) -> str: ...
    def get_actual_text(self) -> str: ...
    def get_alt_text(self) -> str: ...
    def get_background_color(self) -> Tuple[bool, Color]: ...
    def get_baseline_shift(self) -> float: ...
    def get_block_align(self) -> StructureBlockAlign: ...
    def get_border_color(self) -> Tuple[bool, list[Color]]: ...
    def get_border_style(self) -> list[StructureBorderStyle]: ...
    def get_border_thickness(self) -> Tuple[bool, list[float]]: ...
    def get_bounding_box(self) -> Tuple[bool, Rectangle]: ...
    def get_color(self) -> Tuple[bool, Color]: ...
    def get_column_count(self) -> int: ...
    def get_column_gaps(self) -> list[float]: ...
    def get_column_widths(self) -> list[float]: ...
    def get_end_indent(self) -> float: ...
    def get_form_description(self) -> str: ...
    def get_form_role(self) -> StructureFormRole: ...
    def get_form_state(self) -> StructureFormState: ...
    def get_glyph_orientation(self) -> StructureGlyphOrientation: ...
    def get_height(self) -> float: ...
    def get_id(self) -> str: ...
    def get_inline_align(self) -> StructureInlineAlign: ...
    def get_kind(self) -> StructureElementKind: ...
    def get_language(self) -> str: ...
    def get_line_height(self) -> float: ...
    def get_list_numbering(self) -> StructureListNumbering: ...
    def get_padding(self) -> list[float]: ...
    def get_page(self) -> int: ...
    def get_placement(self) -> StructurePlacement: ...
    def get_ruby_align(self) -> StructureRubyAlign: ...
    def get_ruby_position(self) -> StructureRubyPosition: ...
    def get_space_after(self) -> float: ...
    def get_space_before(self) -> float: ...
    def get_start_indent(self) -> float: ...
    def get_table_border_style(self) -> list[StructureBorderStyle]: ...
    def get_table_column_span(self) -> int: ...
    def get_table_headers(self) -> list[str]: ...
    def get_table_padding(self) -> list[float]: ...
    def get_table_row_span(self) -> int: ...
    def get_table_scope(self) -> StructureTableScope: ...
    def get_table_summary(self) -> str: ...
    def get_text(self, flags: StructureGetTextFlags) -> str: ...
    def get_text_align(self) -> StructureTextAlign: ...
    def get_text_decoration_color(self) -> Tuple[bool, Color]: ...
    def get_text_decoration_thickness(self) -> float: ...
    def get_text_decoration_type(self) -> StructureTextDecoration: ...
    def get_text_indent(self) -> float: ...
    def get_text_spans(self) -> list[TextSpan]: ...
    def get_title(self) -> str: ...
    def get_width(self) -> float: ...
    def get_writing_mode(self) -> StructureWritingMode: ...
    def is_block(self) -> bool: ...
    def is_content(self) -> bool: ...
    def is_grouping(self) -> bool: ...
    def is_inline(self) -> bool: ...

class StructureElementIter(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(poppler_document:Poppler.Document) -> Poppler.StructureElementIter
    """

    def copy(self) -> StructureElementIter: ...
    def free(self) -> None: ...
    def get_child(self) -> StructureElementIter: ...
    def get_element(self) -> StructureElement: ...
    @classmethod
    def new(cls, poppler_document: Document) -> StructureElementIter: ...
    def next(self) -> bool: ...

class TextAttributes(GObject.GBoxed):
    """
    :Constructors:

    ::

        TextAttributes()
        new() -> Poppler.TextAttributes
    """

    font_name: str = ...
    font_size: float = ...
    is_underlined: bool = ...
    color: Color = ...
    start_index: int = ...
    end_index: int = ...
    def copy(self) -> TextAttributes: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> TextAttributes: ...

class TextSpan(GObject.GBoxed):
    def copy(self) -> TextSpan: ...
    def free(self) -> None: ...
    def get_color(self) -> Color: ...
    def get_font_name(self) -> str: ...
    def get_text(self) -> str: ...
    def is_bold_font(self) -> bool: ...
    def is_fixed_width_font(self) -> bool: ...
    def is_serif_font(self) -> bool: ...

class AnnotFlag(GObject.GFlags):
    HIDDEN = 2
    INVISIBLE = 1
    LOCKED = 128
    LOCKED_CONTENTS = 512
    NO_ROTATE = 16
    NO_VIEW = 32
    NO_ZOOM = 8
    PRINT = 4
    READ_ONLY = 64
    TOGGLE_NO_VIEW = 256
    UNKNOWN = 0

class FindFlags(GObject.GFlags):
    BACKWARDS = 2
    CASE_SENSITIVE = 1
    DEFAULT = 0
    IGNORE_DIACRITICS = 8
    MULTILINE = 16
    WHOLE_WORDS_ONLY = 4

class Permissions(GObject.GFlags):
    FULL = 255
    OK_TO_ADD_NOTES = 8
    OK_TO_ASSEMBLE = 64
    OK_TO_COPY = 4
    OK_TO_EXTRACT_CONTENTS = 32
    OK_TO_FILL_FORM = 16
    OK_TO_MODIFY = 2
    OK_TO_PRINT = 1
    OK_TO_PRINT_HIGH_RESOLUTION = 128

class PrintFlags(GObject.GFlags):
    ALL = 1
    DOCUMENT = 0
    MARKUP_ANNOTS = 1
    STAMP_ANNOTS_ONLY = 2

class SignatureValidationFlags(GObject.GFlags):
    USE_AIA_CERTIFICATE_FETCH = 4
    VALIDATE_CERTIFICATE = 1
    WITHOUT_OCSP_REVOCATION_CHECK = 2

class StructureGetTextFlags(GObject.GFlags):
    NONE = 0
    RECURSIVE = 1

class ViewerPreferences(GObject.GFlags):
    CENTER_WINDOW = 16
    DIRECTION_RTL = 64
    DISPLAY_DOC_TITLE = 32
    FIT_WINDOW = 8
    HIDE_MENUBAR = 2
    HIDE_TOOLBAR = 1
    HIDE_WINDOWUI = 4
    UNSET = 0

class ActionLayerAction(GObject.GEnum):
    OFF = 1
    ON = 0
    TOGGLE = 2

class ActionMovieOperation(GObject.GEnum):
    PAUSE = 1
    PLAY = 0
    RESUME = 2
    STOP = 3

class ActionType(GObject.GEnum):
    GOTO_DEST = 2
    GOTO_REMOTE = 3
    JAVASCRIPT = 10
    LAUNCH = 4
    MOVIE = 7
    NAMED = 6
    NONE = 1
    OCG_STATE = 9
    RENDITION = 8
    RESET_FORM = 11
    UNKNOWN = 0
    URI = 5

class AdditionalActionType(GObject.GEnum):
    CALCULATE_FIELD = 3
    FIELD_MODIFIED = 0
    FORMAT_FIELD = 1
    VALIDATE_FIELD = 2

class AnnotExternalDataType(GObject.GEnum):
    UNKNOWN = 1

class AnnotFreeTextQuadding(GObject.GEnum):
    CENTERED = 1
    LEFT_JUSTIFIED = 0
    RIGHT_JUSTIFIED = 2

class AnnotMarkupReplyType(GObject.GEnum):
    GROUP = 1
    R = 0

class AnnotStampIcon(GObject.GEnum):
    APPROVED = 1
    AS_IS = 2
    CONFIDENTIAL = 3
    DEPARTMENTAL = 10
    EXPERIMENTAL = 5
    EXPIRED = 6
    FINAL = 4
    FOR_COMMENT = 11
    FOR_PUBLIC_RELEASE = 12
    NONE = 14
    NOT_APPROVED = 7
    NOT_FOR_PUBLIC_RELEASE = 8
    SOLD = 9
    TOP_SECRET = 13
    UNKNOWN = 0

class AnnotTextState(GObject.GEnum):
    ACCEPTED = 2
    CANCELLED = 4
    COMPLETED = 5
    MARKED = 0
    NONE = 6
    REJECTED = 3
    UNKNOWN = 7
    UNMARKED = 1

class AnnotType(GObject.GEnum):
    CARET = 14
    CIRCLE = 6
    FILE_ATTACHMENT = 17
    FREE_TEXT = 3
    HIGHLIGHT = 9
    INK = 15
    LINE = 4
    LINK = 2
    MOVIE = 19
    POLYGON = 7
    POLY_LINE = 8
    POPUP = 16
    PRINTER_MARK = 22
    SCREEN = 21
    SOUND = 18
    SQUARE = 5
    SQUIGGLY = 11
    STAMP = 13
    STRIKE_OUT = 12
    TEXT = 1
    TRAP_NET = 23
    UNDERLINE = 10
    UNKNOWN = 0
    WATERMARK = 24
    WIDGET = 20

class Backend(GObject.GEnum):
    CAIRO = 2
    SPLASH = 1
    UNKNOWN = 0

class CertificateStatus(GObject.GEnum):
    EXPIRED = 4
    GENERIC_ERROR = 5
    NOT_VERIFIED = 6
    REVOKED = 3
    TRUSTED = 0
    UNKNOWN_ISSUER = 2
    UNTRUSTED_ISSUER = 1

class DestType(GObject.GEnum):
    FIT = 2
    FITB = 6
    FITBH = 7
    FITBV = 8
    FITH = 3
    FITR = 5
    FITV = 4
    NAMED = 9
    UNKNOWN = 0
    XYZ = 1

class Error(GObject.GEnum):
    BAD_CATALOG = 3
    DAMAGED = 4
    ENCRYPTED = 1
    INVALID = 0
    OPEN_FILE = 2
    SIGNING = 5
    @staticmethod
    def quark() -> int: ...

class FontType(GObject.GEnum):
    CID_TYPE0 = 7
    CID_TYPE0C = 8
    CID_TYPE0COT = 9
    CID_TYPE2 = 10
    CID_TYPE2OT = 11
    TRUETYPE = 5
    TRUETYPEOT = 6
    TYPE1 = 1
    TYPE1C = 2
    TYPE1COT = 3
    TYPE3 = 4
    UNKNOWN = 0

class FormButtonType(GObject.GEnum):
    CHECK = 1
    PUSH = 0
    RADIO = 2

class FormChoiceType(GObject.GEnum):
    COMBO = 0
    LIST = 1

class FormFieldType(GObject.GEnum):
    BUTTON = 1
    CHOICE = 3
    SIGNATURE = 4
    TEXT = 2
    UNKNOWN = 0

class FormTextType(GObject.GEnum):
    FILE_SELECT = 2
    MULTILINE = 1
    NORMAL = 0

class MoviePlayMode(GObject.GEnum):
    ONCE = 0
    OPEN = 1
    PALINDROME = 3
    REPEAT = 2

class PDFConformance(GObject.GEnum):
    A = 1
    B = 2
    G = 3
    N = 4
    NONE = 8
    P = 5
    PG = 6
    U = 7
    UNSET = 0

class PDFPart(GObject.GEnum):
    NONE = 9
    UNSET = 0

class PDFSubtype(GObject.GEnum):
    NONE = 6
    PDF_A = 1
    PDF_E = 2
    PDF_UA = 3
    PDF_VT = 4
    PDF_X = 5
    UNSET = 0

class PageLayout(GObject.GEnum):
    ONE_COLUMN = 2
    SINGLE_PAGE = 1
    TWO_COLUMN_LEFT = 3
    TWO_COLUMN_RIGHT = 4
    TWO_PAGE_LEFT = 5
    TWO_PAGE_RIGHT = 6
    UNSET = 0

class PageMode(GObject.GEnum):
    FULL_SCREEN = 4
    NONE = 1
    UNSET = 0
    USE_ATTACHMENTS = 6
    USE_OC = 5
    USE_OUTLINES = 2
    USE_THUMBS = 3

class PageTransitionAlignment(GObject.GEnum):
    HORIZONTAL = 0
    VERTICAL = 1

class PageTransitionDirection(GObject.GEnum):
    INWARD = 0
    OUTWARD = 1

class PageTransitionType(GObject.GEnum):
    BLINDS = 2
    BOX = 3
    COVER = 9
    DISSOLVE = 5
    FADE = 11
    FLY = 7
    GLITTER = 6
    PUSH = 8
    REPLACE = 0
    SPLIT = 1
    UNCOVER = 10
    WIPE = 4

class PrintDuplex(GObject.GEnum):
    DUPLEX_FLIP_LONG_EDGE = 3
    DUPLEX_FLIP_SHORT_EDGE = 2
    NONE = 0
    SIMPLEX = 1

class PrintScaling(GObject.GEnum):
    APP_DEFAULT = 0
    NONE = 1

class SelectionStyle(GObject.GEnum):
    GLYPH = 0
    LINE = 2
    WORD = 1

class SignatureStatus(GObject.GEnum):
    DECODING_ERROR = 3
    DIGEST_MISMATCH = 2
    GENERIC_ERROR = 4
    INVALID = 1
    NOT_FOUND = 5
    NOT_VERIFIED = 6
    VALID = 0

class StructureBlockAlign(GObject.GEnum):
    AFTER = 2
    BEFORE = 0
    JUSTIFY = 3
    MIDDLE = 1

class StructureBorderStyle(GObject.GEnum):
    DASHED = 3
    DOTTED = 2
    DOUBLE = 5
    GROOVE = 6
    HIDDEN = 1
    INSET = 7
    NONE = 0
    OUTSET = 8
    SOLID = 4

class StructureElementKind(GObject.GEnum):
    ANNOT = 14
    ARTICLE = 4
    BIBENTRY = 11
    BLOCKQUOTE = 15
    CAPTION = 16
    CODE = 12
    CONTENT = 0
    DIV = 6
    DOCUMENT = 2
    FIGURE = 48
    FORM = 50
    FORMULA = 49
    HEADING = 23
    HEADING_1 = 24
    HEADING_2 = 25
    HEADING_3 = 26
    HEADING_4 = 27
    HEADING_5 = 28
    HEADING_6 = 29
    INDEX = 20
    LINK = 13
    LIST = 30
    LIST_BODY = 33
    LIST_ITEM = 31
    LIST_LABEL = 32
    NONSTRUCT = 17
    NOTE = 9
    OBJECT_REFERENCE = 1
    PARAGRAPH = 22
    PART = 3
    PRIVATE = 21
    QUOTE = 8
    REFERENCE = 10
    RUBY = 41
    RUBY_ANNOT_TEXT = 43
    RUBY_BASE_TEXT = 42
    RUBY_PUNCTUATION = 44
    SECTION = 5
    SPAN = 7
    TABLE = 34
    TABLE_BODY = 40
    TABLE_DATA = 37
    TABLE_FOOTER = 39
    TABLE_HEADER = 38
    TABLE_HEADING = 36
    TABLE_ROW = 35
    TOC = 18
    TOC_ITEM = 19
    WARICHU = 45
    WARICHU_PUNCTUATION = 47
    WARICHU_TEXT = 46

class StructureFormRole(GObject.GEnum):
    CHECKBOX = 4
    PUSH_BUTTON = 2
    RADIO_BUTTON = 1
    TEXT_VALUE = 3
    UNDEFINED = 0

class StructureFormState(GObject.GEnum):
    NEUTRAL = 2
    OFF = 1
    ON = 0

class StructureGlyphOrientation(GObject.GEnum):
    AUTO = 0

class StructureInlineAlign(GObject.GEnum):
    CENTER = 1
    END = 2
    START = 0

class StructureListNumbering(GObject.GEnum):
    CIRCLE = 2
    DECIMAL = 4
    DISC = 1
    LOWER_ALPHA = 8
    LOWER_ROMAN = 6
    NONE = 0
    SQUARE = 3
    UPPER_ALPHA = 7
    UPPER_ROMAN = 5

class StructurePlacement(GObject.GEnum):
    BEFORE = 2
    BLOCK = 0
    END = 4
    INLINE = 1
    START = 3

class StructureRubyAlign(GObject.GEnum):
    CENTER = 1
    DISTRIBUTE = 4
    END = 2
    JUSTIFY = 3
    START = 0

class StructureRubyPosition(GObject.GEnum):
    AFTER = 1
    BEFORE = 0
    INLINE = 3
    WARICHU = 2

class StructureTableScope(GObject.GEnum):
    BOTH = 2
    COLUMN = 1
    ROW = 0

class StructureTextAlign(GObject.GEnum):
    CENTER = 1
    END = 2
    JUSTIFY = 3
    START = 0

class StructureTextDecoration(GObject.GEnum):
    LINETHROUGH = 3
    NONE = 0
    OVERLINE = 2
    UNDERLINE = 1

class StructureWritingMode(GObject.GEnum):
    LR_TB = 0
    RL_TB = 1
    TB_RL = 2
