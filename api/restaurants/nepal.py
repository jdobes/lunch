# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
import logging

from .utils import fetch_html

NAME = "TikTok Nepal"
URL = "https://nepalbrno.cz/poledni.php"
GPS = (49.22448917714069, 16.59026497848504)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    today = date.today()
    last_monday = today - timedelta(days=today.weekday())
    html = fetch_html(URL)
    result = {}
    if html:
        current_date = None
        for day_section in html.find_all("div", {"class": "day-section"}):
            day_title = day_section.find("h2", {"class": "day-title"})
            if not day_title:
                continue
            day_title = day_title.text.strip().upper()
            if "MONDAY" in day_title:
                current_date = last_monday
            elif "TUESDAY" in day_title:
                current_date = last_monday + timedelta(days=1)
            elif "WEDNESDAY" in day_title:
                current_date = last_monday + timedelta(days=2)
            elif "THURSDAY" in day_title:
                current_date = last_monday + timedelta(days=3)
            elif "FRIDAY" in day_title:
                current_date = last_monday + timedelta(days=4)
            else:
                continue
            for menu_item in day_section.find_all("div", {"class": "menu-item"}):
                subtags = [subtag.text.strip() for subtag in menu_item]
                result.setdefault(current_date, []).append(" ".join(subtags))

    return result
