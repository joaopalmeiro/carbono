from urllib.parse import quote, unquote

from .config import Config
from .constants.carbon import CARBON_URL


def encode_url(url: str) -> str:
    return quote(url)


def code2url(code: str, config: Config) -> str:
    return f"{CARBON_URL}?{config}&code={encode_url(code)}"


def int2px(number: int) -> str:
    return f"{number}px"


def int2percent(number: int) -> str:
    return f"{number}%"


def print_url(url: str, sep: str = "&") -> None:
    print(*unquote(url).split(sep), sep="\n")
