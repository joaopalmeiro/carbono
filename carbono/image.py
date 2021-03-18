from pathlib import Path

from pyppeteer import launch

from .constants.carbon import CARBON_IMG_SELECTOR
from .utils import code2url


async def from_url(
    url: str,
    output_dir: str = ".",
    extension: str = "png",
    headless: bool = False,
    timeout: int = 2000,
) -> None:
    output_path = Path(output_dir)
    browser = await launch({"headless": headless})
    page = await browser.newPage()

    await page.goto(url, {"waitUntil": "load"})

    if headless:
        export_container = await page.waitForSelector(CARBON_IMG_SELECTOR)
        # x, y, width, height
        element_bounds = await export_container.boundingBox()

        output_path_and_filename = str(output_path.joinpath("carbon.png"))
        print(element_bounds)

        await export_container.screenshot(
            {"path": output_path_and_filename, "clip": element_bounds}
        )
    else:
        pass


async def from_code(
    code: str,
    output: str = ".",
    extension: str = "png",
    headless: bool = False,
    timeout: int = 2000,
) -> None:
    url = code2url(code)
    await from_url(url, output, extension, headless, timeout)
