from datetime import date, timedelta
import logging
import os

from playwright.sync_api import sync_playwright, expect
from unidecode import unidecode

NAME = "Qwerty"
URL = "https://www.facebook.com/QwertyRestaurant"
GPS = (49.235655201154906, 16.573111921257983)

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

            current_date = None
            weekly_section = False
            weekly_offer = []
            # Strip first line with dates
            for line in lines:
                txt = line.text_content()
                day_identifier = unidecode(txt.lower())
                if "pondeli" == day_identifier:
                    current_date = last_monday
                elif "utery" == day_identifier:
                    current_date = last_monday + timedelta(days=1)
                elif "streda" == day_identifier:
                    current_date = last_monday + timedelta(days=2)
                elif "ctvrtek" == day_identifier:
                    current_date = last_monday + timedelta(days=3)
                elif "patek" == day_identifier:
                    current_date = last_monday + timedelta(days=4)
                elif ("tydenni" in day_identifier or "tydne" in day_identifier) and not "polevka" in day_identifier:
                    current_date = None
                    weekly_section = True
                elif current_date and txt:
                    result.setdefault(current_date, []).append(txt)
                elif weekly_section and txt:
                    weekly_offer.append(txt)

            if weekly_offer:
                for _, offer in result.items():
                    offer.append("")
                    offer.append("All week:")
                    offer.extend(weekly_offer)

            if result:
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
