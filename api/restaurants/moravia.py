# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Moravia"
URL = "https://www.menicka.cz/6898-pivovarska-restaurace-moravia.html"
RESTAURANT_ID = "6898"
GPS = (49.2419954462168, 16.574225830188137)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
