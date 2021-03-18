from urllib.parse import quote

from .constants.carbon import ATTR_TO_QUERY_PARAM
from .constants.params import EXPORT_SIZE


class Config:
    def __init__(
        self, export_size: str = EXPORT_SIZE["X2"], watermark: bool = False
    ) -> None:
        self.export_size = export_size
        self.watermark = watermark

    def __str__(self):
        result = []

        for key, value in vars(self).items():
            result.append(f"{ATTR_TO_QUERY_PARAM[key.lstrip('_')]}={value}")

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
