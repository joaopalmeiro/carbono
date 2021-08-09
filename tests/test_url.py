from carbono.config import Config
from carbono.image import code2url


def test_default_url():
    # https://en.wikibooks.org/wiki/Computer_Programming/Hello_world#Python_3
    code = "print(Hello, World!)"

    # Manually retrieved from https://carbon.now.sh/ (Incognito window)
    default_url = (
        "https://carbon.now.sh/?"
        "bg=rgba%28171%2C+184%2C+195%2C+1%29&"
        "t=seti&"
        "wt=none&"
        "l=auto&"
        "ds=true&"
        "dsyoff=20px&"
        "dsblur=68px&"
        "wc=true&"
        "wa=true&"
        "pv=56px&"
        "ph=56px&"
        "ln=false&"
        "fl=1&"
        "fm=Hack&"
        "fs=14px&"
        "lh=133%25&"
        "si=false&"
        "es=2x&"
        "wm=false&"
        "code=print%28Hello%252C%2520World%21%29"
    )

    generated_url = code2url(code=code, config=Config())

    assert isinstance(generated_url, str)
    assert default_url == generated_url
