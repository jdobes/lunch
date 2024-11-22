# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Radegast Sportpub"
URL = "https://www.menicka.cz/6242-radegast-sportpub.html"
RESTAURANT_ID = "6242"
GPS = (49.1954564, 16.6067429)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
