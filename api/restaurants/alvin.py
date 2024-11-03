# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Alvin"
URL = "https://www.menicka.cz/2774-alvin.html"
RESTAURANT_ID = "2774"


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
