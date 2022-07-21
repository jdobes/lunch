# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "U Hřebíčků"
URL = "https://www.menicka.cz/5349-u-hrebicku.html"
RESTAURANT_ID = "5349"


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
