# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Charlie Square"
URL = "https://www.menicka.cz/3178-charlie-square.html"
RESTAURANT_ID = "3178"
GPS = (49.1927189,16.6087498)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
