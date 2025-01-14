# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Kancl Bistro"
URL = "https://www.menicka.cz/8518-kancl-bistro.html"
RESTAURANT_ID = "8518"
GPS = (49.233248203147234, 16.572702342426847)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
