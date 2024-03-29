# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "U Kotelny"
URL = "https://www.menicka.cz/3934-u-kotelny.html"
RESTAURANT_ID = "3934"


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
