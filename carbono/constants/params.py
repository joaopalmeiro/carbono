from typing import Dict

# export_size/es
# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1029
EXPORT_SIZE: Dict[str, str] = {"X1": "1x", "X2": "2x", "X4": "4x"}

# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1044
DEFAULT_EXPORT_SIZE: str = EXPORT_SIZE["X2"]

# background_color/bg
# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1043
DEFAULT_BG_COLOR: str = "rgba(171, 184, 195, 1)"

# theme/t
# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L34
THEMES: Dict[str, str] = {
    "NIGHT_3024": "3024-night",
    "A11Y_DARK": "a11y-dark",
    "BLACKBOARD": "blackboard",
    "BASE_16_DARK": "base16-dark",
    "BASE_16_LIGHT": "base16-light",
    "COBALT": "cobalt",
    "DRACULA": "dracula",  # or dracula-pro?
    "DUOTONE": "duotone-dark",
    "HOPSCOTCH": "hopscotch",
    "LUCARIO": "lucario",
    "MATERIAL": "material",
    "MONOKAI": "monokai",
    "NIGHT_OWL": "night-owl",
    "NORD": "nord",
    "OCEANIC_NEXT": "oceanic-next",
    "ONE_LIGHT": "one-light",
    "ONE_DARK": "one-dark",
    "PANDA": "panda-syntax",
    "PARAISO": "paraiso-dark",
    "SETI": "seti",
    "SHADES_PURPLE": "shades-of-purple",
    "SOLARIZED_DARK": "solarized dark",
    "SOLARIZED_LIGHT": "solarized light",
    "SYNTHWAVE_84": "synthwave-84",
    "TWILIGHT": "twilight",
    "VERMINAL": "verminal",
    "VSCODE": "vscode",
    "YETI": "yeti",
    "ZENBURN": "zenburn",
}

# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1042
DEFAULT_THEME: str = THEMES["SETI"]

# window_theme/wt
# Source:
# - https://github.com/carbon-app/carbon/blob/main/components/svg/WindowThemes.js
# - https://github.com/carbon-app/carbon/blob/main/components/ThemeSelect.js#L6
WINDOW_THEMES: Dict[str, str] = {
    "NONE": "none",
    "SHARP": "sharp",
    "BLACK_AND_WHITE": "bw",
    "BOXY": "boxy",
}

# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1082
DEFAULT_WINDOW_THEME: str = WINDOW_THEMES["NONE"]
