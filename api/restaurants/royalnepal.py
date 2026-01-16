# -*- coding: utf-8 -*-
from datetime import date, timedelta
import logging

from .utils import fetch_html

NAME = "Royal Nepal"
URL = "https://www.royalnepal.cz/MC/HANDLERS/getDocument.php?name=WEEKLY&location=kralovopole&language=cz"
GPS = (49.22052154321084, 16.58709101916278)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    today = date.today()
    last_monday = today - timedelta(days=today.weekday())
    html = fetch_html(URL)
    result = {}
    if html:
        for weekday, day_section in enumerate(html.find_all("div", {"class": "weekly-template-container12"})):
            current_date = last_monday + timedelta(weekday)
            menu = []
            soup = day_section.find("div", {"mc-template": "soup"})
            if soup:
                menu.append(soup.get_text(" ", True))
            for main in day_section.find_all("div", {"mc-template": "main"}):
                menu.append(main.get_text(" ", True))
            for weekly_main in day_section.find_all("div", {"mc-template": "weekly"}):
                menu.append(weekly_main.get_text(" ", True))
            result[current_date] = menu
    return result
