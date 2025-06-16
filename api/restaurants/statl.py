# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Štatl"
URL = "https://www.menicka.cz/4946-statl.html"
RESTAURANT_ID = "4946"
GPS = (49.1955397, 16.6048724)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
