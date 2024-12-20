# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Pad Thai"
URL = "https://www.menicka.cz/8483-padthai.html"
RESTAURANT_ID = "8483"
GPS = (49.226962510832315, 16.593589162262358)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
