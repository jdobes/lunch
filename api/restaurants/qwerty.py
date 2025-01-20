# -*- coding: utf-8 -*-
import logging
from datetime import date, timedelta
from unidecode import unidecode

from .utils import fetch_html

NAME = "Qwerty"
URL = "https://qwerty-restaurant--catering3.webnode.cz/menu/"
GPS = (49.235655201154906, 16.573111921257983)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def format_line(line):
    return (
        line.text.strip().replace("\n", " ").replace("1)", "\n1)").replace("Kč", "Kč\n")
    )


def parse_menu():
    current_date = None
    last_monday = date.today() - timedelta(days=date.today().weekday())
    result = {}
    weekly_section = False
    weekly_offer = []
    html = fetch_html(URL)
    if html:
        for line in html.find_all("div", {"class": "mt-i cf"}):
            txt = format_line(line)
            day_identifier = unidecode(txt.lower())

            if "pondeli" in day_identifier:
                current_date = last_monday
                txt = txt.replace("PONDĚLÍ", "")
            elif "utery" in day_identifier:
                current_date = last_monday + timedelta(days=1)
                txt = txt.replace("ÚTERÝ", "")
            elif "streda" in day_identifier:
                current_date = last_monday + timedelta(days=2)
                txt = txt.replace("STŘEDA", "")
            elif "ctvrtek" in day_identifier:
                current_date = last_monday + timedelta(days=3)
                txt = txt.replace("ČTVRTEK", "")
            elif "patek" in day_identifier:
                current_date = last_monday + timedelta(days=4)
                txt = txt.replace("PÁTEK", "")
            elif "tydenni" in day_identifier and not "polevka" in day_identifier:
                current_date = None
                weekly_section = True
                txt = txt.replace("TÝDENNÍ MENU", "")

            if current_date and txt:
                result.setdefault(current_date, []).append(txt)
            elif weekly_section and txt:
                weekly_offer.append(txt)

        if weekly_offer:
            for _, offer in result.items():
                offer.append("All week:")
                offer.extend(weekly_offer)

    if not result:
        logger.error("No menu found.")

    return result


if __name__ == "__main__":
    # Debugging
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    parse_menu()
