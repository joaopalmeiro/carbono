from urllib.parse import quote

from .constants.carbon import ATTR_TO_QUERY_PARAM
from .constants.params import (
    DEFAULT_BG_COLOR,
    DEFAULT_DROP_SHADOW_BLUR_RADIUS,
    DEFAULT_DROP_SHADOW_OFFSET_Y,
    DEFAULT_EXPORT_SIZE,
    DEFAULT_FIRST_LINE_NUMBER,
    DEFAULT_FONT,
    DEFAULT_FONT_SIZE,
    DEFAULT_LANGUAGE,
    DEFAULT_LINE_HEIGHT,
    DEFAULT_PADDING_HORIZONTAL,
    DEFAULT_PADDING_VERTICAL,
    DEFAULT_THEME,
    DEFAULT_WINDOW_THEME,
)
from .utils import int2percent, int2px


class Config:
    def __init__(
        self,
        background_color: str = DEFAULT_BG_COLOR,
        theme: str = DEFAULT_THEME,
        window_theme: str = DEFAULT_WINDOW_THEME,
        language: str = DEFAULT_LANGUAGE,
        # Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1078
        drop_shadow: bool = True,
        drop_shadow_offset_Y: str = int2px(DEFAULT_DROP_SHADOW_OFFSET_Y),
        drop_shadow_blur_radius: str = int2px(DEFAULT_DROP_SHADOW_BLUR_RADIUS),
        # Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1087
        window_controls: bool = True,
        # Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1088
        width_adjustment: bool = True,
        padding_vertical: str = int2px(DEFAULT_PADDING_VERTICAL),
        padding_horizontal: str = int2px(DEFAULT_PADDING_HORIZONTAL),
        # Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1089
        line_numbers: bool = False,
        first_line_number: int = DEFAULT_FIRST_LINE_NUMBER,
        font_family: str = DEFAULT_FONT,
        font_size: str = int2px(DEFAULT_FONT_SIZE),
        line_height: str = int2percent(DEFAULT_LINE_HEIGHT),
        export_size: str = DEFAULT_EXPORT_SIZE,
        # Source: https://github.com/carbon-app/carbon/blob/main/lib/constants.js#L1092
        watermark: bool = False,
    ) -> None:
        # Order matters (default order of the query parameters for Carbon)
        self.background_color = background_color
        self.theme = theme
        self.window_theme = window_theme
        self.language = language
        self.drop_shadow = drop_shadow
        self.drop_shadow_offset_Y = drop_shadow_offset_Y
        self.drop_shadow_blur_radius = drop_shadow_blur_radius
        self.window_controls = window_controls
        self.width_adjustment = width_adjustment
        self.padding_vertical = padding_vertical
        self.padding_horizontal = padding_horizontal
        self.line_numbers = line_numbers
        self.first_line_number = first_line_number
        self.font_family = font_family
        self.font_size = font_size
        self.line_height = line_height

        self.export_size = export_size
        self.watermark = watermark

    def __str__(self):
        result = []

        for key, value in vars(self).items():
            query_value = str(value).lower() if isinstance(value, bool) else value

            result.append(f"{ATTR_TO_QUERY_PARAM[key.lstrip('_')]}={query_value}")

        # or `safe="()&="`
        # Source: https://github.com/MrMarble/carbonsh/blob/master/carbonsh/Config.py
        return quote("&".join(result), safe="&=")

    @property
    def export_size(self) -> str:
        return self._export_size

    @export_size.setter
    def export_size(self, export_size: str) -> None:
        self._export_size = export_size

    @property
    def watermark(self) -> bool:
        return self._watermark

    @watermark.setter
    def watermark(self, watermark: bool) -> None:
        self._watermark = watermark
