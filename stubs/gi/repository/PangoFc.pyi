import typing

from gi.repository import GObject
from gi.repository import Gio
from gi.repository import Pango
from gi.repository import fontconfig
T = typing.TypeVar("T")

FONT_FEATURES: str = "fontfeatures"
FONT_VARIATIONS: str = "fontvariations"
GRAVITY: str = "pangogravity"
PRGNAME: str = "prgname"
VERSION: str = "pangoversion"
_namespace: str = "PangoFc"
_version: str = "1.0"

class Decoder(GObject.Object):
    """
    :Constructors:

    ::

        Decoder(**properties)

    Object PangoFcDecoder

    Signals from GObject:
      notify (GParam)
    """
    parent_instance: GObject.Object = ...
    def do_get_charset(self, fcfont: Font) -> fontconfig.CharSet: ...
    def do_get_glyph(self, fcfont: Font, wc: int) -> int: ...
    def get_charset(self, fcfont: Font) -> fontconfig.CharSet: ...
    def get_glyph(self, fcfont: Font, wc: int) -> int: ...
    

class DecoderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DecoderClass()
    """
    parent_class: GObject.ObjectClass = ...
    get_charset: typing.Callable[[Decoder, Font], fontconfig.CharSet] = ...
    get_glyph: typing.Callable[[Decoder, Font, int], int] = ...
    _pango_reserved1: None = ...
    _pango_reserved2: None = ...
    _pango_reserved3: None = ...
    _pango_reserved4: None = ...

class Font(Pango.Font):
    """
    :Constructors:

    ::

        Font(**properties)

    Object PangoFcFont

    Properties from PangoFcFont:
      pattern -> gpointer: Pattern
        The fontconfig pattern for this font
      fontmap -> PangoFcFontMap: Font Map
        The PangoFc font map this font is associated with (Since: 1.26)

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        fontmap: FontMap
        pattern: None
    props: Props = ...
    parent_instance: Pango.Font = ...
    font_pattern: fontconfig.Pattern = ...
    fontmap: Pango.FontMap = ...
    priv: None = ...
    matrix: Pango.Matrix = ...
    description: Pango.FontDescription = ...
    metrics_by_lang: list[None] = ...
    is_hinted: int = ...
    is_transformed: int = ...
    def __init__(self, fontmap: FontMap = ...,
                 pattern: None = ...) -> None: ...
    @staticmethod
    def description_from_pattern(pattern: fontconfig.Pattern, include_size: bool) -> Pango.FontDescription: ...
    def get_glyph(self, wc: str) -> int: ...
    def get_languages(self) -> typing.Optional[list[Pango.Language]]: ...
    def get_unknown_glyph(self, wc: str) -> int: ...
    def has_char(self, wc: str) -> bool: ...
    def kern_glyphs(self, glyphs: Pango.GlyphString) -> None: ...
    def unlock_face(self) -> None: ...
    

class FontClass(GObject.GPointer): ...

class FontMap(Pango.FontMap, Gio.ListModel):
    """
    :Constructors:

    ::

        FontMap(**properties)

    Object PangoFcFontMap

    Signals from GListModel:
      items-changed (guint, guint, guint)

    Properties from PangoFontMap:
      item-type -> GType: 
    
      n-items -> guint: 
    

    Signals from GListModel:
      items-changed (guint, guint, guint)

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        item_type: typing.Type[typing.Any]
        n_items: int
    props: Props = ...
    def cache_clear(self) -> None: ...
    def config_changed(self) -> None: ...
    def create_context(self) -> Pango.Context: ...
    def find_decoder(self, pattern: fontconfig.Pattern) -> typing.Optional[Decoder]: ...
    def set_default_substitute(self, func: typing.Callable[..., None], *data: typing.Any) -> None: ...
    def shutdown(self) -> None: ...
    def substitute_changed(self) -> None: ...
    

class FontMapClass(GObject.GPointer): ...

class FontMapPrivate(GObject.GPointer): ...

