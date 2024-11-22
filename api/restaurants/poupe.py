# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Pivovarský dům Poupě"
URL = "https://www.menicka.cz/8656-pivovarsky-dum-poupe.html"
RESTAURANT_ID = "8656"
GPS = (49.1925546, 16.6052437)


def parse_menu():
    menicka_html = fetch_menicka(RESTAURANT_ID)
    return parse_menicka(menicka_html)
