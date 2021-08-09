from typing import Optional
from urllib.parse import parse_qsl, quote, unquote, urlsplit


def encode_url(url: str) -> str:
    return quote(url)


def int2px(number: int) -> str:
    return f"{number}px"


def int2percent(number: int) -> str:
    return f"{number}%"


def int2factor(number: int) -> str:
    return f"{number}x"


def factor2int(factor: str, symbol: str = "x") -> int:
    return int(factor.rstrip(symbol))


def print_url(url: str, sep: str = "&") -> None:
    print(*unquote(url).split(sep), sep="\n")


def get_url_query_param(url: str, param: str) -> Optional[str]:
    # Source: https://stackoverflow.com/a/21584580
    params = dict(parse_qsl(urlsplit(url).query))

    try:
        return params[param]
    except KeyError:
        return None
