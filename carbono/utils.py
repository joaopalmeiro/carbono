from typing import Optional
from urllib.parse import parse_qsl, quote, unquote_plus, urlsplit

from .constants.carbon import SAFE_ENCODE_URI_COMPONENT_JS


def encode_url(url: str) -> str:
    # Source:
    # - https://github.com/MrMarble/carbonsh/blob/master/carbonsh/utils.py#L12

    # It may be necessary to trim the length to avoid URL length limit errors
    # More info:
    # - https://github.com/carbon-app/carbon/blob/main/lib/routing.js#L46
    # - https://github.com/MrMarble/carbonsh/blob/master/carbonsh/utils.py#L17

    # Carbon encodes the text twice.
    # Used for the code part of the URL.

    # or
    # first_encoding = urllib.parse.quote(url, safe="*()")
    # second_econding = urllib.parse.quote(first_encoding, safe="*")
    # Source: https://github.com/MrMarble/carbonsh/blob/master/carbonsh/utils.py#L13

    return quote(quote(url, safe=SAFE_ENCODE_URI_COMPONENT_JS))


def int2px(number: int) -> str:
    return f"{number}px"


def int2percent(number: int) -> str:
    return f"{number}%"


def int2factor(number: int) -> str:
    return f"{number}x"


def factor2int(factor: str, symbol: str = "x") -> int:
    return int(factor.rstrip(symbol))


def print_url(url: str, sep: str = "&") -> None:
    # `unquote_plus()`: like `unquote()`, but also replaces plus signs with spaces
    # More info:
    # - https://docs.python.org/3.6/library/urllib.parse.html#urllib.parse.unquote_plus
    # - https://docs.python.org/3.6/library/urllib.parse.html#urllib.parse.unquote

    print(*unquote_plus(url).split(sep), sep="\n")
    # or (due to the code part)
    # print(*unquote_plus(unquote_plus(url)).split(sep), sep="\n")


def get_url_query_param(url: str, param: str) -> Optional[str]:
    # Source: https://stackoverflow.com/a/21584580
    params = dict(parse_qsl(urlsplit(url).query))

    try:
        return params[param]
    except KeyError:
        return None
