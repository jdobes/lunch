# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Na Purkyňce"
URL = "https://www.menicka.cz/2647-na-purkynce.html"
RESTAURANT_ID = "2647"


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
