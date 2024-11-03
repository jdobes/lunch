# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Správné Místo"
URL = "https://www.menicka.cz/5335-spravne-misto.html"
RESTAURANT_ID = "5335"
GPS = (49.22367996117323, 16.593952181254043)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
