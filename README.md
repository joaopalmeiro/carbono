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

To obtain the language map from the Carbon codebase, clone the [Carbon repo](https://github.com/carbon-app/carbon) and follow the steps below:

1. `yarn install`.
2. `yarn dev`.
3. Add the following snippet at the end of the `lib/constants.js` file and copy the generated string from the Console panel (Chrome DevTools), for example.

```js
// lib/constants.js

function searchLanguage(l) {
  return (
    LANGUAGE_NAME_HASH[l] || LANGUAGE_MODE_HASH[l] || LANGUAGE_MIME_HASH[l]
  );
}

function getValue(language) {
  const languageMode = searchLanguage(language);

  if (languageMode) {
    return languageMode.mime || languageMode.mode;
  }

  return language;
}

function upperCase(str) {
  return str.toUpperCase();
}

function slugify(str) {
  str = str
    .replace(/#/g, "_sharp")
    .replace(/\+/g, "_plus")
    .replace(/-/g, "_")
    .replace(/\//g, "_")
    .replace(/\./g, "_")
    .replace(/ +/g, "_"); // Replace spaces

  return str;
}

const langMap = Object.fromEntries(
  LANGUAGES.map((l) => [
    upperCase(slugify(l.name)),
    getValue(l.short || l.mode),
  ])
);

console.log(JSON.stringify(langMap, 0, 2));
```

## References

- [Carbonara](https://github.com/petersolopov/carbonara).
- [carbonnow](https://github.com/pokurt/carbon-now-sh-API-Wrapper).
- [carbonsh](https://github.com/MrMarble/carbonsh).

## Notes

- `poetry add "pyppeteer>=0.2.2,<1"`.
- [`encodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) (JavaScript) escapes all characters except:
  - `A-Z a-z 0-9 - _ . ! ~ * ' ( )`.
- [Default values](https://github.com/carbon-app/carbon/blob/main/lib/constants.js).
- [tohash](https://www.npmjs.com/package/tohash) package.
- Open Developer Tools for VS Code: `Help` > `Toggle Developer Tools`.
