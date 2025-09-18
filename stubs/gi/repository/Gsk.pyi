from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

import cairo
from gi.repository import Gdk
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Graphene
from gi.repository import Pango

_SomeSurface = TypeVar("_SomeSurface", bound=cairo.Surface)

_lock = ...  # FIXME Constant
_namespace: str = "Gsk"
_version: str = "4.0"

def path_parse(string: str) -> Optional[Path]: ...
def serialization_error_quark() -> int: ...
def stroke_equal(stroke1: None, stroke2: None) -> bool: ...
def transform_parse(string: str) -> Tuple[bool, Transform]: ...
def value_dup_render_node(value: Any) -> Optional[RenderNode]: ...
def value_get_render_node(value: Any) -> Optional[RenderNode]: ...
def value_set_render_node(value: Any, node: RenderNode) -> None: ...
def value_take_render_node(value: Any, node: Optional[RenderNode] = None) -> None: ...

class BlendNode(RenderNode):
    """
    :Constructors:

    ::

        BlendNode(**properties)
        new(bottom:Gsk.RenderNode, top:Gsk.RenderNode, blend_mode:Gsk.BlendMode) -> Gsk.BlendNode
    """

    def get_blend_mode(self) -> BlendMode: ...
    def get_bottom_child(self) -> RenderNode: ...
    def get_top_child(self) -> RenderNode: ...
    @classmethod
    def new(
        cls, bottom: RenderNode, top: RenderNode, blend_mode: BlendMode
    ) -> BlendNode: ...

class BlurNode(RenderNode):
    """
    :Constructors:

    ::

        BlurNode(**properties)
        new(child:Gsk.RenderNode, radius:float) -> Gsk.BlurNode
    """

    def get_child(self) -> RenderNode: ...
    def get_radius(self) -> float: ...
    @classmethod
    def new(cls, child: RenderNode, radius: float) -> BlurNode: ...

class BorderNode(RenderNode):
    """
    :Constructors:

    ::

        BorderNode(**properties)
        new(outline:Gsk.RoundedRect, border_width:list, border_color:list) -> Gsk.BorderNode
    """

    def get_colors(self) -> Gdk.RGBA: ...
    def get_outline(self) -> RoundedRect: ...
    def get_widths(self) -> list[float]: ...
    @classmethod
    def new(
        cls,
        outline: RoundedRect,
        border_width: Sequence[float],
        border_color: Sequence[Gdk.RGBA],
    ) -> BorderNode: ...

class BroadwayRenderer(Renderer):
    """
    :Constructors:

    ::

        BroadwayRenderer(**properties)
        new() -> Gsk.Renderer

    Object GskBroadwayRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        realized: bool
        surface: Optional[Gdk.Surface]

    props: Props = ...
    @classmethod
    def new(cls) -> BroadwayRenderer: ...

class BroadwayRendererClass(GObject.GPointer): ...

class CairoNode(RenderNode):
    """
    :Constructors:

    ::

        CairoNode(**properties)
        new(bounds:Graphene.Rect) -> Gsk.CairoNode
    """

    def get_draw_context(self) -> cairo.Context: ...
    def get_surface(self) -> cairo.Surface: ...
    @classmethod
    def new(cls, bounds: Graphene.Rect) -> CairoNode: ...

class CairoRenderer(Renderer):
    """
    :Constructors:

    ::

        CairoRenderer(**properties)
        new() -> Gsk.Renderer

    Object GskCairoRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        realized: bool
        surface: Optional[Gdk.Surface]

    props: Props = ...
    @classmethod
    def new(cls) -> CairoRenderer: ...

class CairoRendererClass(GObject.GPointer): ...

class ClipNode(RenderNode):
    """
    :Constructors:

    ::

        ClipNode(**properties)
        new(child:Gsk.RenderNode, clip:Graphene.Rect) -> Gsk.ClipNode
    """

    def get_child(self) -> RenderNode: ...
    def get_clip(self) -> Graphene.Rect: ...
    @classmethod
    def new(cls, child: RenderNode, clip: Graphene.Rect) -> ClipNode: ...

class ColorMatrixNode(RenderNode):
    """
    :Constructors:

    ::

        ColorMatrixNode(**properties)
        new(child:Gsk.RenderNode, color_matrix:Graphene.Matrix, color_offset:Graphene.Vec4) -> Gsk.ColorMatrixNode
    """

    def get_child(self) -> RenderNode: ...
    def get_color_matrix(self) -> Graphene.Matrix: ...
    def get_color_offset(self) -> Graphene.Vec4: ...
    @classmethod
    def new(
        cls,
        child: RenderNode,
        color_matrix: Graphene.Matrix,
        color_offset: Graphene.Vec4,
    ) -> ColorMatrixNode: ...

class ColorNode(RenderNode):
    """
    :Constructors:

    ::

        ColorNode(**properties)
        new(rgba:Gdk.RGBA, bounds:Graphene.Rect) -> Gsk.ColorNode
    """

    def get_color(self) -> Gdk.RGBA: ...
    @classmethod
    def new(cls, rgba: Gdk.RGBA, bounds: Graphene.Rect) -> ColorNode: ...

class ColorStop(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorStop()
    """

    offset: float = ...
    color: Gdk.RGBA = ...

class ConicGradientNode(RenderNode):
    """
    :Constructors:

    ::

        ConicGradientNode(**properties)
        new(bounds:Graphene.Rect, center:Graphene.Point, rotation:float, color_stops:list) -> Gsk.ConicGradientNode
    """

    def get_angle(self) -> float: ...
    def get_center(self) -> Graphene.Point: ...
    def get_color_stops(self) -> list[ColorStop]: ...
    def get_n_color_stops(self) -> int: ...
    def get_rotation(self) -> float: ...
    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        center: Graphene.Point,
        rotation: float,
        color_stops: Sequence[ColorStop],
    ) -> ConicGradientNode: ...

class ContainerNode(RenderNode):
    """
    :Constructors:

    ::

        ContainerNode(**properties)
        new(children:list) -> Gsk.ContainerNode
    """

    def get_child(self, idx: int) -> RenderNode: ...
    def get_n_children(self) -> int: ...
    @classmethod
    def new(cls, children: Sequence[RenderNode]) -> ContainerNode: ...

class CrossFadeNode(RenderNode):
    """
    :Constructors:

    ::

        CrossFadeNode(**properties)
        new(start:Gsk.RenderNode, end:Gsk.RenderNode, progress:float) -> Gsk.CrossFadeNode
    """

    def get_end_child(self) -> RenderNode: ...
    def get_progress(self) -> float: ...
    def get_start_child(self) -> RenderNode: ...
    @classmethod
    def new(
        cls, start: RenderNode, end: RenderNode, progress: float
    ) -> CrossFadeNode: ...

class DebugNode(RenderNode):
    """
    :Constructors:

    ::

        DebugNode(**properties)
        new(child:Gsk.RenderNode, message:str) -> Gsk.DebugNode
    """

    def get_child(self) -> RenderNode: ...
    def get_message(self) -> str: ...
    @classmethod
    def new(cls, child: RenderNode, message: str) -> DebugNode: ...

class FillNode(RenderNode):
    """
    :Constructors:

    ::

        FillNode(**properties)
        new(child:Gsk.RenderNode, path:Gsk.Path, fill_rule:Gsk.FillRule) -> Gsk.FillNode
    """

    def get_child(self) -> RenderNode: ...
    def get_fill_rule(self) -> FillRule: ...
    def get_path(self) -> Path: ...
    @classmethod
    def new(cls, child: RenderNode, path: Path, fill_rule: FillRule) -> FillNode: ...

class GLRenderer(Renderer):
    """
    :Constructors:

    ::

        GLRenderer(**properties)
        new() -> Gsk.Renderer

    Object GskGLRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        realized: bool
        surface: Optional[Gdk.Surface]

    props: Props = ...
    @classmethod
    def new(cls) -> GLRenderer: ...

class GLRendererClass(GObject.GPointer): ...

class GLShader(GObject.Object):
    """
    :Constructors:

    ::

        GLShader(**properties)
        new_from_bytes(sourcecode:GLib.Bytes) -> Gsk.GLShader
        new_from_resource(resource_path:str) -> Gsk.GLShader

    Object GskGLShader

    Properties from GskGLShader:
      source -> GBytes: source
      resource -> gchararray: resource

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        resource: Optional[str]
        source: GLib.Bytes

    props: Props = ...
    def __init__(self, resource: str = ..., source: GLib.Bytes = ...): ...
    def compile(self, renderer: Renderer) -> bool: ...
    def find_uniform_by_name(self, name: str) -> int: ...
    def get_arg_bool(self, args: GLib.Bytes, idx: int) -> bool: ...
    def get_arg_float(self, args: GLib.Bytes, idx: int) -> float: ...
    def get_arg_int(self, args: GLib.Bytes, idx: int) -> int: ...
    def get_arg_uint(self, args: GLib.Bytes, idx: int) -> int: ...
    def get_arg_vec2(
        self, args: GLib.Bytes, idx: int, out_value: Graphene.Vec2
    ) -> None: ...
    def get_arg_vec3(
        self, args: GLib.Bytes, idx: int, out_value: Graphene.Vec3
    ) -> None: ...
    def get_arg_vec4(
        self, args: GLib.Bytes, idx: int, out_value: Graphene.Vec4
    ) -> None: ...
    def get_args_size(self) -> int: ...
    def get_n_textures(self) -> int: ...
    def get_n_uniforms(self) -> int: ...
    def get_resource(self) -> Optional[str]: ...
    def get_source(self) -> GLib.Bytes: ...
    def get_uniform_name(self, idx: int) -> str: ...
    def get_uniform_offset(self, idx: int) -> int: ...
    def get_uniform_type(self, idx: int) -> GLUniformType: ...
    @classmethod
    def new_from_bytes(cls, sourcecode: GLib.Bytes) -> GLShader: ...
    @classmethod
    def new_from_resource(cls, resource_path: str) -> GLShader: ...

class GLShaderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GLShaderClass()
    """

    parent_class: GObject.ObjectClass = ...

class GLShaderNode(RenderNode):
    """
    :Constructors:

    ::

        GLShaderNode(**properties)
        new(shader:Gsk.GLShader, bounds:Graphene.Rect, args:GLib.Bytes, children:list=None) -> Gsk.GLShaderNode
    """

    def get_args(self) -> GLib.Bytes: ...
    def get_child(self, idx: int) -> RenderNode: ...
    def get_n_children(self) -> int: ...
    def get_shader(self) -> GLShader: ...
    @classmethod
    def new(
        cls,
        shader: GLShader,
        bounds: Graphene.Rect,
        args: GLib.Bytes,
        children: Optional[Sequence[RenderNode]] = None,
    ) -> GLShaderNode: ...

class InsetShadowNode(RenderNode):
    """
    :Constructors:

    ::

        InsetShadowNode(**properties)
        new(outline:Gsk.RoundedRect, color:Gdk.RGBA, dx:float, dy:float, spread:float, blur_radius:float) -> Gsk.InsetShadowNode
    """

    def get_blur_radius(self) -> float: ...
    def get_color(self) -> Gdk.RGBA: ...
    def get_dx(self) -> float: ...
    def get_dy(self) -> float: ...
    def get_outline(self) -> RoundedRect: ...
    def get_spread(self) -> float: ...
    @classmethod
    def new(
        cls,
        outline: RoundedRect,
        color: Gdk.RGBA,
        dx: float,
        dy: float,
        spread: float,
        blur_radius: float,
    ) -> InsetShadowNode: ...

class LinearGradientNode(RenderNode):
    """
    :Constructors:

    ::

        LinearGradientNode(**properties)
        new(bounds:Graphene.Rect, start:Graphene.Point, end:Graphene.Point, color_stops:list) -> Gsk.LinearGradientNode
    """

    def get_color_stops(self) -> list[ColorStop]: ...
    def get_end(self) -> Graphene.Point: ...
    def get_n_color_stops(self) -> int: ...
    def get_start(self) -> Graphene.Point: ...
    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        start: Graphene.Point,
        end: Graphene.Point,
        color_stops: Sequence[ColorStop],
    ) -> LinearGradientNode: ...

class MaskNode(RenderNode):
    """
    :Constructors:

    ::

        MaskNode(**properties)
        new(source:Gsk.RenderNode, mask:Gsk.RenderNode, mask_mode:Gsk.MaskMode) -> Gsk.MaskNode
    """

    def get_mask(self) -> RenderNode: ...
    def get_mask_mode(self) -> MaskMode: ...
    def get_source(self) -> RenderNode: ...
    @classmethod
    def new(
        cls, source: RenderNode, mask: RenderNode, mask_mode: MaskMode
    ) -> MaskNode: ...

class NglRenderer(Renderer):
    """
    :Constructors:

    ::

        NglRenderer(**properties)
        new() -> Gsk.Renderer

    Object GskNglRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        realized: bool
        surface: Optional[Gdk.Surface]

    props: Props = ...
    @classmethod
    def new(cls) -> NglRenderer: ...

class OpacityNode(RenderNode):
    """
    :Constructors:

    ::

        OpacityNode(**properties)
        new(child:Gsk.RenderNode, opacity:float) -> Gsk.OpacityNode
    """

    def get_child(self) -> RenderNode: ...
    def get_opacity(self) -> float: ...
    @classmethod
    def new(cls, child: RenderNode, opacity: float) -> OpacityNode: ...

class OutsetShadowNode(RenderNode):
    """
    :Constructors:

    ::

        OutsetShadowNode(**properties)
        new(outline:Gsk.RoundedRect, color:Gdk.RGBA, dx:float, dy:float, spread:float, blur_radius:float) -> Gsk.OutsetShadowNode
    """

    def get_blur_radius(self) -> float: ...
    def get_color(self) -> Gdk.RGBA: ...
    def get_dx(self) -> float: ...
    def get_dy(self) -> float: ...
    def get_outline(self) -> RoundedRect: ...
    def get_spread(self) -> float: ...
    @classmethod
    def new(
        cls,
        outline: RoundedRect,
        color: Gdk.RGBA,
        dx: float,
        dy: float,
        spread: float,
        blur_radius: float,
    ) -> OutsetShadowNode: ...

class ParseLocation(GObject.GPointer):
    """
    :Constructors:

    ::

        ParseLocation()
    """

    bytes: int = ...
    chars: int = ...
    lines: int = ...
    line_bytes: int = ...
    line_chars: int = ...

class Path(GObject.GBoxed):
    def foreach(
        self, flags: PathForeachFlags, func: Callable[..., bool], *user_data: Any
    ) -> bool: ...
    def get_bounds(self) -> Tuple[bool, Graphene.Rect]: ...
    def get_closest_point(
        self, point: Graphene.Point, threshold: float
    ) -> Tuple[bool, PathPoint, float]: ...
    def get_end_point(self) -> Tuple[bool, PathPoint]: ...
    def get_start_point(self) -> Tuple[bool, PathPoint]: ...
    def get_stroke_bounds(self, stroke: Stroke) -> Tuple[bool, Graphene.Rect]: ...
    def in_fill(self, point: Graphene.Point, fill_rule: FillRule) -> bool: ...
    def is_closed(self) -> bool: ...
    def is_empty(self) -> bool: ...
    @staticmethod
    def parse(string: str) -> Optional[Path]: ...
    def print_(self, string: GLib.String) -> None: ...
    def ref(self) -> Path: ...
    def to_cairo(self, cr: cairo.Context[_SomeSurface]) -> None: ...
    def to_string(self) -> str: ...
    def unref(self) -> None: ...

class PathBuilder(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gsk.PathBuilder
    """

    def add_cairo_path(self, path: cairo.Path) -> None: ...
    def add_circle(self, center: Graphene.Point, radius: float) -> None: ...
    def add_layout(self, layout: Pango.Layout) -> None: ...
    def add_path(self, path: Path) -> None: ...
    def add_rect(self, rect: Graphene.Rect) -> None: ...
    def add_reverse_path(self, path: Path) -> None: ...
    def add_rounded_rect(self, rect: RoundedRect) -> None: ...
    def add_segment(self, path: Path, start: PathPoint, end: PathPoint) -> None: ...
    def arc_to(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def close(self) -> None: ...
    def conic_to(
        self, x1: float, y1: float, x2: float, y2: float, weight: float
    ) -> None: ...
    def cubic_to(
        self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
    ) -> None: ...
    def get_current_point(self) -> Graphene.Point: ...
    def html_arc_to(
        self, x1: float, y1: float, x2: float, y2: float, radius: float
    ) -> None: ...
    def line_to(self, x: float, y: float) -> None: ...
    def move_to(self, x: float, y: float) -> None: ...
    @classmethod
    def new(cls) -> PathBuilder: ...
    def quad_to(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def ref(self) -> PathBuilder: ...
    def rel_arc_to(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def rel_conic_to(
        self, x1: float, y1: float, x2: float, y2: float, weight: float
    ) -> None: ...
    def rel_cubic_to(
        self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
    ) -> None: ...
    def rel_html_arc_to(
        self, x1: float, y1: float, x2: float, y2: float, radius: float
    ) -> None: ...
    def rel_line_to(self, x: float, y: float) -> None: ...
    def rel_move_to(self, x: float, y: float) -> None: ...
    def rel_quad_to(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def rel_svg_arc_to(
        self,
        rx: float,
        ry: float,
        x_axis_rotation: float,
        large_arc: bool,
        positive_sweep: bool,
        x: float,
        y: float,
    ) -> None: ...
    def svg_arc_to(
        self,
        rx: float,
        ry: float,
        x_axis_rotation: float,
        large_arc: bool,
        positive_sweep: bool,
        x: float,
        y: float,
    ) -> None: ...
    def to_path(self) -> Path: ...
    def unref(self) -> None: ...

class PathMeasure(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(path:Gsk.Path) -> Gsk.PathMeasure
        new_with_tolerance(path:Gsk.Path, tolerance:float) -> Gsk.PathMeasure
    """

    def get_length(self) -> float: ...
    def get_path(self) -> Path: ...
    def get_point(self, distance: float) -> Tuple[bool, PathPoint]: ...
    def get_tolerance(self) -> float: ...
    @classmethod
    def new(cls, path: Path) -> PathMeasure: ...
    @classmethod
    def new_with_tolerance(cls, path: Path, tolerance: float) -> PathMeasure: ...
    def ref(self) -> PathMeasure: ...
    def unref(self) -> None: ...

class PathPoint(GObject.GBoxed):
    def compare(self, point2: PathPoint) -> int: ...
    def copy(self) -> PathPoint: ...
    def equal(self, point2: PathPoint) -> bool: ...
    def free(self) -> None: ...
    def get_curvature(
        self, path: Path, direction: PathDirection
    ) -> Tuple[float, Graphene.Point]: ...
    def get_distance(self, measure: PathMeasure) -> float: ...
    def get_position(self, path: Path) -> Graphene.Point: ...
    def get_rotation(self, path: Path, direction: PathDirection) -> float: ...
    def get_tangent(self, path: Path, direction: PathDirection) -> Graphene.Vec2: ...

class RadialGradientNode(RenderNode):
    """
    :Constructors:

    ::

        RadialGradientNode(**properties)
        new(bounds:Graphene.Rect, center:Graphene.Point, hradius:float, vradius:float, start:float, end:float, color_stops:list) -> Gsk.RadialGradientNode
    """

    def get_center(self) -> Graphene.Point: ...
    def get_color_stops(self) -> list[ColorStop]: ...
    def get_end(self) -> float: ...
    def get_hradius(self) -> float: ...
    def get_n_color_stops(self) -> int: ...
    def get_start(self) -> float: ...
    def get_vradius(self) -> float: ...
    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        center: Graphene.Point,
        hradius: float,
        vradius: float,
        start: float,
        end: float,
        color_stops: Sequence[ColorStop],
    ) -> RadialGradientNode: ...

class RenderNode:
    """
    :Constructors:

    ::

        RenderNode(**properties)
    """

    @staticmethod
    def deserialize(
        bytes: GLib.Bytes,
        error_func: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> Optional[RenderNode]: ...
    def draw(self, cr: cairo.Context[_SomeSurface]) -> None: ...
    def get_bounds(self) -> Graphene.Rect: ...
    def get_node_type(self) -> RenderNodeType: ...
    def ref(self) -> RenderNode: ...
    def serialize(self) -> GLib.Bytes: ...
    def unref(self) -> None: ...
    def write_to_file(self, filename: str) -> bool: ...

class Renderer(GObject.Object):
    """
    :Constructors:

    ::

        Renderer(**properties)
        new_for_surface(surface:Gdk.Surface) -> Gsk.Renderer or None

    Object GskRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        realized: bool
        surface: Optional[Gdk.Surface]

    props: Props = ...
    def get_surface(self) -> Optional[Gdk.Surface]: ...
    def is_realized(self) -> bool: ...
    @classmethod
    def new_for_surface(cls, surface: Gdk.Surface) -> Optional[Renderer]: ...
    def realize(self, surface: Optional[Gdk.Surface] = None) -> bool: ...
    def realize_for_display(self, display: Gdk.Display) -> bool: ...
    def render(
        self, root: RenderNode, region: Optional[cairo.Region] = None
    ) -> None: ...
    def render_texture(
        self, root: RenderNode, viewport: Optional[Graphene.Rect] = None
    ) -> Gdk.Texture: ...
    def unrealize(self) -> None: ...

class RendererClass(GObject.GPointer): ...

class RepeatNode(RenderNode):
    """
    :Constructors:

    ::

        RepeatNode(**properties)
        new(bounds:Graphene.Rect, child:Gsk.RenderNode, child_bounds:Graphene.Rect=None) -> Gsk.RepeatNode
    """

    def get_child(self) -> RenderNode: ...
    def get_child_bounds(self) -> Graphene.Rect: ...
    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        child: RenderNode,
        child_bounds: Optional[Graphene.Rect] = None,
    ) -> RepeatNode: ...

class RepeatingLinearGradientNode(RenderNode):
    """
    :Constructors:

    ::

        RepeatingLinearGradientNode(**properties)
        new(bounds:Graphene.Rect, start:Graphene.Point, end:Graphene.Point, color_stops:list) -> Gsk.RepeatingLinearGradientNode
    """

    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        start: Graphene.Point,
        end: Graphene.Point,
        color_stops: Sequence[ColorStop],
    ) -> RepeatingLinearGradientNode: ...

class RepeatingRadialGradientNode(RenderNode):
    """
    :Constructors:

    ::

        RepeatingRadialGradientNode(**properties)
        new(bounds:Graphene.Rect, center:Graphene.Point, hradius:float, vradius:float, start:float, end:float, color_stops:list) -> Gsk.RepeatingRadialGradientNode
    """

    @classmethod
    def new(
        cls,
        bounds: Graphene.Rect,
        center: Graphene.Point,
        hradius: float,
        vradius: float,
        start: float,
        end: float,
        color_stops: Sequence[ColorStop],
    ) -> RepeatingRadialGradientNode: ...

class RoundedClipNode(RenderNode):
    """
    :Constructors:

    ::

        RoundedClipNode(**properties)
        new(child:Gsk.RenderNode, clip:Gsk.RoundedRect) -> Gsk.RoundedClipNode
    """

    def get_child(self) -> RenderNode: ...
    def get_clip(self) -> RoundedRect: ...
    @classmethod
    def new(cls, child: RenderNode, clip: RoundedRect) -> RoundedClipNode: ...

class RoundedRect(GObject.GPointer):
    """
    :Constructors:

    ::

        RoundedRect()
    """

    bounds: Graphene.Rect = ...
    corner: list[Graphene.Size] = ...
    def contains_point(self, point: Graphene.Point) -> bool: ...
    def contains_rect(self, rect: Graphene.Rect) -> bool: ...
    def init(
        self,
        bounds: Graphene.Rect,
        top_left: Graphene.Size,
        top_right: Graphene.Size,
        bottom_right: Graphene.Size,
        bottom_left: Graphene.Size,
    ) -> RoundedRect: ...
    def init_copy(self, src: RoundedRect) -> RoundedRect: ...
    def init_from_rect(self, bounds: Graphene.Rect, radius: float) -> RoundedRect: ...
    def intersects_rect(self, rect: Graphene.Rect) -> bool: ...
    def is_rectilinear(self) -> bool: ...
    def normalize(self) -> RoundedRect: ...
    def offset(self, dx: float, dy: float) -> RoundedRect: ...
    def shrink(
        self, top: float, right: float, bottom: float, left: float
    ) -> RoundedRect: ...

class ShaderArgsBuilder(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(shader:Gsk.GLShader, initial_values:GLib.Bytes=None) -> Gsk.ShaderArgsBuilder
    """

    @classmethod
    def new(
        cls, shader: GLShader, initial_values: Optional[GLib.Bytes] = None
    ) -> ShaderArgsBuilder: ...
    def ref(self) -> ShaderArgsBuilder: ...
    def set_bool(self, idx: int, value: bool) -> None: ...
    def set_float(self, idx: int, value: float) -> None: ...
    def set_int(self, idx: int, value: int) -> None: ...
    def set_uint(self, idx: int, value: int) -> None: ...
    def set_vec2(self, idx: int, value: Graphene.Vec2) -> None: ...
    def set_vec3(self, idx: int, value: Graphene.Vec3) -> None: ...
    def set_vec4(self, idx: int, value: Graphene.Vec4) -> None: ...
    def to_args(self) -> GLib.Bytes: ...
    def unref(self) -> None: ...

class Shadow(GObject.GPointer):
    """
    :Constructors:

    ::

        Shadow()
    """

    color: Gdk.RGBA = ...
    dx: float = ...
    dy: float = ...
    radius: float = ...

class ShadowNode(RenderNode):
    """
    :Constructors:

    ::

        ShadowNode(**properties)
        new(child:Gsk.RenderNode, shadows:list) -> Gsk.ShadowNode
    """

    def get_child(self) -> RenderNode: ...
    def get_n_shadows(self) -> int: ...
    def get_shadow(self, i: int) -> Shadow: ...
    @classmethod
    def new(cls, child: RenderNode, shadows: Sequence[Shadow]) -> ShadowNode: ...

class Stroke(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(line_width:float) -> Gsk.Stroke
    """

    def copy(self) -> Stroke: ...
    @staticmethod
    def equal(stroke1: None, stroke2: None) -> bool: ...
    def free(self) -> None: ...
    def get_dash(self) -> Optional[list[float]]: ...
    def get_dash_offset(self) -> float: ...
    def get_line_cap(self) -> LineCap: ...
    def get_line_join(self) -> LineJoin: ...
    def get_line_width(self) -> float: ...
    def get_miter_limit(self) -> float: ...
    @classmethod
    def new(cls, line_width: float) -> Stroke: ...
    def set_dash(self, dash: Optional[Sequence[float]] = None) -> None: ...
    def set_dash_offset(self, offset: float) -> None: ...
    def set_line_cap(self, line_cap: LineCap) -> None: ...
    def set_line_join(self, line_join: LineJoin) -> None: ...
    def set_line_width(self, line_width: float) -> None: ...
    def set_miter_limit(self, limit: float) -> None: ...
    def to_cairo(self, cr: cairo.Context[_SomeSurface]) -> None: ...

class StrokeNode(RenderNode):
    """
    :Constructors:

    ::

        StrokeNode(**properties)
        new(child:Gsk.RenderNode, path:Gsk.Path, stroke:Gsk.Stroke) -> Gsk.StrokeNode
    """

    def get_child(self) -> RenderNode: ...
    def get_path(self) -> Path: ...
    def get_stroke(self) -> Stroke: ...
    @classmethod
    def new(cls, child: RenderNode, path: Path, stroke: Stroke) -> StrokeNode: ...

class SubsurfaceNode(RenderNode):
    """
    :Constructors:

    ::

        SubsurfaceNode(**properties)
    """

    def get_child(self) -> RenderNode: ...

class TextNode(RenderNode):
    """
    :Constructors:

    ::

        TextNode(**properties)
        new(font:Pango.Font, glyphs:Pango.GlyphString, color:Gdk.RGBA, offset:Graphene.Point) -> Gsk.TextNode or None
    """

    def get_color(self) -> Gdk.RGBA: ...
    def get_font(self) -> Pango.Font: ...
    def get_glyphs(self) -> list[Pango.GlyphInfo]: ...
    def get_num_glyphs(self) -> int: ...
    def get_offset(self) -> Graphene.Point: ...
    def has_color_glyphs(self) -> bool: ...
    @classmethod
    def new(
        cls,
        font: Pango.Font,
        glyphs: Pango.GlyphString,
        color: Gdk.RGBA,
        offset: Graphene.Point,
    ) -> Optional[TextNode]: ...

class TextureNode(RenderNode):
    """
    :Constructors:

    ::

        TextureNode(**properties)
        new(texture:Gdk.Texture, bounds:Graphene.Rect) -> Gsk.TextureNode
    """

    def get_texture(self) -> Gdk.Texture: ...
    @classmethod
    def new(cls, texture: Gdk.Texture, bounds: Graphene.Rect) -> TextureNode: ...

class TextureScaleNode(RenderNode):
    """
    :Constructors:

    ::

        TextureScaleNode(**properties)
        new(texture:Gdk.Texture, bounds:Graphene.Rect, filter:Gsk.ScalingFilter) -> Gsk.TextureScaleNode
    """

    def get_filter(self) -> ScalingFilter: ...
    def get_texture(self) -> Gdk.Texture: ...
    @classmethod
    def new(
        cls, texture: Gdk.Texture, bounds: Graphene.Rect, filter: ScalingFilter
    ) -> TextureScaleNode: ...

class Transform(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gsk.Transform
    """

    def equal(self, second: Optional[Transform] = None) -> bool: ...
    def get_category(self) -> TransformCategory: ...
    def invert(self) -> Optional[Transform]: ...
    def matrix(self, matrix: Graphene.Matrix) -> Transform: ...
    @classmethod
    def new(cls) -> Transform: ...
    @staticmethod
    def parse(string: str) -> Tuple[bool, Transform]: ...
    def perspective(self, depth: float) -> Transform: ...
    def print_(self, string: GLib.String) -> None: ...
    def ref(self) -> Optional[Transform]: ...
    def rotate(self, angle: float) -> Optional[Transform]: ...
    def rotate_3d(self, angle: float, axis: Graphene.Vec3) -> Optional[Transform]: ...
    def scale(self, factor_x: float, factor_y: float) -> Optional[Transform]: ...
    def scale_3d(
        self, factor_x: float, factor_y: float, factor_z: float
    ) -> Optional[Transform]: ...
    def skew(self, skew_x: float, skew_y: float) -> Optional[Transform]: ...
    def to_2d(self) -> Tuple[float, float, float, float, float, float]: ...
    def to_2d_components(
        self,
    ) -> Tuple[float, float, float, float, float, float, float]: ...
    def to_affine(self) -> Tuple[float, float, float, float]: ...
    def to_matrix(self) -> Graphene.Matrix: ...
    def to_string(self) -> str: ...
    def to_translate(self) -> Tuple[float, float]: ...
    def transform(self, other: Optional[Transform] = None) -> Optional[Transform]: ...
    def transform_bounds(self, rect: Graphene.Rect) -> Graphene.Rect: ...
    def transform_point(self, point: Graphene.Point) -> Graphene.Point: ...
    def translate(self, point: Graphene.Point) -> Optional[Transform]: ...
    def translate_3d(self, point: Graphene.Point3D) -> Optional[Transform]: ...
    def unref(self) -> None: ...

class TransformNode(RenderNode):
    """
    :Constructors:

    ::

        TransformNode(**properties)
        new(child:Gsk.RenderNode, transform:Gsk.Transform) -> Gsk.TransformNode
    """

    def get_child(self) -> RenderNode: ...
    def get_transform(self) -> Transform: ...
    @classmethod
    def new(cls, child: RenderNode, transform: Transform) -> TransformNode: ...

class VulkanRenderer(Renderer):
    """
    :Constructors:

    ::

        VulkanRenderer(**properties)
        new() -> Gsk.Renderer

    Object GskVulkanRenderer

    Properties from GskRenderer:
      realized -> gboolean: realized
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        realized: bool
        surface: Optional[Gdk.Surface]

    props: Props = ...
    @classmethod
    def new(cls) -> VulkanRenderer: ...

class VulkanRendererClass(GObject.GPointer): ...

class PathForeachFlags(GObject.GFlags):
    CONIC = 4
    CUBIC = 2
    ONLY_LINES = 0
    QUAD = 1

class BlendMode(GObject.GEnum):
    COLOR = 12
    COLOR_BURN = 7
    COLOR_DODGE = 6
    DARKEN = 4
    DEFAULT = 0
    DIFFERENCE = 10
    EXCLUSION = 11
    HARD_LIGHT = 8
    HUE = 13
    LIGHTEN = 5
    LUMINOSITY = 15
    MULTIPLY = 1
    OVERLAY = 3
    SATURATION = 14
    SCREEN = 2
    SOFT_LIGHT = 9

class Corner(GObject.GEnum):
    BOTTOM_LEFT = 3
    BOTTOM_RIGHT = 2
    TOP_LEFT = 0
    TOP_RIGHT = 1

class FillRule(GObject.GEnum):
    EVEN_ODD = 1
    WINDING = 0

class GLUniformType(GObject.GEnum):
    BOOL = 4
    FLOAT = 1
    INT = 2
    NONE = 0
    UINT = 3
    VEC2 = 5
    VEC3 = 6
    VEC4 = 7

class LineCap(GObject.GEnum):
    BUTT = 0
    ROUND = 1
    SQUARE = 2

class LineJoin(GObject.GEnum):
    BEVEL = 2
    MITER = 0
    ROUND = 1

class MaskMode(GObject.GEnum):
    ALPHA = 0
    INVERTED_ALPHA = 1
    INVERTED_LUMINANCE = 3
    LUMINANCE = 2

class PathDirection(GObject.GEnum):
    FROM_END = 3
    FROM_START = 0
    TO_END = 2
    TO_START = 1

class PathOperation(GObject.GEnum):
    CLOSE = 1
    CONIC = 5
    CUBIC = 4
    LINE = 2
    MOVE = 0
    QUAD = 3

class RenderNodeType(GObject.GEnum):
    BLEND_NODE = 20
    BLUR_NODE = 23
    BORDER_NODE = 9
    CAIRO_NODE = 2
    CLIP_NODE = 17
    COLOR_MATRIX_NODE = 15
    COLOR_NODE = 3
    CONIC_GRADIENT_NODE = 8
    CONTAINER_NODE = 1
    CROSS_FADE_NODE = 21
    DEBUG_NODE = 24
    FILL_NODE = 28
    GL_SHADER_NODE = 25
    INSET_SHADOW_NODE = 11
    LINEAR_GRADIENT_NODE = 4
    MASK_NODE = 27
    NOT_A_RENDER_NODE = 0
    OPACITY_NODE = 14
    OUTSET_SHADOW_NODE = 12
    RADIAL_GRADIENT_NODE = 6
    REPEATING_LINEAR_GRADIENT_NODE = 5
    REPEATING_RADIAL_GRADIENT_NODE = 7
    REPEAT_NODE = 16
    ROUNDED_CLIP_NODE = 18
    SHADOW_NODE = 19
    STROKE_NODE = 29
    SUBSURFACE_NODE = 30
    TEXTURE_NODE = 10
    TEXTURE_SCALE_NODE = 26
    TEXT_NODE = 22
    TRANSFORM_NODE = 13

class ScalingFilter(GObject.GEnum):
    LINEAR = 0
    NEAREST = 1
    TRILINEAR = 2

class SerializationError(GObject.GEnum):
    INVALID_DATA = 2
    UNSUPPORTED_FORMAT = 0
    UNSUPPORTED_VERSION = 1
    @staticmethod
    def quark() -> int: ...

class TransformCategory(GObject.GEnum):
    ANY = 1
    IDENTITY = 6
    UNKNOWN = 0
