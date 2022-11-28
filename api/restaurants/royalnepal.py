# -*- coding: utf-8 -*-
from datetime import date, timedelta
import logging

from unidecode import unidecode

from .utils import fetch_html

NAME = "Royal Nepal"
URL = "https://www.royalnepal.cz/#daily-menu"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def format_date_line(day_menu):
    day = day_menu.find("p", {"class": "weeklyDay"})
    if day:
        return unidecode(day.text.lower())
    else:
        return ""


def format_menu(day_menu):
    lines = []
    for table in day_menu.find_all("table", {"class": "mealContainer"}):
        for tr in table.find_all("tr", {"class": "menuPageMealName"}):
            buff = []
            for td in tr.find_all("td"):
                text = td.text.strip()
                if text:
                    buff.append(text)
            lines.append(" ".join(buff))
    return lines


def parse_menu():
    today = date.today()
    last_monday = today - timedelta(days=today.weekday())
    html = fetch_html(URL)
    result = {}
    if html:
        current_date = last_monday
        menu = html.find("ul", {"class": "daily-menu"})
        for day_menu in menu.find_all('div', {"class": "weeklyDayCont"}):
            if "pondeli" in format_date_line(day_menu):
                result[current_date] = format_menu(day_menu)
            elif "utery" in format_date_line(day_menu):
                current_date = last_monday + timedelta(days=1)
                result[current_date] = format_menu(day_menu)
            elif "streda" in format_date_line(day_menu):
                current_date = last_monday + timedelta(days=2)
                result[current_date] = format_menu(day_menu)
            elif "ctvrtek" in format_date_line(day_menu):
                current_date = last_monday + timedelta(days=3)
                result[current_date] = format_menu(day_menu)
            elif "patek" in format_date_line(day_menu):
                current_date = last_monday + timedelta(days=4)
                result[current_date] = format_menu(day_menu)

    return result
