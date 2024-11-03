# -*- coding: utf-8 -*-
from datetime import date, timedelta
import logging

from unidecode import unidecode

from .utils import fetch_html

NAME = "Royal Nepal"
URL = "https://www.royalnepal.cz/kralovo-pole/weekly-menu"
GPS = (49.22052154321084, 16.58709101916278)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def format_line(row):
    return " ".join([col.text.strip().replace("\n", "") for col in row.find_all("div", recursive=False)])


def parse_menu():
    today = date.today()
    last_monday = today - timedelta(days=today.weekday())
    html = fetch_html(URL)
    result = {}
    if html:
        current_date = None
        for row in html.find_all("div", {"class": "row"}):
            txt = format_line(row)
            if "pondeli" in unidecode(txt.lower()):
                current_date = last_monday
            elif "utery" in unidecode(txt.lower()):
                current_date = last_monday + timedelta(days=1)
            elif "streda" in unidecode(txt.lower()):
                current_date = last_monday + timedelta(days=2)
            elif "ctvrtek" in unidecode(txt.lower()):
                current_date = last_monday + timedelta(days=3)
            elif "patek" in unidecode(txt.lower()):
                current_date = last_monday + timedelta(days=4)
            elif current_date and txt:
                result.setdefault(current_date, []).append(txt)
    return result
