# -*- coding: utf-8 -*-
from datetime import date
from .utils import fetch_html

NAME = "Rubín"
URL = "http://restauracerubin.cz/"


def parse_menu():
    today = date.today()
    html = fetch_html(URL)
    result = {}
    if html:
        result[today] = []
        for table in html.find_all("table", class_="menu_table"):
            for tr in table.find_all("tr"):
                cells = [td.text.strip() for td in tr.find_all("td")]
                result[today].append(' '.join(cells))

    return result
