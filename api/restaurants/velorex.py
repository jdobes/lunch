# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
import logging

from .utils import fetch_html

NAME = "Velorex"
URL = "https://www.primesteak.cz/menu/denni-menu/"

def parse_menu():
    today = date.today()
    html = fetch_html(URL)
    result = {}
    if html:
        menu = html.find('div', { 'class': 'menu today'})
        if menu:
            result[today] = []
            for tr in menu.find_all('tr'):
                line = [td.text.strip() for td in tr.find_all('td')]
                result[today].append(' '.join(line))

    return result

if __name__ == '__main__':
    print(parse_menu())
