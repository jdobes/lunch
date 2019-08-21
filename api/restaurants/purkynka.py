# -*- coding: utf-8 -*-
from datetime import date, timedelta
import logging
import re

from .utils import fetch_html

NAME = "Na Purkyňce"
URL = "http://www.napurkynce.cz/denni-menu/"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_start_date(date_interval):
    end_date = date_interval.split("-")[1].strip()
    end_date_parts = end_date.split(".")
    year = end_date_parts[2]
    if not year:
        year = date.today().year
    end_date = date(int(year),
                    day=int(end_date_parts[0]),
                    month=int(end_date_parts[1]))
    # FIXME: doesn't work for shorter weeks
    start_day = end_date - timedelta(days=4)
    return start_day


def parse_menu():
    today = date.today()
    html = fetch_html(URL)
    result = {}
    if html:
        start_day = None
        for p in html.find_all("p", {"align": "center"}):
            if p.text.startswith("Polední menu"):
                date_interval = p.text.split()[2]
                start_day = get_start_date(date_interval)
            elif re.match(r"\d+\.\d+\.?-\s*\d+\.\d+\.?", p.text):
                date_interval = p.text
                start_day = get_start_date(date_interval)
        if start_day:
            current_date = None
            for span in html.find_all("p", {"align": None}):
                if span.find("strong"):
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

