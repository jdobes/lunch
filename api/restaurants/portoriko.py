# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Portoriko"
URL = "https://www.menicka.cz/8467-portoriko.html"
RESTAURANT_ID = "8467"
GPS = (49.229342495214716, 16.585719232937716)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
