# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
import logging

from .utils import fetch_html

NAME = "TikTok Nepal"
URL = "https://nepalbrno.cz/weekly-menu/"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    today = date.today()
    last_monday = today - timedelta(days=today.weekday())
    html = fetch_html(URL)
    result = {}
    if html:
        current_date = None
        for tr in html.find_all("tr"):
            for td in tr.find_all("td"):
                txt = td.text.strip()
                if "MONDAY" in txt.upper():
                    current_date = last_monday
                elif "TUESDAY" in txt.upper():
                    current_date = last_monday + timedelta(days=1)
                elif "WEDNESDAY" in txt.upper():
                    current_date = last_monday + timedelta(days=2)
                elif "THURSDAY" in txt.upper():
                    current_date = last_monday + timedelta(days=3)
                elif "FRIDAY" in txt.upper():
                    current_date = last_monday + timedelta(days=4)
                elif current_date:
                    if txt.endswith("Kč"):
                        result[current_date][-1] += " %s" % txt  # should always follow a meal
                    elif txt:  # filter out empty strings
                        result.setdefault(current_date, []).append(txt)
    return result
