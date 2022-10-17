# -*- coding: utf-8 -*-
from datetime import date, timedelta

from .utils import fetch_html

NAME = "Jean Paul's"
URL = "https://www.jpbistro.cz/menu-technopark/index.php"


def parse_menu():
    today = date.today()
    last_monday = today - timedelta(days=today.weekday())
    html = fetch_html(URL)
    result = {}
    if html:
        current_date = None
        menu = html.find('div', { 'class': 'denni-menu'})
        if menu:
            for tag in menu:
                if tag.name == "h2":
                    if "pondělí" in tag.text.lower():
                        current_date = last_monday
                    elif "úterý" in tag.text.lower():
                        current_date = last_monday + timedelta(days=1)
                    elif "středa" in tag.text.lower():
                        current_date = last_monday + timedelta(days=2)
                    elif "čtvrtek" in tag.text.lower():
                        current_date = last_monday + timedelta(days=3)
                    elif "pátek" in tag.text.lower():
                        current_date = last_monday + timedelta(days=4)
                elif tag.name == "table" and current_date:
                    result[current_date] = []
                    for tr in tag.find_all('tr'):
                        line = [td.text.strip() for td in tr.find_all('td')]
                        result[current_date].append(' '.join(line))

    return result
