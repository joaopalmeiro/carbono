from urllib.parse import quote

from .constants.misc import CARBON_URL


def encode_url(url: str) -> str:
    return quote(url)


def code2url(code: str) -> str:
    return f"{CARBON_URL}?&code={(encode_url(code))}"


def int2px(number) -> str:
    return f"{number}px"


def int2percent(number) -> str:
    return f"{number}%"
