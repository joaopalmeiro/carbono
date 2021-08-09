from typing import Dict

from .languages import EXTRACTED_LANGUAGES

# export_size/es
# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1029
EXPORT_SIZE: Dict[str, str] = {"X1": "1x", "X2": "2x", "X4": "4x"}

# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1044
DEFAULT_EXPORT_SIZE: str = EXPORT_SIZE["X2"]

# background_color/bg
# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1043
DEFAULT_BG_COLOR: str = "rgba(171, 184, 195, 1)"

# theme/t
# Source:
# - https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L34
# - https://github.com/yonicd/carbonate/blob/master/R/set_get_functions.R
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

# language/l

# Note: Bash is named "application/x-sh", for example
# Export the configuration (JSON) file to confirm the correct value for
# each supported language (Settings (gear icon) > Misc > Export config)

# Source:

# - https://github.com/carbon-app/carbon/blob/main/components/Carbon.js#L33
# - https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L624
# (`LANGUAGE_NAME_HASH[l] || LANGUAGE_MODE_HASH[l] || LANGUAGE_MIME_HASH[l]`)
# Note: `LANGUAGE_NAME_HASH` uses `"short"` (not `"name"`) as an ID
# So, for each language, check the following keys in the order presented here
# and consider the value of the last existing key:
# 1. short
# 2. mode
# 3. mime
# In practice, it is between `mode` and `mime`.
# - https://github.com/petersolopov/carbonara#post-apicook
LANGUAGES: Dict[str, str] = EXTRACTED_LANGUAGES

# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1041
DEFAULT_LANGUAGE: str = LANGUAGES["AUTO"]

# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1079
DEFAULT_DROP_SHADOW_OFFSET_Y: int = 20  # px

# Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1080
DEFAULT_DROP_SHADOW_BLUR_RADIUS: int = 68  # px
