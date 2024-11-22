# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Padowetz"
URL = "https://www.menicka.cz/2743-restaurant-padowetz.html"
RESTAURANT_ID = "2743"
GPS = (49.1910635, 16.6081007)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
