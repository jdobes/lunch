# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Velorex"
URL = "https://www.menicka.cz/6714-velorex.html"
RESTAURANT_ID = "6714"


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
