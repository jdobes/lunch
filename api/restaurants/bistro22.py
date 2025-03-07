# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Bistro 22"
URL = "https://www.menicka.cz/6042-bistro-22.html"
RESTAURANT_ID = "6042"
GPS = (49.23297778720801, 16.572881702739807)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
