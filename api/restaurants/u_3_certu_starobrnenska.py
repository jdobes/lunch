# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "U Třech čertů - Starobrněnská"
URL = "https://www.menicka.cz/8402-u-trech-certu-starobrnenska.html"
RESTAURANT_ID = "8402"
GPS = (49.192292, 16.607138)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
