# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
import logging

from .utils import fetch_html

NAME = "Prime Steak"
URL = "https://www.primesteak.cz/menu/denni-menu/"
GPS = (49.23179189396761, 16.590378328190717)

def parse_menu():
    today = date.today()
    html = fetch_html(URL)
    result = {}
    if html:
        menu = html.find('div', { 'class': 'menu today'})
        if menu:
            for tr in menu.find_all('tr'):
                line = [td.text.strip() for td in tr.find_all('td')]
                result.setdefault(today, []).append(' '.join(line))

    return result

if __name__ == '__main__':
    print(parse_menu())
