from datetime import date, timedelta
import logging
import os

from playwright.sync_api import sync_playwright, expect
from unidecode import unidecode

NAME = "Sesamo"
URL = "https://www.facebook.com/sesamobrno"
GPS = (49.22562107171892, 16.581867425634258)

PLAYWRIGHT_PROXY = os.getenv("PLAYWRIGHT_PROXY", "")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    result = {}
    last_monday = date.today() - timedelta(days=date.today().weekday())
    with sync_playwright() as playwright:
        kwargs = {
            "viewport": {"width": 1080, "height": 1920},
            "locale": "cs-CZ"
        }
        if PLAYWRIGHT_PROXY:
            kwargs["proxy"] = {"server": PLAYWRIGHT_PROXY}
        browser = playwright.firefox.launch(headless=True)
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
            show_more_clicked = False
            if show_more_button.is_visible():
                show_more_clicked = True
                show_more_button.click()
            lines = post.locator("[style='text-align: start;']").all()
            logger.debug("Post %d, show_more_clicked=%s, lines=%d", idx+1, show_more_clicked, len(lines))

            lines = [line.text_content() for line in lines]

            menu_found = False
            for line in lines:
                if "denni menu" in unidecode(line.lower()):
                    menu_found = True
                    break

            if menu_found:
                for days_offset in range(5):
                    current_date = last_monday + timedelta(days=days_offset)
                    # Copy the full text to all days because the format is really inconsistent every week
                    result[current_date] = lines
                logger.debug("Seems like post %d contains menu, skipping the rest.", idx+1)
                break

        #page.pause()
        #page.screenshot(path="example.png")
        browser.close()

        if not result:
            logger.debug("No menu found in posts.")

    return result


if __name__ == "__main__":
    # Debugging
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    parse_menu()
