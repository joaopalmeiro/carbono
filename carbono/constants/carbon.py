from typing import Dict

CARBON_URL: str = "https://carbon.now.sh/"
# Carbonara: "#export-container  .container-bg"
CARBON_IMG_SELECTOR: str = "#export-container"
CARBON_MENU_SELECTOR: str = "#export-menu"
CARBON_PNG_SELECTOR: str = "#export-png"
CARBON_SVG_SELECTOR: str = "#export-svg"
CARBON_FILENAME: str = "carbon.png"

ATTR_TO_QUERY_PARAM: Dict[str, str] = {
    "background_color": "bg",
    "drop_shadow": "ds",
    "drop_shadow_blur_radius": "dsblur",
    "drop_shadow_offset_Y": "dsyoff",
    "export_size": "es",
    "font_family": "fm",
    "first_line_number": "fl",
    "font_size": "fs",
    "language": "l",
    "line_height": "lh",
    "line_numbers": "ln",
    "padding_horizontal": "ph",
    "padding_vertical": "pv",
    # Unsupported query parameter (only available in exported configuration)
    # More info: https://github.com/petersolopov/carbonara#unsupported-params
    "squared_image": "si",
    "theme": "t",
    "watermark": "wm",
    "width_adjustment": "wa",
    "window_controls": "wc",
    "window_theme": "wt",
}
