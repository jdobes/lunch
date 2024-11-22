# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Tusto Titanium"
URL = "https://www.menicka.cz/2787-tusto-titanium.html"
RESTAURANT_ID = "2787"
GPS = (49.1881093, 16.6062952)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
