# carbono

A Python package to generate snippet images via [Carbon](https://carbon.now.sh/) programmatically.

## Usage

```python
import asyncio

from carbono.image import from_code

code = """import asyncio

async def func():
    return "Hello, World!"

if __name__ == '__main__':
    asyncio.run(func())"""

loop = asyncio.get_event_loop()
loop.run_until_complete(from_code(code))
```

## Development

- `poetry install`.
- `poetry shell`.

## References

- [Carbonara](https://github.com/petersolopov/carbonara).
- [carbonnow](https://github.com/pokurt/carbon-now-sh-API-Wrapper).
- [carbonsh](https://github.com/MrMarble/carbonsh).

## Notes

- `poetry add "pyppeteer>=0.2.2,<1"`.
- [`encodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) (JavaScript) escapes all characters except:
  - `A-Z a-z 0-9 - _ . ! ~ * ' ( )`.
- [Default values](https://github.com/carbon-app/carbon/blob/main/lib/constants.js).
