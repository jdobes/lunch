# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Kanas Restaurant"
URL = "https://www.menicka.cz/2684-kanas-restaurant.html"
RESTAURANT_ID = "2684"
GPS = (49.22818841008108, 16.57621211364726)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
