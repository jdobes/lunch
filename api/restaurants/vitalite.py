# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Vitalite"
URL = "https://www.menicka.cz/2713-vitalite-zdravy-restaurant.html"
RESTAURANT_ID = "2713"
GPS = (49.23376373453886, 16.58362622482164)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
