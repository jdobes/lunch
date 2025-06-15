# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Sesamo"
URL = "https://www.menicka.cz/9544-sesamo.html"
RESTAURANT_ID = "9544"
GPS = (49.22562107171892, 16.581867425634258)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
