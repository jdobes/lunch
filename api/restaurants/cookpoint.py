# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Cook Point"
URL = "https://www.menicka.cz/4931-cook-point.html"
RESTAURANT_ID = "4931"
GPS = (49.23315155270968, 16.5747760173388)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
