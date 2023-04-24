# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Portoriko"
URL = "https://www.menicka.cz/8467-portoriko.html"
RESTAURANT_ID = "8467"


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
