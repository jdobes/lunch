# -*- coding: utf-8 -*-
from datetime import date, timedelta
import logging

from .utils import fetch_html

NAME = "Liquid Bread"
URL = "http://www.liquidbread.cz/liquidbread/liquidbread/mainmenu/daily-menu/"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    today = date.today()
    html = fetch_html(URL)
    result = {}
    if html:
        start_day = None
        for elem in html.find_all(["h2", "p"]):
            if elem.text.lower().startswith("polední menu") or elem.text.lower().startswith("denní menu"):
                date_interval = "".join(elem.text.split()[2:])
                end_date = date_interval.split("-")[1]
                end_date_parts = end_date.split(".")
                end_date = date(int(end_date_parts[2]),
                                day=int(end_date_parts[0]),
                                month=int(end_date_parts[1]))
                # FIXME: doesn't work for shorter weeks
                start_day = end_date - timedelta(days=4)

        if start_day:
            current_date = None
            for span in html.find_all("p", {"align": None}):
                if span.text.upper().startswith("PO") or span.text.upper().startswith("ÚT") or span.text.upper().startswith("ST") or \
                    span.text.upper().startswith("ČT") or span.text.upper().startswith("PÁ"):
                    if current_date is None:
                        current_date = start_day
                    else:
                        current_date += timedelta(days=1)
                    if today <= current_date:
                        result[current_date] = [span.text]
                elif current_date and current_date in result and span.text and not span.text.isspace():
                    result[current_date].append(span.text)
    return result


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    result = parse_menu()
    logger.info(result)
