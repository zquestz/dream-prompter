import typing

import cairo
from gi.repository import Atk
from gi.repository import Babl
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Gegl
from gi.repository import Gimp
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Pango
T = typing.TypeVar("T")
_SomeSurface = typing.TypeVar("_SomeSurface", bound=cairo.Surface)

COLOR_SELECTOR_BAR_SIZE: int = 15
COLOR_SELECTOR_SIZE: int = 150
ICON_APPLICATION_EXIT: str = "application-exit"
ICON_ASPECT_LANDSCAPE: str = "gimp-landscape"
ICON_ASPECT_PORTRAIT: str = "gimp-portrait"
ICON_ATTACH: str = "gimp-attach"
ICON_BUSINESS_CARD: str = "gimp-business-card"
ICON_CAP_BUTT: str = "gimp-cap-butt"
ICON_CAP_ROUND: str = "gimp-cap-round"
ICON_CAP_SQUARE: str = "gimp-cap-square"
ICON_CENTER: str = "gimp-center"
ICON_CENTER_HORIZONTAL: str = "gimp-hcenter"
ICON_CENTER_VERTICAL: str = "gimp-vcenter"
ICON_CHAIN_HORIZONTAL: str = "gimp-hchain"
ICON_CHAIN_HORIZONTAL_BROKEN: str = "gimp-hchain-broken"
ICON_CHAIN_VERTICAL: str = "gimp-vchain"
ICON_CHAIN_VERTICAL_BROKEN: str = "gimp-vchain-broken"
ICON_CHANNEL: str = "gimp-channel"
ICON_CHANNEL_ALPHA: str = "gimp-channel-alpha"
ICON_CHANNEL_BLUE: str = "gimp-channel-blue"
ICON_CHANNEL_GRAY: str = "gimp-channel-gray"
ICON_CHANNEL_GREEN: str = "gimp-channel-green"
ICON_CHANNEL_INDEXED: str = "gimp-channel-indexed"
ICON_CHANNEL_RED: str = "gimp-channel-red"
ICON_CHAR_PICKER: str = "gimp-char-picker"
ICON_CLOSE: str = "gimp-close"
ICON_CLOSE_ALL: str = "gimp-close-all"
ICON_COLORMAP: str = "gimp-colormap"
ICON_COLORS_DEFAULT: str = "gimp-default-colors"
ICON_COLORS_SWAP: str = "gimp-swap-colors"
ICON_COLOR_PICKER_BLACK: str = "gimp-color-picker-black"
ICON_COLOR_PICKER_GRAY: str = "gimp-color-picker-gray"
ICON_COLOR_PICKER_WHITE: str = "gimp-color-picker-white"
ICON_COLOR_PICK_FROM_SCREEN: str = "gimp-color-pick-from-screen"
ICON_COLOR_SELECTOR_CMYK: str = "gimp-color-cmyk"
ICON_COLOR_SELECTOR_TRIANGLE: str = "gimp-color-triangle"
ICON_COLOR_SELECTOR_WATER: str = "gimp-color-water"
ICON_COLOR_SPACE_LINEAR: str = "gimp-color-space-linear"
ICON_COLOR_SPACE_NON_LINEAR: str = "gimp-color-space-non-linear"
ICON_COLOR_SPACE_PERCEPTUAL: str = "gimp-color-space-perceptual"
ICON_CONTROLLER: str = "gimp-controller"
ICON_CONTROLLER_KEYBOARD: str = "gimp-controller-keyboard"
ICON_CONTROLLER_LINUX_INPUT: str = "gimp-controller-linux-input"
ICON_CONTROLLER_MIDI: str = "gimp-controller-midi"
ICON_CONTROLLER_WHEEL: str = "gimp-controller-wheel"
ICON_CONVERT_GRAYSCALE: str = "gimp-convert-grayscale"
ICON_CONVERT_INDEXED: str = "gimp-convert-indexed"
ICON_CONVERT_RGB: str = "gimp-convert-rgb"
ICON_CURSOR: str = "gimp-cursor"
ICON_CURVE_FREE: str = "gimp-curve-free"
ICON_CURVE_SMOOTH: str = "gimp-curve-smooth"
ICON_DETACH: str = "gimp-detach"
ICON_DIALOG_CHANNELS: str = "gimp-channels"
ICON_DIALOG_DASHBOARD: str = "gimp-dashboard"
ICON_DIALOG_DEVICE_STATUS: str = "gimp-device-status"
ICON_DIALOG_ERROR: str = "dialog-error"
ICON_DIALOG_IMAGES: str = "gimp-images"
ICON_DIALOG_INFORMATION: str = "dialog-information"
ICON_DIALOG_LAYERS: str = "gimp-layers"
ICON_DIALOG_NAVIGATION: str = "gimp-navigation"
ICON_DIALOG_PATHS: str = "gimp-paths"
ICON_DIALOG_QUESTION: str = "dialog-question"
ICON_DIALOG_RESHOW_FILTER: str = "gimp-reshow-filter"
ICON_DIALOG_TOOLS: str = "gimp-tools"
ICON_DIALOG_TOOL_OPTIONS: str = "gimp-tool-options"
ICON_DIALOG_UNDO_HISTORY: str = "gimp-undo-history"
ICON_DIALOG_WARNING: str = "dialog-warning"
ICON_DISPLAY: str = "gimp-display"
ICON_DISPLAY_FILTER: str = "gimp-display-filter"
ICON_DISPLAY_FILTER_CLIP_WARNING: str = "gimp-display-filter-clip-warning"
ICON_DISPLAY_FILTER_COLORBLIND: str = "gimp-display-filter-colorblind"
ICON_DISPLAY_FILTER_CONTRAST: str = "gimp-display-filter-contrast"
ICON_DISPLAY_FILTER_GAMMA: str = "gimp-display-filter-gamma"
ICON_DISPLAY_FILTER_LCMS: str = "gimp-display-filter-lcms"
ICON_DISPLAY_FILTER_PROOF: str = "gimp-display-filter-proof"
ICON_DOCUMENT_NEW: str = "document-new"
ICON_DOCUMENT_OPEN: str = "document-open"
ICON_DOCUMENT_OPEN_RECENT: str = "document-open-recent"
ICON_DOCUMENT_PAGE_SETUP: str = "document-page-setup"
ICON_DOCUMENT_PRINT: str = "document-print"
ICON_DOCUMENT_PRINT_RESOLUTION: str = "document-print"
ICON_DOCUMENT_PROPERTIES: str = "document-properties"
ICON_DOCUMENT_REVERT: str = "document-revert"
ICON_DOCUMENT_SAVE: str = "document-save"
ICON_DOCUMENT_SAVE_AS: str = "document-save-as"
ICON_DYNAMICS: str = "gimp-dynamics"
ICON_EDIT: str = "gtk-edit"
ICON_EDIT_CLEAR: str = "edit-clear"
ICON_EDIT_COPY: str = "edit-copy"
ICON_EDIT_CUT: str = "edit-cut"
ICON_EDIT_DELETE: str = "edit-delete"
ICON_EDIT_FIND: str = "edit-find"
ICON_EDIT_PASTE: str = "edit-paste"
ICON_EDIT_PASTE_AS_NEW: str = "gimp-paste-as-new"
ICON_EDIT_PASTE_INTO: str = "gimp-paste-into"
ICON_EDIT_REDO: str = "edit-redo"
ICON_EDIT_UNDO: str = "edit-undo"
ICON_EFFECT: str = "gimp-effects"
ICON_EVEN_HORIZONTAL_GAP: str = "gimp-even-horizontal-gap"
ICON_EVEN_VERTICAL_GAP: str = "gimp-even-vertical-gap"
ICON_FILE_MANAGER: str = "gimp-file-manager"
ICON_FILL_HORIZONTAL: str = "gimp-hfill"
ICON_FILL_VERTICAL: str = "gimp-vfill"
ICON_FOLDER_NEW: str = "folder-new"
ICON_FONT: str = "gtk-select-font"
ICON_FORMAT_INDENT_LESS: str = "format-indent-less"
ICON_FORMAT_INDENT_MORE: str = "format-indent-more"
ICON_FORMAT_JUSTIFY_CENTER: str = "format-justify-center"
ICON_FORMAT_JUSTIFY_FILL: str = "format-justify-fill"
ICON_FORMAT_JUSTIFY_LEFT: str = "format-justify-left"
ICON_FORMAT_JUSTIFY_RIGHT: str = "format-justify-right"
ICON_FORMAT_TEXT_BOLD: str = "format-text-bold"
ICON_FORMAT_TEXT_DIRECTION_LTR: str = "format-text-direction-ltr"
ICON_FORMAT_TEXT_DIRECTION_RTL: str = "format-text-direction-rtl"
ICON_FORMAT_TEXT_DIRECTION_TTB_LTR: str = "gimp-text-dir-ttb-ltr"
ICON_FORMAT_TEXT_DIRECTION_TTB_LTR_UPRIGHT: str = "gimp-text-dir-ttb-ltr-upright"
ICON_FORMAT_TEXT_DIRECTION_TTB_RTL: str = "gimp-text-dir-ttb-rtl"
ICON_FORMAT_TEXT_DIRECTION_TTB_RTL_UPRIGHT: str = "gimp-text-dir-ttb-rtl-upright"
ICON_FORMAT_TEXT_ITALIC: str = "format-text-italic"
ICON_FORMAT_TEXT_SPACING_LETTER: str = "gimp-letter-spacing"
ICON_FORMAT_TEXT_SPACING_LINE: str = "gimp-line-spacing"
ICON_FORMAT_TEXT_STRIKETHROUGH: str = "format-text-strikethrough"
ICON_FORMAT_TEXT_UNDERLINE: str = "format-text-underline"
ICON_FRAME: str = "gimp-frame"
ICON_GEGL: str = "gimp-gegl"
ICON_GO_BOTTOM: str = "go-bottom"
ICON_GO_DOWN: str = "go-down"
ICON_GO_FIRST: str = "go-first"
ICON_GO_HOME: str = "go-home"
ICON_GO_LAST: str = "go-last"
ICON_GO_NEXT: str = "go-next"
ICON_GO_PREVIOUS: str = "go-previous"
ICON_GO_TOP: str = "go-top"
ICON_GO_UP: str = "go-up"
ICON_GRADIENT_BILINEAR: str = "gimp-gradient-bilinear"
ICON_GRADIENT_CONICAL_ASYMMETRIC: str = "gimp-gradient-conical-asymmetric"
ICON_GRADIENT_CONICAL_SYMMETRIC: str = "gimp-gradient-conical-symmetric"
ICON_GRADIENT_LINEAR: str = "gimp-gradient-linear"
ICON_GRADIENT_RADIAL: str = "gimp-gradient-radial"
ICON_GRADIENT_SHAPEBURST_ANGULAR: str = "gimp-gradient-shapeburst-angular"
ICON_GRADIENT_SHAPEBURST_DIMPLED: str = "gimp-gradient-shapeburst-dimpled"
ICON_GRADIENT_SHAPEBURST_SPHERICAL: str = "gimp-gradient-shapeburst-spherical"
ICON_GRADIENT_SPIRAL_ANTICLOCKWISE: str = "gimp-gradient-spiral-anticlockwise"
ICON_GRADIENT_SPIRAL_CLOCKWISE: str = "gimp-gradient-spiral-clockwise"
ICON_GRADIENT_SQUARE: str = "gimp-gradient-square"
ICON_GRAVITY_EAST: str = "gimp-gravity-east"
ICON_GRAVITY_NORTH: str = "gimp-gravity-north"
ICON_GRAVITY_NORTH_EAST: str = "gimp-gravity-north-east"
ICON_GRAVITY_NORTH_WEST: str = "gimp-gravity-north-west"
ICON_GRAVITY_SOUTH: str = "gimp-gravity-south"
ICON_GRAVITY_SOUTH_EAST: str = "gimp-gravity-south-east"
ICON_GRAVITY_SOUTH_WEST: str = "gimp-gravity-south-west"
ICON_GRAVITY_WEST: str = "gimp-gravity-west"
ICON_GRID: str = "gimp-grid"
ICON_HELP: str = "system-help"
ICON_HELP_ABOUT: str = "help-about"
ICON_HELP_USER_MANUAL: str = "gimp-user-manual"
ICON_HISTOGRAM: str = "gimp-histogram"
ICON_HISTOGRAM_LINEAR: str = "gimp-histogram-linear"
ICON_HISTOGRAM_LOGARITHMIC: str = "gimp-histogram-logarithmic"
ICON_IMAGE: str = "gimp-image"
ICON_IMAGE_OPEN: str = "gimp-image-open"
ICON_IMAGE_RELOAD: str = "gimp-image-reload"
ICON_INPUT_DEVICE: str = "gimp-input-device"
ICON_INVERT: str = "gimp-invert"
ICON_JOIN_BEVEL: str = "gimp-join-bevel"
ICON_JOIN_MITER: str = "gimp-join-miter"
ICON_JOIN_ROUND: str = "gimp-join-round"
ICON_LAYER: str = "gimp-layer"
ICON_LAYER_ANCHOR: str = "gimp-anchor"
ICON_LAYER_FLOATING_SELECTION: str = "gimp-floating-selection"
ICON_LAYER_MASK: str = "gimp-layer-mask"
ICON_LAYER_MERGE_DOWN: str = "gimp-merge-down"
ICON_LAYER_TEXT_LAYER: str = "gimp-text-layer"
ICON_LAYER_TO_IMAGESIZE: str = "gimp-layer-to-imagesize"
ICON_LINKED: str = "gimp-linked"
ICON_LIST: str = "gimp-list"
ICON_LIST_ADD: str = "list-add"
ICON_LIST_REMOVE: str = "list-remove"
ICON_LOCK: str = "gimp-lock"
ICON_LOCK_ALPHA: str = "gimp-lock-alpha"
ICON_LOCK_CONTENT: str = "gimp-lock-content"
ICON_LOCK_MULTI: str = "gimp-lock-multi"
ICON_LOCK_PATH: str = "gimp-lock-path"
ICON_LOCK_POSITION: str = "gimp-lock-position"
ICON_LOCK_VISIBILITY: str = "gimp-lock-visibility"
ICON_MARKER: str = "gimp-marker"
ICON_MENU_LEFT: str = "gimp-menu-left"
ICON_MENU_RIGHT: str = "gimp-menu-right"
ICON_OBJECT_DUPLICATE: str = "gimp-duplicate"
ICON_OBJECT_FLIP_HORIZONTAL: str = "object-flip-horizontal"
ICON_OBJECT_FLIP_VERTICAL: str = "object-flip-vertical"
ICON_OBJECT_RESIZE: str = "gimp-resize"
ICON_OBJECT_ROTATE_180: str = "gimp-rotate-180"
ICON_OBJECT_ROTATE_270: str = "object-rotate-left"
ICON_OBJECT_ROTATE_90: str = "object-rotate-right"
ICON_OBJECT_SCALE: str = "gimp-scale"
ICON_PALETTE: str = "gtk-select-color"
ICON_PATH: str = "gimp-path"
ICON_PATH_STROKE: str = "gimp-path-stroke"
ICON_PATTERN: str = "gimp-pattern"
ICON_PIVOT_CENTER: str = "gimp-pivot-center"
ICON_PIVOT_EAST: str = "gimp-pivot-east"
ICON_PIVOT_NORTH: str = "gimp-pivot-north"
ICON_PIVOT_NORTH_EAST: str = "gimp-pivot-north-east"
ICON_PIVOT_NORTH_WEST: str = "gimp-pivot-north-west"
ICON_PIVOT_SOUTH: str = "gimp-pivot-south"
ICON_PIVOT_SOUTH_EAST: str = "gimp-pivot-south-east"
ICON_PIVOT_SOUTH_WEST: str = "gimp-pivot-south-west"
ICON_PIVOT_WEST: str = "gimp-pivot-west"
ICON_PLUGIN: str = "gimp-plugin"
ICON_PREFERENCES_SYSTEM: str = "preferences-system"
ICON_PROCESS_STOP: str = "process-stop"
ICON_QUICK_MASK_OFF: str = "gimp-quick-mask-off"
ICON_QUICK_MASK_ON: str = "gimp-quick-mask-on"
ICON_RECORD: str = "media-record"
ICON_RESET: str = "gimp-reset"
ICON_SAMPLE_POINT: str = "gimp-sample-point"
ICON_SELECTION: str = "gimp-selection"
ICON_SELECTION_ADD: str = "gimp-selection-add"
ICON_SELECTION_ALL: str = "gimp-selection-all"
ICON_SELECTION_BORDER: str = "gimp-selection-border"
ICON_SELECTION_GROW: str = "gimp-selection-grow"
ICON_SELECTION_INTERSECT: str = "gimp-selection-intersect"
ICON_SELECTION_NONE: str = "gimp-selection-none"
ICON_SELECTION_REPLACE: str = "gimp-selection-replace"
ICON_SELECTION_SHRINK: str = "gimp-selection-shrink"
ICON_SELECTION_STROKE: str = "gimp-selection-stroke"
ICON_SELECTION_SUBTRACT: str = "gimp-selection-subtract"
ICON_SELECTION_TO_CHANNEL: str = "gimp-selection-to-channel"
ICON_SELECTION_TO_PATH: str = "gimp-selection-to-path"
ICON_SHAPE_CIRCLE: str = "gimp-shape-circle"
ICON_SHAPE_DIAMOND: str = "gimp-shape-diamond"
ICON_SHAPE_SQUARE: str = "gimp-shape-square"
ICON_SHRED: str = "gimp-shred"
ICON_SMARTPHONE: str = "gimp-smartphone"
ICON_SYMMETRY: str = "gimp-symmetry"
ICON_SYSTEM_RUN: str = "system-run"
ICON_TEMPLATE: str = "gimp-template"
ICON_TEXTURE: str = "gimp-texture"
ICON_TOOL_AIRBRUSH: str = "gimp-tool-airbrush"
ICON_TOOL_ALIGN: str = "gimp-tool-align"
ICON_TOOL_BLUR: str = "gimp-tool-blur"
ICON_TOOL_BRIGHTNESS_CONTRAST: str = "gimp-tool-brightness-contrast"
ICON_TOOL_BUCKET_FILL: str = "gimp-tool-bucket-fill"
ICON_TOOL_BY_COLOR_SELECT: str = "gimp-tool-by-color-select"
ICON_TOOL_CAGE: str = "gimp-tool-cage"
ICON_TOOL_CLONE: str = "gimp-tool-clone"
ICON_TOOL_COLORIZE: str = "gimp-tool-colorize"
ICON_TOOL_COLOR_BALANCE: str = "gimp-tool-color-balance"
ICON_TOOL_COLOR_PICKER: str = "gimp-tool-color-picker"
ICON_TOOL_COLOR_TEMPERATURE: str = "gimp-tool-color-temperature"
ICON_TOOL_CROP: str = "gimp-tool-crop"
ICON_TOOL_CURVES: str = "gimp-tool-curves"
ICON_TOOL_DESATURATE: str = "gimp-tool-desaturate"
ICON_TOOL_DODGE: str = "gimp-tool-dodge"
ICON_TOOL_ELLIPSE_SELECT: str = "gimp-tool-ellipse-select"
ICON_TOOL_ERASER: str = "gimp-tool-eraser"
ICON_TOOL_EXPOSURE: str = "gimp-tool-exposure"
ICON_TOOL_FLIP: str = "gimp-tool-flip"
ICON_TOOL_FOREGROUND_SELECT: str = "gimp-tool-foreground-select"
ICON_TOOL_FREE_SELECT: str = "gimp-tool-free-select"
ICON_TOOL_FUZZY_SELECT: str = "gimp-tool-fuzzy-select"
ICON_TOOL_GRADIENT: str = "gimp-tool-gradient"
ICON_TOOL_HANDLE_TRANSFORM: str = "gimp-tool-handle-transform"
ICON_TOOL_HEAL: str = "gimp-tool-heal"
ICON_TOOL_HUE_SATURATION: str = "gimp-tool-hue-saturation"
ICON_TOOL_INK: str = "gimp-tool-ink"
ICON_TOOL_ISCISSORS: str = "gimp-tool-iscissors"
ICON_TOOL_LEVELS: str = "gimp-tool-levels"
ICON_TOOL_MEASURE: str = "gimp-tool-measure"
ICON_TOOL_MOVE: str = "gimp-tool-move"
ICON_TOOL_MYPAINT_BRUSH: str = "gimp-tool-mypaint-brush"
ICON_TOOL_N_POINT_DEFORMATION: str = "gimp-tool-n-point-deformation"
ICON_TOOL_OFFSET: str = "gimp-tool-offset"
ICON_TOOL_PAINTBRUSH: str = "gimp-tool-paintbrush"
ICON_TOOL_PAINT_SELECT: str = "gimp-tool-paint-select"
ICON_TOOL_PATH: str = "gimp-tool-path"
ICON_TOOL_PENCIL: str = "gimp-tool-pencil"
ICON_TOOL_PERSPECTIVE: str = "gimp-tool-perspective"
ICON_TOOL_PERSPECTIVE_CLONE: str = "gimp-tool-perspective-clone"
ICON_TOOL_POSTERIZE: str = "gimp-tool-posterize"
ICON_TOOL_PRESET: str = "gimp-tool-preset"
ICON_TOOL_RECT_SELECT: str = "gimp-tool-rect-select"
ICON_TOOL_ROTATE: str = "gimp-tool-rotate"
ICON_TOOL_SCALE: str = "gimp-tool-scale"
ICON_TOOL_SEAMLESS_CLONE: str = "gimp-tool-seamless-clone"
ICON_TOOL_SHADOWS_HIGHLIGHTS: str = "gimp-tool-shadows-highlights"
ICON_TOOL_SHEAR: str = "gimp-tool-shear"
ICON_TOOL_SMUDGE: str = "gimp-tool-smudge"
ICON_TOOL_TEXT: str = "gimp-tool-text"
ICON_TOOL_THRESHOLD: str = "gimp-tool-threshold"
ICON_TOOL_TRANSFORM_3D: str = "gimp-tool-transform-3d"
ICON_TOOL_UNIFIED_TRANSFORM: str = "gimp-tool-unified-transform"
ICON_TOOL_WARP: str = "gimp-tool-warp"
ICON_TOOL_ZOOM: str = "gimp-tool-zoom"
ICON_TRANSFORM_3D_CAMERA: str = "gimp-transform-3d-camera"
ICON_TRANSFORM_3D_MOVE: str = "gimp-transform-3d-move"
ICON_TRANSFORM_3D_ROTATE: str = "gimp-transform-3d-rotate"
ICON_TRANSPARENCY: str = "gimp-transparency"
ICON_VIDEO: str = "gimp-video"
ICON_VIEW_FULLSCREEN: str = "view-fullscreen"
ICON_VIEW_REFRESH: str = "view-refresh"
ICON_VIEW_SHRINK_WRAP: str = "view-shrink-wrap"
ICON_VIEW_ZOOM_FILL: str = "view-zoom-fill"
ICON_VISIBLE: str = "gimp-visible"
ICON_WEB: str = "gimp-web"
ICON_WILBER: str = "gimp-wilber"
ICON_WILBER_EEK: str = "gimp-wilber-eek"
ICON_WINDOW_CLOSE: str = "window-close"
ICON_WINDOW_MOVE_TO_SCREEN: str = "gimp-move-to-screen"
ICON_WINDOW_NEW: str = "window-new"
ICON_ZOOM_FIT_BEST: str = "zoom-fit-best"
ICON_ZOOM_FOLLOW_WINDOW: str = "gimp-zoom-follow-window"
ICON_ZOOM_IN: str = "zoom-in"
ICON_ZOOM_ORIGINAL: str = "zoom-original"
ICON_ZOOM_OUT: str = "zoom-out"
_namespace: str = "GimpUi"
_version: str = "3.0"

def cairo_set_focus_line_pattern(cr: cairo.Context[_SomeSurface], widget: Gtk.Widget) -> bool: ...
def cairo_set_source_color(cr: cairo.Context[_SomeSurface], color: Gegl.Color, config: Gimp.ColorConfig, softproof: bool, widget: typing.Optional[Gtk.Widget] = None) -> None: ...
def cairo_surface_create_from_pixbuf(pixbuf: GdkPixbuf.Pixbuf) -> cairo.Surface: ...
def context_help(widget: Gtk.Widget) -> None: ...
def coordinates_new(unit: Gimp.Unit, unit_format: str, menu_show_pixels: bool, menu_show_percent: bool, spinbutton_width: int, update_policy: SizeEntryUpdatePolicy, chainbutton_active: bool, chain_constrains_ratio: bool, xlabel: str, x: float, xres: float, lower_boundary_x: float, upper_boundary_x: float, xsize_0: float, xsize_100: float, ylabel: str, y: float, yres: float, lower_boundary_y: float, upper_boundary_y: float, ysize_0: float, ysize_100: float) -> Gtk.Widget: ...
def double_adjustment_update(adjustment: Gtk.Adjustment) -> float: ...
def enum_icon_box_new(enum_type: typing.Type[typing.Any], icon_prefix: str, icon_size: Gtk.IconSize, callback: typing.Optional[typing.Callable[..., None]] = None, *callback_data: typing.Any) -> typing.Tuple[Gtk.Widget, Gtk.Widget]: ...
def enum_icon_box_new_with_range(enum_type: typing.Type[typing.Any], minimum: int, maximum: int, icon_prefix: str, icon_size: Gtk.IconSize, callback: typing.Optional[typing.Callable[..., None]] = None, *callback_data: typing.Any) -> typing.Tuple[Gtk.Widget, Gtk.Widget]: ...
def enum_icon_box_set_child_padding(icon_box: Gtk.Widget, xpad: int, ypad: int) -> None: ...
def enum_icon_box_set_icon_size(icon_box: Gtk.Widget, icon_size: Gtk.IconSize) -> None: ...
def enum_radio_box_new(enum_type: typing.Type[typing.Any], callback: typing.Optional[typing.Callable[..., None]] = None, *callback_data: typing.Any) -> typing.Tuple[Gtk.Widget, Gtk.Widget]: ...
def enum_radio_box_new_with_range(enum_type: typing.Type[typing.Any], minimum: int, maximum: int, callback: typing.Optional[typing.Callable[..., None]] = None, *callback_data: typing.Any) -> typing.Tuple[Gtk.Widget, Gtk.Widget]: ...
def enum_radio_frame_new(enum_type: typing.Type[typing.Any], label_widget: typing.Optional[Gtk.Widget] = None, callback: typing.Optional[typing.Callable[..., None]] = None, *callback_data: typing.Any) -> typing.Tuple[Gtk.Widget, Gtk.Widget]: ...
def enum_radio_frame_new_with_range(enum_type: typing.Type[typing.Any], minimum: int, maximum: int, label_widget: typing.Optional[Gtk.Widget] = None, callback: typing.Optional[typing.Callable[..., None]] = None, *callback_data: typing.Any) -> typing.Tuple[Gtk.Widget, Gtk.Widget]: ...
def event_triggers_context_menu(event: Gdk.Event, on_release: bool) -> bool: ...
def float_adjustment_update(adjustment: Gtk.Adjustment) -> float: ...
def get_monitor_at_pointer() -> Gdk.Monitor: ...
def grid_attach_aligned(grid: Gtk.Grid, left: int, top: int, label_text: str, label_xalign: float, label_yalign: float, widget: Gtk.Widget, widget_columns: int) -> Gtk.Widget: ...
def help_connect(widget: Gtk.Widget, tooltip: typing.Optional[str], help_func: typing.Callable[..., None], help_id: str, *help_data: typing.Any) -> None: ...
def help_id_quark() -> int: ...
def help_set_help_data(widget: Gtk.Widget, tooltip: typing.Optional[str], help_id: str) -> None: ...
def help_set_help_data_with_markup(widget: Gtk.Widget, tooltip: str, help_id: str) -> None: ...
def icons_init() -> None: ...
def icons_set_icon_theme(path: Gio.File) -> bool: ...
def init(prog_name: str) -> None: ...
def int_adjustment_update(adjustment: Gtk.Adjustment) -> int: ...
def int_radio_group_set_active(radio_button: Gtk.RadioButton, item_data: int) -> None: ...
def monitor_get_color_profile(monitor: Gdk.Monitor) -> typing.Optional[Gimp.ColorProfile]: ...
def proc_view_new(procedure_name: str) -> Gtk.Widget: ...
def prop_boolean_combo_box_new(config: GObject.Object, property_name: str, true_text: str, false_text: str) -> Gtk.Widget: ...
def prop_boolean_radio_frame_new(config: GObject.Object, property_name: str, title: typing.Optional[str], true_text: str, false_text: str) -> Gtk.Widget: ...
def prop_brush_chooser_new(config: GObject.Object, property_name: str, chooser_title: typing.Optional[str] = None) -> Gtk.Widget: ...
def prop_check_button_new(config: GObject.Object, property_name: str, label: typing.Optional[str] = None) -> Gtk.Widget: ...
def prop_choice_combo_box_new(config: GObject.Object, property_name: str) -> Gtk.Widget: ...
def prop_choice_radio_frame_new(config: GObject.Object, property_name: str) -> Gtk.Widget: ...
def prop_color_area_new(config: GObject.Object, property_name: str, width: int, height: int, type: ColorAreaType) -> Gtk.Widget: ...
def prop_color_select_new(config: GObject.Object, property_name: str, width: int, height: int, type: ColorAreaType) -> Gtk.Widget: ...
def prop_coordinates_connect(config: GObject.Object, x_property_name: str, y_property_name: str, unit_property_name: str, sizeentry: Gtk.Widget, chainbutton: Gtk.Widget, xresolution: float, yresolution: float) -> bool: ...
def prop_coordinates_new(config: GObject.Object, x_property_name: str, y_property_name: str, unit_property_name: str, unit_format: str, update_policy: SizeEntryUpdatePolicy, xresolution: float, yresolution: float, has_chainbutton: bool) -> Gtk.Widget: ...
def prop_drawable_chooser_new(config: GObject.Object, property_name: str, chooser_title: typing.Optional[str] = None) -> Gtk.Widget: ...
def prop_entry_new(config: GObject.Object, property_name: str, max_len: int) -> Gtk.Widget: ...
def prop_enum_check_button_new(config: GObject.Object, property_name: str, label: typing.Optional[str], false_value: int, true_value: int) -> Gtk.Widget: ...
def prop_enum_combo_box_new(config: GObject.Object, property_name: str, minimum: int, maximum: int) -> Gtk.Widget: ...
def prop_enum_icon_box_new(config: GObject.Object, property_name: str, icon_prefix: str, minimum: int, maximum: int) -> Gtk.Widget: ...
def prop_enum_label_new(config: GObject.Object, property_name: str) -> Gtk.Widget: ...
def prop_enum_radio_box_new(config: GObject.Object, property_name: str, minimum: int, maximum: int) -> Gtk.Widget: ...
def prop_enum_radio_frame_new(config: GObject.Object, property_name: str, title: typing.Optional[str], minimum: int, maximum: int) -> Gtk.Widget: ...
def prop_expander_new(config: GObject.Object, property_name: str, label: typing.Optional[str] = None) -> Gtk.Widget: ...
def prop_file_chooser_button_new(config: GObject.Object, property_name: str, title: typing.Optional[str], action: Gtk.FileChooserAction) -> Gtk.Widget: ...
def prop_file_chooser_button_new_with_dialog(config: GObject.Object, property_name: str, dialog: Gtk.Widget) -> Gtk.Widget: ...
def prop_file_chooser_new(config: GObject.Object, property_name: str, label: typing.Optional[str] = None, title: typing.Optional[str] = None) -> Gtk.Widget: ...
def prop_font_chooser_new(config: GObject.Object, property_name: str, chooser_title: typing.Optional[str] = None) -> Gtk.Widget: ...
def prop_gradient_chooser_new(config: GObject.Object, property_name: str, chooser_title: typing.Optional[str] = None) -> Gtk.Widget: ...
def prop_hscale_new(config: GObject.Object, property_name: str, step_increment: float, page_increment: float, digits: int) -> Gtk.Widget: ...
def prop_icon_image_new(config: GObject.Object, property_name: str, icon_size: Gtk.IconSize) -> Gtk.Widget: ...
def prop_int_combo_box_new(config: GObject.Object, property_name: str, store: IntStore) -> Gtk.Widget: ...
def prop_int_radio_frame_new(config: GObject.Object, property_name: str, title: typing.Optional[str], store: IntStore) -> Gtk.Widget: ...
def prop_label_color_new(config: GObject.Object, property_name: str, editable: bool) -> Gtk.Widget: ...
def prop_label_entry_new(config: GObject.Object, property_name: str, max_len: int) -> Gtk.Widget: ...
def prop_label_new(config: GObject.Object, property_name: str) -> Gtk.Widget: ...
def prop_label_spin_new(config: GObject.Object, property_name: str, digits: int) -> Gtk.Widget: ...
def prop_memsize_entry_new(config: GObject.Object, property_name: str) -> Gtk.Widget: ...
def prop_palette_chooser_new(config: GObject.Object, property_name: str, chooser_title: typing.Optional[str] = None) -> Gtk.Widget: ...
def prop_path_editor_new(config: GObject.Object, path_property_name: str, writable_property_name: str, filechooser_title: str) -> Gtk.Widget: ...
def prop_pattern_chooser_new(config: GObject.Object, property_name: str, chooser_title: typing.Optional[str] = None) -> Gtk.Widget: ...
def prop_pointer_combo_box_new(config: GObject.Object, property_name: str, store: IntStore) -> Gtk.Widget: ...
def prop_scale_entry_new(config: GObject.Object, property_name: str, label: typing.Optional[str], factor: float, limit_scale: bool, lower_limit: float, upper_limit: float) -> Gtk.Widget: ...
def prop_size_entry_new(config: GObject.Object, property_name: str, property_is_pixel: bool, unit_property_name: str, unit_format: str, update_policy: SizeEntryUpdatePolicy, resolution: float) -> Gtk.Widget: ...
def prop_spin_button_new(config: GObject.Object, property_name: str, step_increment: float, page_increment: float, digits: int) -> Gtk.Widget: ...
def prop_spin_scale_new(config: GObject.Object, property_name: str, step_increment: float, page_increment: float, digits: int) -> Gtk.Widget: ...
def prop_string_combo_box_new(config: GObject.Object, property_name: str, model: Gtk.TreeModel, id_column: int, label_column: int) -> Gtk.Widget: ...
def prop_switch_new(config: GObject.Object, property_name: str, label: str) -> typing.Tuple[Gtk.Widget, Gtk.Widget, Gtk.Widget]: ...
def prop_text_buffer_new(config: GObject.Object, property_name: str, max_len: int) -> Gtk.TextBuffer: ...
def prop_unit_combo_box_new(config: GObject.Object, property_name: str) -> Gtk.Widget: ...
def prop_widget_set_factor(widget: Gtk.Widget, factor: float, step_increment: float, page_increment: float, digits: int) -> None: ...
def query_boolean_box(title: str, parent: Gtk.Widget, help_func: typing.Callable[[str, None], None], help_id: str, icon_name: str, message: str, true_button: str, false_button: str, object: GObject.Object, signal: str, callback: typing.Callable[..., None], *data: typing.Any) -> Gtk.Widget: ...
def query_double_box(title: str, parent: Gtk.Widget, help_func: typing.Callable[[str, None], None], help_id: str, message: str, initial: float, lower: float, upper: float, digits: int, object: GObject.Object, signal: str, callback: typing.Callable[..., None], *data: typing.Any) -> Gtk.Widget: ...
def query_int_box(title: str, parent: Gtk.Widget, help_func: typing.Callable[[str, None], None], help_id: str, message: str, initial: int, lower: int, upper: int, object: GObject.Object, signal: str, callback: typing.Callable[..., None], *data: typing.Any) -> Gtk.Widget: ...
def query_size_box(title: str, parent: Gtk.Widget, help_func: typing.Callable[[str, None], None], help_id: str, message: str, initial: float, lower: float, upper: float, digits: int, unit: Gimp.Unit, resolution: float, dot_for_dot: bool, object: GObject.Object, signal: str, callback: typing.Callable[..., None], *data: typing.Any) -> Gtk.Widget: ...
def query_string_box(title: str, parent: Gtk.Widget, help_func: typing.Callable[[str, None], None], help_id: str, message: str, initial: str, object: GObject.Object, signal: str, callback: typing.Callable[..., None], *data: typing.Any) -> Gtk.Widget: ...
def radio_button_update(widget: Gtk.Widget) -> int: ...
def random_seed_new(seed: int, random_seed: bool) -> Gtk.Widget: ...
def scroll_adjustment_values(sevent: Gdk.EventScroll, hadj: typing.Optional[Gtk.Adjustment] = None, vadj: typing.Optional[Gtk.Adjustment] = None) -> typing.Tuple[float, float]: ...
def standard_help_func(help_id: str, help_data: None) -> None: ...
def toggle_button_update(widget: Gtk.Widget) -> bool: ...
def uint_adjustment_update(adjustment: Gtk.Adjustment) -> int: ...
def widget_animation_enabled() -> bool: ...
def widget_free_native_handle(widget: Gtk.Widget) -> GLib.Bytes: ...
def widget_get_color_profile(widget: Gtk.Widget) -> typing.Optional[Gimp.ColorProfile]: ...
def widget_get_color_transform(widget: Gtk.Widget, config: Gimp.ColorConfig, src_profile: Gimp.ColorProfile, src_format: Babl.Object, dest_format: Babl.Object, softproof_profile: Gimp.ColorProfile, proof_intent: Gimp.ColorRenderingIntent, proof_bpc: bool) -> typing.Optional[Gimp.ColorTransform]: ...
def widget_get_monitor(widget: Gtk.Widget) -> Gdk.Monitor: ...
def widget_get_render_space(widget: Gtk.Widget, config: Gimp.ColorConfig) -> Babl.Object: ...
def widget_set_native_handle(widget: Gtk.Widget) -> GLib.Bytes: ...
def widget_track_monitor(widget: Gtk.Widget, monitor_changed_callback: typing.Callable[..., None], *user_data: typing.Any) -> None: ...
def widgets_error_quark() -> int: ...
def window_set_transient(window: Gtk.Window) -> None: ...
def window_set_transient_for(window: Gtk.Window, handle: GLib.Bytes) -> None: ...
def window_set_transient_for_display(window: Gtk.Window, display: Gimp.Display) -> None: ...
def zoom_button_new(model: ZoomModel, zoom_type: ZoomType, icon_size: Gtk.IconSize) -> Gtk.Widget: ...

class AspectPreview(Preview, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        AspectPreview(**properties)
        new_from_drawable(drawable:Gimp.Drawable) -> Gtk.Widget

    Object GimpAspectPreview

    Properties from GimpAspectPreview:
      drawable -> GimpDrawable: Drawable
        The drawable this preview is attached to

    Signals from GimpPreview:
      invalidated ()

    Properties from GimpPreview:
      update -> gboolean: Update
        Whether the preview should update automatically

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        drawable: Gimp.Drawable
        update: bool
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, drawable: Gimp.Drawable = ...,
                 update: bool = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    @classmethod
    def new_from_drawable(cls, drawable: Gimp.Drawable) -> AspectPreview: ...
    

class AspectPreviewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AspectPreviewClass()
    """
    parent_class: PreviewClass = ...

class Browser(Gtk.Paned, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        Browser(**properties)
        new() -> Gtk.Widget

    Object GimpBrowser

    Signals from GimpBrowser:
      search (gchararray, gint)

    Signals from GtkPaned:
      cycle-child-focus (gboolean) -> gboolean
      toggle-handle-focus () -> gboolean
      move-handle (GtkScrollType) -> gboolean
      cycle-handle-focus (gboolean) -> gboolean
      accept-position () -> gboolean
      cancel-position () -> gboolean

    Properties from GtkPaned:
      position -> gint: Position
        Position of paned separator in pixels (0 means all the way to the left/top)
      position-set -> gboolean: Position Set
        TRUE if the Position property should be used
      min-position -> gint: Minimal Position
        Smallest possible value for the "position" property
      max-position -> gint: Maximal Position
        Largest possible value for the "position" property
      wide-handle -> gboolean: Wide Handle
        Whether the paned should have a prominent handle

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        max_position: int
        min_position: int
        position: int
        position_set: bool
        wide_handle: bool
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, position: int = ...,
                 position_set: bool = ...,
                 wide_handle: bool = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_left_vbox(self) -> Gtk.Box: ...
    def get_right_vbox(self) -> Gtk.Box: ...
    @classmethod
    def new(cls) -> Browser: ...
    def set_search_summary(self, summary: str) -> None: ...
    def set_widget(self, widget: Gtk.Widget) -> None: ...
    def show_message(self, message: str) -> None: ...
    

class BrowserClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BrowserClass()
    """
    parent_class: Gtk.PanedClass = ...

class BrushChooser(ResourceChooser, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        BrushChooser(**properties)
        new(title:str=None, label:str=None, brush:Gimp.Brush=None) -> Gtk.Widget

    Object GimpBrushChooser

    Signals from GimpResourceChooser:
      resource-set (GObject, gboolean)

    Properties from GimpResourceChooser:
      title -> gchararray: Title
        The title to be used for the resource selection popup dialog
      label -> gchararray: Label
        The label to be used next to the button
      resource -> GimpResource: Resource
        The currently selected resource

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        label: str
        resource: Gimp.Resource
        title: str
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, label: str = ...,
                 resource: Gimp.Resource = ...,
                 title: str = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    @classmethod
    def new(cls, title: typing.Optional[str] = None, label: typing.Optional[str] = None, brush: typing.Optional[Gimp.Brush] = None) -> BrushChooser: ...
    

class BrushChooserClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BrushChooserClass()
    """
    parent_class: ResourceChooserClass = ...

class BusyBox(Gtk.Box, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        BusyBox(**properties)
        new(message:str=None) -> Gtk.Widget

    Object GimpBusyBox

    Properties from GimpBusyBox:
      message -> gchararray: Message
        The message to display

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        message: str
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, message: str = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_message(self) -> str: ...
    @classmethod
    def new(cls, message: typing.Optional[str] = None) -> BusyBox: ...
    def set_message(self, message: str) -> None: ...
    

class BusyBoxClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BusyBoxClass()
    """
    parent_class: Gtk.BoxClass = ...

class Button(Gtk.Button, Atk.ImplementorIface, Gtk.Actionable, Gtk.Activatable, Gtk.Buildable):
    """
    :Constructors:

    ::

        Button(**properties)
        new() -> Gtk.Widget

    Object GimpButton

    Signals from GimpButton:
      extended-clicked (GdkModifierType)

    Signals from GtkButton:
      activate ()
      pressed ()
      released ()
      clicked ()
      enter ()
      leave ()

    Properties from GtkButton:
      label -> gchararray: Label
        Text of the label widget inside the button, if the button contains a label widget
      image -> GtkWidget: Image widget
        Child widget to appear next to the button text
      relief -> GtkReliefStyle: Border relief
        The border relief style
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key
      use-stock -> gboolean: Use stock
        If set, the label is used to pick a stock item instead of being displayed
      xalign -> gfloat: Horizontal alignment for child
        Horizontal position of child in available space. 0.0 is left aligned, 1.0 is right aligned
      yalign -> gfloat: Vertical alignment for child
        Vertical position of child in available space. 0.0 is top aligned, 1.0 is bottom aligned
      image-position -> GtkPositionType: Image position
        The position of the image relative to the text
      always-show-image -> gboolean: Always show image
        Whether the image will always be shown

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        always_show_image: bool
        image: typing.Optional[Gtk.Widget]
        image_position: Gtk.PositionType
        label: str
        relief: Gtk.ReliefStyle
        use_stock: bool
        use_underline: bool
        xalign: float
        yalign: float
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        action_name: typing.Optional[str]
        action_target: GLib.Variant
        related_action: Gtk.Action
        use_action_appearance: bool
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Button = ...
    def __init__(self, always_show_image: bool = ...,
                 image: typing.Optional[Gtk.Widget] = ...,
                 image_position: Gtk.PositionType = ...,
                 label: str = ...,
                 relief: Gtk.ReliefStyle = ...,
                 use_stock: bool = ...,
                 use_underline: bool = ...,
                 xalign: float = ...,
                 yalign: float = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 action_name: typing.Optional[str] = ...,
                 action_target: GLib.Variant = ...,
                 related_action: Gtk.Action = ...,
                 use_action_appearance: bool = ...) -> None: ...
    def do_extended_clicked(self, modifier_state: Gdk.ModifierType) -> None: ...
    def extended_clicked(self, modifier_state: Gdk.ModifierType) -> None: ...
    @classmethod
    def new(cls) -> Button: ...
    

class ButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ButtonClass()
    """
    parent_class: Gtk.ButtonClass = ...
    extended_clicked: typing.Callable[[Button, Gdk.ModifierType], None] = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class CellRendererColor(Gtk.CellRenderer):
    """
    :Constructors:

    ::

        CellRendererColor(**properties)
        new() -> Gtk.CellRenderer

    Object GimpCellRendererColor

    Properties from GimpCellRendererColor:
      color -> GeglColor: Color
        The displayed color
      opaque -> gboolean: Opaque
        Whether to show transparency
      icon-size -> gint: Icon Size
        The cell's size

    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)

    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
        Editable mode of the CellRenderer
      visible -> gboolean: visible
        Display the cell
      sensitive -> gboolean: Sensitive
        Display the cell sensitive
      xalign -> gfloat: xalign
        The x-align
      yalign -> gfloat: yalign
        The y-align
      xpad -> guint: xpad
        The xpad
      ypad -> guint: ypad
        The ypad
      width -> gint: width
        The fixed width
      height -> gint: height
        The fixed height
      is-expander -> gboolean: Is Expander
        Row has children
      is-expanded -> gboolean: Is Expanded
        Row is an expander row, and is expanded
      cell-background -> gchararray: Cell background color name
        Cell background color as a string
      cell-background-gdk -> GdkColor: Cell background color
        Cell background color as a GdkColor
      cell-background-rgba -> GdkRGBA: Cell background RGBA color
        Cell background color as a GdkRGBA
      cell-background-set -> gboolean: Cell background set
        Whether the cell background color is set
      editing -> gboolean: Editing
        Whether the cell renderer is currently in editing mode

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        color: Gegl.Color
        icon_size: int
        opaque: bool
        cell_background_gdk: Gdk.Color
        cell_background_rgba: Gdk.RGBA
        cell_background_set: bool
        editing: bool
        height: int
        is_expanded: bool
        is_expander: bool
        mode: Gtk.CellRendererMode
        sensitive: bool
        visible: bool
        width: int
        xalign: float
        xpad: int
        yalign: float
        ypad: int
        cell_background: str
    props: Props = ...
    def __init__(self, color: Gegl.Color = ...,
                 icon_size: int = ...,
                 opaque: bool = ...,
                 cell_background: str = ...,
                 cell_background_gdk: Gdk.Color = ...,
                 cell_background_rgba: Gdk.RGBA = ...,
                 cell_background_set: bool = ...,
                 height: int = ...,
                 is_expanded: bool = ...,
                 is_expander: bool = ...,
                 mode: Gtk.CellRendererMode = ...,
                 sensitive: bool = ...,
                 visible: bool = ...,
                 width: int = ...,
                 xalign: float = ...,
                 xpad: int = ...,
                 yalign: float = ...,
                 ypad: int = ...) -> None: ...
    @classmethod
    def new(cls) -> CellRendererColor: ...
    

class CellRendererColorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CellRendererColorClass()
    """
    parent_class: Gtk.CellRendererClass = ...

class CellRendererToggle(Gtk.CellRendererToggle):
    """
    :Constructors:

    ::

        CellRendererToggle(**properties)
        new(icon_name:str) -> Gtk.CellRenderer

    Object GimpCellRendererToggle

    Signals from GimpCellRendererToggle:
      clicked (gchararray, GdkModifierType)

    Properties from GimpCellRendererToggle:
      icon-name -> gchararray: Icon Name
        The icon to display
      icon-size -> gint: Icon Size
        The desired icon size to use in pixel (before applying scaling factor)
      override-background -> gboolean: Override Background
        Draw the background if the row is selected

    Signals from GtkCellRendererToggle:
      toggled (gchararray)

    Properties from GtkCellRendererToggle:
      activatable -> gboolean: Activatable
        The toggle button can be activated
      active -> gboolean: Toggle state
        The toggle state of the button
      radio -> gboolean: Radio state
        Draw the toggle button as a radio button
      inconsistent -> gboolean: Inconsistent state
        The inconsistent state of the button
      indicator-size -> gint: Indicator size
        Size of check or radio indicator

    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)

    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
        Editable mode of the CellRenderer
      visible -> gboolean: visible
        Display the cell
      sensitive -> gboolean: Sensitive
        Display the cell sensitive
      xalign -> gfloat: xalign
        The x-align
      yalign -> gfloat: yalign
        The y-align
      xpad -> guint: xpad
        The xpad
      ypad -> guint: ypad
        The ypad
      width -> gint: width
        The fixed width
      height -> gint: height
        The fixed height
      is-expander -> gboolean: Is Expander
        Row has children
      is-expanded -> gboolean: Is Expanded
        Row is an expander row, and is expanded
      cell-background -> gchararray: Cell background color name
        Cell background color as a string
      cell-background-gdk -> GdkColor: Cell background color
        Cell background color as a GdkColor
      cell-background-rgba -> GdkRGBA: Cell background RGBA color
        Cell background color as a GdkRGBA
      cell-background-set -> gboolean: Cell background set
        Whether the cell background color is set
      editing -> gboolean: Editing
        Whether the cell renderer is currently in editing mode

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        icon_name: str
        icon_size: int
        override_background: bool
        activatable: bool
        active: bool
        inconsistent: bool
        indicator_size: int
        radio: bool
        cell_background_gdk: Gdk.Color
        cell_background_rgba: Gdk.RGBA
        cell_background_set: bool
        editing: bool
        height: int
        is_expanded: bool
        is_expander: bool
        mode: Gtk.CellRendererMode
        sensitive: bool
        visible: bool
        width: int
        xalign: float
        xpad: int
        yalign: float
        ypad: int
        cell_background: str
    props: Props = ...
    def __init__(self, icon_name: str = ...,
                 icon_size: int = ...,
                 override_background: bool = ...,
                 activatable: bool = ...,
                 active: bool = ...,
                 inconsistent: bool = ...,
                 indicator_size: int = ...,
                 radio: bool = ...,
                 cell_background: str = ...,
                 cell_background_gdk: Gdk.Color = ...,
                 cell_background_rgba: Gdk.RGBA = ...,
                 cell_background_set: bool = ...,
                 height: int = ...,
                 is_expanded: bool = ...,
                 is_expander: bool = ...,
                 mode: Gtk.CellRendererMode = ...,
                 sensitive: bool = ...,
                 visible: bool = ...,
                 width: int = ...,
                 xalign: float = ...,
                 xpad: int = ...,
                 yalign: float = ...,
                 ypad: int = ...) -> None: ...
    def clicked(self, path: str, state: Gdk.ModifierType) -> None: ...
    @classmethod
    def new(cls, icon_name: str) -> CellRendererToggle: ...
    

class CellRendererToggleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CellRendererToggleClass()
    """
    parent_class: Gtk.CellRendererToggleClass = ...

class ChainButton(Gtk.Grid, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        ChainButton(**properties)
        new(position:GimpUi.ChainPosition) -> Gtk.Widget

    Object GimpChainButton

    Signals from GimpChainButton:
      toggled ()

    Properties from GimpChainButton:
      position -> GimpChainPosition: Position
        The chain's position
      icon-size -> GtkIconSize: Icon Size
        The chain's icon size
      active -> gboolean: Active
        The chain's toggled state

    Properties from GtkGrid:
      row-spacing -> gint: Row spacing
        The amount of space between two consecutive rows
      column-spacing -> gint: Column spacing
        The amount of space between two consecutive columns
      row-homogeneous -> gboolean: Row Homogeneous
        If TRUE, the rows are all the same height
      column-homogeneous -> gboolean: Column Homogeneous
        If TRUE, the columns are all the same width
      baseline-row -> gint: Baseline Row
        The row to align the to the baseline when valign is GTK_ALIGN_BASELINE

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        active: bool
        icon_size: Gtk.IconSize
        position: ChainPosition
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, active: bool = ...,
                 icon_size: Gtk.IconSize = ...,
                 position: ChainPosition = ...,
                 baseline_row: int = ...,
                 column_homogeneous: bool = ...,
                 column_spacing: int = ...,
                 row_homogeneous: bool = ...,
                 row_spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_active(self) -> bool: ...
    def get_button(self) -> Gtk.Button: ...
    def get_icon_size(self) -> Gtk.IconSize: ...
    @classmethod
    def new(cls, position: ChainPosition) -> ChainButton: ...
    def set_active(self, active: bool) -> None: ...
    def set_icon_size(self, size: Gtk.IconSize) -> None: ...
    

class ChainButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ChainButtonClass()
    """
    parent_class: Gtk.GridClass = ...

class ChannelComboBox(IntComboBox, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.CellLayout):
    """
    :Constructors:

    ::

        ChannelComboBox(**properties)
        new(constraint:GimpUi.ItemConstraintFunc=None) -> Gtk.Widget

    Object GimpChannelComboBox

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Properties from GimpIntComboBox:
      ellipsize -> PangoEllipsizeMode: Ellipsize
        Ellipsize mode for the used text cell renderer
      label -> gchararray: Label
        An optional label to be displayed
      layout -> GimpIntComboBoxLayout: Layout
        Combo box layout
      value -> gint: Value
        Value of active item

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkComboBox:
      changed ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray

    Properties from GtkComboBox:
      model -> GtkTreeModel: ComboBox model
        The model for the combo box
      wrap-width -> gint: Wrap width
        Wrap width for laying out the items in a grid
      row-span-column -> gint: Row span column
        TreeModel column containing the row span values
      column-span-column -> gint: Column span column
        TreeModel column containing the column span values
      active -> gint: Active item
        The item which is currently active
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether dropdowns should have a tearoff menu item
      tearoff-title -> gchararray: Tearoff Title
        A title that may be displayed by the window manager when the popup is torn-off
      has-frame -> gboolean: Has Frame
        Whether the combo box draws a frame around the child
      popup-shown -> gboolean: Popup shown
        Whether the combo's dropdown is shown
      button-sensitivity -> GtkSensitivityType: Button Sensitivity
        Whether the dropdown button is sensitive when the model is empty
      has-entry -> gboolean: Has Entry
        Whether combo box has an entry
      entry-text-column -> gint: Entry Text Column
        The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE
      popup-fixed-width -> gboolean: Popup Fixed Width
        Whether the popup's width should be a fixed width matching the allocated width of the combo box
      id-column -> gint: ID Column
        The column in the combo box's model that provides string IDs for the values in the model
      active-id -> gchararray: Active id
        The value of the id column for the active row
      cell-area -> GtkCellArea: Cell Area
        The GtkCellArea used to layout cells

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        ellipsize: Pango.EllipsizeMode
        label: str
        layout: IntComboBoxLayout
        value: int
        active: int
        active_id: typing.Optional[str]
        add_tearoffs: bool
        button_sensitivity: Gtk.SensitivityType
        cell_area: Gtk.CellArea
        column_span_column: int
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        id_column: int
        model: Gtk.TreeModel
        popup_fixed_width: bool
        popup_shown: bool
        row_span_column: int
        tearoff_title: str
        wrap_width: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, ellipsize: Pango.EllipsizeMode = ...,
                 label: str = ...,
                 layout: IntComboBoxLayout = ...,
                 value: int = ...,
                 active: int = ...,
                 active_id: typing.Optional[str] = ...,
                 add_tearoffs: bool = ...,
                 button_sensitivity: Gtk.SensitivityType = ...,
                 cell_area: Gtk.CellArea = ...,
                 column_span_column: int = ...,
                 entry_text_column: int = ...,
                 has_entry: bool = ...,
                 has_frame: bool = ...,
                 id_column: int = ...,
                 model: typing.Optional[Gtk.TreeModel] = ...,
                 popup_fixed_width: bool = ...,
                 row_span_column: int = ...,
                 tearoff_title: str = ...,
                 wrap_width: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    @classmethod
    def new(cls, constraint: typing.Optional[typing.Callable[..., bool]] = None, *data: typing.Any) -> ChannelComboBox: ...
    

class ColorArea(Gtk.DrawingArea, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        ColorArea(**properties)
        new(color:Gegl.Color, type:GimpUi.ColorAreaType, drag_mask:Gdk.ModifierType) -> Gtk.Widget

    Object GimpColorArea

    Signals from GimpColorArea:
      color-changed ()

    Properties from GimpColorArea:
      color -> GeglColor: Color
        The displayed color
      type -> GimpColorAreaType: Type
        The type of the color area
      drag-mask -> GdkModifierType: Drag Mask
        The modifier mask that triggers dragging the color
      draw-border -> gboolean: Draw Border
        Whether to draw a thin border in the foreground color around the area

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        color: Gegl.Color
        draw_border: bool
        type: ColorAreaType
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        drag_mask: Gdk.ModifierType
    props: Props = ...
    def __init__(self, color: Gegl.Color = ...,
                 drag_mask: Gdk.ModifierType = ...,
                 draw_border: bool = ...,
                 type: ColorAreaType = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    def enable_drag(self, drag_mask: Gdk.ModifierType) -> None: ...
    def get_color(self) -> Gegl.Color: ...
    def has_alpha(self) -> bool: ...
    @classmethod
    def new(cls, color: Gegl.Color, type: ColorAreaType, drag_mask: Gdk.ModifierType) -> ColorArea: ...
    def set_color(self, color: Gegl.Color) -> None: ...
    def set_color_config(self, config: Gimp.ColorConfig) -> None: ...
    def set_draw_border(self, draw_border: bool) -> None: ...
    def set_out_of_gamut(self, out_of_gamut: bool) -> None: ...
    def set_type(self, type: ColorAreaType) -> None: ...
    

class ColorAreaClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorAreaClass()
    """
    parent_class: Gtk.DrawingAreaClass = ...

class ColorButton(Button, Atk.ImplementorIface, Gtk.Actionable, Gtk.Activatable, Gtk.Buildable):
    """
    :Constructors:

    ::

        ColorButton(**properties)
        new(title:str, width:int, height:int, color:Gegl.Color, type:GimpUi.ColorAreaType) -> Gtk.Widget

    Object GimpColorButton

    Signals from GimpColorButton:
      color-changed ()

    Properties from GimpColorButton:
      title -> gchararray: Title
        The title to be used for the color selection dialog
      color -> GeglColor: Color
        The color displayed in the button's color area
      type -> GimpColorAreaType: Type
        The type of the button's color area
      continuous-update -> gboolean: Contiguous Update
        The update policy of the color button
      area-width -> gint: Area Width
        The minimum width of the button's GimpColorArea
      area-height -> gint: Area Height
        The minimum height of the button's GimpColorArea
      color-config -> GimpColorConfig: Color Config
        The color config object used

    Signals from GimpButton:
      extended-clicked (GdkModifierType)

    Signals from GtkButton:
      activate ()
      pressed ()
      released ()
      clicked ()
      enter ()
      leave ()

    Properties from GtkButton:
      label -> gchararray: Label
        Text of the label widget inside the button, if the button contains a label widget
      image -> GtkWidget: Image widget
        Child widget to appear next to the button text
      relief -> GtkReliefStyle: Border relief
        The border relief style
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key
      use-stock -> gboolean: Use stock
        If set, the label is used to pick a stock item instead of being displayed
      xalign -> gfloat: Horizontal alignment for child
        Horizontal position of child in available space. 0.0 is left aligned, 1.0 is right aligned
      yalign -> gfloat: Vertical alignment for child
        Vertical position of child in available space. 0.0 is top aligned, 1.0 is bottom aligned
      image-position -> GtkPositionType: Image position
        The position of the image relative to the text
      always-show-image -> gboolean: Always show image
        Whether the image will always be shown

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        color: Gegl.Color
        color_config: Gimp.ColorConfig
        continuous_update: bool
        title: str
        type: ColorAreaType
        always_show_image: bool
        image: typing.Optional[Gtk.Widget]
        image_position: Gtk.PositionType
        label: str
        relief: Gtk.ReliefStyle
        use_stock: bool
        use_underline: bool
        xalign: float
        yalign: float
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        action_name: typing.Optional[str]
        action_target: GLib.Variant
        related_action: Gtk.Action
        use_action_appearance: bool
        area_height: int
        area_width: int
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Button = ...
    def __init__(self, area_height: int = ...,
                 area_width: int = ...,
                 color: Gegl.Color = ...,
                 color_config: Gimp.ColorConfig = ...,
                 continuous_update: bool = ...,
                 title: str = ...,
                 type: ColorAreaType = ...,
                 always_show_image: bool = ...,
                 image: typing.Optional[Gtk.Widget] = ...,
                 image_position: Gtk.PositionType = ...,
                 label: str = ...,
                 relief: Gtk.ReliefStyle = ...,
                 use_stock: bool = ...,
                 use_underline: bool = ...,
                 xalign: float = ...,
                 yalign: float = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 action_name: typing.Optional[str] = ...,
                 action_target: GLib.Variant = ...,
                 related_action: Gtk.Action = ...,
                 use_action_appearance: bool = ...) -> None: ...
    def do_color_changed(self) -> None: ...
    def do_get_action_type(self) -> typing.Type[typing.Any]: ...
    def get_action_group(self) -> Gio.SimpleActionGroup: ...
    def get_color(self) -> Gegl.Color: ...
    def get_title(self) -> str: ...
    def get_update(self) -> bool: ...
    def has_alpha(self) -> bool: ...
    @classmethod
    def new(cls, title: str, width: int, height: int, color: Gegl.Color, type: ColorAreaType) -> ColorButton: ...
    def set_color(self, color: Gegl.Color) -> None: ...
    def set_color_config(self, config: Gimp.ColorConfig) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_type(self, type: ColorAreaType) -> None: ...
    def set_update(self, continuous: bool) -> None: ...
    

class ColorButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorButtonClass()
    """
    parent_class: ButtonClass = ...
    color_changed: typing.Callable[[ColorButton], None] = ...
    get_action_type: typing.Callable[[ColorButton], typing.Type[typing.Any]] = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class ColorDisplay(GObject.Object, Gimp.ConfigInterface):
    """
    :Constructors:

    ::

        ColorDisplay(**properties)

    Object GimpColorDisplay

    Signals from GimpColorDisplay:
      changed ()

    Properties from GimpColorDisplay:
      enabled -> gboolean: Enabled
        Whether this display filter is enabled
      color-config -> GimpColorConfig: Color Config
        The color config used for this filter
      color-managed -> GimpColorManaged: Color Managed
        The color managed pixel source that is filtered

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        color_config: Gimp.ColorConfig
        color_managed: Gimp.ColorManaged
        enabled: bool
    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, color_config: Gimp.ColorConfig = ...,
                 color_managed: Gimp.ColorManaged = ...,
                 enabled: bool = ...) -> None: ...
    def changed(self) -> None: ...
    def clone(self) -> ColorDisplay: ...
    def configure(self) -> Gtk.Widget: ...
    def configure_reset(self) -> None: ...
    def convert_buffer(self, buffer: Gegl.Buffer, area: Gegl.Rectangle) -> None: ...
    def do_changed(self) -> None: ...
    def do_configure(self) -> Gtk.Widget: ...
    def do_convert_buffer(self, buffer: Gegl.Buffer, area: Gegl.Rectangle) -> None: ...
    def get_config(self) -> Gimp.ColorConfig: ...
    def get_enabled(self) -> bool: ...
    def get_managed(self) -> Gimp.ColorManaged: ...
    def load_state(self, state: Gimp.Parasite) -> None: ...
    def save_state(self) -> Gimp.Parasite: ...
    def set_enabled(self, enabled: bool) -> None: ...
    

class ColorDisplayClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorDisplayClass()
    """
    parent_class: GObject.ObjectClass = ...
    name: str = ...
    help_id: str = ...
    icon_name: str = ...
    convert_buffer: typing.Callable[[ColorDisplay, Gegl.Buffer, Gegl.Rectangle], None] = ...
    configure: typing.Callable[[ColorDisplay], Gtk.Widget] = ...
    changed: typing.Callable[[ColorDisplay], None] = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class ColorDisplayStack(GObject.Object):
    """
    :Constructors:

    ::

        ColorDisplayStack(**properties)
        new() -> GimpUi.ColorDisplayStack

    Object GimpColorDisplayStack

    Signals from GimpColorDisplayStack:
      changed ()
      added (GimpColorDisplay, gint)
      removed (GimpColorDisplay)
      reordered (GimpColorDisplay, gint)

    Signals from GObject:
      notify (GParam)
    """
    def add(self, display: ColorDisplay) -> None: ...
    def changed(self) -> None: ...
    def clone(self) -> ColorDisplayStack: ...
    def convert_buffer(self, buffer: Gegl.Buffer, area: Gegl.Rectangle) -> None: ...
    def get_filters(self) -> list[ColorDisplay]: ...
    @classmethod
    def new(cls) -> ColorDisplayStack: ...
    def remove(self, display: ColorDisplay) -> None: ...
    def reorder_down(self, display: ColorDisplay) -> None: ...
    def reorder_up(self, display: ColorDisplay) -> None: ...
    

class ColorDisplayStackClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorDisplayStackClass()
    """
    parent_class: GObject.ObjectClass = ...

class ColorHexEntry(Gtk.Entry, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.Editable):
    """
    :Constructors:

    ::

        ColorHexEntry(**properties)
        new() -> Gtk.Widget

    Object GimpColorHexEntry

    Signals from GimpColorHexEntry:
      color-changed ()

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkEntry:
      activate ()
      populate-popup (GtkWidget)
      move-cursor (GtkMovementStep, gint, gboolean)
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      icon-press (GtkEntryIconPosition, GdkEvent)
      icon-release (GtkEntryIconPosition, GdkEvent)
      preedit-changed (gchararray)
      insert-emoji ()

    Properties from GtkEntry:
      buffer -> GtkEntryBuffer: Text Buffer
        Text buffer object which actually stores entry text
      cursor-position -> gint: Cursor Position
        The current position of the insertion cursor in chars
      selection-bound -> gint: Selection Bound
        The position of the opposite end of the selection from the cursor in chars
      editable -> gboolean: Editable
        Whether the entry contents can be edited
      max-length -> gint: Maximum length
        Maximum number of characters for this entry. Zero if no maximum
      visibility -> gboolean: Visibility
        FALSE displays the "invisible char" instead of the actual text (password mode)
      has-frame -> gboolean: Has Frame
        FALSE removes outside bevel from entry
      inner-border -> GtkBorder: Inner Border
        Border between text and frame. Overrides the inner-border style property
      invisible-char -> guint: Invisible character
        The character to use when masking entry contents (in "password mode")
      activates-default -> gboolean: Activates default
        Whether to activate the default widget (such as the default button in a dialog) when Enter is pressed
      width-chars -> gint: Width in chars
        Number of characters to leave space for in the entry
      max-width-chars -> gint: Maximum width in characters
        The desired maximum width of the entry, in characters
      scroll-offset -> gint: Scroll offset
        Number of pixels of the entry scrolled off the screen to the left
      text -> gchararray: Text
        The contents of the entry
      xalign -> gfloat: X align
        The horizontal alignment, from 0 (left) to 1 (right). Reversed for RTL layouts.
      truncate-multiline -> gboolean: Truncate multiline
        Whether to truncate multiline pastes to one line.
      shadow-type -> GtkShadowType: Shadow type
        Which kind of shadow to draw around the entry when has-frame is set
      overwrite-mode -> gboolean: Overwrite mode
        Whether new text overwrites existing text
      text-length -> guint: Text length
        Length of the text currently in the entry
      invisible-char-set -> gboolean: Invisible character set
        Whether the invisible character has been set
      caps-lock-warning -> gboolean: Caps Lock warning
        Whether password entries will show a warning when Caps Lock is on
      progress-fraction -> gdouble: Progress Fraction
        The current fraction of the task that's been completed
      progress-pulse-step -> gdouble: Progress Pulse Step
        The fraction of total entry width to move the progress bouncing block for each call to gtk_entry_progress_pulse()
      primary-icon-pixbuf -> GdkPixbuf: Primary pixbuf
        Primary pixbuf for the entry
      secondary-icon-pixbuf -> GdkPixbuf: Secondary pixbuf
        Secondary pixbuf for the entry
      primary-icon-stock -> gchararray: Primary stock ID
        Stock ID for primary icon
      secondary-icon-stock -> gchararray: Secondary stock ID
        Stock ID for secondary icon
      primary-icon-name -> gchararray: Primary icon name
        Icon name for primary icon
      secondary-icon-name -> gchararray: Secondary icon name
        Icon name for secondary icon
      primary-icon-gicon -> GIcon: Primary GIcon
        GIcon for primary icon
      secondary-icon-gicon -> GIcon: Secondary GIcon
        GIcon for secondary icon
      primary-icon-storage-type -> GtkImageType: Primary storage type
        The representation being used for primary icon
      secondary-icon-storage-type -> GtkImageType: Secondary storage type
        The representation being used for secondary icon
      primary-icon-activatable -> gboolean: Primary icon activatable
        Whether the primary icon is activatable
      secondary-icon-activatable -> gboolean: Secondary icon activatable
        Whether the secondary icon is activatable
      primary-icon-sensitive -> gboolean: Primary icon sensitive
        Whether the primary icon is sensitive
      secondary-icon-sensitive -> gboolean: Secondary icon sensitive
        Whether the secondary icon is sensitive
      primary-icon-tooltip-text -> gchararray: Primary icon tooltip text
        The contents of the tooltip on the primary icon
      secondary-icon-tooltip-text -> gchararray: Secondary icon tooltip text
        The contents of the tooltip on the secondary icon
      primary-icon-tooltip-markup -> gchararray: Primary icon tooltip markup
        The contents of the tooltip on the primary icon
      secondary-icon-tooltip-markup -> gchararray: Secondary icon tooltip markup
        The contents of the tooltip on the secondary icon
      im-module -> gchararray: IM module
        Which IM module should be used
      placeholder-text -> gchararray: Placeholder text
        Show text in the entry when it's empty and unfocused
      completion -> GtkEntryCompletion: Completion
        The auxiliary completion object
      input-purpose -> GtkInputPurpose: Purpose
        Purpose of the text field
      input-hints -> GtkInputHints: hints
        Hints for the text field behaviour
      attributes -> PangoAttrList: Attributes
        A list of style attributes to apply to the text of the label
      populate-all -> gboolean: Populate all
        Whether to emit ::populate-popup for touch popups
      tabs -> PangoTabArray: Tabs
        A list of tabstop locations to apply to the text of the entry
      show-emoji-icon -> gboolean: Emoji icon
        Whether to show an icon for Emoji
      enable-emoji-completion -> gboolean: Enable Emoji completion
        Whether to suggest Emoji replacements

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        activates_default: bool
        attributes: typing.Optional[Pango.AttrList]
        buffer: Gtk.EntryBuffer
        caps_lock_warning: bool
        completion: Gtk.EntryCompletion
        cursor_position: int
        editable: bool
        enable_emoji_completion: bool
        has_frame: bool
        im_module: str
        inner_border: typing.Optional[Gtk.Border]
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        invisible_char: int
        invisible_char_set: bool
        max_length: int
        max_width_chars: int
        overwrite_mode: bool
        placeholder_text: str
        populate_all: bool
        primary_icon_activatable: bool
        primary_icon_gicon: Gio.Icon
        primary_icon_name: str
        primary_icon_pixbuf: GdkPixbuf.Pixbuf
        primary_icon_sensitive: bool
        primary_icon_stock: str
        primary_icon_storage_type: Gtk.ImageType
        primary_icon_tooltip_markup: str
        primary_icon_tooltip_text: str
        progress_fraction: float
        progress_pulse_step: float
        scroll_offset: int
        secondary_icon_activatable: bool
        secondary_icon_gicon: Gio.Icon
        secondary_icon_name: str
        secondary_icon_pixbuf: GdkPixbuf.Pixbuf
        secondary_icon_sensitive: bool
        secondary_icon_stock: str
        secondary_icon_storage_type: Gtk.ImageType
        secondary_icon_tooltip_markup: str
        secondary_icon_tooltip_text: str
        selection_bound: int
        shadow_type: Gtk.ShadowType
        show_emoji_icon: bool
        tabs: typing.Optional[Pango.TabArray]
        text: str
        text_length: int
        truncate_multiline: bool
        visibility: bool
        width_chars: int
        xalign: float
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
    props: Props = ...
    def __init__(self, activates_default: bool = ...,
                 attributes: Pango.AttrList = ...,
                 buffer: Gtk.EntryBuffer = ...,
                 caps_lock_warning: bool = ...,
                 completion: typing.Optional[Gtk.EntryCompletion] = ...,
                 editable: bool = ...,
                 enable_emoji_completion: bool = ...,
                 has_frame: bool = ...,
                 im_module: str = ...,
                 inner_border: typing.Optional[Gtk.Border] = ...,
                 input_hints: Gtk.InputHints = ...,
                 input_purpose: Gtk.InputPurpose = ...,
                 invisible_char: int = ...,
                 invisible_char_set: bool = ...,
                 max_length: int = ...,
                 max_width_chars: int = ...,
                 overwrite_mode: bool = ...,
                 placeholder_text: typing.Optional[str] = ...,
                 populate_all: bool = ...,
                 primary_icon_activatable: bool = ...,
                 primary_icon_gicon: Gio.Icon = ...,
                 primary_icon_name: str = ...,
                 primary_icon_pixbuf: GdkPixbuf.Pixbuf = ...,
                 primary_icon_sensitive: bool = ...,
                 primary_icon_stock: str = ...,
                 primary_icon_tooltip_markup: str = ...,
                 primary_icon_tooltip_text: str = ...,
                 progress_fraction: float = ...,
                 progress_pulse_step: float = ...,
                 secondary_icon_activatable: bool = ...,
                 secondary_icon_gicon: Gio.Icon = ...,
                 secondary_icon_name: str = ...,
                 secondary_icon_pixbuf: GdkPixbuf.Pixbuf = ...,
                 secondary_icon_sensitive: bool = ...,
                 secondary_icon_stock: str = ...,
                 secondary_icon_tooltip_markup: str = ...,
                 secondary_icon_tooltip_text: str = ...,
                 shadow_type: Gtk.ShadowType = ...,
                 show_emoji_icon: bool = ...,
                 tabs: Pango.TabArray = ...,
                 text: str = ...,
                 truncate_multiline: bool = ...,
                 visibility: bool = ...,
                 width_chars: int = ...,
                 xalign: float = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    def get_color(self) -> Gegl.Color: ...
    @classmethod
    def new(cls) -> ColorHexEntry: ...
    def set_color(self, color: Gegl.Color) -> None: ...
    

class ColorHexEntryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorHexEntryClass()
    """
    parent_class: Gtk.EntryClass = ...

class ColorNotebook(ColorSelector, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        ColorNotebook(**properties)

    Object GimpColorNotebook

    Signals from GimpColorSelector:
      color-changed (GeglColor)
      channel-changed (GimpColorSelectorChannel)
      model-visible-changed (GimpColorSelectorModel, gboolean)
      simulation (gboolean)

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def enable_simulation(self, enabled: bool) -> None: ...
    def get_current_selector(self) -> ColorSelector: ...
    def get_notebook(self) -> Gtk.Notebook: ...
    def get_selectors(self) -> list[ColorSelector]: ...
    def set_format(self, format: Babl.Object) -> None: ...
    def set_has_page(self, page_type: typing.Type[typing.Any], has_page: bool) -> Gtk.Widget: ...
    def set_simulation(self, profile: Gimp.ColorProfile, intent: Gimp.ColorRenderingIntent, bpc: bool) -> None: ...
    

class ColorNotebookClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorNotebookClass()
    """
    parent_class: ColorSelectorClass = ...

class ColorProfileChooserDialog(Gtk.FileChooserDialog, Atk.ImplementorIface, Gtk.Buildable, Gtk.FileChooser):
    """
    :Constructors:

    ::

        ColorProfileChooserDialog(**properties)
        new(title:str, parent:Gtk.Window, action:Gtk.FileChooserAction) -> Gtk.Widget

    Object GimpColorProfileChooserDialog

    Signals from GtkFileChooser:
      selection-changed ()
      current-folder-changed ()
      update-preview ()
      file-activated ()
      confirm-overwrite () -> GtkFileChooserConfirmation

    Signals from GtkFileChooser:
      selection-changed ()
      current-folder-changed ()
      update-preview ()
      file-activated ()
      confirm-overwrite () -> GtkFileChooserConfirmation

    Signals from GtkDialog:
      response (gint)
      close ()

    Properties from GtkDialog:
      use-header-bar -> gint: Use Header Bar
        Use Header Bar for actions.

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        use_header_bar: int
        accept_focus: bool
        application: typing.Optional[Gtk.Application]
        attached_to: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: typing.Optional[GdkPixbuf.Pixbuf]
        icon_name: typing.Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: typing.Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: typing.Optional[str]
        transient_for: typing.Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        action: Gtk.FileChooserAction
        create_folders: bool
        do_overwrite_confirmation: bool
        extra_widget: typing.Optional[Gtk.Widget]
        filter: typing.Optional[Gtk.FileFilter]
        local_only: bool
        preview_widget: typing.Optional[Gtk.Widget]
        preview_widget_active: bool
        select_multiple: bool
        show_hidden: bool
        use_preview_label: bool
        startup_id: str
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, use_header_bar: int = ...,
                 accept_focus: bool = ...,
                 application: typing.Optional[Gtk.Application] = ...,
                 attached_to: typing.Optional[Gtk.Widget] = ...,
                 decorated: bool = ...,
                 default_height: int = ...,
                 default_width: int = ...,
                 deletable: bool = ...,
                 destroy_with_parent: bool = ...,
                 focus_on_map: bool = ...,
                 focus_visible: bool = ...,
                 gravity: Gdk.Gravity = ...,
                 has_resize_grip: bool = ...,
                 hide_titlebar_when_maximized: bool = ...,
                 icon: typing.Optional[GdkPixbuf.Pixbuf] = ...,
                 icon_name: typing.Optional[str] = ...,
                 mnemonics_visible: bool = ...,
                 modal: bool = ...,
                 resizable: bool = ...,
                 role: str = ...,
                 screen: Gdk.Screen = ...,
                 skip_pager_hint: bool = ...,
                 skip_taskbar_hint: bool = ...,
                 startup_id: str = ...,
                 title: str = ...,
                 transient_for: typing.Optional[Gtk.Window] = ...,
                 type: Gtk.WindowType = ...,
                 type_hint: Gdk.WindowTypeHint = ...,
                 urgency_hint: bool = ...,
                 window_position: Gtk.WindowPosition = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 action: Gtk.FileChooserAction = ...,
                 create_folders: bool = ...,
                 do_overwrite_confirmation: bool = ...,
                 extra_widget: Gtk.Widget = ...,
                 filter: Gtk.FileFilter = ...,
                 local_only: bool = ...,
                 preview_widget: Gtk.Widget = ...,
                 preview_widget_active: bool = ...,
                 select_multiple: bool = ...,
                 show_hidden: bool = ...,
                 use_preview_label: bool = ...) -> None: ...
    @classmethod
    def new(cls, title: str, parent: Gtk.Window, action: Gtk.FileChooserAction) -> ColorProfileChooserDialog: ...
    

class ColorProfileChooserDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorProfileChooserDialogClass()
    """
    parent_class: Gtk.FileChooserDialogClass = ...

class ColorProfileComboBox(Gtk.ComboBox, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.CellLayout):
    """
    :Constructors:

    ::

        ColorProfileComboBox(**properties)
        new(dialog:Gtk.Widget, history:Gio.File) -> Gtk.Widget
        new_with_model(dialog:Gtk.Widget, model:Gtk.TreeModel) -> Gtk.Widget

    Object GimpColorProfileComboBox

    Properties from GimpColorProfileComboBox:
      dialog -> GtkDialog: Dialog
        The dialog to present when selecting profiles from disk
      model -> GimpColorProfileStore: Model
        The profile store used for this combo box

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkComboBox:
      changed ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray

    Properties from GtkComboBox:
      model -> GtkTreeModel: ComboBox model
        The model for the combo box
      wrap-width -> gint: Wrap width
        Wrap width for laying out the items in a grid
      row-span-column -> gint: Row span column
        TreeModel column containing the row span values
      column-span-column -> gint: Column span column
        TreeModel column containing the column span values
      active -> gint: Active item
        The item which is currently active
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether dropdowns should have a tearoff menu item
      tearoff-title -> gchararray: Tearoff Title
        A title that may be displayed by the window manager when the popup is torn-off
      has-frame -> gboolean: Has Frame
        Whether the combo box draws a frame around the child
      popup-shown -> gboolean: Popup shown
        Whether the combo's dropdown is shown
      button-sensitivity -> GtkSensitivityType: Button Sensitivity
        Whether the dropdown button is sensitive when the model is empty
      has-entry -> gboolean: Has Entry
        Whether combo box has an entry
      entry-text-column -> gint: Entry Text Column
        The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE
      popup-fixed-width -> gboolean: Popup Fixed Width
        Whether the popup's width should be a fixed width matching the allocated width of the combo box
      id-column -> gint: ID Column
        The column in the combo box's model that provides string IDs for the values in the model
      active-id -> gchararray: Active id
        The value of the id column for the active row
      cell-area -> GtkCellArea: Cell Area
        The GtkCellArea used to layout cells

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        dialog: Gtk.Dialog
        model: ColorProfileStore
        active: int
        active_id: typing.Optional[str]
        add_tearoffs: bool
        button_sensitivity: Gtk.SensitivityType
        cell_area: Gtk.CellArea
        column_span_column: int
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        id_column: int
        popup_fixed_width: bool
        popup_shown: bool
        row_span_column: int
        tearoff_title: str
        wrap_width: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, dialog: Gtk.Dialog = ...,
                 model: ColorProfileStore = ...,
                 active: int = ...,
                 active_id: typing.Optional[str] = ...,
                 add_tearoffs: bool = ...,
                 button_sensitivity: Gtk.SensitivityType = ...,
                 cell_area: Gtk.CellArea = ...,
                 column_span_column: int = ...,
                 entry_text_column: int = ...,
                 has_entry: bool = ...,
                 has_frame: bool = ...,
                 id_column: int = ...,
                 popup_fixed_width: bool = ...,
                 row_span_column: int = ...,
                 tearoff_title: str = ...,
                 wrap_width: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    def add_file(self, file: Gio.File, label: str) -> None: ...
    def get_active_file(self) -> Gio.File: ...
    @classmethod
    def new(cls, dialog: Gtk.Widget, history: Gio.File) -> ColorProfileComboBox: ...
    @classmethod
    def new_with_model(cls, dialog: Gtk.Widget, model: Gtk.TreeModel) -> ColorProfileComboBox: ...
    def set_active_file(self, file: Gio.File, label: str) -> None: ...
    def set_active_profile(self, profile: Gimp.ColorProfile) -> None: ...
    

class ColorProfileComboBoxClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorProfileComboBoxClass()
    """
    parent_class: Gtk.ComboBoxClass = ...

class ColorProfileStore(Gtk.ListStore, Gtk.Buildable, Gtk.TreeDragDest, Gtk.TreeDragSource, Gtk.TreeModel, Gtk.TreeSortable):
    """
    :Constructors:

    ::

        ColorProfileStore(**properties)
        new(history:Gio.File) -> Gtk.ListStore

    Object GimpColorProfileStore

    Properties from GimpColorProfileStore:
      history -> GFile: History
        Filen of the color history used to populate the profile store

    Signals from GtkTreeModel:
      row-inserted (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      row-changed (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)

    Signals from GtkTreeSortable:
      sort-column-changed ()

    Signals from GtkTreeModel:
      row-inserted (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      row-changed (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)

    Signals from GtkTreeSortable:
      sort-column-changed ()

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        history: Gio.File
    props: Props = ...
    def __init__(self, history: Gio.File = ...) -> None: ...
    def add_file(self, file: Gio.File, label: str) -> None: ...
    @classmethod
    def new(cls, history: Gio.File) -> ColorProfileStore: ...
    

class ColorProfileStoreClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorProfileStoreClass()
    """
    parent_class: Gtk.ListStoreClass = ...

class ColorProfileView(Gtk.TextView, Atk.ImplementorIface, Gtk.Buildable, Gtk.Scrollable):
    """
    :Constructors:

    ::

        ColorProfileView(**properties)
        new() -> Gtk.Widget

    Object GimpColorProfileView

    Signals from GtkTextView:
      populate-popup (GtkWidget)
      move-cursor (GtkMovementStep, gint, gboolean)
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      preedit-changed (gchararray)
      insert-emoji ()
      move-viewport (GtkScrollStep, gint)
      set-anchor ()
      select-all (gboolean)
      toggle-cursor-visible ()
      extend-selection (GtkTextExtendSelection, GtkTextIter, GtkTextIter, GtkTextIter) -> gboolean

    Properties from GtkTextView:
      pixels-above-lines -> gint: Pixels Above Lines
        Pixels of blank space above paragraphs
      pixels-below-lines -> gint: Pixels Below Lines
        Pixels of blank space below paragraphs
      pixels-inside-wrap -> gint: Pixels Inside Wrap
        Pixels of blank space between wrapped lines in a paragraph
      editable -> gboolean: Editable
        Whether the text can be modified by the user
      wrap-mode -> GtkWrapMode: Wrap Mode
        Whether to wrap lines never, at word boundaries, or at character boundaries
      justification -> GtkJustification: Justification
        Left, right, or center justification
      left-margin -> gint: Left Margin
        Width of the left margin in pixels
      right-margin -> gint: Right Margin
        Width of the right margin in pixels
      top-margin -> gint: Top Margin
        Height of the top margin in pixels
      bottom-margin -> gint: Bottom Margin
        Height of the bottom margin in pixels
      indent -> gint: Indent
        Amount to indent the paragraph, in pixels
      tabs -> PangoTabArray: Tabs
        Custom tabs for this text
      cursor-visible -> gboolean: Cursor Visible
        If the insertion cursor is shown
      buffer -> GtkTextBuffer: Buffer
        The buffer which is displayed
      overwrite -> gboolean: Overwrite mode
        Whether entered text overwrites existing contents
      accepts-tab -> gboolean: Accepts tab
        Whether Tab will result in a tab character being entered
      im-module -> gchararray: IM module
        Which IM module should be used
      input-purpose -> GtkInputPurpose: Purpose
        Purpose of the text field
      input-hints -> GtkInputHints: hints
        Hints for the text field behaviour
      populate-all -> gboolean: Populate all
        Whether to emit ::populate-popup for touch popups
      monospace -> gboolean: Monospace
        Whether to use a monospace font

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        accepts_tab: bool
        bottom_margin: int
        buffer: Gtk.TextBuffer
        cursor_visible: bool
        editable: bool
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
        populate_all: bool
        right_margin: int
        tabs: typing.Optional[Pango.TabArray]
        top_margin: int
        wrap_mode: Gtk.WrapMode
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        hadjustment: Gtk.Adjustment
        hscroll_policy: Gtk.ScrollablePolicy
        vadjustment: Gtk.Adjustment
        vscroll_policy: Gtk.ScrollablePolicy
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, accepts_tab: bool = ...,
                 bottom_margin: int = ...,
                 buffer: typing.Optional[Gtk.TextBuffer] = ...,
                 cursor_visible: bool = ...,
                 editable: bool = ...,
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
                 populate_all: bool = ...,
                 right_margin: int = ...,
                 tabs: Pango.TabArray = ...,
                 top_margin: int = ...,
                 wrap_mode: Gtk.WrapMode = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 hadjustment: typing.Optional[Gtk.Adjustment] = ...,
                 hscroll_policy: Gtk.ScrollablePolicy = ...,
                 vadjustment: typing.Optional[Gtk.Adjustment] = ...,
                 vscroll_policy: Gtk.ScrollablePolicy = ...) -> None: ...
    @classmethod
    def new(cls) -> ColorProfileView: ...
    def set_error(self, message: str) -> None: ...
    def set_profile(self, profile: Gimp.ColorProfile) -> None: ...
    

class ColorProfileViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorProfileViewClass()
    """
    parent_class: Gtk.TextViewClass = ...

class ColorScale(Gtk.Scale, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        ColorScale(**properties)
        new(orientation:Gtk.Orientation, channel:GimpUi.ColorSelectorChannel) -> Gtk.Widget

    Object GimpColorScale

    Properties from GimpColorScale:
      channel -> GimpColorSelectorChannel: Channel
        The channel which is edited by the color scale

    Signals from GtkScale:
      format-value (gdouble) -> gchararray

    Properties from GtkScale:
      digits -> gint: Digits
        The number of decimal places that are displayed in the value
      draw-value -> gboolean: Draw Value
        Whether the current value is displayed as a string next to the slider
      has-origin -> gboolean: Has Origin
        Whether the scale has an origin
      value-pos -> GtkPositionType: Value Position
        The position in which the current value is displayed

    Signals from GtkRange:
      value-changed ()
      adjust-bounds (gdouble)
      move-slider (GtkScrollType)
      change-value (GtkScrollType, gdouble) -> gboolean

    Properties from GtkRange:
      adjustment -> GtkAdjustment: Adjustment
        The GtkAdjustment that contains the current value of this range object
      inverted -> gboolean: Inverted
        Invert direction slider moves to increase range value
      lower-stepper-sensitivity -> GtkSensitivityType: Lower stepper sensitivity
        The sensitivity policy for the stepper that points to the adjustment's lower side
      upper-stepper-sensitivity -> GtkSensitivityType: Upper stepper sensitivity
        The sensitivity policy for the stepper that points to the adjustment's upper side
      show-fill-level -> gboolean: Show Fill Level
        Whether to display a fill level indicator graphics on trough.
      restrict-to-fill-level -> gboolean: Restrict to Fill Level
        Whether to restrict the upper boundary to the fill level.
      fill-level -> gdouble: Fill Level
        The fill level.
      round-digits -> gint: Round Digits
        The number of digits to round the value to.

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        channel: ColorSelectorChannel
        digits: int
        draw_value: bool
        has_origin: bool
        value_pos: Gtk.PositionType
        adjustment: Gtk.Adjustment
        fill_level: float
        inverted: bool
        lower_stepper_sensitivity: Gtk.SensitivityType
        restrict_to_fill_level: bool
        round_digits: int
        show_fill_level: bool
        upper_stepper_sensitivity: Gtk.SensitivityType
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(self, channel: ColorSelectorChannel = ...,
                 digits: int = ...,
                 draw_value: bool = ...,
                 has_origin: bool = ...,
                 value_pos: Gtk.PositionType = ...,
                 adjustment: Gtk.Adjustment = ...,
                 fill_level: float = ...,
                 inverted: bool = ...,
                 lower_stepper_sensitivity: Gtk.SensitivityType = ...,
                 restrict_to_fill_level: bool = ...,
                 round_digits: int = ...,
                 show_fill_level: bool = ...,
                 upper_stepper_sensitivity: Gtk.SensitivityType = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    @classmethod
    def new(cls, orientation: Gtk.Orientation, channel: ColorSelectorChannel) -> ColorScale: ...
    def set_channel(self, channel: ColorSelectorChannel) -> None: ...
    def set_color(self, color: Gegl.Color) -> None: ...
    def set_color_config(self, config: Gimp.ColorConfig) -> None: ...
    def set_format(self, format: Babl.Object) -> None: ...
    

class ColorScaleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorScaleClass()
    """
    parent_class: Gtk.ScaleClass = ...

class ColorScaleEntry(ScaleEntry, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        ColorScaleEntry(**properties)
        new(text:str, value:float, lower:float, upper:float, digits:int) -> Gtk.Widget

    Object GimpColorScaleEntry

    Signals from GimpLabelSpin:
      value-changed ()

    Properties from GimpLabelSpin:
      value -> gdouble: value
        Current value
      lower -> gdouble: lower
        Minimum value
      upper -> gdouble: upper
        Max value
      digits -> gint: digits
        The number of decimal places to display

    Signals from GimpLabeled:
      mnemonic-widget-changed (GtkWidget)

    Properties from GimpLabeled:
      label -> gchararray: Label text
        The text of the label part of this widget

    Properties from GtkGrid:
      row-spacing -> gint: Row spacing
        The amount of space between two consecutive rows
      column-spacing -> gint: Column spacing
        The amount of space between two consecutive columns
      row-homogeneous -> gboolean: Row Homogeneous
        If TRUE, the rows are all the same height
      column-homogeneous -> gboolean: Column Homogeneous
        If TRUE, the columns are all the same width
      baseline-row -> gint: Baseline Row
        The row to align the to the baseline when valign is GTK_ALIGN_BASELINE

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        digits: int
        lower: float
        upper: float
        value: float
        label: str
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, digits: int = ...,
                 lower: float = ...,
                 upper: float = ...,
                 value: float = ...,
                 label: str = ...,
                 baseline_row: int = ...,
                 column_homogeneous: bool = ...,
                 column_spacing: int = ...,
                 row_homogeneous: bool = ...,
                 row_spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    @classmethod
    def new(cls, text: str, value: float, lower: float, upper: float, digits: int) -> ColorScaleEntry: ...
    

class ColorScaleEntryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorScaleEntryClass()
    """
    parent_class: ScaleEntryClass = ...

class ColorScales(GObject.GPointer): ...

class ColorSelect(GObject.GPointer): ...

class ColorSelection(Gtk.Box, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        ColorSelection(**properties)
        new() -> Gtk.Widget

    Object GimpColorSelection

    Signals from GimpColorSelection:
      color-changed ()

    Properties from GimpColorSelection:
      config -> GimpColorConfig: Config
        The color config used by this color selection

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        config: Gimp.ColorConfig
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, config: Gimp.ColorConfig = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def color_changed(self) -> None: ...
    def get_color(self) -> Gegl.Color: ...
    def get_notebook(self) -> Gtk.Widget: ...
    def get_old_color(self) -> Gegl.Color: ...
    def get_right_vbox(self) -> Gtk.Box: ...
    def get_show_alpha(self) -> bool: ...
    @classmethod
    def new(cls) -> ColorSelection: ...
    def reset(self) -> None: ...
    def set_color(self, color: Gegl.Color) -> None: ...
    def set_config(self, config: Gimp.ColorConfig) -> None: ...
    def set_format(self, format: Babl.Object) -> None: ...
    def set_old_color(self, color: Gegl.Color) -> None: ...
    def set_show_alpha(self, show_alpha: bool) -> None: ...
    def set_simulation(self, profile: Gimp.ColorProfile, intent: Gimp.ColorRenderingIntent, bpc: bool) -> None: ...
    

class ColorSelectionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorSelectionClass()
    """
    parent_class: Gtk.BoxClass = ...

class ColorSelector(Gtk.Box, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        ColorSelector(**properties)

    Object GimpColorSelector

    Signals from GimpColorSelector:
      color-changed (GeglColor)
      channel-changed (GimpColorSelectorChannel)
      model-visible-changed (GimpColorSelectorModel, gboolean)
      simulation (gboolean)

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Box = ...
    def __init__(self, baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def do_channel_changed(self, channel: ColorSelectorChannel) -> None: ...
    def do_color_changed(self, color: Gegl.Color) -> None: ...
    def do_model_visible_changed(self, model: ColorSelectorModel, visible: bool) -> None: ...
    def do_set_channel(self, channel: ColorSelectorChannel) -> None: ...
    def do_set_color(self, color: Gegl.Color) -> None: ...
    def do_set_config(self, config: Gimp.ColorConfig) -> None: ...
    def do_set_format(self, format: Babl.Object) -> None: ...
    def do_set_model_visible(self, model: ColorSelectorModel, visible: bool) -> None: ...
    def do_set_show_alpha(self, show_alpha: bool) -> None: ...
    def do_set_simulation(self, profile: Gimp.ColorProfile, intent: Gimp.ColorRenderingIntent, bpc: bool) -> None: ...
    def do_set_toggles_sensitive(self, sensitive: bool) -> None: ...
    def do_set_toggles_visible(self, visible: bool) -> None: ...
    def do_simulation(self, enabled: bool) -> None: ...
    def enable_simulation(self, enabled: bool) -> bool: ...
    def get_channel(self) -> ColorSelectorChannel: ...
    def get_color(self) -> Gegl.Color: ...
    def get_model_visible(self, model: ColorSelectorModel) -> bool: ...
    def get_show_alpha(self) -> bool: ...
    def get_simulation(self, profile: Gimp.ColorProfile, intent: Gimp.ColorRenderingIntent, bpc: bool) -> bool: ...
    def get_toggles_sensitive(self) -> bool: ...
    def get_toggles_visible(self) -> bool: ...
    def set_channel(self, channel: ColorSelectorChannel) -> None: ...
    def set_color(self, color: Gegl.Color) -> None: ...
    def set_config(self, config: Gimp.ColorConfig) -> None: ...
    def set_format(self, format: Babl.Object) -> None: ...
    def set_model_visible(self, model: ColorSelectorModel, visible: bool) -> None: ...
    def set_show_alpha(self, show_alpha: bool) -> None: ...
    def set_simulation(self, profile: Gimp.ColorProfile, intent: Gimp.ColorRenderingIntent, bpc: bool) -> None: ...
    def set_toggles_sensitive(self, sensitive: bool) -> None: ...
    def set_toggles_visible(self, visible: bool) -> None: ...
    

class ColorSelectorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ColorSelectorClass()
    """
    parent_class: Gtk.BoxClass = ...
    name: str = ...
    help_id: str = ...
    icon_name: str = ...
    set_toggles_visible: typing.Callable[[ColorSelector, bool], None] = ...
    set_toggles_sensitive: typing.Callable[[ColorSelector, bool], None] = ...
    set_show_alpha: typing.Callable[[ColorSelector, bool], None] = ...
    set_color: typing.Callable[[ColorSelector, Gegl.Color], None] = ...
    set_channel: typing.Callable[[ColorSelector, ColorSelectorChannel], None] = ...
    set_model_visible: typing.Callable[[ColorSelector, ColorSelectorModel, bool], None] = ...
    set_config: typing.Callable[[ColorSelector, Gimp.ColorConfig], None] = ...
    set_format: typing.Callable[[ColorSelector, Babl.Object], None] = ...
    set_simulation: typing.Callable[[ColorSelector, Gimp.ColorProfile, Gimp.ColorRenderingIntent, bool], None] = ...
    color_changed: typing.Callable[[ColorSelector, Gegl.Color], None] = ...
    channel_changed: typing.Callable[[ColorSelector, ColorSelectorChannel], None] = ...
    model_visible_changed: typing.Callable[[ColorSelector, ColorSelectorModel, bool], None] = ...
    simulation: typing.Callable[[ColorSelector, bool], None] = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class Controller(GObject.GPointer): ...

class Dialog(Gtk.Dialog, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        Dialog(**properties)

    Object GimpDialog

    Properties from GimpDialog:
      help-func -> gpointer: Help Func
        The help function to call when F1 is hit
      help-id -> gchararray: Help ID
        The help ID to pass to help-func
      parent -> GtkWidget: Parent
        The dialog's parent widget

    Signals from GtkDialog:
      response (gint)
      close ()

    Properties from GtkDialog:
      use-header-bar -> gint: Use Header Bar
        Use Header Bar for actions.

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        help_func: None
        help_id: str
        use_header_bar: int
        accept_focus: bool
        application: typing.Optional[Gtk.Application]
        attached_to: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: typing.Optional[GdkPixbuf.Pixbuf]
        icon_name: typing.Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: typing.Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: typing.Optional[str]
        transient_for: typing.Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        startup_id: str
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Dialog = ...
    def __init__(self, help_func: None = ...,
                 help_id: str = ...,
                 parent: Gtk.Widget = ...,
                 use_header_bar: int = ...,
                 accept_focus: bool = ...,
                 application: typing.Optional[Gtk.Application] = ...,
                 attached_to: typing.Optional[Gtk.Widget] = ...,
                 decorated: bool = ...,
                 default_height: int = ...,
                 default_width: int = ...,
                 deletable: bool = ...,
                 destroy_with_parent: bool = ...,
                 focus_on_map: bool = ...,
                 focus_visible: bool = ...,
                 gravity: Gdk.Gravity = ...,
                 has_resize_grip: bool = ...,
                 hide_titlebar_when_maximized: bool = ...,
                 icon: typing.Optional[GdkPixbuf.Pixbuf] = ...,
                 icon_name: typing.Optional[str] = ...,
                 mnemonics_visible: bool = ...,
                 modal: bool = ...,
                 resizable: bool = ...,
                 role: str = ...,
                 screen: Gdk.Screen = ...,
                 skip_pager_hint: bool = ...,
                 skip_taskbar_hint: bool = ...,
                 startup_id: str = ...,
                 title: str = ...,
                 transient_for: typing.Optional[Gtk.Window] = ...,
                 type: Gtk.WindowType = ...,
                 type_hint: Gdk.WindowTypeHint = ...,
                 urgency_hint: bool = ...,
                 window_position: Gtk.WindowPosition = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    def add_button(self, button_text: str, response_id: int) -> Gtk.Widget: ...
    def get_native_handle(self) -> GLib.Bytes: ...
    def run(self) -> int: ...
    def set_alternative_button_order_from_array(self, order: typing.Sequence[int]) -> None: ...
    

class DialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DialogClass()
    """
    parent_class: Gtk.DialogClass = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class DrawableChooser(Gtk.Box, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        DrawableChooser(**properties)
        new(title:str=None, label:str=None, drawable_type:GType, drawable:Gimp.Drawable=None) -> Gtk.Widget

    Object GimpDrawableChooser

    Properties from GimpDrawableChooser:
      title -> gchararray: Title
        The title to be used for the drawable selection popup dialog
      label -> gchararray: Label
        The label to be used next to the button
      drawable -> GimpDrawable: Drawable
        The currently selected drawable
      drawable-type -> GType: Allowed drawable Type
        The GType of the drawable property

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        drawable: Gimp.Drawable
        drawable_type: typing.Type[typing.Any]
        label: str
        title: str
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, drawable: Gimp.Drawable = ...,
                 drawable_type: typing.Type[typing.Any] = ...,
                 label: str = ...,
                 title: str = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_drawable(self) -> Gimp.Drawable: ...
    def get_label(self) -> Gtk.Widget: ...
    @classmethod
    def new(cls, title: typing.Optional[str], label: typing.Optional[str], drawable_type: typing.Type[typing.Any], drawable: typing.Optional[Gimp.Drawable] = None) -> DrawableChooser: ...
    def set_drawable(self, drawable: Gimp.Drawable) -> None: ...
    

class DrawableChooserClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DrawableChooserClass()
    """
    parent_class: Gtk.BoxClass = ...

class DrawableComboBox(IntComboBox, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.CellLayout):
    """
    :Constructors:

    ::

        DrawableComboBox(**properties)
        new(constraint:GimpUi.ItemConstraintFunc=None) -> Gtk.Widget

    Object GimpDrawableComboBox

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Properties from GimpIntComboBox:
      ellipsize -> PangoEllipsizeMode: Ellipsize
        Ellipsize mode for the used text cell renderer
      label -> gchararray: Label
        An optional label to be displayed
      layout -> GimpIntComboBoxLayout: Layout
        Combo box layout
      value -> gint: Value
        Value of active item

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkComboBox:
      changed ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray

    Properties from GtkComboBox:
      model -> GtkTreeModel: ComboBox model
        The model for the combo box
      wrap-width -> gint: Wrap width
        Wrap width for laying out the items in a grid
      row-span-column -> gint: Row span column
        TreeModel column containing the row span values
      column-span-column -> gint: Column span column
        TreeModel column containing the column span values
      active -> gint: Active item
        The item which is currently active
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether dropdowns should have a tearoff menu item
      tearoff-title -> gchararray: Tearoff Title
        A title that may be displayed by the window manager when the popup is torn-off
      has-frame -> gboolean: Has Frame
        Whether the combo box draws a frame around the child
      popup-shown -> gboolean: Popup shown
        Whether the combo's dropdown is shown
      button-sensitivity -> GtkSensitivityType: Button Sensitivity
        Whether the dropdown button is sensitive when the model is empty
      has-entry -> gboolean: Has Entry
        Whether combo box has an entry
      entry-text-column -> gint: Entry Text Column
        The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE
      popup-fixed-width -> gboolean: Popup Fixed Width
        Whether the popup's width should be a fixed width matching the allocated width of the combo box
      id-column -> gint: ID Column
        The column in the combo box's model that provides string IDs for the values in the model
      active-id -> gchararray: Active id
        The value of the id column for the active row
      cell-area -> GtkCellArea: Cell Area
        The GtkCellArea used to layout cells

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        ellipsize: Pango.EllipsizeMode
        label: str
        layout: IntComboBoxLayout
        value: int
        active: int
        active_id: typing.Optional[str]
        add_tearoffs: bool
        button_sensitivity: Gtk.SensitivityType
        cell_area: Gtk.CellArea
        column_span_column: int
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        id_column: int
        model: Gtk.TreeModel
        popup_fixed_width: bool
        popup_shown: bool
        row_span_column: int
        tearoff_title: str
        wrap_width: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, ellipsize: Pango.EllipsizeMode = ...,
                 label: str = ...,
                 layout: IntComboBoxLayout = ...,
                 value: int = ...,
                 active: int = ...,
                 active_id: typing.Optional[str] = ...,
                 add_tearoffs: bool = ...,
                 button_sensitivity: Gtk.SensitivityType = ...,
                 cell_area: Gtk.CellArea = ...,
                 column_span_column: int = ...,
                 entry_text_column: int = ...,
                 has_entry: bool = ...,
                 has_frame: bool = ...,
                 id_column: int = ...,
                 model: typing.Optional[Gtk.TreeModel] = ...,
                 popup_fixed_width: bool = ...,
                 row_span_column: int = ...,
                 tearoff_title: str = ...,
                 wrap_width: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    @classmethod
    def new(cls, constraint: typing.Optional[typing.Callable[..., bool]] = None, *data: typing.Any) -> DrawableComboBox: ...
    

class DrawablePreview(ScrolledPreview, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        DrawablePreview(**properties)
        new_from_drawable(drawable:Gimp.Drawable) -> Gtk.Widget

    Object GimpDrawablePreview

    Properties from GimpDrawablePreview:
      drawable -> GimpDrawable: Drawable
        The drawable this preview is attached to

    Signals from GimpPreview:
      invalidated ()

    Properties from GimpPreview:
      update -> gboolean: Update
        Whether the preview should update automatically

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        drawable: Gimp.Drawable
        update: bool
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, drawable: Gimp.Drawable = ...,
                 update: bool = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_drawable(self) -> Gimp.Drawable: ...
    @classmethod
    def new_from_drawable(cls, drawable: Gimp.Drawable) -> DrawablePreview: ...
    

class DrawablePreviewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DrawablePreviewClass()
    """
    parent_class: ScrolledPreviewClass = ...

class EnumComboBox(IntComboBox, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.CellLayout):
    """
    :Constructors:

    ::

        EnumComboBox(**properties)
        new(enum_type:GType) -> Gtk.Widget
        new_with_model(enum_store:GimpUi.EnumStore) -> Gtk.Widget

    Object GimpEnumComboBox

    Properties from GimpEnumComboBox:
      model -> GimpEnumStore: Model
        The enum store used by this combo box

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Properties from GimpIntComboBox:
      ellipsize -> PangoEllipsizeMode: Ellipsize
        Ellipsize mode for the used text cell renderer
      label -> gchararray: Label
        An optional label to be displayed
      layout -> GimpIntComboBoxLayout: Layout
        Combo box layout
      value -> gint: Value
        Value of active item

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkComboBox:
      changed ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray

    Properties from GtkComboBox:
      model -> GtkTreeModel: ComboBox model
        The model for the combo box
      wrap-width -> gint: Wrap width
        Wrap width for laying out the items in a grid
      row-span-column -> gint: Row span column
        TreeModel column containing the row span values
      column-span-column -> gint: Column span column
        TreeModel column containing the column span values
      active -> gint: Active item
        The item which is currently active
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether dropdowns should have a tearoff menu item
      tearoff-title -> gchararray: Tearoff Title
        A title that may be displayed by the window manager when the popup is torn-off
      has-frame -> gboolean: Has Frame
        Whether the combo box draws a frame around the child
      popup-shown -> gboolean: Popup shown
        Whether the combo's dropdown is shown
      button-sensitivity -> GtkSensitivityType: Button Sensitivity
        Whether the dropdown button is sensitive when the model is empty
      has-entry -> gboolean: Has Entry
        Whether combo box has an entry
      entry-text-column -> gint: Entry Text Column
        The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE
      popup-fixed-width -> gboolean: Popup Fixed Width
        Whether the popup's width should be a fixed width matching the allocated width of the combo box
      id-column -> gint: ID Column
        The column in the combo box's model that provides string IDs for the values in the model
      active-id -> gchararray: Active id
        The value of the id column for the active row
      cell-area -> GtkCellArea: Cell Area
        The GtkCellArea used to layout cells

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        model: EnumStore
        ellipsize: Pango.EllipsizeMode
        label: str
        layout: IntComboBoxLayout
        value: int
        active: int
        active_id: typing.Optional[str]
        add_tearoffs: bool
        button_sensitivity: Gtk.SensitivityType
        cell_area: Gtk.CellArea
        column_span_column: int
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        id_column: int
        popup_fixed_width: bool
        popup_shown: bool
        row_span_column: int
        tearoff_title: str
        wrap_width: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        child: Gtk.Widget
    props: Props = ...
    parent_instance: IntComboBox = ...
    def __init__(self, model: EnumStore = ...,
                 ellipsize: Pango.EllipsizeMode = ...,
                 label: str = ...,
                 layout: IntComboBoxLayout = ...,
                 value: int = ...,
                 active: int = ...,
                 active_id: typing.Optional[str] = ...,
                 add_tearoffs: bool = ...,
                 button_sensitivity: Gtk.SensitivityType = ...,
                 cell_area: Gtk.CellArea = ...,
                 column_span_column: int = ...,
                 entry_text_column: int = ...,
                 has_entry: bool = ...,
                 has_frame: bool = ...,
                 id_column: int = ...,
                 popup_fixed_width: bool = ...,
                 row_span_column: int = ...,
                 tearoff_title: str = ...,
                 wrap_width: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    @classmethod
    def new(cls, enum_type: typing.Type[typing.Any]) -> EnumComboBox: ...
    @classmethod
    def new_with_model(cls, enum_store: EnumStore) -> EnumComboBox: ...
    def set_icon_prefix(self, icon_prefix: str) -> None: ...
    

class EnumComboBoxClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EnumComboBoxClass()
    """
    parent_class: IntComboBoxClass = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class EnumLabel(Gtk.Label, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        EnumLabel(**properties)
        new(enum_type:GType, value:int) -> Gtk.Widget

    Object GimpEnumLabel

    Properties from GimpEnumLabel:
      enum-type -> GType: Enum Type
        The type of the displayed enum
      enum-value -> gint: Enum Value
        The enum value to display

    Signals from GtkLabel:
      populate-popup (GtkMenu)
      move-cursor (GtkMovementStep, gint, gboolean)
      copy-clipboard ()
      activate-current-link ()
      activate-link (gchararray) -> gboolean

    Properties from GtkLabel:
      label -> gchararray: Label
        The text of the label
      attributes -> PangoAttrList: Attributes
        A list of style attributes to apply to the text of the label
      use-markup -> gboolean: Use markup
        The text of the label includes XML markup. See pango_parse_markup()
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key
      justify -> GtkJustification: Justification
        The alignment of the lines in the text of the label relative to each other. This does NOT affect the alignment of the label within its allocation. See GtkLabel:xalign for that
      pattern -> gchararray: Pattern
        A string with _ characters in positions correspond to characters in the text to underline
      wrap -> gboolean: Line wrap
        If set, wrap lines if the text becomes too wide
      wrap-mode -> PangoWrapMode: Line wrap mode
        If wrap is set, controls how linewrapping is done
      selectable -> gboolean: Selectable
        Whether the label text can be selected with the mouse
      mnemonic-keyval -> guint: Mnemonic key
        The mnemonic accelerator key for this label
      mnemonic-widget -> GtkWidget: Mnemonic widget
        The widget to be activated when the label's mnemonic key is pressed
      cursor-position -> gint: Cursor Position
        The current position of the insertion cursor in chars
      selection-bound -> gint: Selection Bound
        The position of the opposite end of the selection from the cursor in chars
      ellipsize -> PangoEllipsizeMode: Ellipsize
        The preferred place to ellipsize the string, if the label does not have enough room to display the entire string
      width-chars -> gint: Width In Characters
        The desired width of the label, in characters
      single-line-mode -> gboolean: Single Line Mode
        Whether the label is in single line mode
      angle -> gdouble: Angle
        Angle at which the label is rotated
      max-width-chars -> gint: Maximum Width In Characters
        The desired maximum width of the label, in characters
      track-visited-links -> gboolean: Track visited links
        Whether visited links should be tracked
      lines -> gint: Number of lines
        The desired number of lines, when ellipsizing a wrapping label
      xalign -> gfloat: X align
        The horizontal alignment, from 0 (left) to 1 (right). Reversed for RTL layouts.
      yalign -> gfloat: Y align
        The vertical alignment, from 0 (top) to 1 (bottom)

    Properties from GtkMisc:
      xalign -> gfloat: X align
        The horizontal alignment, from 0 (left) to 1 (right). Reversed for RTL layouts.
      yalign -> gfloat: Y align
        The vertical alignment, from 0 (top) to 1 (bottom)
      xpad -> gint: X pad
        The amount of space to add on the left and right of the widget, in pixels
      ypad -> gint: Y pad
        The amount of space to add on the top and bottom of the widget, in pixels

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        enum_type: typing.Type[typing.Any]
        angle: float
        attributes: typing.Optional[Pango.AttrList]
        cursor_position: int
        ellipsize: Pango.EllipsizeMode
        justify: Gtk.Justification
        label: str
        lines: int
        max_width_chars: int
        mnemonic_keyval: int
        mnemonic_widget: typing.Optional[Gtk.Widget]
        selectable: bool
        selection_bound: int
        single_line_mode: bool
        track_visited_links: bool
        use_markup: bool
        use_underline: bool
        width_chars: int
        wrap: bool
        wrap_mode: Pango.WrapMode
        xalign: float
        yalign: float
        xpad: int
        ypad: int
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        enum_value: int
        pattern: str
    props: Props = ...
    def __init__(self, enum_type: typing.Type[typing.Any] = ...,
                 enum_value: int = ...,
                 angle: float = ...,
                 attributes: typing.Optional[Pango.AttrList] = ...,
                 ellipsize: Pango.EllipsizeMode = ...,
                 justify: Gtk.Justification = ...,
                 label: str = ...,
                 lines: int = ...,
                 max_width_chars: int = ...,
                 mnemonic_widget: typing.Optional[Gtk.Widget] = ...,
                 pattern: str = ...,
                 selectable: bool = ...,
                 single_line_mode: bool = ...,
                 track_visited_links: bool = ...,
                 use_markup: bool = ...,
                 use_underline: bool = ...,
                 width_chars: int = ...,
                 wrap: bool = ...,
                 wrap_mode: Pango.WrapMode = ...,
                 xalign: float = ...,
                 yalign: float = ...,
                 xpad: int = ...,
                 ypad: int = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    @classmethod
    def new(cls, enum_type: typing.Type[typing.Any], value: int) -> EnumLabel: ...
    def set_value(self, value: int) -> None: ...
    

class EnumLabelClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EnumLabelClass()
    """
    parent_class: Gtk.ScaleClass = ...

class EnumStore(IntStore, Gtk.Buildable, Gtk.TreeDragDest, Gtk.TreeDragSource, Gtk.TreeModel, Gtk.TreeSortable):
    """
    :Constructors:

    ::

        EnumStore(**properties)
        new(enum_type:GType) -> Gtk.ListStore
        new_with_range(enum_type:GType, minimum:int, maximum:int) -> Gtk.ListStore

    Object GimpEnumStore

    Properties from GimpEnumStore:
      enum-type -> GType: Enum Type
        The type of the enum

    Signals from GtkTreeModel:
      row-inserted (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      row-changed (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)

    Signals from GtkTreeSortable:
      sort-column-changed ()

    Properties from GimpIntStore:
      user-data-type -> GType: User Data Type
        The GType of the user_data column

    Signals from GtkTreeModel:
      row-inserted (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      row-changed (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)

    Signals from GtkTreeSortable:
      sort-column-changed ()

    Signals from GtkTreeModel:
      row-inserted (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      row-changed (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)

    Signals from GtkTreeSortable:
      sort-column-changed ()

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        enum_type: typing.Type[typing.Any]
        user_data_type: typing.Type[typing.Any]
    props: Props = ...
    def __init__(self, enum_type: typing.Type[typing.Any] = ...,
                 user_data_type: typing.Type[typing.Any] = ...) -> None: ...
    @classmethod
    def new(cls, enum_type: typing.Type[typing.Any]) -> EnumStore: ...
    @classmethod
    def new_with_range(cls, enum_type: typing.Type[typing.Any], minimum: int, maximum: int) -> EnumStore: ...
    def set_icon_prefix(self, icon_prefix: str) -> None: ...
    

class EnumStoreClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EnumStoreClass()
    """
    parent_class: IntStoreClass = ...

class ExportProcedureDialog(ProcedureDialog, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        ExportProcedureDialog(**properties)
        new(procedure:Gimp.ExportProcedure, config:Gimp.ProcedureConfig, image:Gimp.Image) -> Gtk.Widget

    Object GimpExportProcedureDialog

    Properties from GimpProcedureDialog:
      procedure -> GimpProcedure: Procedure
        The GimpProcedure this dialog is used with
      config -> GimpProcedureConfig: Config
        The GimpProcedureConfig this dialog is editing

    Properties from GimpDialog:
      help-func -> gpointer: Help Func
        The help function to call when F1 is hit
      help-id -> gchararray: Help ID
        The help ID to pass to help-func
      parent -> GtkWidget: Parent
        The dialog's parent widget

    Signals from GtkDialog:
      response (gint)
      close ()

    Properties from GtkDialog:
      use-header-bar -> gint: Use Header Bar
        Use Header Bar for actions.

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        config: Gimp.ProcedureConfig
        procedure: Gimp.Procedure
        help_func: None
        help_id: str
        use_header_bar: int
        accept_focus: bool
        application: typing.Optional[Gtk.Application]
        attached_to: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: typing.Optional[GdkPixbuf.Pixbuf]
        icon_name: typing.Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: typing.Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: typing.Optional[str]
        transient_for: typing.Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        startup_id: str
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, config: Gimp.ProcedureConfig = ...,
                 procedure: Gimp.Procedure = ...,
                 help_func: None = ...,
                 help_id: str = ...,
                 parent: Gtk.Widget = ...,
                 use_header_bar: int = ...,
                 accept_focus: bool = ...,
                 application: typing.Optional[Gtk.Application] = ...,
                 attached_to: typing.Optional[Gtk.Widget] = ...,
                 decorated: bool = ...,
                 default_height: int = ...,
                 default_width: int = ...,
                 deletable: bool = ...,
                 destroy_with_parent: bool = ...,
                 focus_on_map: bool = ...,
                 focus_visible: bool = ...,
                 gravity: Gdk.Gravity = ...,
                 has_resize_grip: bool = ...,
                 hide_titlebar_when_maximized: bool = ...,
                 icon: typing.Optional[GdkPixbuf.Pixbuf] = ...,
                 icon_name: typing.Optional[str] = ...,
                 mnemonics_visible: bool = ...,
                 modal: bool = ...,
                 resizable: bool = ...,
                 role: str = ...,
                 screen: Gdk.Screen = ...,
                 skip_pager_hint: bool = ...,
                 skip_taskbar_hint: bool = ...,
                 startup_id: str = ...,
                 title: str = ...,
                 transient_for: typing.Optional[Gtk.Window] = ...,
                 type: Gtk.WindowType = ...,
                 type_hint: Gdk.WindowTypeHint = ...,
                 urgency_hint: bool = ...,
                 window_position: Gtk.WindowPosition = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    def add_metadata(self, property: str) -> None: ...
    @classmethod
    def new(cls, procedure: Gimp.ExportProcedure, config: Gimp.ProcedureConfig, image: Gimp.Image) -> ExportProcedureDialog: ...
    

class ExportProcedureDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ExportProcedureDialogClass()
    """
    parent_class: ProcedureDialogClass = ...

class FileChooser(Gtk.Box, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        FileChooser(**properties)
        new(action:Gimp.FileChooserAction, label:str=None, title:str=None, file:Gio.File=None) -> Gtk.Widget

    Object GimpFileChooser

    Properties from GimpFileChooser:
      action -> GimpFileChooserAction: Action
        The action determining the chooser UI
      label -> gchararray: Label
        The label to be used next to the button
      title -> gchararray: Title
        The title to be used for the file selection popup dialog and as placeholder text in file entry.
      file -> GFile: File
        The currently selected file

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        action: Gimp.FileChooserAction
        file: Gio.File
        label: typing.Optional[str]
        title: typing.Optional[str]
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, action: Gimp.FileChooserAction = ...,
                 file: Gio.File = ...,
                 label: typing.Optional[str] = ...,
                 title: typing.Optional[str] = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_action(self) -> Gimp.FileChooserAction: ...
    def get_file(self) -> Gio.File: ...
    def get_label(self) -> typing.Optional[str]: ...
    def get_label_widget(self) -> Gtk.Widget: ...
    def get_title(self) -> typing.Optional[str]: ...
    @classmethod
    def new(cls, action: Gimp.FileChooserAction, label: typing.Optional[str] = None, title: typing.Optional[str] = None, file: typing.Optional[Gio.File] = None) -> FileChooser: ...
    def set_action(self, action: Gimp.FileChooserAction) -> None: ...
    def set_file(self, file: Gio.File) -> None: ...
    def set_label(self, text: typing.Optional[str] = None) -> None: ...
    def set_title(self, text: typing.Optional[str] = None) -> None: ...
    

class FileChooserClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FileChooserClass()
    """
    parent_class: Gtk.BoxClass = ...

class FileEntry(GObject.GPointer): ...

class FontChooser(ResourceChooser, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        FontChooser(**properties)
        new(title:str=None, label:str=None, font:Gimp.Font=None) -> Gtk.Widget

    Object GimpFontChooser

    Signals from GimpResourceChooser:
      resource-set (GObject, gboolean)

    Properties from GimpResourceChooser:
      title -> gchararray: Title
        The title to be used for the resource selection popup dialog
      label -> gchararray: Label
        The label to be used next to the button
      resource -> GimpResource: Resource
        The currently selected resource

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        label: str
        resource: Gimp.Resource
        title: str
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, label: str = ...,
                 resource: Gimp.Resource = ...,
                 title: str = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    @classmethod
    def new(cls, title: typing.Optional[str] = None, label: typing.Optional[str] = None, font: typing.Optional[Gimp.Font] = None) -> FontChooser: ...
    

class FontChooserClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FontChooserClass()
    """
    parent_class: ResourceChooserClass = ...

class Frame(Gtk.Frame, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        Frame(**properties)
        new(label:str=None) -> Gtk.Widget

    Object GimpFrame

    Properties from GtkFrame:
      label -> gchararray: Label
        Text of the frame's label
      label-xalign -> gfloat: Label xalign
        The horizontal alignment of the label
      label-yalign -> gfloat: Label yalign
        The vertical alignment of the label
      shadow-type -> GtkShadowType: Frame shadow
        Appearance of the frame border
      label-widget -> GtkWidget: Label widget
        A widget to display in place of the usual frame label

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        label: typing.Optional[str]
        label_widget: typing.Optional[Gtk.Widget]
        label_xalign: float
        label_yalign: float
        shadow_type: Gtk.ShadowType
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Frame = ...
    def __init__(self, label: typing.Optional[str] = ...,
                 label_widget: typing.Optional[Gtk.Widget] = ...,
                 label_xalign: float = ...,
                 label_yalign: float = ...,
                 shadow_type: Gtk.ShadowType = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    @classmethod
    def new(cls, label: typing.Optional[str] = None) -> Frame: ...
    

class FrameClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FrameClass()
    """
    parent_class: Gtk.FrameClass = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class GradientChooser(ResourceChooser, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        GradientChooser(**properties)
        new(title:str=None, label:str=None, gradient:Gimp.Gradient=None) -> Gtk.Widget

    Object GimpGradientChooser

    Signals from GimpResourceChooser:
      resource-set (GObject, gboolean)

    Properties from GimpResourceChooser:
      title -> gchararray: Title
        The title to be used for the resource selection popup dialog
      label -> gchararray: Label
        The label to be used next to the button
      resource -> GimpResource: Resource
        The currently selected resource

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        label: str
        resource: Gimp.Resource
        title: str
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, label: str = ...,
                 resource: Gimp.Resource = ...,
                 title: str = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    @classmethod
    def new(cls, title: typing.Optional[str] = None, label: typing.Optional[str] = None, gradient: typing.Optional[Gimp.Gradient] = None) -> GradientChooser: ...
    

class GradientChooserClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GradientChooserClass()
    """
    parent_class: ResourceChooserClass = ...

class HintBox(Gtk.Box, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        HintBox(**properties)
        new(hint:str) -> Gtk.Widget

    Object GimpHintBox

    Properties from GimpHintBox:
      icon-name -> gchararray: Icon Name
        The icon to show next to the hint
      hint -> gchararray: Hint
        The hint to display

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        hint: str
        icon_name: str
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, hint: str = ...,
                 icon_name: str = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    @classmethod
    def new(cls, hint: str) -> HintBox: ...
    

class HintBoxClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HintBoxClass()
    """
    parent_class: Gtk.BoxClass = ...

class ImageComboBox(IntComboBox, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.CellLayout):
    """
    :Constructors:

    ::

        ImageComboBox(**properties)
        new(constraint:GimpUi.ImageConstraintFunc=None) -> Gtk.Widget

    Object GimpImageComboBox

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Properties from GimpIntComboBox:
      ellipsize -> PangoEllipsizeMode: Ellipsize
        Ellipsize mode for the used text cell renderer
      label -> gchararray: Label
        An optional label to be displayed
      layout -> GimpIntComboBoxLayout: Layout
        Combo box layout
      value -> gint: Value
        Value of active item

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkComboBox:
      changed ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray

    Properties from GtkComboBox:
      model -> GtkTreeModel: ComboBox model
        The model for the combo box
      wrap-width -> gint: Wrap width
        Wrap width for laying out the items in a grid
      row-span-column -> gint: Row span column
        TreeModel column containing the row span values
      column-span-column -> gint: Column span column
        TreeModel column containing the column span values
      active -> gint: Active item
        The item which is currently active
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether dropdowns should have a tearoff menu item
      tearoff-title -> gchararray: Tearoff Title
        A title that may be displayed by the window manager when the popup is torn-off
      has-frame -> gboolean: Has Frame
        Whether the combo box draws a frame around the child
      popup-shown -> gboolean: Popup shown
        Whether the combo's dropdown is shown
      button-sensitivity -> GtkSensitivityType: Button Sensitivity
        Whether the dropdown button is sensitive when the model is empty
      has-entry -> gboolean: Has Entry
        Whether combo box has an entry
      entry-text-column -> gint: Entry Text Column
        The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE
      popup-fixed-width -> gboolean: Popup Fixed Width
        Whether the popup's width should be a fixed width matching the allocated width of the combo box
      id-column -> gint: ID Column
        The column in the combo box's model that provides string IDs for the values in the model
      active-id -> gchararray: Active id
        The value of the id column for the active row
      cell-area -> GtkCellArea: Cell Area
        The GtkCellArea used to layout cells

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        ellipsize: Pango.EllipsizeMode
        label: str
        layout: IntComboBoxLayout
        value: int
        active: int
        active_id: typing.Optional[str]
        add_tearoffs: bool
        button_sensitivity: Gtk.SensitivityType
        cell_area: Gtk.CellArea
        column_span_column: int
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        id_column: int
        model: Gtk.TreeModel
        popup_fixed_width: bool
        popup_shown: bool
        row_span_column: int
        tearoff_title: str
        wrap_width: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, ellipsize: Pango.EllipsizeMode = ...,
                 label: str = ...,
                 layout: IntComboBoxLayout = ...,
                 value: int = ...,
                 active: int = ...,
                 active_id: typing.Optional[str] = ...,
                 add_tearoffs: bool = ...,
                 button_sensitivity: Gtk.SensitivityType = ...,
                 cell_area: Gtk.CellArea = ...,
                 column_span_column: int = ...,
                 entry_text_column: int = ...,
                 has_entry: bool = ...,
                 has_frame: bool = ...,
                 id_column: int = ...,
                 model: typing.Optional[Gtk.TreeModel] = ...,
                 popup_fixed_width: bool = ...,
                 row_span_column: int = ...,
                 tearoff_title: str = ...,
                 wrap_width: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    @classmethod
    def new(cls, constraint: typing.Optional[typing.Callable[..., bool]] = None, *data: typing.Any) -> ImageComboBox: ...
    

class ImageComboBoxClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ImageComboBoxClass()
    """
    parent_class: IntComboBoxClass = ...

class IntComboBox(Gtk.ComboBox, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.CellLayout):
    """
    :Constructors:

    ::

        IntComboBox(**properties)
        new(labels:list) -> Gtk.Widget

    Object GimpIntComboBox

    Properties from GimpIntComboBox:
      ellipsize -> PangoEllipsizeMode: Ellipsize
        Ellipsize mode for the used text cell renderer
      label -> gchararray: Label
        An optional label to be displayed
      layout -> GimpIntComboBoxLayout: Layout
        Combo box layout
      value -> gint: Value
        Value of active item

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkComboBox:
      changed ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray

    Properties from GtkComboBox:
      model -> GtkTreeModel: ComboBox model
        The model for the combo box
      wrap-width -> gint: Wrap width
        Wrap width for laying out the items in a grid
      row-span-column -> gint: Row span column
        TreeModel column containing the row span values
      column-span-column -> gint: Column span column
        TreeModel column containing the column span values
      active -> gint: Active item
        The item which is currently active
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether dropdowns should have a tearoff menu item
      tearoff-title -> gchararray: Tearoff Title
        A title that may be displayed by the window manager when the popup is torn-off
      has-frame -> gboolean: Has Frame
        Whether the combo box draws a frame around the child
      popup-shown -> gboolean: Popup shown
        Whether the combo's dropdown is shown
      button-sensitivity -> GtkSensitivityType: Button Sensitivity
        Whether the dropdown button is sensitive when the model is empty
      has-entry -> gboolean: Has Entry
        Whether combo box has an entry
      entry-text-column -> gint: Entry Text Column
        The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE
      popup-fixed-width -> gboolean: Popup Fixed Width
        Whether the popup's width should be a fixed width matching the allocated width of the combo box
      id-column -> gint: ID Column
        The column in the combo box's model that provides string IDs for the values in the model
      active-id -> gchararray: Active id
        The value of the id column for the active row
      cell-area -> GtkCellArea: Cell Area
        The GtkCellArea used to layout cells

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        ellipsize: Pango.EllipsizeMode
        label: str
        layout: IntComboBoxLayout
        value: int
        active: int
        active_id: typing.Optional[str]
        add_tearoffs: bool
        button_sensitivity: Gtk.SensitivityType
        cell_area: Gtk.CellArea
        column_span_column: int
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        id_column: int
        model: Gtk.TreeModel
        popup_fixed_width: bool
        popup_shown: bool
        row_span_column: int
        tearoff_title: str
        wrap_width: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.ComboBox = ...
    def __init__(self, ellipsize: Pango.EllipsizeMode = ...,
                 label: str = ...,
                 layout: IntComboBoxLayout = ...,
                 value: int = ...,
                 active: int = ...,
                 active_id: typing.Optional[str] = ...,
                 add_tearoffs: bool = ...,
                 button_sensitivity: Gtk.SensitivityType = ...,
                 cell_area: Gtk.CellArea = ...,
                 column_span_column: int = ...,
                 entry_text_column: int = ...,
                 has_entry: bool = ...,
                 has_frame: bool = ...,
                 id_column: int = ...,
                 model: typing.Optional[Gtk.TreeModel] = ...,
                 popup_fixed_width: bool = ...,
                 row_span_column: int = ...,
                 tearoff_title: str = ...,
                 wrap_width: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    def connect(self, value: int, callback: typing.Callable[..., None], *data: typing.Any) -> int: ...
    def get_active(self) -> typing.Tuple[bool, int]: ...
    def get_active_user_data(self) -> typing.Tuple[bool, None]: ...
    def get_label(self) -> str: ...
    def get_layout(self) -> IntComboBoxLayout: ...
    @classmethod
    def new(cls, labels: typing.Sequence[str]) -> IntComboBox: ...
    def set_active(self, value: int) -> bool: ...
    def set_active_by_user_data(self, user_data: None) -> bool: ...
    def set_label(self, label: str) -> None: ...
    def set_layout(self, layout: IntComboBoxLayout) -> None: ...
    def set_sensitivity(self, func: typing.Callable[..., bool], *data: typing.Any) -> None: ...
    

class IntComboBoxClass(GObject.GPointer):
    """
    :Constructors:

    ::

        IntComboBoxClass()
    """
    parent_class: Gtk.ComboBoxClass = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class IntRadioFrame(Frame, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        IntRadioFrame(**properties)
        new(labels:list) -> Gtk.Widget
        new_from_store(title:str, store:GimpUi.IntStore) -> Gtk.Widget

    Object GimpIntRadioFrame

    Properties from GimpIntRadioFrame:
      value -> gint: Value
        Value of active item
      store -> GimpIntStore: GimpRadioFrame int store
        The int store for the radio frame

    Properties from GtkFrame:
      label -> gchararray: Label
        Text of the frame's label
      label-xalign -> gfloat: Label xalign
        The horizontal alignment of the label
      label-yalign -> gfloat: Label yalign
        The vertical alignment of the label
      shadow-type -> GtkShadowType: Frame shadow
        Appearance of the frame border
      label-widget -> GtkWidget: Label widget
        A widget to display in place of the usual frame label

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        store: IntStore
        value: int
        label: typing.Optional[str]
        label_widget: typing.Optional[Gtk.Widget]
        label_xalign: float
        label_yalign: float
        shadow_type: Gtk.ShadowType
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, store: IntStore = ...,
                 value: int = ...,
                 label: typing.Optional[str] = ...,
                 label_widget: typing.Optional[Gtk.Widget] = ...,
                 label_xalign: float = ...,
                 label_yalign: float = ...,
                 shadow_type: Gtk.ShadowType = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    def get_active(self) -> int: ...
    def get_active_user_data(self) -> typing.Tuple[bool, None]: ...
    @classmethod
    def new(cls, labels: typing.Sequence[str]) -> IntRadioFrame: ...
    @classmethod
    def new_from_store(cls, title: str, store: IntStore) -> IntRadioFrame: ...
    def set_active(self, value: int) -> bool: ...
    def set_active_by_user_data(self, user_data: None) -> bool: ...
    def set_sensitivity(self, func: typing.Callable[..., bool], *data: typing.Any) -> None: ...
    def set_title(self, title: str, with_mnemonic: bool) -> None: ...
    

class IntRadioFrameClass(GObject.GPointer):
    """
    :Constructors:

    ::

        IntRadioFrameClass()
    """
    parent_class: FrameClass = ...

class IntStore(Gtk.ListStore, Gtk.Buildable, Gtk.TreeDragDest, Gtk.TreeDragSource, Gtk.TreeModel, Gtk.TreeSortable):
    """
    :Constructors:

    ::

        IntStore(**properties)
        new(labels:list) -> Gtk.ListStore

    Object GimpIntStore

    Properties from GimpIntStore:
      user-data-type -> GType: User Data Type
        The GType of the user_data column

    Signals from GtkTreeModel:
      row-inserted (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      row-changed (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)

    Signals from GtkTreeSortable:
      sort-column-changed ()

    Signals from GtkTreeModel:
      row-inserted (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      row-changed (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)

    Signals from GtkTreeSortable:
      sort-column-changed ()

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        user_data_type: typing.Type[typing.Any]
    props: Props = ...
    parent_instance: Gtk.ListStore = ...
    def __init__(self, user_data_type: typing.Type[typing.Any] = ...) -> None: ...
    @staticmethod
    def lookup_by_user_data(model: Gtk.TreeModel, user_data: None) -> typing.Tuple[bool, Gtk.TreeIter]: ...
    @staticmethod
    def lookup_by_value(model: Gtk.TreeModel, value: int) -> typing.Tuple[bool, Gtk.TreeIter]: ...
    @classmethod
    def new(cls, labels: typing.Sequence[str]) -> IntStore: ...
    

class IntStoreClass(GObject.GPointer):
    """
    :Constructors:

    ::

        IntStoreClass()
    """
    parent_class: Gtk.ListStoreClass = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class LabelColor(Labeled, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        LabelColor(**properties)
        new(label:str, color:Gegl.Color, editable:bool) -> Gtk.Widget

    Object GimpLabelColor

    Signals from GimpLabelColor:
      value-changed ()

    Properties from GimpLabelColor:
      value -> GeglColor: Color
        The displayed color
      editable -> gboolean: Whether the color can be edited
        Whether the color can be edited

    Signals from GimpLabeled:
      mnemonic-widget-changed (GtkWidget)

    Properties from GimpLabeled:
      label -> gchararray: Label text
        The text of the label part of this widget

    Properties from GtkGrid:
      row-spacing -> gint: Row spacing
        The amount of space between two consecutive rows
      column-spacing -> gint: Column spacing
        The amount of space between two consecutive columns
      row-homogeneous -> gboolean: Row Homogeneous
        If TRUE, the rows are all the same height
      column-homogeneous -> gboolean: Column Homogeneous
        If TRUE, the columns are all the same width
      baseline-row -> gint: Baseline Row
        The row to align the to the baseline when valign is GTK_ALIGN_BASELINE

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        editable: bool
        value: Gegl.Color
        label: str
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, editable: bool = ...,
                 value: Gegl.Color = ...,
                 label: str = ...,
                 baseline_row: int = ...,
                 column_homogeneous: bool = ...,
                 column_spacing: int = ...,
                 row_homogeneous: bool = ...,
                 row_spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_color_widget(self) -> Gtk.Widget: ...
    def get_value(self) -> Gegl.Color: ...
    def is_editable(self) -> bool: ...
    @classmethod
    def new(cls, label: str, color: Gegl.Color, editable: bool) -> LabelColor: ...
    def set_editable(self, editable: bool) -> None: ...
    def set_value(self, value: Gegl.Color) -> None: ...
    

class LabelColorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LabelColorClass()
    """
    parent_class: LabeledClass = ...

class LabelEntry(Labeled, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        LabelEntry(**properties)
        new(label:str) -> Gtk.Widget

    Object GimpLabelEntry

    Signals from GimpLabelEntry:
      value-changed ()

    Properties from GimpLabelEntry:
      value -> gchararray: Entry text
        The text in the entry

    Signals from GimpLabeled:
      mnemonic-widget-changed (GtkWidget)

    Properties from GimpLabeled:
      label -> gchararray: Label text
        The text of the label part of this widget

    Properties from GtkGrid:
      row-spacing -> gint: Row spacing
        The amount of space between two consecutive rows
      column-spacing -> gint: Column spacing
        The amount of space between two consecutive columns
      row-homogeneous -> gboolean: Row Homogeneous
        If TRUE, the rows are all the same height
      column-homogeneous -> gboolean: Column Homogeneous
        If TRUE, the columns are all the same width
      baseline-row -> gint: Baseline Row
        The row to align the to the baseline when valign is GTK_ALIGN_BASELINE

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        value: str
        label: str
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, value: str = ...,
                 label: str = ...,
                 baseline_row: int = ...,
                 column_homogeneous: bool = ...,
                 column_spacing: int = ...,
                 row_homogeneous: bool = ...,
                 row_spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_entry(self) -> Gtk.Widget: ...
    def get_value(self) -> str: ...
    @classmethod
    def new(cls, label: str) -> LabelEntry: ...
    def set_value(self, value: str) -> None: ...
    

class LabelEntryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LabelEntryClass()
    """
    parent_class: LabeledClass = ...

class LabelIntWidget(Labeled, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        LabelIntWidget(**properties)
        new(text:str, widget:Gtk.Widget) -> Gtk.Widget

    Object GimpLabelIntWidget

    Signals from GimpLabelIntWidget:
      value-changed ()

    Properties from GimpLabelIntWidget:
      value -> gint: value
        Current value
      widget -> GtkWidget: widget
        Integer widget

    Signals from GimpLabeled:
      mnemonic-widget-changed (GtkWidget)

    Properties from GimpLabeled:
      label -> gchararray: Label text
        The text of the label part of this widget

    Properties from GtkGrid:
      row-spacing -> gint: Row spacing
        The amount of space between two consecutive rows
      column-spacing -> gint: Column spacing
        The amount of space between two consecutive columns
      row-homogeneous -> gboolean: Row Homogeneous
        If TRUE, the rows are all the same height
      column-homogeneous -> gboolean: Column Homogeneous
        If TRUE, the columns are all the same width
      baseline-row -> gint: Baseline Row
        The row to align the to the baseline when valign is GTK_ALIGN_BASELINE

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        value: int
        widget: Gtk.Widget
        label: str
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, value: int = ...,
                 widget: Gtk.Widget = ...,
                 label: str = ...,
                 baseline_row: int = ...,
                 column_homogeneous: bool = ...,
                 column_spacing: int = ...,
                 row_homogeneous: bool = ...,
                 row_spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_widget(self) -> Gtk.Widget: ...
    @classmethod
    def new(cls, text: str, widget: Gtk.Widget) -> LabelIntWidget: ...
    

class LabelIntWidgetClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LabelIntWidgetClass()
    """
    parent_class: LabeledClass = ...

class LabelSpin(Labeled, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        LabelSpin(**properties)
        new(text:str, value:float, lower:float, upper:float, digits:int) -> Gtk.Widget

    Object GimpLabelSpin

    Signals from GimpLabelSpin:
      value-changed ()

    Properties from GimpLabelSpin:
      value -> gdouble: value
        Current value
      lower -> gdouble: lower
        Minimum value
      upper -> gdouble: upper
        Max value
      digits -> gint: digits
        The number of decimal places to display

    Signals from GimpLabeled:
      mnemonic-widget-changed (GtkWidget)

    Properties from GimpLabeled:
      label -> gchararray: Label text
        The text of the label part of this widget

    Properties from GtkGrid:
      row-spacing -> gint: Row spacing
        The amount of space between two consecutive rows
      column-spacing -> gint: Column spacing
        The amount of space between two consecutive columns
      row-homogeneous -> gboolean: Row Homogeneous
        If TRUE, the rows are all the same height
      column-homogeneous -> gboolean: Column Homogeneous
        If TRUE, the columns are all the same width
      baseline-row -> gint: Baseline Row
        The row to align the to the baseline when valign is GTK_ALIGN_BASELINE

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        digits: int
        lower: float
        upper: float
        value: float
        label: str
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Labeled = ...
    def __init__(self, digits: int = ...,
                 lower: float = ...,
                 upper: float = ...,
                 value: float = ...,
                 label: str = ...,
                 baseline_row: int = ...,
                 column_homogeneous: bool = ...,
                 column_spacing: int = ...,
                 row_homogeneous: bool = ...,
                 row_spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def do_value_changed(self) -> None: ...
    def get_spin_button(self) -> Gtk.Widget: ...
    def get_value(self) -> float: ...
    @classmethod
    def new(cls, text: str, value: float, lower: float, upper: float, digits: int) -> LabelSpin: ...
    def set_digits(self, digits: int) -> None: ...
    def set_increments(self, step: float, page: float) -> None: ...
    def set_value(self, value: float) -> None: ...
    

class LabelSpinClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LabelSpinClass()
    """
    parent_class: LabeledClass = ...
    value_changed: typing.Callable[[LabelSpin], None] = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class LabelStringWidget(Labeled, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        LabelStringWidget(**properties)
        new(text:str, widget:Gtk.Widget) -> Gtk.Widget

    Object GimpLabelStringWidget

    Signals from GimpLabelStringWidget:
      value-changed ()

    Properties from GimpLabelStringWidget:
      value -> gchararray: value
        Current value
      widget -> GtkWidget: widget
        String widget

    Signals from GimpLabeled:
      mnemonic-widget-changed (GtkWidget)

    Properties from GimpLabeled:
      label -> gchararray: Label text
        The text of the label part of this widget

    Properties from GtkGrid:
      row-spacing -> gint: Row spacing
        The amount of space between two consecutive rows
      column-spacing -> gint: Column spacing
        The amount of space between two consecutive columns
      row-homogeneous -> gboolean: Row Homogeneous
        If TRUE, the rows are all the same height
      column-homogeneous -> gboolean: Column Homogeneous
        If TRUE, the columns are all the same width
      baseline-row -> gint: Baseline Row
        The row to align the to the baseline when valign is GTK_ALIGN_BASELINE

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        value: str
        widget: Gtk.Widget
        label: str
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, value: str = ...,
                 widget: Gtk.Widget = ...,
                 label: str = ...,
                 baseline_row: int = ...,
                 column_homogeneous: bool = ...,
                 column_spacing: int = ...,
                 row_homogeneous: bool = ...,
                 row_spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_widget(self) -> Gtk.Widget: ...
    @classmethod
    def new(cls, text: str, widget: Gtk.Widget) -> LabelStringWidget: ...
    

class LabelStringWidgetClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LabelStringWidgetClass()
    """
    parent_class: LabeledClass = ...

class Labeled(Gtk.Grid, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        Labeled(**properties)

    Object GimpLabeled

    Signals from GimpLabeled:
      mnemonic-widget-changed (GtkWidget)

    Properties from GimpLabeled:
      label -> gchararray: Label text
        The text of the label part of this widget

    Properties from GtkGrid:
      row-spacing -> gint: Row spacing
        The amount of space between two consecutive rows
      column-spacing -> gint: Column spacing
        The amount of space between two consecutive columns
      row-homogeneous -> gboolean: Row Homogeneous
        If TRUE, the rows are all the same height
      column-homogeneous -> gboolean: Column Homogeneous
        If TRUE, the columns are all the same width
      baseline-row -> gint: Baseline Row
        The row to align the to the baseline when valign is GTK_ALIGN_BASELINE

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        label: str
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Grid = ...
    def __init__(self, label: str = ...,
                 baseline_row: int = ...,
                 column_homogeneous: bool = ...,
                 column_spacing: int = ...,
                 row_homogeneous: bool = ...,
                 row_spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def do_mnemonic_widget_changed(self, widget: Gtk.Widget) -> None: ...
    def get_label(self) -> Gtk.Label: ...
    def get_text(self) -> str: ...
    def set_text(self, text: str) -> None: ...
    

class LabeledClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LabeledClass()
    """
    parent_class: Gtk.GridClass = ...
    mnemonic_widget_changed: typing.Callable[[Labeled, Gtk.Widget], None] = ...
    populate: None = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class LayerComboBox(IntComboBox, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.CellLayout):
    """
    :Constructors:

    ::

        LayerComboBox(**properties)
        new(constraint:GimpUi.ItemConstraintFunc=None) -> Gtk.Widget

    Object GimpLayerComboBox

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Properties from GimpIntComboBox:
      ellipsize -> PangoEllipsizeMode: Ellipsize
        Ellipsize mode for the used text cell renderer
      label -> gchararray: Label
        An optional label to be displayed
      layout -> GimpIntComboBoxLayout: Layout
        Combo box layout
      value -> gint: Value
        Value of active item

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkComboBox:
      changed ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray

    Properties from GtkComboBox:
      model -> GtkTreeModel: ComboBox model
        The model for the combo box
      wrap-width -> gint: Wrap width
        Wrap width for laying out the items in a grid
      row-span-column -> gint: Row span column
        TreeModel column containing the row span values
      column-span-column -> gint: Column span column
        TreeModel column containing the column span values
      active -> gint: Active item
        The item which is currently active
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether dropdowns should have a tearoff menu item
      tearoff-title -> gchararray: Tearoff Title
        A title that may be displayed by the window manager when the popup is torn-off
      has-frame -> gboolean: Has Frame
        Whether the combo box draws a frame around the child
      popup-shown -> gboolean: Popup shown
        Whether the combo's dropdown is shown
      button-sensitivity -> GtkSensitivityType: Button Sensitivity
        Whether the dropdown button is sensitive when the model is empty
      has-entry -> gboolean: Has Entry
        Whether combo box has an entry
      entry-text-column -> gint: Entry Text Column
        The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE
      popup-fixed-width -> gboolean: Popup Fixed Width
        Whether the popup's width should be a fixed width matching the allocated width of the combo box
      id-column -> gint: ID Column
        The column in the combo box's model that provides string IDs for the values in the model
      active-id -> gchararray: Active id
        The value of the id column for the active row
      cell-area -> GtkCellArea: Cell Area
        The GtkCellArea used to layout cells

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        ellipsize: Pango.EllipsizeMode
        label: str
        layout: IntComboBoxLayout
        value: int
        active: int
        active_id: typing.Optional[str]
        add_tearoffs: bool
        button_sensitivity: Gtk.SensitivityType
        cell_area: Gtk.CellArea
        column_span_column: int
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        id_column: int
        model: Gtk.TreeModel
        popup_fixed_width: bool
        popup_shown: bool
        row_span_column: int
        tearoff_title: str
        wrap_width: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, ellipsize: Pango.EllipsizeMode = ...,
                 label: str = ...,
                 layout: IntComboBoxLayout = ...,
                 value: int = ...,
                 active: int = ...,
                 active_id: typing.Optional[str] = ...,
                 add_tearoffs: bool = ...,
                 button_sensitivity: Gtk.SensitivityType = ...,
                 cell_area: Gtk.CellArea = ...,
                 column_span_column: int = ...,
                 entry_text_column: int = ...,
                 has_entry: bool = ...,
                 has_frame: bool = ...,
                 id_column: int = ...,
                 model: typing.Optional[Gtk.TreeModel] = ...,
                 popup_fixed_width: bool = ...,
                 row_span_column: int = ...,
                 tearoff_title: str = ...,
                 wrap_width: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    @classmethod
    def new(cls, constraint: typing.Optional[typing.Callable[..., bool]] = None, *data: typing.Any) -> LayerComboBox: ...
    

class MemsizeEntry(Gtk.Box, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        MemsizeEntry(**properties)
        new(value:int, lower:int, upper:int) -> Gtk.Widget

    Object GimpMemsizeEntry

    Signals from GimpMemsizeEntry:
      value-changed ()

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_spinbutton(self) -> Gtk.SpinButton: ...
    def get_value(self) -> int: ...
    @classmethod
    def new(cls, value: int, lower: int, upper: int) -> MemsizeEntry: ...
    def set_value(self, value: int) -> None: ...
    

class MemsizeEntryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MemsizeEntryClass()
    """
    parent_class: Gtk.BoxClass = ...

class NumberPairEntry(Gtk.Entry, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.Editable):
    """
    :Constructors:

    ::

        NumberPairEntry(**properties)
        new(separators:str, allow_simplification:bool, min_valid_value:float, max_valid_value:float) -> Gtk.Widget

    Object GimpNumberPairEntry

    Signals from GimpNumberPairEntry:
      numbers-changed ()
      ratio-changed ()

    Properties from GimpNumberPairEntry:
      left-number -> gdouble: Left number
        The left number
      right-number -> gdouble: Right number
        The right number
      default-left-number -> gdouble: Default left number
        The default left number
      default-right-number -> gdouble: Default right number
        The default right number
      user-override -> gboolean: User override
        Whether the widget is in 'user override' mode
      separators -> gchararray: Separators
        A string of valid separators
      default-text -> gchararray: Default text
        String to show when in automatic mode
      allow-simplification -> gboolean: Allow simplification
        Whether to allow simplification
      min-valid-value -> gdouble: Min valid value
        Minimum value valid when parsing input
      max-valid-value -> gdouble: Max valid value
        Maximum value valid when parsing input
      ratio -> gdouble: Ratio
        The value as ratio
      aspect -> GimpAspectType: Aspect
        The value as aspect

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkEntry:
      activate ()
      populate-popup (GtkWidget)
      move-cursor (GtkMovementStep, gint, gboolean)
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      icon-press (GtkEntryIconPosition, GdkEvent)
      icon-release (GtkEntryIconPosition, GdkEvent)
      preedit-changed (gchararray)
      insert-emoji ()

    Properties from GtkEntry:
      buffer -> GtkEntryBuffer: Text Buffer
        Text buffer object which actually stores entry text
      cursor-position -> gint: Cursor Position
        The current position of the insertion cursor in chars
      selection-bound -> gint: Selection Bound
        The position of the opposite end of the selection from the cursor in chars
      editable -> gboolean: Editable
        Whether the entry contents can be edited
      max-length -> gint: Maximum length
        Maximum number of characters for this entry. Zero if no maximum
      visibility -> gboolean: Visibility
        FALSE displays the "invisible char" instead of the actual text (password mode)
      has-frame -> gboolean: Has Frame
        FALSE removes outside bevel from entry
      inner-border -> GtkBorder: Inner Border
        Border between text and frame. Overrides the inner-border style property
      invisible-char -> guint: Invisible character
        The character to use when masking entry contents (in "password mode")
      activates-default -> gboolean: Activates default
        Whether to activate the default widget (such as the default button in a dialog) when Enter is pressed
      width-chars -> gint: Width in chars
        Number of characters to leave space for in the entry
      max-width-chars -> gint: Maximum width in characters
        The desired maximum width of the entry, in characters
      scroll-offset -> gint: Scroll offset
        Number of pixels of the entry scrolled off the screen to the left
      text -> gchararray: Text
        The contents of the entry
      xalign -> gfloat: X align
        The horizontal alignment, from 0 (left) to 1 (right). Reversed for RTL layouts.
      truncate-multiline -> gboolean: Truncate multiline
        Whether to truncate multiline pastes to one line.
      shadow-type -> GtkShadowType: Shadow type
        Which kind of shadow to draw around the entry when has-frame is set
      overwrite-mode -> gboolean: Overwrite mode
        Whether new text overwrites existing text
      text-length -> guint: Text length
        Length of the text currently in the entry
      invisible-char-set -> gboolean: Invisible character set
        Whether the invisible character has been set
      caps-lock-warning -> gboolean: Caps Lock warning
        Whether password entries will show a warning when Caps Lock is on
      progress-fraction -> gdouble: Progress Fraction
        The current fraction of the task that's been completed
      progress-pulse-step -> gdouble: Progress Pulse Step
        The fraction of total entry width to move the progress bouncing block for each call to gtk_entry_progress_pulse()
      primary-icon-pixbuf -> GdkPixbuf: Primary pixbuf
        Primary pixbuf for the entry
      secondary-icon-pixbuf -> GdkPixbuf: Secondary pixbuf
        Secondary pixbuf for the entry
      primary-icon-stock -> gchararray: Primary stock ID
        Stock ID for primary icon
      secondary-icon-stock -> gchararray: Secondary stock ID
        Stock ID for secondary icon
      primary-icon-name -> gchararray: Primary icon name
        Icon name for primary icon
      secondary-icon-name -> gchararray: Secondary icon name
        Icon name for secondary icon
      primary-icon-gicon -> GIcon: Primary GIcon
        GIcon for primary icon
      secondary-icon-gicon -> GIcon: Secondary GIcon
        GIcon for secondary icon
      primary-icon-storage-type -> GtkImageType: Primary storage type
        The representation being used for primary icon
      secondary-icon-storage-type -> GtkImageType: Secondary storage type
        The representation being used for secondary icon
      primary-icon-activatable -> gboolean: Primary icon activatable
        Whether the primary icon is activatable
      secondary-icon-activatable -> gboolean: Secondary icon activatable
        Whether the secondary icon is activatable
      primary-icon-sensitive -> gboolean: Primary icon sensitive
        Whether the primary icon is sensitive
      secondary-icon-sensitive -> gboolean: Secondary icon sensitive
        Whether the secondary icon is sensitive
      primary-icon-tooltip-text -> gchararray: Primary icon tooltip text
        The contents of the tooltip on the primary icon
      secondary-icon-tooltip-text -> gchararray: Secondary icon tooltip text
        The contents of the tooltip on the secondary icon
      primary-icon-tooltip-markup -> gchararray: Primary icon tooltip markup
        The contents of the tooltip on the primary icon
      secondary-icon-tooltip-markup -> gchararray: Secondary icon tooltip markup
        The contents of the tooltip on the secondary icon
      im-module -> gchararray: IM module
        Which IM module should be used
      placeholder-text -> gchararray: Placeholder text
        Show text in the entry when it's empty and unfocused
      completion -> GtkEntryCompletion: Completion
        The auxiliary completion object
      input-purpose -> GtkInputPurpose: Purpose
        Purpose of the text field
      input-hints -> GtkInputHints: hints
        Hints for the text field behaviour
      attributes -> PangoAttrList: Attributes
        A list of style attributes to apply to the text of the label
      populate-all -> gboolean: Populate all
        Whether to emit ::populate-popup for touch popups
      tabs -> PangoTabArray: Tabs
        A list of tabstop locations to apply to the text of the entry
      show-emoji-icon -> gboolean: Emoji icon
        Whether to show an icon for Emoji
      enable-emoji-completion -> gboolean: Enable Emoji completion
        Whether to suggest Emoji replacements

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        allow_simplification: bool
        aspect: AspectType
        default_left_number: float
        default_right_number: float
        default_text: typing.Optional[str]
        left_number: float
        max_valid_value: float
        min_valid_value: float
        ratio: float
        right_number: float
        separators: str
        user_override: bool
        activates_default: bool
        attributes: typing.Optional[Pango.AttrList]
        buffer: Gtk.EntryBuffer
        caps_lock_warning: bool
        completion: Gtk.EntryCompletion
        cursor_position: int
        editable: bool
        enable_emoji_completion: bool
        has_frame: bool
        im_module: str
        inner_border: typing.Optional[Gtk.Border]
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        invisible_char: int
        invisible_char_set: bool
        max_length: int
        max_width_chars: int
        overwrite_mode: bool
        placeholder_text: str
        populate_all: bool
        primary_icon_activatable: bool
        primary_icon_gicon: Gio.Icon
        primary_icon_name: str
        primary_icon_pixbuf: GdkPixbuf.Pixbuf
        primary_icon_sensitive: bool
        primary_icon_stock: str
        primary_icon_storage_type: Gtk.ImageType
        primary_icon_tooltip_markup: str
        primary_icon_tooltip_text: str
        progress_fraction: float
        progress_pulse_step: float
        scroll_offset: int
        secondary_icon_activatable: bool
        secondary_icon_gicon: Gio.Icon
        secondary_icon_name: str
        secondary_icon_pixbuf: GdkPixbuf.Pixbuf
        secondary_icon_sensitive: bool
        secondary_icon_stock: str
        secondary_icon_storage_type: Gtk.ImageType
        secondary_icon_tooltip_markup: str
        secondary_icon_tooltip_text: str
        selection_bound: int
        shadow_type: Gtk.ShadowType
        show_emoji_icon: bool
        tabs: typing.Optional[Pango.TabArray]
        text: str
        text_length: int
        truncate_multiline: bool
        visibility: bool
        width_chars: int
        xalign: float
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
    props: Props = ...
    def __init__(self, allow_simplification: bool = ...,
                 aspect: AspectType = ...,
                 default_left_number: float = ...,
                 default_right_number: float = ...,
                 default_text: str = ...,
                 left_number: float = ...,
                 max_valid_value: float = ...,
                 min_valid_value: float = ...,
                 ratio: float = ...,
                 right_number: float = ...,
                 separators: str = ...,
                 user_override: bool = ...,
                 activates_default: bool = ...,
                 attributes: Pango.AttrList = ...,
                 buffer: Gtk.EntryBuffer = ...,
                 caps_lock_warning: bool = ...,
                 completion: typing.Optional[Gtk.EntryCompletion] = ...,
                 editable: bool = ...,
                 enable_emoji_completion: bool = ...,
                 has_frame: bool = ...,
                 im_module: str = ...,
                 inner_border: typing.Optional[Gtk.Border] = ...,
                 input_hints: Gtk.InputHints = ...,
                 input_purpose: Gtk.InputPurpose = ...,
                 invisible_char: int = ...,
                 invisible_char_set: bool = ...,
                 max_length: int = ...,
                 max_width_chars: int = ...,
                 overwrite_mode: bool = ...,
                 placeholder_text: typing.Optional[str] = ...,
                 populate_all: bool = ...,
                 primary_icon_activatable: bool = ...,
                 primary_icon_gicon: Gio.Icon = ...,
                 primary_icon_name: str = ...,
                 primary_icon_pixbuf: GdkPixbuf.Pixbuf = ...,
                 primary_icon_sensitive: bool = ...,
                 primary_icon_stock: str = ...,
                 primary_icon_tooltip_markup: str = ...,
                 primary_icon_tooltip_text: str = ...,
                 progress_fraction: float = ...,
                 progress_pulse_step: float = ...,
                 secondary_icon_activatable: bool = ...,
                 secondary_icon_gicon: Gio.Icon = ...,
                 secondary_icon_name: str = ...,
                 secondary_icon_pixbuf: GdkPixbuf.Pixbuf = ...,
                 secondary_icon_sensitive: bool = ...,
                 secondary_icon_stock: str = ...,
                 secondary_icon_tooltip_markup: str = ...,
                 secondary_icon_tooltip_text: str = ...,
                 shadow_type: Gtk.ShadowType = ...,
                 show_emoji_icon: bool = ...,
                 tabs: Pango.TabArray = ...,
                 text: str = ...,
                 truncate_multiline: bool = ...,
                 visibility: bool = ...,
                 width_chars: int = ...,
                 xalign: float = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    def get_aspect(self) -> AspectType: ...
    def get_default_text(self) -> typing.Optional[str]: ...
    def get_default_values(self) -> typing.Tuple[float, float]: ...
    def get_ratio(self) -> float: ...
    def get_user_override(self) -> bool: ...
    def get_values(self) -> typing.Tuple[float, float]: ...
    @classmethod
    def new(cls, separators: str, allow_simplification: bool, min_valid_value: float, max_valid_value: float) -> NumberPairEntry: ...
    def set_aspect(self, aspect: AspectType) -> None: ...
    def set_default_text(self, string: str) -> None: ...
    def set_default_values(self, left: float, right: float) -> None: ...
    def set_ratio(self, ratio: float) -> None: ...
    def set_user_override(self, user_override: bool) -> None: ...
    def set_values(self, left: float, right: float) -> None: ...
    

class NumberPairEntryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NumberPairEntryClass()
    """
    parent_class: Gtk.EntryClass = ...

class OffsetArea(Gtk.DrawingArea, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        OffsetArea(**properties)
        new(orig_width:int, orig_height:int) -> Gtk.Widget

    Object GimpOffsetArea

    Signals from GimpOffsetArea:
      offsets-changed (gint, gint)

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
    props: Props = ...
    def __init__(self, app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    @classmethod
    def new(cls, orig_width: int, orig_height: int) -> OffsetArea: ...
    def set_offsets(self, offset_x: int, offset_y: int) -> None: ...
    def set_pixbuf(self, pixbuf: GdkPixbuf.Pixbuf) -> None: ...
    def set_size(self, width: int, height: int) -> None: ...
    

class OffsetAreaClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OffsetAreaClass()
    """
    parent_class: Gtk.DrawingAreaClass = ...

class PageSelector(Gtk.Box, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        PageSelector(**properties)
        new() -> Gtk.Widget

    Object GimpPageSelector

    Signals from GimpPageSelector:
      selection-changed ()
      activate ()

    Properties from GimpPageSelector:
      n-pages -> gint: N Pages
        The number of pages to open
      target -> GimpPageSelectorTarget: Target
        the target to open to

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        n_pages: int
        target: PageSelectorTarget
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, n_pages: int = ...,
                 target: PageSelectorTarget = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_n_pages(self) -> int: ...
    def get_page_label(self, page_no: int) -> typing.Optional[str]: ...
    def get_page_thumbnail(self, page_no: int) -> typing.Optional[GdkPixbuf.Pixbuf]: ...
    def get_selected_pages(self) -> list[int]: ...
    def get_selected_range(self) -> str: ...
    def get_target(self) -> PageSelectorTarget: ...
    @classmethod
    def new(cls) -> PageSelector: ...
    def page_is_selected(self, page_no: int) -> bool: ...
    def select_all(self) -> None: ...
    def select_page(self, page_no: int) -> None: ...
    def select_range(self, range: str) -> None: ...
    def set_n_pages(self, n_pages: int) -> None: ...
    def set_page_label(self, page_no: int, label: str) -> None: ...
    def set_page_thumbnail(self, page_no: int, thumbnail: GdkPixbuf.Pixbuf) -> None: ...
    def set_target(self, target: PageSelectorTarget) -> None: ...
    def unselect_all(self) -> None: ...
    def unselect_page(self, page_no: int) -> None: ...
    

class PageSelectorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PageSelectorClass()
    """
    parent_class: Gtk.BoxClass = ...

class PaletteChooser(ResourceChooser, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        PaletteChooser(**properties)
        new(title:str=None, label:str=None, palette:Gimp.Palette=None) -> Gtk.Widget

    Object GimpPaletteChooser

    Signals from GimpResourceChooser:
      resource-set (GObject, gboolean)

    Properties from GimpResourceChooser:
      title -> gchararray: Title
        The title to be used for the resource selection popup dialog
      label -> gchararray: Label
        The label to be used next to the button
      resource -> GimpResource: Resource
        The currently selected resource

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        label: str
        resource: Gimp.Resource
        title: str
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, label: str = ...,
                 resource: Gimp.Resource = ...,
                 title: str = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    @classmethod
    def new(cls, title: typing.Optional[str] = None, label: typing.Optional[str] = None, palette: typing.Optional[Gimp.Palette] = None) -> PaletteChooser: ...
    

class PaletteChooserClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PaletteChooserClass()
    """
    parent_class: ResourceChooserClass = ...

class PathComboBox(IntComboBox, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.CellLayout):
    """
    :Constructors:

    ::

        PathComboBox(**properties)
        new(constraint:GimpUi.ItemConstraintFunc=None) -> Gtk.Widget

    Object GimpPathComboBox

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Properties from GimpIntComboBox:
      ellipsize -> PangoEllipsizeMode: Ellipsize
        Ellipsize mode for the used text cell renderer
      label -> gchararray: Label
        An optional label to be displayed
      layout -> GimpIntComboBoxLayout: Layout
        Combo box layout
      value -> gint: Value
        Value of active item

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkComboBox:
      changed ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray

    Properties from GtkComboBox:
      model -> GtkTreeModel: ComboBox model
        The model for the combo box
      wrap-width -> gint: Wrap width
        Wrap width for laying out the items in a grid
      row-span-column -> gint: Row span column
        TreeModel column containing the row span values
      column-span-column -> gint: Column span column
        TreeModel column containing the column span values
      active -> gint: Active item
        The item which is currently active
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether dropdowns should have a tearoff menu item
      tearoff-title -> gchararray: Tearoff Title
        A title that may be displayed by the window manager when the popup is torn-off
      has-frame -> gboolean: Has Frame
        Whether the combo box draws a frame around the child
      popup-shown -> gboolean: Popup shown
        Whether the combo's dropdown is shown
      button-sensitivity -> GtkSensitivityType: Button Sensitivity
        Whether the dropdown button is sensitive when the model is empty
      has-entry -> gboolean: Has Entry
        Whether combo box has an entry
      entry-text-column -> gint: Entry Text Column
        The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE
      popup-fixed-width -> gboolean: Popup Fixed Width
        Whether the popup's width should be a fixed width matching the allocated width of the combo box
      id-column -> gint: ID Column
        The column in the combo box's model that provides string IDs for the values in the model
      active-id -> gchararray: Active id
        The value of the id column for the active row
      cell-area -> GtkCellArea: Cell Area
        The GtkCellArea used to layout cells

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        ellipsize: Pango.EllipsizeMode
        label: str
        layout: IntComboBoxLayout
        value: int
        active: int
        active_id: typing.Optional[str]
        add_tearoffs: bool
        button_sensitivity: Gtk.SensitivityType
        cell_area: Gtk.CellArea
        column_span_column: int
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        id_column: int
        model: Gtk.TreeModel
        popup_fixed_width: bool
        popup_shown: bool
        row_span_column: int
        tearoff_title: str
        wrap_width: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, ellipsize: Pango.EllipsizeMode = ...,
                 label: str = ...,
                 layout: IntComboBoxLayout = ...,
                 value: int = ...,
                 active: int = ...,
                 active_id: typing.Optional[str] = ...,
                 add_tearoffs: bool = ...,
                 button_sensitivity: Gtk.SensitivityType = ...,
                 cell_area: Gtk.CellArea = ...,
                 column_span_column: int = ...,
                 entry_text_column: int = ...,
                 has_entry: bool = ...,
                 has_frame: bool = ...,
                 id_column: int = ...,
                 model: typing.Optional[Gtk.TreeModel] = ...,
                 popup_fixed_width: bool = ...,
                 row_span_column: int = ...,
                 tearoff_title: str = ...,
                 wrap_width: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    @classmethod
    def new(cls, constraint: typing.Optional[typing.Callable[..., bool]] = None, *data: typing.Any) -> PathComboBox: ...
    

class PathEditor(Gtk.Box, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        PathEditor(**properties)
        new(title:str, path:str=None) -> Gtk.Widget

    Object GimpPathEditor

    Signals from GimpPathEditor:
      path-changed ()
      writable-changed ()

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_dir_writable(self, directory: str) -> bool: ...
    def get_path(self) -> str: ...
    def get_writable_path(self) -> str: ...
    @classmethod
    def new(cls, title: str, path: typing.Optional[str] = None) -> PathEditor: ...
    def set_dir_writable(self, directory: str, writable: bool) -> None: ...
    def set_path(self, path: str) -> None: ...
    def set_writable_path(self, path: str) -> None: ...
    

class PathEditorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PathEditorClass()
    """
    parent_class: Gtk.BoxClass = ...

class PatternChooser(ResourceChooser, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        PatternChooser(**properties)
        new(title:str=None, label:str=None, pattern:Gimp.Pattern=None) -> Gtk.Widget

    Object GimpPatternChooser

    Signals from GimpResourceChooser:
      resource-set (GObject, gboolean)

    Properties from GimpResourceChooser:
      title -> gchararray: Title
        The title to be used for the resource selection popup dialog
      label -> gchararray: Label
        The label to be used next to the button
      resource -> GimpResource: Resource
        The currently selected resource

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        label: str
        resource: Gimp.Resource
        title: str
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, label: str = ...,
                 resource: Gimp.Resource = ...,
                 title: str = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    @classmethod
    def new(cls, title: typing.Optional[str] = None, label: typing.Optional[str] = None, pattern: typing.Optional[Gimp.Pattern] = None) -> PatternChooser: ...
    

class PatternChooserClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PatternChooserClass()
    """
    parent_class: ResourceChooserClass = ...

class PickButton(Gtk.Button, Atk.ImplementorIface, Gtk.Actionable, Gtk.Activatable, Gtk.Buildable):
    """
    :Constructors:

    ::

        PickButton(**properties)
        new() -> Gtk.Widget

    Object GimpPickButton

    Signals from GimpPickButton:
      color-picked (GeglColor)

    Signals from GtkButton:
      activate ()
      pressed ()
      released ()
      clicked ()
      enter ()
      leave ()

    Properties from GtkButton:
      label -> gchararray: Label
        Text of the label widget inside the button, if the button contains a label widget
      image -> GtkWidget: Image widget
        Child widget to appear next to the button text
      relief -> GtkReliefStyle: Border relief
        The border relief style
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key
      use-stock -> gboolean: Use stock
        If set, the label is used to pick a stock item instead of being displayed
      xalign -> gfloat: Horizontal alignment for child
        Horizontal position of child in available space. 0.0 is left aligned, 1.0 is right aligned
      yalign -> gfloat: Vertical alignment for child
        Vertical position of child in available space. 0.0 is top aligned, 1.0 is bottom aligned
      image-position -> GtkPositionType: Image position
        The position of the image relative to the text
      always-show-image -> gboolean: Always show image
        Whether the image will always be shown

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        always_show_image: bool
        image: typing.Optional[Gtk.Widget]
        image_position: Gtk.PositionType
        label: str
        relief: Gtk.ReliefStyle
        use_stock: bool
        use_underline: bool
        xalign: float
        yalign: float
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        action_name: typing.Optional[str]
        action_target: GLib.Variant
        related_action: Gtk.Action
        use_action_appearance: bool
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Button = ...
    def __init__(self, always_show_image: bool = ...,
                 image: typing.Optional[Gtk.Widget] = ...,
                 image_position: Gtk.PositionType = ...,
                 label: str = ...,
                 relief: Gtk.ReliefStyle = ...,
                 use_stock: bool = ...,
                 use_underline: bool = ...,
                 xalign: float = ...,
                 yalign: float = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 action_name: typing.Optional[str] = ...,
                 action_target: GLib.Variant = ...,
                 related_action: Gtk.Action = ...,
                 use_action_appearance: bool = ...) -> None: ...
    def do_color_picked(self, color: Gegl.Color) -> None: ...
    @classmethod
    def new(cls) -> PickButton: ...
    

class PickButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PickButtonClass()
    """
    parent_class: Gtk.ButtonClass = ...
    color_picked: typing.Callable[[PickButton, Gegl.Color], None] = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class Preview(Gtk.Box, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        Preview(**properties)

    Object GimpPreview

    Signals from GimpPreview:
      invalidated ()

    Properties from GimpPreview:
      update -> gboolean: Update
        Whether the preview should update automatically

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        update: bool
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Box = ...
    def __init__(self, update: bool = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def do_draw_buffer(self, buffer: typing.Sequence[int], rowstride: int) -> None: ...
    def do_draw_thumb(self, area: PreviewArea, width: int, height: int) -> None: ...
    def do_invalidated(self) -> None: ...
    def do_set_cursor(self) -> None: ...
    def do_transform(self, src_x: int, src_y: int) -> typing.Tuple[int, int]: ...
    def do_untransform(self, src_x: int, src_y: int) -> typing.Tuple[int, int]: ...
    def draw(self) -> None: ...
    def draw_buffer(self, buffer: typing.Sequence[int], rowstride: int) -> None: ...
    def get_area(self) -> PreviewArea: ...
    def get_bounds(self) -> typing.Tuple[int, int, int, int]: ...
    def get_controls(self) -> Gtk.Box: ...
    def get_default_cursor(self) -> Gdk.Cursor: ...
    def get_frame(self) -> Gtk.AspectFrame: ...
    def get_grid(self) -> Gtk.Grid: ...
    def get_offsets(self) -> typing.Tuple[int, int]: ...
    def get_position(self) -> typing.Tuple[int, int]: ...
    def get_size(self) -> typing.Tuple[int, int]: ...
    def get_update(self) -> bool: ...
    def invalidate(self) -> None: ...
    def set_bounds(self, xmin: int, ymin: int, xmax: int, ymax: int) -> None: ...
    def set_default_cursor(self, cursor: Gdk.Cursor) -> None: ...
    def set_offsets(self, xoff: int, yoff: int) -> None: ...
    def set_size(self, width: int, height: int) -> None: ...
    def set_update(self, update: bool) -> None: ...
    def transform(self, src_x: int, src_y: int) -> typing.Tuple[int, int]: ...
    def untransform(self, src_x: int, src_y: int) -> typing.Tuple[int, int]: ...
    

class PreviewArea(Gtk.DrawingArea, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        PreviewArea(**properties)
        new() -> Gtk.Widget

    Object GimpPreviewArea

    Properties from GimpPreviewArea:
      check-size -> GimpCheckSize: Check Size
        The size of the checkerboard pattern indicating transparency
      check-type -> GimpCheckType: Check Style
        The colors of the checkerboard pattern indicating transparency
      check-custom-color1 -> GeglColor: Custom Checks Color 1
        The first color of the checkerboard pattern indicating transparency
      check-custom-color2 -> GeglColor: Custom Checks Color 2
        The second color of the checkerboard pattern indicating transparency

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        check_custom_color1: Gegl.Color
        check_custom_color2: Gegl.Color
        check_size: Gimp.CheckSize
        check_type: Gimp.CheckType
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
    props: Props = ...
    def __init__(self, check_custom_color1: Gegl.Color = ...,
                 check_custom_color2: Gegl.Color = ...,
                 check_size: Gimp.CheckSize = ...,
                 check_type: Gimp.CheckType = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    def blend(self, x: int, y: int, width: int, height: int, type: Gimp.ImageType, buf1: typing.Sequence[int], rowstride1: int, buf2: typing.Sequence[int], rowstride2: int, opacity: int) -> None: ...
    def draw(self, x: int, y: int, width: int, height: int, type: Gimp.ImageType, buf: typing.Sequence[int], rowstride: int) -> None: ...
    def fill(self, x: int, y: int, width: int, height: int, red: int, green: int, blue: int) -> None: ...
    def get_size(self) -> typing.Tuple[int, int]: ...
    def mask(self, x: int, y: int, width: int, height: int, type: Gimp.ImageType, buf1: typing.Sequence[int], rowstride1: int, buf2: typing.Sequence[int], rowstride2: int, mask: typing.Sequence[int], rowstride_mask: int) -> None: ...
    def menu_popup(self, event: typing.Optional[Gdk.EventButton] = None) -> None: ...
    @classmethod
    def new(cls) -> PreviewArea: ...
    def reset(self) -> None: ...
    def set_color_config(self, config: Gimp.ColorConfig) -> None: ...
    def set_colormap(self, colormap: typing.Sequence[int], num_colors: int) -> None: ...
    def set_max_size(self, width: int, height: int) -> None: ...
    def set_offsets(self, x: int, y: int) -> None: ...
    

class PreviewAreaClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PreviewAreaClass()
    """
    parent_class: Gtk.DrawingAreaClass = ...

class PreviewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PreviewClass()
    """
    parent_class: Gtk.BoxClass = ...
    draw: typing.Callable[[Preview], None] = ...
    draw_thumb: typing.Callable[[Preview, PreviewArea, int, int], None] = ...
    draw_buffer: typing.Callable[[Preview, typing.Sequence[int], int], None] = ...
    set_cursor: typing.Callable[[Preview], None] = ...
    transform: typing.Callable[[Preview, int, int], typing.Tuple[int, int]] = ...
    untransform: typing.Callable[[Preview, int, int], typing.Tuple[int, int]] = ...
    invalidated: typing.Callable[[Preview], None] = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class ProcBrowserDialog(Dialog, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        ProcBrowserDialog(**properties)

    Object GimpProcBrowserDialog

    Signals from GimpProcBrowserDialog:
      selection-changed ()
      row-activated ()

    Properties from GimpDialog:
      help-func -> gpointer: Help Func
        The help function to call when F1 is hit
      help-id -> gchararray: Help ID
        The help ID to pass to help-func
      parent -> GtkWidget: Parent
        The dialog's parent widget

    Signals from GtkDialog:
      response (gint)
      close ()

    Properties from GtkDialog:
      use-header-bar -> gint: Use Header Bar
        Use Header Bar for actions.

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        help_func: None
        help_id: str
        use_header_bar: int
        accept_focus: bool
        application: typing.Optional[Gtk.Application]
        attached_to: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: typing.Optional[GdkPixbuf.Pixbuf]
        icon_name: typing.Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: typing.Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: typing.Optional[str]
        transient_for: typing.Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        startup_id: str
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, help_func: None = ...,
                 help_id: str = ...,
                 parent: Gtk.Widget = ...,
                 use_header_bar: int = ...,
                 accept_focus: bool = ...,
                 application: typing.Optional[Gtk.Application] = ...,
                 attached_to: typing.Optional[Gtk.Widget] = ...,
                 decorated: bool = ...,
                 default_height: int = ...,
                 default_width: int = ...,
                 deletable: bool = ...,
                 destroy_with_parent: bool = ...,
                 focus_on_map: bool = ...,
                 focus_visible: bool = ...,
                 gravity: Gdk.Gravity = ...,
                 has_resize_grip: bool = ...,
                 hide_titlebar_when_maximized: bool = ...,
                 icon: typing.Optional[GdkPixbuf.Pixbuf] = ...,
                 icon_name: typing.Optional[str] = ...,
                 mnemonics_visible: bool = ...,
                 modal: bool = ...,
                 resizable: bool = ...,
                 role: str = ...,
                 screen: Gdk.Screen = ...,
                 skip_pager_hint: bool = ...,
                 skip_taskbar_hint: bool = ...,
                 startup_id: str = ...,
                 title: str = ...,
                 transient_for: typing.Optional[Gtk.Window] = ...,
                 type: Gtk.WindowType = ...,
                 type_hint: Gdk.WindowTypeHint = ...,
                 urgency_hint: bool = ...,
                 window_position: Gtk.WindowPosition = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    def get_selected(self) -> typing.Optional[str]: ...
    

class ProcBrowserDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProcBrowserDialogClass()
    """
    parent_class: DialogClass = ...

class ProcedureDialog(Dialog, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        ProcedureDialog(**properties)
        new(procedure:Gimp.Procedure, config:Gimp.ProcedureConfig, title:str=None) -> Gtk.Widget

    Object GimpProcedureDialog

    Properties from GimpProcedureDialog:
      procedure -> GimpProcedure: Procedure
        The GimpProcedure this dialog is used with
      config -> GimpProcedureConfig: Config
        The GimpProcedureConfig this dialog is editing

    Properties from GimpDialog:
      help-func -> gpointer: Help Func
        The help function to call when F1 is hit
      help-id -> gchararray: Help ID
        The help ID to pass to help-func
      parent -> GtkWidget: Parent
        The dialog's parent widget

    Signals from GtkDialog:
      response (gint)
      close ()

    Properties from GtkDialog:
      use-header-bar -> gint: Use Header Bar
        Use Header Bar for actions.

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        config: Gimp.ProcedureConfig
        procedure: Gimp.Procedure
        help_func: None
        help_id: str
        use_header_bar: int
        accept_focus: bool
        application: typing.Optional[Gtk.Application]
        attached_to: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: typing.Optional[GdkPixbuf.Pixbuf]
        icon_name: typing.Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: typing.Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: typing.Optional[str]
        transient_for: typing.Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        startup_id: str
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Dialog = ...
    def __init__(self, config: Gimp.ProcedureConfig = ...,
                 procedure: Gimp.Procedure = ...,
                 help_func: None = ...,
                 help_id: str = ...,
                 parent: Gtk.Widget = ...,
                 use_header_bar: int = ...,
                 accept_focus: bool = ...,
                 application: typing.Optional[Gtk.Application] = ...,
                 attached_to: typing.Optional[Gtk.Widget] = ...,
                 decorated: bool = ...,
                 default_height: int = ...,
                 default_width: int = ...,
                 deletable: bool = ...,
                 destroy_with_parent: bool = ...,
                 focus_on_map: bool = ...,
                 focus_visible: bool = ...,
                 gravity: Gdk.Gravity = ...,
                 has_resize_grip: bool = ...,
                 hide_titlebar_when_maximized: bool = ...,
                 icon: typing.Optional[GdkPixbuf.Pixbuf] = ...,
                 icon_name: typing.Optional[str] = ...,
                 mnemonics_visible: bool = ...,
                 modal: bool = ...,
                 resizable: bool = ...,
                 role: str = ...,
                 screen: Gdk.Screen = ...,
                 skip_pager_hint: bool = ...,
                 skip_taskbar_hint: bool = ...,
                 startup_id: str = ...,
                 title: str = ...,
                 transient_for: typing.Optional[Gtk.Window] = ...,
                 type: Gtk.WindowType = ...,
                 type_hint: Gdk.WindowTypeHint = ...,
                 urgency_hint: bool = ...,
                 window_position: Gtk.WindowPosition = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    def do_fill_end(self, procedure: Gimp.Procedure, config: Gimp.ProcedureConfig) -> None: ...
    def do_fill_start(self, procedure: Gimp.Procedure, config: Gimp.ProcedureConfig) -> None: ...
    def fill(self, properties: typing.Optional[list[str]] = None) -> None: ...
    def fill_box(self, container_id: str, properties: typing.Optional[list[str]] = None) -> Gtk.Widget: ...
    def fill_expander(self, container_id: str, title_id: typing.Optional[str], invert_title: bool, contents_id: typing.Optional[str] = None) -> Gtk.Widget: ...
    def fill_flowbox(self, container_id: str, properties: typing.Optional[list[str]] = None) -> Gtk.Widget: ...
    def fill_frame(self, container_id: str, title_id: typing.Optional[str], invert_title: bool, contents_id: typing.Optional[str] = None) -> Gtk.Widget: ...
    def fill_notebook(self, container_id: str, label_list: list[str], page_list: list[str]) -> Gtk.Widget: ...
    def fill_paned(self, container_id: str, orientation: Gtk.Orientation, child1_id: typing.Optional[str] = None, child2_id: typing.Optional[str] = None) -> Gtk.Widget: ...
    def fill_scrolled_window(self, container_id: str, contents_id: str) -> Gtk.Widget: ...
    def get_color_widget(self, property: str, editable: bool, type: ColorAreaType) -> Gtk.Widget: ...
    def get_drawable_preview(self, preview_id: str, drawable: Gimp.Drawable) -> Gtk.Widget: ...
    def get_int_combo(self, property: str, store: IntStore) -> Gtk.Widget: ...
    def get_int_radio(self, property: str, store: IntStore) -> Gtk.Widget: ...
    def get_label(self, label_id: str, text: str, is_markup: bool, with_mnemonic: bool) -> Gtk.Widget: ...
    def get_scale_entry(self, property: str, factor: float) -> Gtk.Widget: ...
    def get_size_entry(self, property: str, property_is_pixel: bool, unit_property: str, unit_format: str, update_policy: SizeEntryUpdatePolicy, resolution: float) -> Gtk.Widget: ...
    def get_spin_scale(self, property: str, factor: float) -> Gtk.Widget: ...
    def get_widget(self, property: str, widget_type: typing.Type[typing.Any]) -> Gtk.Widget: ...
    @classmethod
    def new(cls, procedure: Gimp.Procedure, config: Gimp.ProcedureConfig, title: typing.Optional[str] = None) -> ProcedureDialog: ...
    def run(self) -> bool: ...
    def set_ok_label(self, ok_label: str) -> None: ...
    def set_sensitive(self, property: str, sensitive: bool, config: typing.Optional[GObject.Object], config_property: typing.Optional[str], config_invert: bool) -> None: ...
    def set_sensitive_if_in(self, property: str, config: typing.Optional[GObject.Object], config_property: str, values: Gimp.ValueArray, in_values: bool) -> None: ...
    

class ProcedureDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProcedureDialogClass()
    """
    parent_class: DialogClass = ...
    fill_start: typing.Callable[[ProcedureDialog, Gimp.Procedure, Gimp.ProcedureConfig], None] = ...
    fill_end: typing.Callable[[ProcedureDialog, Gimp.Procedure, Gimp.ProcedureConfig], None] = ...
    fill_list: None = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class ProgressBar(Gtk.ProgressBar, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        ProgressBar(**properties)
        new() -> Gtk.Widget

    Object GimpProgressBar

    Properties from GtkProgressBar:
      fraction -> gdouble: Fraction
        The fraction of total work that has been completed
      pulse-step -> gdouble: Pulse Step
        The fraction of total progress to move the bouncing block when pulsed
      inverted -> gboolean: Inverted
        Invert the direction in which the progress bar grows
      text -> gchararray: Text
        Text to be displayed in the progress bar
      show-text -> gboolean: Show text
        Whether the progress is shown as text.
      ellipsize -> PangoEllipsizeMode: Ellipsize
        The preferred place to ellipsize the string, if the progress bar does not have enough room to display the entire string, if at all.

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        ellipsize: Pango.EllipsizeMode
        fraction: float
        inverted: bool
        pulse_step: float
        show_text: bool
        text: typing.Optional[str]
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(self, ellipsize: Pango.EllipsizeMode = ...,
                 fraction: float = ...,
                 inverted: bool = ...,
                 pulse_step: float = ...,
                 show_text: bool = ...,
                 text: typing.Optional[str] = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    @classmethod
    def new(cls) -> ProgressBar: ...
    

class ProgressBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProgressBarClass()
    """
    parent_class: Gtk.ProgressBarClass = ...

class ResourceChooser(Gtk.Box, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        ResourceChooser(**properties)

    Object GimpResourceChooser

    Signals from GimpResourceChooser:
      resource-set (GObject, gboolean)

    Properties from GimpResourceChooser:
      title -> gchararray: Title
        The title to be used for the resource selection popup dialog
      label -> gchararray: Label
        The label to be used next to the button
      resource -> GimpResource: Resource
        The currently selected resource

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        label: str
        resource: Gimp.Resource
        title: str
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Box = ...
    def __init__(self, label: str = ...,
                 resource: Gimp.Resource = ...,
                 title: str = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def do_draw_interior(self) -> None: ...
    def do_resource_set(self, resource: Gimp.Resource, dialog_closing: bool) -> None: ...
    def get_label(self) -> Gtk.Widget: ...
    def get_resource(self) -> Gimp.Resource: ...
    def set_resource(self, resource: Gimp.Resource) -> None: ...
    

class ResourceChooserClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ResourceChooserClass()
    """
    parent_class: Gtk.BoxClass = ...
    resource_set: typing.Callable[[ResourceChooser, Gimp.Resource, bool], None] = ...
    draw_interior: typing.Callable[[ResourceChooser], None] = ...
    resource_type: typing.Type[typing.Any] = ...
    padding: list[None] = ...

class Ruler(Gtk.Widget, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        Ruler(**properties)
        new(orientation:Gtk.Orientation) -> Gtk.Widget

    Object GimpRuler

    Properties from GimpRuler:
      orientation -> GtkOrientation: Orientation
        The orientation of the ruler
      unit -> GimpUnit: Unit
        Unit of ruler
      lower -> gdouble: Lower
        Lower limit of ruler
      upper -> gdouble: Upper
        Upper limit of ruler
      position -> gdouble: Position
        Position of mark on the ruler
      max-size -> gdouble: Max Size
        Maximum size of the ruler

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        lower: float
        max_size: float
        orientation: Gtk.Orientation
        position: float
        unit: Gimp.Unit
        upper: float
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
    props: Props = ...
    def __init__(self, lower: float = ...,
                 max_size: float = ...,
                 orientation: Gtk.Orientation = ...,
                 position: float = ...,
                 unit: Gimp.Unit = ...,
                 upper: float = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    def add_track_widget(self, widget: Gtk.Widget) -> None: ...
    def get_position(self) -> float: ...
    def get_range(self) -> typing.Tuple[float, float, float]: ...
    def get_unit(self) -> Gimp.Unit: ...
    @classmethod
    def new(cls, orientation: Gtk.Orientation) -> Ruler: ...
    def remove_track_widget(self, widget: Gtk.Widget) -> None: ...
    def set_position(self, position: float) -> None: ...
    def set_range(self, lower: float, upper: float, max_size: float) -> None: ...
    def set_unit(self, unit: Gimp.Unit) -> None: ...
    

class RulerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RulerClass()
    """
    parent_class: Gtk.WidgetClass = ...

class ScaleEntry(LabelSpin, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        ScaleEntry(**properties)
        new(text:str, value:float, lower:float, upper:float, digits:int) -> Gtk.Widget

    Object GimpScaleEntry

    Signals from GimpLabelSpin:
      value-changed ()

    Properties from GimpLabelSpin:
      value -> gdouble: value
        Current value
      lower -> gdouble: lower
        Minimum value
      upper -> gdouble: upper
        Max value
      digits -> gint: digits
        The number of decimal places to display

    Signals from GimpLabeled:
      mnemonic-widget-changed (GtkWidget)

    Properties from GimpLabeled:
      label -> gchararray: Label text
        The text of the label part of this widget

    Properties from GtkGrid:
      row-spacing -> gint: Row spacing
        The amount of space between two consecutive rows
      column-spacing -> gint: Column spacing
        The amount of space between two consecutive columns
      row-homogeneous -> gboolean: Row Homogeneous
        If TRUE, the rows are all the same height
      column-homogeneous -> gboolean: Column Homogeneous
        If TRUE, the columns are all the same width
      baseline-row -> gint: Baseline Row
        The row to align the to the baseline when valign is GTK_ALIGN_BASELINE

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        digits: int
        lower: float
        upper: float
        value: float
        label: str
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    parent_instance: LabelSpin = ...
    def __init__(self, digits: int = ...,
                 lower: float = ...,
                 upper: float = ...,
                 value: float = ...,
                 label: str = ...,
                 baseline_row: int = ...,
                 column_homogeneous: bool = ...,
                 column_spacing: int = ...,
                 row_homogeneous: bool = ...,
                 row_spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_logarithmic(self) -> bool: ...
    def get_range(self) -> Gtk.Range: ...
    @classmethod
    def new(cls, text: str, value: float, lower: float, upper: float, digits: int) -> ScaleEntry: ...
    def set_bounds(self, lower: float, upper: float, limit_scale: bool) -> None: ...
    def set_logarithmic(self, logarithmic: bool) -> None: ...
    

class ScaleEntryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ScaleEntryClass()
    """
    parent_class: LabelSpinClass = ...
    new_range_widget: None = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class ScrolledPreview(Preview, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        ScrolledPreview(**properties)

    Object GimpScrolledPreview

    Signals from GimpPreview:
      invalidated ()

    Properties from GimpPreview:
      update -> gboolean: Update
        Whether the preview should update automatically

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        update: bool
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Preview = ...
    def __init__(self, update: bool = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def freeze(self) -> None: ...
    def get_adjustments(self) -> typing.Tuple[Gtk.Adjustment, Gtk.Adjustment]: ...
    def set_policy(self, hscrollbar_policy: Gtk.PolicyType, vscrollbar_policy: Gtk.PolicyType) -> None: ...
    def set_position(self, x: int, y: int) -> None: ...
    def thaw(self) -> None: ...
    

class ScrolledPreviewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ScrolledPreviewClass()
    """
    parent_class: PreviewClass = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class SizeEntry(Gtk.Grid, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        SizeEntry(**properties)
        new(number_of_fields:int, unit:Gimp.Unit, unit_format:str, menu_show_pixels:bool, menu_show_percent:bool, show_refval:bool, spinbutton_width:int, update_policy:GimpUi.SizeEntryUpdatePolicy) -> Gtk.Widget

    Object GimpSizeEntry

    Signals from GimpSizeEntry:
      value-changed ()
      refval-changed ()
      unit-changed ()

    Properties from GtkGrid:
      row-spacing -> gint: Row spacing
        The amount of space between two consecutive rows
      column-spacing -> gint: Column spacing
        The amount of space between two consecutive columns
      row-homogeneous -> gboolean: Row Homogeneous
        If TRUE, the rows are all the same height
      column-homogeneous -> gboolean: Column Homogeneous
        If TRUE, the columns are all the same width
      baseline-row -> gint: Baseline Row
        The row to align the to the baseline when valign is GTK_ALIGN_BASELINE

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, baseline_row: int = ...,
                 column_homogeneous: bool = ...,
                 column_spacing: int = ...,
                 row_homogeneous: bool = ...,
                 row_spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def add_field(self, value_spinbutton: Gtk.SpinButton, refval_spinbutton: typing.Optional[Gtk.SpinButton] = None) -> None: ...
    def attach_label(self, text: str, row: int, column: int, alignment: float) -> Gtk.Widget: ...
    def get_help_widget(self, field: int) -> Gtk.Widget: ...
    def get_n_fields(self) -> int: ...
    def get_refval(self, field: int) -> float: ...
    def get_unit(self) -> Gimp.Unit: ...
    def get_unit_combo(self) -> UnitComboBox: ...
    def get_update_policy(self) -> SizeEntryUpdatePolicy: ...
    def get_value(self, field: int) -> float: ...
    def grab_focus(self) -> None: ...
    @classmethod
    def new(cls, number_of_fields: int, unit: Gimp.Unit, unit_format: str, menu_show_pixels: bool, menu_show_percent: bool, show_refval: bool, spinbutton_width: int, update_policy: SizeEntryUpdatePolicy) -> SizeEntry: ...
    def set_activates_default(self, setting: bool) -> None: ...
    def set_pixel_digits(self, digits: int) -> None: ...
    def set_refval(self, field: int, refval: float) -> None: ...
    def set_refval_boundaries(self, field: int, lower: float, upper: float) -> None: ...
    def set_refval_digits(self, field: int, digits: int) -> None: ...
    def set_resolution(self, field: int, resolution: float, keep_size: bool) -> None: ...
    def set_size(self, field: int, lower: float, upper: float) -> None: ...
    def set_unit(self, unit: Gimp.Unit) -> None: ...
    def set_value(self, field: int, value: float) -> None: ...
    def set_value_boundaries(self, field: int, lower: float, upper: float) -> None: ...
    def show_unit_menu(self, show: bool) -> None: ...
    

class SizeEntryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SizeEntryClass()
    """
    parent_class: Gtk.GridClass = ...

class SpinButton(Gtk.SpinButton, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.Editable, Gtk.Orientable):
    """
    :Constructors:

    ::

        SpinButton(**properties)
        new(adjustment:Gtk.Adjustment=None, climb_rate:float, digits:int) -> Gtk.Widget
        new_with_range(min:float, max:float, step:float) -> Gtk.Widget

    Object GimpSpinButton

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkSpinButton:
      value-changed ()
      change-value (GtkScrollType)
      input (gpointer) -> gint
      output () -> gboolean
      wrapped ()

    Properties from GtkSpinButton:
      adjustment -> GtkAdjustment: Adjustment
        The adjustment that holds the value of the spin button
      climb-rate -> gdouble: Climb Rate
        The acceleration rate when you hold down a button or key
      digits -> guint: Digits
        The number of decimal places to display
      snap-to-ticks -> gboolean: Snap to Ticks
        Whether erroneous values are automatically changed to a spin button's nearest step increment
      numeric -> gboolean: Numeric
        Whether non-numeric characters should be ignored
      wrap -> gboolean: Wrap
        Whether a spin button should wrap upon reaching its limits
      update-policy -> GtkSpinButtonUpdatePolicy: Update Policy
        Whether the spin button should update always, or only when the value is legal
      value -> gdouble: Value
        Reads the current value, or sets a new value

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkEntry:
      activate ()
      populate-popup (GtkWidget)
      move-cursor (GtkMovementStep, gint, gboolean)
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      icon-press (GtkEntryIconPosition, GdkEvent)
      icon-release (GtkEntryIconPosition, GdkEvent)
      preedit-changed (gchararray)
      insert-emoji ()

    Properties from GtkEntry:
      buffer -> GtkEntryBuffer: Text Buffer
        Text buffer object which actually stores entry text
      cursor-position -> gint: Cursor Position
        The current position of the insertion cursor in chars
      selection-bound -> gint: Selection Bound
        The position of the opposite end of the selection from the cursor in chars
      editable -> gboolean: Editable
        Whether the entry contents can be edited
      max-length -> gint: Maximum length
        Maximum number of characters for this entry. Zero if no maximum
      visibility -> gboolean: Visibility
        FALSE displays the "invisible char" instead of the actual text (password mode)
      has-frame -> gboolean: Has Frame
        FALSE removes outside bevel from entry
      inner-border -> GtkBorder: Inner Border
        Border between text and frame. Overrides the inner-border style property
      invisible-char -> guint: Invisible character
        The character to use when masking entry contents (in "password mode")
      activates-default -> gboolean: Activates default
        Whether to activate the default widget (such as the default button in a dialog) when Enter is pressed
      width-chars -> gint: Width in chars
        Number of characters to leave space for in the entry
      max-width-chars -> gint: Maximum width in characters
        The desired maximum width of the entry, in characters
      scroll-offset -> gint: Scroll offset
        Number of pixels of the entry scrolled off the screen to the left
      text -> gchararray: Text
        The contents of the entry
      xalign -> gfloat: X align
        The horizontal alignment, from 0 (left) to 1 (right). Reversed for RTL layouts.
      truncate-multiline -> gboolean: Truncate multiline
        Whether to truncate multiline pastes to one line.
      shadow-type -> GtkShadowType: Shadow type
        Which kind of shadow to draw around the entry when has-frame is set
      overwrite-mode -> gboolean: Overwrite mode
        Whether new text overwrites existing text
      text-length -> guint: Text length
        Length of the text currently in the entry
      invisible-char-set -> gboolean: Invisible character set
        Whether the invisible character has been set
      caps-lock-warning -> gboolean: Caps Lock warning
        Whether password entries will show a warning when Caps Lock is on
      progress-fraction -> gdouble: Progress Fraction
        The current fraction of the task that's been completed
      progress-pulse-step -> gdouble: Progress Pulse Step
        The fraction of total entry width to move the progress bouncing block for each call to gtk_entry_progress_pulse()
      primary-icon-pixbuf -> GdkPixbuf: Primary pixbuf
        Primary pixbuf for the entry
      secondary-icon-pixbuf -> GdkPixbuf: Secondary pixbuf
        Secondary pixbuf for the entry
      primary-icon-stock -> gchararray: Primary stock ID
        Stock ID for primary icon
      secondary-icon-stock -> gchararray: Secondary stock ID
        Stock ID for secondary icon
      primary-icon-name -> gchararray: Primary icon name
        Icon name for primary icon
      secondary-icon-name -> gchararray: Secondary icon name
        Icon name for secondary icon
      primary-icon-gicon -> GIcon: Primary GIcon
        GIcon for primary icon
      secondary-icon-gicon -> GIcon: Secondary GIcon
        GIcon for secondary icon
      primary-icon-storage-type -> GtkImageType: Primary storage type
        The representation being used for primary icon
      secondary-icon-storage-type -> GtkImageType: Secondary storage type
        The representation being used for secondary icon
      primary-icon-activatable -> gboolean: Primary icon activatable
        Whether the primary icon is activatable
      secondary-icon-activatable -> gboolean: Secondary icon activatable
        Whether the secondary icon is activatable
      primary-icon-sensitive -> gboolean: Primary icon sensitive
        Whether the primary icon is sensitive
      secondary-icon-sensitive -> gboolean: Secondary icon sensitive
        Whether the secondary icon is sensitive
      primary-icon-tooltip-text -> gchararray: Primary icon tooltip text
        The contents of the tooltip on the primary icon
      secondary-icon-tooltip-text -> gchararray: Secondary icon tooltip text
        The contents of the tooltip on the secondary icon
      primary-icon-tooltip-markup -> gchararray: Primary icon tooltip markup
        The contents of the tooltip on the primary icon
      secondary-icon-tooltip-markup -> gchararray: Secondary icon tooltip markup
        The contents of the tooltip on the secondary icon
      im-module -> gchararray: IM module
        Which IM module should be used
      placeholder-text -> gchararray: Placeholder text
        Show text in the entry when it's empty and unfocused
      completion -> GtkEntryCompletion: Completion
        The auxiliary completion object
      input-purpose -> GtkInputPurpose: Purpose
        Purpose of the text field
      input-hints -> GtkInputHints: hints
        Hints for the text field behaviour
      attributes -> PangoAttrList: Attributes
        A list of style attributes to apply to the text of the label
      populate-all -> gboolean: Populate all
        Whether to emit ::populate-popup for touch popups
      tabs -> PangoTabArray: Tabs
        A list of tabstop locations to apply to the text of the entry
      show-emoji-icon -> gboolean: Emoji icon
        Whether to show an icon for Emoji
      enable-emoji-completion -> gboolean: Enable Emoji completion
        Whether to suggest Emoji replacements

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        adjustment: Gtk.Adjustment
        climb_rate: float
        digits: int
        numeric: bool
        snap_to_ticks: bool
        update_policy: Gtk.SpinButtonUpdatePolicy
        value: float
        wrap: bool
        activates_default: bool
        attributes: typing.Optional[Pango.AttrList]
        buffer: Gtk.EntryBuffer
        caps_lock_warning: bool
        completion: Gtk.EntryCompletion
        cursor_position: int
        editable: bool
        enable_emoji_completion: bool
        has_frame: bool
        im_module: str
        inner_border: typing.Optional[Gtk.Border]
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        invisible_char: int
        invisible_char_set: bool
        max_length: int
        max_width_chars: int
        overwrite_mode: bool
        placeholder_text: str
        populate_all: bool
        primary_icon_activatable: bool
        primary_icon_gicon: Gio.Icon
        primary_icon_name: str
        primary_icon_pixbuf: GdkPixbuf.Pixbuf
        primary_icon_sensitive: bool
        primary_icon_stock: str
        primary_icon_storage_type: Gtk.ImageType
        primary_icon_tooltip_markup: str
        primary_icon_tooltip_text: str
        progress_fraction: float
        progress_pulse_step: float
        scroll_offset: int
        secondary_icon_activatable: bool
        secondary_icon_gicon: Gio.Icon
        secondary_icon_name: str
        secondary_icon_pixbuf: GdkPixbuf.Pixbuf
        secondary_icon_sensitive: bool
        secondary_icon_stock: str
        secondary_icon_storage_type: Gtk.ImageType
        secondary_icon_tooltip_markup: str
        secondary_icon_tooltip_text: str
        selection_bound: int
        shadow_type: Gtk.ShadowType
        show_emoji_icon: bool
        tabs: typing.Optional[Pango.TabArray]
        text: str
        text_length: int
        truncate_multiline: bool
        visibility: bool
        width_chars: int
        xalign: float
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        orientation: Gtk.Orientation
    props: Props = ...
    parent_instance: Gtk.SpinButton = ...
    def __init__(self, adjustment: Gtk.Adjustment = ...,
                 climb_rate: float = ...,
                 digits: int = ...,
                 numeric: bool = ...,
                 snap_to_ticks: bool = ...,
                 update_policy: Gtk.SpinButtonUpdatePolicy = ...,
                 value: float = ...,
                 wrap: bool = ...,
                 activates_default: bool = ...,
                 attributes: Pango.AttrList = ...,
                 buffer: Gtk.EntryBuffer = ...,
                 caps_lock_warning: bool = ...,
                 completion: typing.Optional[Gtk.EntryCompletion] = ...,
                 editable: bool = ...,
                 enable_emoji_completion: bool = ...,
                 has_frame: bool = ...,
                 im_module: str = ...,
                 inner_border: typing.Optional[Gtk.Border] = ...,
                 input_hints: Gtk.InputHints = ...,
                 input_purpose: Gtk.InputPurpose = ...,
                 invisible_char: int = ...,
                 invisible_char_set: bool = ...,
                 max_length: int = ...,
                 max_width_chars: int = ...,
                 overwrite_mode: bool = ...,
                 placeholder_text: typing.Optional[str] = ...,
                 populate_all: bool = ...,
                 primary_icon_activatable: bool = ...,
                 primary_icon_gicon: Gio.Icon = ...,
                 primary_icon_name: str = ...,
                 primary_icon_pixbuf: GdkPixbuf.Pixbuf = ...,
                 primary_icon_sensitive: bool = ...,
                 primary_icon_stock: str = ...,
                 primary_icon_tooltip_markup: str = ...,
                 primary_icon_tooltip_text: str = ...,
                 progress_fraction: float = ...,
                 progress_pulse_step: float = ...,
                 secondary_icon_activatable: bool = ...,
                 secondary_icon_gicon: Gio.Icon = ...,
                 secondary_icon_name: str = ...,
                 secondary_icon_pixbuf: GdkPixbuf.Pixbuf = ...,
                 secondary_icon_sensitive: bool = ...,
                 secondary_icon_stock: str = ...,
                 secondary_icon_tooltip_markup: str = ...,
                 secondary_icon_tooltip_text: str = ...,
                 shadow_type: Gtk.ShadowType = ...,
                 show_emoji_icon: bool = ...,
                 tabs: Pango.TabArray = ...,
                 text: str = ...,
                 truncate_multiline: bool = ...,
                 visibility: bool = ...,
                 width_chars: int = ...,
                 xalign: float = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    @classmethod
    def new(cls, adjustment: typing.Optional[Gtk.Adjustment], climb_rate: float, digits: int) -> SpinButton: ...
    @classmethod
    def new_with_range(cls, min: float, max: float, step: float) -> SpinButton: ...
    

class SpinButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SpinButtonClass()
    """
    parent_class: Gtk.SpinButtonClass = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class SpinScale(SpinButton, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.Editable, Gtk.Orientable):
    """
    :Constructors:

    ::

        SpinScale(**properties)
        new(adjustment:Gtk.Adjustment, label:str, digits:int) -> Gtk.Widget

    Object GimpSpinScale

    Properties from GimpSpinScale:
      label -> gchararray: label

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkSpinButton:
      value-changed ()
      change-value (GtkScrollType)
      input (gpointer) -> gint
      output () -> gboolean
      wrapped ()

    Properties from GtkSpinButton:
      adjustment -> GtkAdjustment: Adjustment
        The adjustment that holds the value of the spin button
      climb-rate -> gdouble: Climb Rate
        The acceleration rate when you hold down a button or key
      digits -> guint: Digits
        The number of decimal places to display
      snap-to-ticks -> gboolean: Snap to Ticks
        Whether erroneous values are automatically changed to a spin button's nearest step increment
      numeric -> gboolean: Numeric
        Whether non-numeric characters should be ignored
      wrap -> gboolean: Wrap
        Whether a spin button should wrap upon reaching its limits
      update-policy -> GtkSpinButtonUpdatePolicy: Update Policy
        Whether the spin button should update always, or only when the value is legal
      value -> gdouble: Value
        Reads the current value, or sets a new value

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkEntry:
      activate ()
      populate-popup (GtkWidget)
      move-cursor (GtkMovementStep, gint, gboolean)
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      icon-press (GtkEntryIconPosition, GdkEvent)
      icon-release (GtkEntryIconPosition, GdkEvent)
      preedit-changed (gchararray)
      insert-emoji ()

    Properties from GtkEntry:
      buffer -> GtkEntryBuffer: Text Buffer
        Text buffer object which actually stores entry text
      cursor-position -> gint: Cursor Position
        The current position of the insertion cursor in chars
      selection-bound -> gint: Selection Bound
        The position of the opposite end of the selection from the cursor in chars
      editable -> gboolean: Editable
        Whether the entry contents can be edited
      max-length -> gint: Maximum length
        Maximum number of characters for this entry. Zero if no maximum
      visibility -> gboolean: Visibility
        FALSE displays the "invisible char" instead of the actual text (password mode)
      has-frame -> gboolean: Has Frame
        FALSE removes outside bevel from entry
      inner-border -> GtkBorder: Inner Border
        Border between text and frame. Overrides the inner-border style property
      invisible-char -> guint: Invisible character
        The character to use when masking entry contents (in "password mode")
      activates-default -> gboolean: Activates default
        Whether to activate the default widget (such as the default button in a dialog) when Enter is pressed
      width-chars -> gint: Width in chars
        Number of characters to leave space for in the entry
      max-width-chars -> gint: Maximum width in characters
        The desired maximum width of the entry, in characters
      scroll-offset -> gint: Scroll offset
        Number of pixels of the entry scrolled off the screen to the left
      text -> gchararray: Text
        The contents of the entry
      xalign -> gfloat: X align
        The horizontal alignment, from 0 (left) to 1 (right). Reversed for RTL layouts.
      truncate-multiline -> gboolean: Truncate multiline
        Whether to truncate multiline pastes to one line.
      shadow-type -> GtkShadowType: Shadow type
        Which kind of shadow to draw around the entry when has-frame is set
      overwrite-mode -> gboolean: Overwrite mode
        Whether new text overwrites existing text
      text-length -> guint: Text length
        Length of the text currently in the entry
      invisible-char-set -> gboolean: Invisible character set
        Whether the invisible character has been set
      caps-lock-warning -> gboolean: Caps Lock warning
        Whether password entries will show a warning when Caps Lock is on
      progress-fraction -> gdouble: Progress Fraction
        The current fraction of the task that's been completed
      progress-pulse-step -> gdouble: Progress Pulse Step
        The fraction of total entry width to move the progress bouncing block for each call to gtk_entry_progress_pulse()
      primary-icon-pixbuf -> GdkPixbuf: Primary pixbuf
        Primary pixbuf for the entry
      secondary-icon-pixbuf -> GdkPixbuf: Secondary pixbuf
        Secondary pixbuf for the entry
      primary-icon-stock -> gchararray: Primary stock ID
        Stock ID for primary icon
      secondary-icon-stock -> gchararray: Secondary stock ID
        Stock ID for secondary icon
      primary-icon-name -> gchararray: Primary icon name
        Icon name for primary icon
      secondary-icon-name -> gchararray: Secondary icon name
        Icon name for secondary icon
      primary-icon-gicon -> GIcon: Primary GIcon
        GIcon for primary icon
      secondary-icon-gicon -> GIcon: Secondary GIcon
        GIcon for secondary icon
      primary-icon-storage-type -> GtkImageType: Primary storage type
        The representation being used for primary icon
      secondary-icon-storage-type -> GtkImageType: Secondary storage type
        The representation being used for secondary icon
      primary-icon-activatable -> gboolean: Primary icon activatable
        Whether the primary icon is activatable
      secondary-icon-activatable -> gboolean: Secondary icon activatable
        Whether the secondary icon is activatable
      primary-icon-sensitive -> gboolean: Primary icon sensitive
        Whether the primary icon is sensitive
      secondary-icon-sensitive -> gboolean: Secondary icon sensitive
        Whether the secondary icon is sensitive
      primary-icon-tooltip-text -> gchararray: Primary icon tooltip text
        The contents of the tooltip on the primary icon
      secondary-icon-tooltip-text -> gchararray: Secondary icon tooltip text
        The contents of the tooltip on the secondary icon
      primary-icon-tooltip-markup -> gchararray: Primary icon tooltip markup
        The contents of the tooltip on the primary icon
      secondary-icon-tooltip-markup -> gchararray: Secondary icon tooltip markup
        The contents of the tooltip on the secondary icon
      im-module -> gchararray: IM module
        Which IM module should be used
      placeholder-text -> gchararray: Placeholder text
        Show text in the entry when it's empty and unfocused
      completion -> GtkEntryCompletion: Completion
        The auxiliary completion object
      input-purpose -> GtkInputPurpose: Purpose
        Purpose of the text field
      input-hints -> GtkInputHints: hints
        Hints for the text field behaviour
      attributes -> PangoAttrList: Attributes
        A list of style attributes to apply to the text of the label
      populate-all -> gboolean: Populate all
        Whether to emit ::populate-popup for touch popups
      tabs -> PangoTabArray: Tabs
        A list of tabstop locations to apply to the text of the entry
      show-emoji-icon -> gboolean: Emoji icon
        Whether to show an icon for Emoji
      enable-emoji-completion -> gboolean: Enable Emoji completion
        Whether to suggest Emoji replacements

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        label: str
        adjustment: Gtk.Adjustment
        climb_rate: float
        digits: int
        numeric: bool
        snap_to_ticks: bool
        update_policy: Gtk.SpinButtonUpdatePolicy
        value: float
        wrap: bool
        activates_default: bool
        attributes: typing.Optional[Pango.AttrList]
        buffer: Gtk.EntryBuffer
        caps_lock_warning: bool
        completion: Gtk.EntryCompletion
        cursor_position: int
        editable: bool
        enable_emoji_completion: bool
        has_frame: bool
        im_module: str
        inner_border: typing.Optional[Gtk.Border]
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        invisible_char: int
        invisible_char_set: bool
        max_length: int
        max_width_chars: int
        overwrite_mode: bool
        placeholder_text: str
        populate_all: bool
        primary_icon_activatable: bool
        primary_icon_gicon: Gio.Icon
        primary_icon_name: str
        primary_icon_pixbuf: GdkPixbuf.Pixbuf
        primary_icon_sensitive: bool
        primary_icon_stock: str
        primary_icon_storage_type: Gtk.ImageType
        primary_icon_tooltip_markup: str
        primary_icon_tooltip_text: str
        progress_fraction: float
        progress_pulse_step: float
        scroll_offset: int
        secondary_icon_activatable: bool
        secondary_icon_gicon: Gio.Icon
        secondary_icon_name: str
        secondary_icon_pixbuf: GdkPixbuf.Pixbuf
        secondary_icon_sensitive: bool
        secondary_icon_stock: str
        secondary_icon_storage_type: Gtk.ImageType
        secondary_icon_tooltip_markup: str
        secondary_icon_tooltip_text: str
        selection_bound: int
        shadow_type: Gtk.ShadowType
        show_emoji_icon: bool
        tabs: typing.Optional[Pango.TabArray]
        text: str
        text_length: int
        truncate_multiline: bool
        visibility: bool
        width_chars: int
        xalign: float
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(self, label: str = ...,
                 adjustment: Gtk.Adjustment = ...,
                 climb_rate: float = ...,
                 digits: int = ...,
                 numeric: bool = ...,
                 snap_to_ticks: bool = ...,
                 update_policy: Gtk.SpinButtonUpdatePolicy = ...,
                 value: float = ...,
                 wrap: bool = ...,
                 activates_default: bool = ...,
                 attributes: Pango.AttrList = ...,
                 buffer: Gtk.EntryBuffer = ...,
                 caps_lock_warning: bool = ...,
                 completion: typing.Optional[Gtk.EntryCompletion] = ...,
                 editable: bool = ...,
                 enable_emoji_completion: bool = ...,
                 has_frame: bool = ...,
                 im_module: str = ...,
                 inner_border: typing.Optional[Gtk.Border] = ...,
                 input_hints: Gtk.InputHints = ...,
                 input_purpose: Gtk.InputPurpose = ...,
                 invisible_char: int = ...,
                 invisible_char_set: bool = ...,
                 max_length: int = ...,
                 max_width_chars: int = ...,
                 overwrite_mode: bool = ...,
                 placeholder_text: typing.Optional[str] = ...,
                 populate_all: bool = ...,
                 primary_icon_activatable: bool = ...,
                 primary_icon_gicon: Gio.Icon = ...,
                 primary_icon_name: str = ...,
                 primary_icon_pixbuf: GdkPixbuf.Pixbuf = ...,
                 primary_icon_sensitive: bool = ...,
                 primary_icon_stock: str = ...,
                 primary_icon_tooltip_markup: str = ...,
                 primary_icon_tooltip_text: str = ...,
                 progress_fraction: float = ...,
                 progress_pulse_step: float = ...,
                 secondary_icon_activatable: bool = ...,
                 secondary_icon_gicon: Gio.Icon = ...,
                 secondary_icon_name: str = ...,
                 secondary_icon_pixbuf: GdkPixbuf.Pixbuf = ...,
                 secondary_icon_sensitive: bool = ...,
                 secondary_icon_stock: str = ...,
                 secondary_icon_tooltip_markup: str = ...,
                 secondary_icon_tooltip_text: str = ...,
                 shadow_type: Gtk.ShadowType = ...,
                 show_emoji_icon: bool = ...,
                 tabs: Pango.TabArray = ...,
                 text: str = ...,
                 truncate_multiline: bool = ...,
                 visibility: bool = ...,
                 width_chars: int = ...,
                 xalign: float = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_constrain_drag(self) -> bool: ...
    def get_gamma(self) -> float: ...
    def get_label(self) -> str: ...
    def get_mnemonic_keyval(self) -> int: ...
    def get_scale_limits(self, lower: float, upper: float) -> bool: ...
    @classmethod
    def new(cls, adjustment: Gtk.Adjustment, label: str, digits: int) -> SpinScale: ...
    def set_constrain_drag(self, constrain: bool) -> None: ...
    def set_gamma(self, gamma: float) -> None: ...
    def set_label(self, label: str) -> None: ...
    def set_scale_limits(self, lower: float, upper: float) -> None: ...
    def unset_scale_limits(self) -> None: ...
    

class SpinScaleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SpinScaleClass()
    """
    parent_class: SpinButtonClass = ...

class StringComboBox(Gtk.ComboBox, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.CellLayout):
    """
    :Constructors:

    ::

        StringComboBox(**properties)
        new(model:Gtk.TreeModel, id_column:int, label_column:int) -> Gtk.Widget

    Object GimpStringComboBox

    Properties from GimpStringComboBox:
      id-column -> gint: ID Column
        The model column that holds the ID
      label-column -> gint: Label Column
        The model column that holds the label
      ellipsize -> PangoEllipsizeMode: Ellipsize
        Ellipsize mode for the text cell renderer
      value -> gchararray: Value
        Value of active item

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkComboBox:
      changed ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray

    Properties from GtkComboBox:
      model -> GtkTreeModel: ComboBox model
        The model for the combo box
      wrap-width -> gint: Wrap width
        Wrap width for laying out the items in a grid
      row-span-column -> gint: Row span column
        TreeModel column containing the row span values
      column-span-column -> gint: Column span column
        TreeModel column containing the column span values
      active -> gint: Active item
        The item which is currently active
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether dropdowns should have a tearoff menu item
      tearoff-title -> gchararray: Tearoff Title
        A title that may be displayed by the window manager when the popup is torn-off
      has-frame -> gboolean: Has Frame
        Whether the combo box draws a frame around the child
      popup-shown -> gboolean: Popup shown
        Whether the combo's dropdown is shown
      button-sensitivity -> GtkSensitivityType: Button Sensitivity
        Whether the dropdown button is sensitive when the model is empty
      has-entry -> gboolean: Has Entry
        Whether combo box has an entry
      entry-text-column -> gint: Entry Text Column
        The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE
      popup-fixed-width -> gboolean: Popup Fixed Width
        Whether the popup's width should be a fixed width matching the allocated width of the combo box
      id-column -> gint: ID Column
        The column in the combo box's model that provides string IDs for the values in the model
      active-id -> gchararray: Active id
        The value of the id column for the active row
      cell-area -> GtkCellArea: Cell Area
        The GtkCellArea used to layout cells

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        ellipsize: Pango.EllipsizeMode
        id_column: int
        label_column: int
        value: str
        active: int
        active_id: typing.Optional[str]
        add_tearoffs: bool
        button_sensitivity: Gtk.SensitivityType
        cell_area: Gtk.CellArea
        column_span_column: int
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        model: Gtk.TreeModel
        popup_fixed_width: bool
        popup_shown: bool
        row_span_column: int
        tearoff_title: str
        wrap_width: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.ComboBox = ...
    def __init__(self, ellipsize: Pango.EllipsizeMode = ...,
                 id_column: int = ...,
                 label_column: int = ...,
                 value: str = ...,
                 active: int = ...,
                 active_id: typing.Optional[str] = ...,
                 add_tearoffs: bool = ...,
                 button_sensitivity: Gtk.SensitivityType = ...,
                 cell_area: Gtk.CellArea = ...,
                 column_span_column: int = ...,
                 entry_text_column: int = ...,
                 has_entry: bool = ...,
                 has_frame: bool = ...,
                 model: typing.Optional[Gtk.TreeModel] = ...,
                 popup_fixed_width: bool = ...,
                 row_span_column: int = ...,
                 tearoff_title: str = ...,
                 wrap_width: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    def get_active(self) -> str: ...
    @classmethod
    def new(cls, model: Gtk.TreeModel, id_column: int, label_column: int) -> StringComboBox: ...
    def set_active(self, id: str) -> bool: ...
    def set_sensitivity(self, func: typing.Callable[..., bool], *data: typing.Any) -> None: ...
    

class StringComboBoxClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StringComboBoxClass()
    """
    parent_class: Gtk.ComboBoxClass = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class UnitComboBox(Gtk.ComboBox, Atk.ImplementorIface, Gtk.Buildable, Gtk.CellEditable, Gtk.CellLayout):
    """
    :Constructors:

    ::

        UnitComboBox(**properties)
        new() -> Gtk.Widget
        new_with_model(model:GimpUi.UnitStore) -> Gtk.Widget

    Object GimpUnitComboBox

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkComboBox:
      changed ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray

    Properties from GtkComboBox:
      model -> GtkTreeModel: ComboBox model
        The model for the combo box
      wrap-width -> gint: Wrap width
        Wrap width for laying out the items in a grid
      row-span-column -> gint: Row span column
        TreeModel column containing the row span values
      column-span-column -> gint: Column span column
        TreeModel column containing the column span values
      active -> gint: Active item
        The item which is currently active
      add-tearoffs -> gboolean: Add tearoffs to menus
        Whether dropdowns should have a tearoff menu item
      tearoff-title -> gchararray: Tearoff Title
        A title that may be displayed by the window manager when the popup is torn-off
      has-frame -> gboolean: Has Frame
        Whether the combo box draws a frame around the child
      popup-shown -> gboolean: Popup shown
        Whether the combo's dropdown is shown
      button-sensitivity -> GtkSensitivityType: Button Sensitivity
        Whether the dropdown button is sensitive when the model is empty
      has-entry -> gboolean: Has Entry
        Whether combo box has an entry
      entry-text-column -> gint: Entry Text Column
        The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE
      popup-fixed-width -> gboolean: Popup Fixed Width
        Whether the popup's width should be a fixed width matching the allocated width of the combo box
      id-column -> gint: ID Column
        The column in the combo box's model that provides string IDs for the values in the model
      active-id -> gchararray: Active id
        The value of the id column for the active row
      cell-area -> GtkCellArea: Cell Area
        The GtkCellArea used to layout cells

    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        active: int
        active_id: typing.Optional[str]
        add_tearoffs: bool
        button_sensitivity: Gtk.SensitivityType
        cell_area: Gtk.CellArea
        column_span_column: int
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        id_column: int
        model: Gtk.TreeModel
        popup_fixed_width: bool
        popup_shown: bool
        row_span_column: int
        tearoff_title: str
        wrap_width: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        editing_canceled: bool
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, active: int = ...,
                 active_id: typing.Optional[str] = ...,
                 add_tearoffs: bool = ...,
                 button_sensitivity: Gtk.SensitivityType = ...,
                 cell_area: Gtk.CellArea = ...,
                 column_span_column: int = ...,
                 entry_text_column: int = ...,
                 has_entry: bool = ...,
                 has_frame: bool = ...,
                 id_column: int = ...,
                 model: typing.Optional[Gtk.TreeModel] = ...,
                 popup_fixed_width: bool = ...,
                 row_span_column: int = ...,
                 tearoff_title: str = ...,
                 wrap_width: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 editing_canceled: bool = ...) -> None: ...
    def get_active(self) -> Gimp.Unit: ...
    @classmethod
    def new(cls) -> UnitComboBox: ...
    @classmethod
    def new_with_model(cls, model: UnitStore) -> UnitComboBox: ...
    def set_active(self, unit: Gimp.Unit) -> None: ...
    

class UnitComboBoxClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnitComboBoxClass()
    """
    parent_class: Gtk.ComboBoxClass = ...

class UnitStore(GObject.Object, Gtk.TreeModel):
    """
    :Constructors:

    ::

        UnitStore(**properties)
        new(num_values:int) -> GimpUi.UnitStore

    Object GimpUnitStore

    Properties from GimpUnitStore:
      num-values -> gint: Num Values
        The number of values this store provides
      has-pixels -> gboolean: Has Pixels
        Whether the store has GIMP_UNIT_PIXELS
      has-percent -> gboolean: Has Percent
        Whether the store has GIMP_UNIT_PERCENT
      short-format -> gchararray: Short Format
        Format string for a short label
      long-format -> gchararray: Long Format
        Format string for a long label

    Signals from GtkTreeModel:
      row-inserted (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      row-changed (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        has_percent: bool
        has_pixels: bool
        long_format: str
        num_values: int
        short_format: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, has_percent: bool = ...,
                 has_pixels: bool = ...,
                 long_format: str = ...,
                 num_values: int = ...,
                 short_format: str = ...) -> None: ...
    def get_has_percent(self) -> bool: ...
    def get_has_pixels(self) -> bool: ...
    def get_nth_value(self, unit: Gimp.Unit, index: int) -> float: ...
    @classmethod
    def new(cls, num_values: int) -> UnitStore: ...
    def set_has_percent(self, has_percent: bool) -> None: ...
    def set_has_pixels(self, has_pixels: bool) -> None: ...
    def set_pixel_value(self, index: int, value: float) -> None: ...
    def set_resolution(self, index: int, resolution: float) -> None: ...
    

class UnitStoreClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnitStoreClass()
    """
    parent_class: GObject.ObjectClass = ...
    _gimp_reserved0: None = ...
    _gimp_reserved1: None = ...
    _gimp_reserved2: None = ...
    _gimp_reserved3: None = ...
    _gimp_reserved4: None = ...
    _gimp_reserved5: None = ...
    _gimp_reserved6: None = ...
    _gimp_reserved7: None = ...
    _gimp_reserved8: None = ...
    _gimp_reserved9: None = ...

class VectorLoadProcedureDialog(ProcedureDialog, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        VectorLoadProcedureDialog(**properties)
        new(procedure:Gimp.VectorLoadProcedure, config:Gimp.ProcedureConfig, extracted_data:Gimp.VectorLoadData=None, file:Gio.File=None) -> Gtk.Widget

    Object GimpVectorLoadProcedureDialog

    Properties from GimpProcedureDialog:
      procedure -> GimpProcedure: Procedure
        The GimpProcedure this dialog is used with
      config -> GimpProcedureConfig: Config
        The GimpProcedureConfig this dialog is editing

    Properties from GimpDialog:
      help-func -> gpointer: Help Func
        The help function to call when F1 is hit
      help-id -> gchararray: Help ID
        The help ID to pass to help-func
      parent -> GtkWidget: Parent
        The dialog's parent widget

    Signals from GtkDialog:
      response (gint)
      close ()

    Properties from GtkDialog:
      use-header-bar -> gint: Use Header Bar
        Use Header Bar for actions.

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximization
        If this window's titlebar should be hidden when the window is maximized
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialog
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximized
        Whether the window is maximized

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        config: Gimp.ProcedureConfig
        procedure: Gimp.Procedure
        help_func: None
        help_id: str
        use_header_bar: int
        accept_focus: bool
        application: typing.Optional[Gtk.Application]
        attached_to: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: typing.Optional[GdkPixbuf.Pixbuf]
        icon_name: typing.Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: typing.Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: typing.Optional[str]
        transient_for: typing.Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        startup_id: str
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, config: Gimp.ProcedureConfig = ...,
                 procedure: Gimp.Procedure = ...,
                 help_func: None = ...,
                 help_id: str = ...,
                 parent: Gtk.Widget = ...,
                 use_header_bar: int = ...,
                 accept_focus: bool = ...,
                 application: typing.Optional[Gtk.Application] = ...,
                 attached_to: typing.Optional[Gtk.Widget] = ...,
                 decorated: bool = ...,
                 default_height: int = ...,
                 default_width: int = ...,
                 deletable: bool = ...,
                 destroy_with_parent: bool = ...,
                 focus_on_map: bool = ...,
                 focus_visible: bool = ...,
                 gravity: Gdk.Gravity = ...,
                 has_resize_grip: bool = ...,
                 hide_titlebar_when_maximized: bool = ...,
                 icon: typing.Optional[GdkPixbuf.Pixbuf] = ...,
                 icon_name: typing.Optional[str] = ...,
                 mnemonics_visible: bool = ...,
                 modal: bool = ...,
                 resizable: bool = ...,
                 role: str = ...,
                 screen: Gdk.Screen = ...,
                 skip_pager_hint: bool = ...,
                 skip_taskbar_hint: bool = ...,
                 startup_id: str = ...,
                 title: str = ...,
                 transient_for: typing.Optional[Gtk.Window] = ...,
                 type: Gtk.WindowType = ...,
                 type_hint: Gdk.WindowTypeHint = ...,
                 urgency_hint: bool = ...,
                 window_position: Gtk.WindowPosition = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    @classmethod
    def new(cls, procedure: Gimp.VectorLoadProcedure, config: Gimp.ProcedureConfig, extracted_data: typing.Optional[Gimp.VectorLoadData] = None, file: typing.Optional[Gio.File] = None) -> VectorLoadProcedureDialog: ...
    

class VectorLoadProcedureDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VectorLoadProcedureDialogClass()
    """
    parent_class: ProcedureDialogClass = ...

class ZoomModel(GObject.Object):
    """
    :Constructors:

    ::

        ZoomModel(**properties)
        new() -> GimpUi.ZoomModel

    Object GimpZoomModel

    Signals from GimpZoomModel:
      zoomed (gdouble, gdouble)

    Properties from GimpZoomModel:
      value -> gdouble: Value
        Zoom factor
      minimum -> gdouble: Minimum
        Lower limit for the zoom factor
      maximum -> gdouble: Maximum
        Upper limit for the zoom factor
      fraction -> gchararray: Fraction
        The zoom factor expressed as a fraction
      percentage -> gchararray: Percentage
        The zoom factor expressed as a percentage

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        fraction: str
        maximum: float
        minimum: float
        percentage: str
        value: float
    props: Props = ...
    def __init__(self, maximum: float = ...,
                 minimum: float = ...,
                 value: float = ...) -> None: ...
    def get_factor(self) -> float: ...
    def get_fraction(self) -> typing.Tuple[int, int]: ...
    @classmethod
    def new(cls) -> ZoomModel: ...
    def set_range(self, min: float, max: float) -> None: ...
    def zoom(self, zoom_type: ZoomType, scale: float) -> None: ...
    @staticmethod
    def zoom_step(zoom_type: ZoomType, scale: float, delta: float) -> float: ...
    

class ZoomModelClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ZoomModelClass()
    """
    parent_class: GObject.ObjectClass = ...

class ZoomPreview(ScrolledPreview, Atk.ImplementorIface, Gtk.Buildable, Gtk.Orientable):
    """
    :Constructors:

    ::

        ZoomPreview(**properties)
        new_from_drawable(drawable:Gimp.Drawable) -> Gtk.Widget
        new_with_model_from_drawable(drawable:Gimp.Drawable, model:GimpUi.ZoomModel) -> Gtk.Widget

    Object GimpZoomPreview

    Properties from GimpZoomPreview:
      drawable -> GimpDrawable: Drawable
        The drawable this preview is attached to
      model -> GimpZoomModel: Model
        The zoom preview's GimpZoomModel

    Signals from GimpPreview:
      invalidated ()

    Properties from GimpPreview:
      update -> gboolean: Update
        Whether the preview should update automatically

    Properties from GtkBox:
      spacing -> gint: Spacing
        The amount of space between children
      homogeneous -> gboolean: Homogeneous
        Whether the children should all be the same size
      baseline-position -> GtkBaselinePosition: Baseline position
        The position of the baseline aligned widgets if extra space is available

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

    Signals from GtkWidget:
      destroy ()
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        drawable: Gimp.Drawable
        model: ZoomModel
        update: bool
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        border_width: int
        resize_mode: Gtk.ResizeMode
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: typing.Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: typing.Optional[Gdk.Window]
        orientation: Gtk.Orientation
        child: Gtk.Widget
    props: Props = ...
    def __init__(self, drawable: Gimp.Drawable = ...,
                 model: ZoomModel = ...,
                 update: bool = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 border_width: int = ...,
                 child: Gtk.Widget = ...,
                 resize_mode: Gtk.ResizeMode = ...,
                 app_paintable: bool = ...,
                 can_default: bool = ...,
                 can_focus: bool = ...,
                 double_buffered: bool = ...,
                 events: Gdk.EventMask = ...,
                 expand: bool = ...,
                 focus_on_click: bool = ...,
                 halign: Gtk.Align = ...,
                 has_default: bool = ...,
                 has_focus: bool = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 is_focus: bool = ...,
                 margin: int = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 no_show_all: bool = ...,
                 opacity: float = ...,
                 parent: Gtk.Container = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 style: typing.Optional[Gtk.Style] = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def get_drawable(self) -> Gimp.Drawable: ...
    def get_factor(self) -> float: ...
    def get_model(self) -> ZoomModel: ...
    def get_source(self) -> typing.Tuple[bytes, int, int, int]: ...
    @classmethod
    def new_from_drawable(cls, drawable: Gimp.Drawable) -> ZoomPreview: ...
    @classmethod
    def new_with_model_from_drawable(cls, drawable: Gimp.Drawable, model: ZoomModel) -> ZoomPreview: ...
    

class ZoomPreviewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ZoomPreviewClass()
    """
    parent_class: ScrolledPreviewClass = ...

class AspectType(GObject.GEnum):
    LANDSCAPE = 2
    PORTRAIT = 1
    SQUARE = 0

class ChainPosition(GObject.GEnum):
    BOTTOM = 2
    LEFT = 1
    RIGHT = 3
    TOP = 0

class ColorAreaType(GObject.GEnum):
    FLAT = 0
    LARGE_CHECKS = 2
    SMALL_CHECKS = 1

class ColorSelectorChannel(GObject.GEnum):
    ALPHA = 6
    BLUE = 5
    GREEN = 4
    HUE = 0
    LCH_CHROMA = 8
    LCH_HUE = 9
    LCH_LIGHTNESS = 7
    RED = 3
    SATURATION = 1
    VALUE = 2

class ColorSelectorModel(GObject.GEnum):
    HSV = 2
    LCH = 1
    RGB = 0

class IntComboBoxLayout(GObject.GEnum):
    ABBREVIATED = 1
    FULL = 2
    ICON_ONLY = 0

class IntStoreColumns(GObject.GEnum):
    ABBREV = 2
    ICON_NAME = 3
    LABEL = 1
    NUM_COLUMNS = 6
    PIXBUF = 4
    USER_DATA = 5
    VALUE = 0

class PageSelectorTarget(GObject.GEnum):
    IMAGES = 1
    LAYERS = 0

class SizeEntryUpdatePolicy(GObject.GEnum):
    NONE = 0
    RESOLUTION = 2
    SIZE = 1

class WidgetsError(GObject.GEnum):
    WIDGETS_PARSE_ERROR = 0

class ZoomType(GObject.GEnum):
    IN = 0
    OUT = 1

