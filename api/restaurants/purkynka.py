# -*- coding: utf-8 -*-
from datetime import date, timedelta
import logging

from .utils import fetch_html

NAME = "Na Purkyňce"
URL = "http://www.napurkynce.cz/denni-menu/"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    today = date.today()
    html = fetch_html(URL)
    result = {}
    if html:
        start_day = None
        for p in html.find_all("p", {"align": "center"}):
            if p.text.startswith("Polední menu"):
                date_interval = p.text.split()[2]
                end_date = date_interval.split("-")[1]
                end_date_parts = end_date.split(".")
                end_date = date(int(end_date_parts[2]),
                                day=int(end_date_parts[0]),
                                month=int(end_date_parts[1]))
                # FIXME: doesn't work for shorter weeks
                start_day = end_date - timedelta(days=4)
        
        if start_day:
            current_date = None
            for span in html.find_all("span", {"style": "font-size: small;"}):
                if span.find("strong"):
                    if current_date is None:
                        current_date = start_day
                    else:
                        current_date += timedelta(days=1)
                    if today <= current_date:
                        result[current_date] = [span.text]
                elif current_date and current_date in result:
                    result[current_date].append(span.text)
    return result
