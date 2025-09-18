import typing

from gi.repository import Gio
from gi.repository import Pango
from gi.repository import PangoFc
from gi.repository import fontconfig
from gi.repository import freetype2
T = typing.TypeVar("T")

_namespace: str = "PangoFT2"
_version: str = "1.0"

def font_get_coverage(font: Pango.Font, language: Pango.Language) -> Pango.Coverage: ...
def font_get_kerning(font: Pango.Font, left: int, right: int) -> int: ...
def get_unknown_glyph(font: Pango.Font) -> int: ...
def render(bitmap: freetype2.Bitmap, font: Pango.Font, glyphs: Pango.GlyphString, x: int, y: int) -> None: ...
def render_layout(bitmap: freetype2.Bitmap, layout: Pango.Layout, x: int, y: int) -> None: ...
def render_layout_line(bitmap: freetype2.Bitmap, line: Pango.LayoutLine, x: int, y: int) -> None: ...
def render_layout_line_subpixel(bitmap: freetype2.Bitmap, line: Pango.LayoutLine, x: int, y: int) -> None: ...
def render_layout_subpixel(bitmap: freetype2.Bitmap, layout: Pango.Layout, x: int, y: int) -> None: ...
def render_transformed(bitmap: freetype2.Bitmap, matrix: typing.Optional[Pango.Matrix], font: Pango.Font, glyphs: Pango.GlyphString, x: int, y: int) -> None: ...
def shutdown_display() -> None: ...

class FontMap(PangoFc.FontMap, Gio.ListModel):
    """
    :Constructors:

    ::

        FontMap(**properties)
        new() -> Pango.FontMap

    Object PangoFT2FontMap

    Signals from GListModel:
      items-changed (guint, guint, guint)

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
    @classmethod
    def new(cls) -> FontMap: ...
    def set_default_substitute(self, func: typing.Callable[..., None], *data: typing.Any) -> None: ...
    def set_resolution(self, dpi_x: float, dpi_y: float) -> None: ...
    def substitute_changed(self) -> None: ...
    

