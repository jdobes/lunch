# -*- coding: utf-8 -*-
from datetime import date, timedelta
import logging

from .utils import fetch_html

NAME = "Royal Nepal"
URL = "https://www.royalnepal.cz/MC/HANDLERS/getDocument.php?name=WEEKLY&location=kralovopole&language=cz"
GPS = (49.22052154321084, 16.58709101916278)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


WEEKDAYS = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4}


def parse_menu():
    today = date.today()
    last_monday = today - timedelta(days=today.weekday())
    html = fetch_html(URL)
    result = {}
    if html:
        for day_section in html.find_all("div", {"class": "tabCont"}):
            weekday = WEEKDAYS.get(day_section.get("mc-data"))
            if weekday is None:
                continue
            current_date = last_monday + timedelta(weekday)
            result[current_date] = [item.get_text(" ", True) for item in day_section.find_all("div", {"mc-template": "item"})]
    return result
