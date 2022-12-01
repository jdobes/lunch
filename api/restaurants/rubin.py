# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Rubín"
URL = "https://www.menicka.cz/2749-restaurace-rubin.html"
RESTAURANT_ID = "2749"


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
