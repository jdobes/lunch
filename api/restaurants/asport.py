# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "A-Sport Hotel"
URL = "https://www.menicka.cz/2680-restaurace-campo-a-sport-hotel.html"
RESTAURANT_ID = "2680"
GPS = (49.226724688140656, 16.584220478889034)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
