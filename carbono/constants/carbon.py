from typing import Dict

CARBON_URL: str = "https://carbon.now.sh/"
CARBON_IMG_SELECTOR: str = "#export-container"

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
    "squared_image": "si",
    "theme": "t",
    "watermark": "wm",
    "width_adjustment": "wa",
    "window_controls": "wc",
    "window_theme": "wt",
}
