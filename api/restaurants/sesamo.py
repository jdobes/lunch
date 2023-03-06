# -*- coding: utf-8 -*-
from datetime import date, timedelta

from unidecode import unidecode

from .utils import fetch_html

NAME = "Sesamo"
URL = "https://sesamobrno.cz/menu/"


def format_date_line(tr):
    columns = [td.text.strip() for td in tr.find_all('td')]
    return unidecode(columns[1].lower())


def format_menu_line(tr):
    columns = [td.text.strip() for td in tr.find_all('td')]
    if not any(columns):
        return ""
    return f"{columns[0]} - {columns[1]} {columns[3]} Kč"


def parse_menu():
    today = date.today()
    last_monday = today - timedelta(days=today.weekday())
    html = fetch_html(URL)
    result = {}
    if html:
        current_date = None
        all_days_menu = []
        buffered_lines = []
        menu = html.find("article").find("table")
        for tr in menu.find_all('tr'):
            if "pondeli" in format_date_line(tr):
                buffered_lines = all_days_menu.copy()
                current_date = last_monday
            elif "utery" in format_date_line(tr):
                if current_date:
                    result[current_date] = buffered_lines
                buffered_lines = all_days_menu.copy()
                current_date = last_monday + timedelta(days=1)
            elif "streda" in format_date_line(tr):
                if current_date:
                    result[current_date] = buffered_lines
                buffered_lines = all_days_menu.copy()
                current_date = last_monday + timedelta(days=2)
            elif "ctvrtek" in format_date_line(tr):
                if current_date:
                    result[current_date] = buffered_lines
                buffered_lines = all_days_menu.copy()
                current_date = last_monday + timedelta(days=3)
            elif "patek" in format_date_line(tr):
                if current_date:
                    result[current_date] = buffered_lines
                buffered_lines = all_days_menu.copy()
                current_date = last_monday + timedelta(days=4)
            else:
                if not current_date:
                    all_days_menu.append(format_menu_line(tr))
                else:
                    buffered_lines.append(format_menu_line(tr))
        if current_date:
            result[current_date] = buffered_lines

    return result
