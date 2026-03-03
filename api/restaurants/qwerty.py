import logging
import os
import requests

from playwright.sync_api import sync_playwright, expect

from .utils import gemini_parse_menu

NAME = "Qwerty"
URL = "https://www.facebook.com/QwertyRestaurant"
GPS = (49.235655201154906, 16.573111921257983)

PLAYWRIGHT_WS_ENDPOINT = os.getenv("PLAYWRIGHT_WS_ENDPOINT", "")
PLAYWRIGHT_PROXY = os.getenv("PLAYWRIGHT_PROXY", "")

GEMINI_PROMPT = """Obrázek obsahuje denní menu na celý týden.
Pro každý den poskládej seznam, co je právě k dispozici - jídla pro konkrétní den + týdenní menu + stálá nabídka.
Vynechej alergeny označené čísly. Na konec každého řádku přidej cenu, pokud je k dispozici.
Na začátek řádku, který označuje polévku, přidej "Polévka: ".
Rozděl výsledek do jednotlivých sekcí - polévky, menu označené čísly, stálé menu - které jsou odděleny prázdným řádkem.
Pokud se nejedná o seznam jídel na celý týden, vrať prázdný výsledek.
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    result = {}
    if not PLAYWRIGHT_WS_ENDPOINT:
        logger.warning("Playwright websocket not set! Can't sync.")
        return result
    downloaded = []
    with sync_playwright() as playwright:
        kwargs = {
            "viewport": {"width": 1080, "height": 1920},
            "locale": "cs-CZ"
        }
        if PLAYWRIGHT_PROXY:
            kwargs["proxy"] = {"server": PLAYWRIGHT_PROXY}
        browser = playwright.chromium.connect(PLAYWRIGHT_WS_ENDPOINT)
        context = browser.new_context(**kwargs)
        page = context.new_page()
        page.goto(URL)

        cookie_button = page.get_by_role("button", name="Odmítnout")
        expect(cookie_button).to_be_visible()
        cookie_button.click()

        login_close_button = page.get_by_role("button", name="Zavřít")
        expect(login_close_button).to_be_visible()
        login_close_button.click()

        # Wait for initial posts to load
        page.wait_for_load_state("networkidle")

        posts = page.locator("[data-ad-preview='message']").all()
        logger.debug("Checking last %d posts.", len(posts))
        for idx, post in enumerate(posts):
            show_more_button = post.get_by_role("button", name="Zobrazit víc")
            if show_more_button.is_visible():
                show_more_button.click()

            try:
                article = post.locator("xpath=ancestor::div[@role='article']")
                images = article.locator("img").all()
                for img_idx, img in enumerate(images):
                    src = img.get_attribute("src")
                    height = img.get_attribute("height")
                    height = int(height) if height else 0
                    # Should be a large image, but it's scaled to render resolution, just guess some value
                    if src and height > 400:
                        try:
                            response = requests.get(src, timeout=10)
                            if response.status_code == 200:
                                filename = f"/tmp/qwerty_{idx}_{img_idx}.jpg"
                                with open(filename, "wb") as f:
                                    f.write(response.content)
                                logger.debug("Downloaded image %s", filename)
                                downloaded.append(filename)
                        except Exception as e:
                            logger.warning("Failed to download image: %s", e)
            except Exception as e:
                logger.warning("Error processing post images: %s", e)

        #page.pause()
        #page.screenshot(path="example.png")
        browser.close()

    # Try the newest image, if the image isn't menu we are screwed
    if downloaded:
        result = gemini_parse_menu(downloaded[0], GEMINI_PROMPT)

    if not result:
        logger.warning("No menu found in the last image.")

    # Cleanup
    for image_path in downloaded:
        os.unlink(image_path)

    return result


if __name__ == "__main__":
    # Debugging
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    parse_menu()
