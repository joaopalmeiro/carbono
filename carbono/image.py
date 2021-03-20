from pathlib import Path
from typing import Optional

from pyppeteer import launch

from .config import Config
from .constants.carbon import ATTR_TO_QUERY_PARAM, CARBON_IMG_SELECTOR
from .utils import code2url, factor2int, get_url_query_param


async def from_url(
    url: str,
    output_dir: str = ".",
    extension: str = "png",
    headless: bool = False,
    timeout: int = 2000,
    device_scale_factor: Optional[int] = None,
) -> None:
    output_path = Path(output_dir)

    if device_scale_factor is None:
        export_size_value = get_url_query_param(url, ATTR_TO_QUERY_PARAM["export_size"])
        scale_factor = (
            factor2int(export_size_value) if export_size_value is not None else 2
        )

        device_scale_factor = scale_factor

    browser = await launch({"headless": headless})
    page = await browser.newPage()

    # Carbonara: `"width": 8192`, `"height": 2048`
    # deviceScaleFactor (float): Default to 1.0
    await page.setViewport(
        {"width": 1600, "height": 1000, "deviceScaleFactor": float(device_scale_factor)}
    )

    await page.goto(url, {"waitUntil": "load"})

    if headless:
        export_container = await page.waitForSelector(CARBON_IMG_SELECTOR)
        # x, y, width, height
        element_bounds = await export_container.boundingBox()

        output_path_and_filename = str(output_path.joinpath("carbon.png"))

        # "clip":
        # {
        #     **element_bounds,
        #     "x": round(element_bounds["x"]),
        #     "height": round(element_bounds["height"]) - 1,
        # }

        await export_container.screenshot(
            {"path": output_path_and_filename, "clip": element_bounds}
        )
    else:
        print(str(output_path.joinpath("")))
        print(str(output_path))

        await page._client.send(
            "Page.setDownloadBehavior",
            {"behavior": "allow", "downloadPath": str(output_path.joinpath(""))},
        )

        save_image_trigger = await page.waitForSelector("#export-menu")
        await save_image_trigger.click()

        png_export_trigger = await page.querySelector("#export-png")
        svg_export_trigger = await page.querySelector("#export-svg")

        if extension == "png":
            await png_export_trigger.click()
        elif extension == "svg":
            await svg_export_trigger.click()

        await page.waitFor(timeout)
        await browser.close()


async def from_code(
    code: str,
    config: Config,
    output_dir: str = ".",
    extension: str = "png",
    headless: bool = False,
    timeout: int = 2000,
) -> None:
    url = code2url(code, config)
    device_scale_factor = factor2int(config.export_size)

    await from_url(url, output_dir, extension, headless, timeout, device_scale_factor)
