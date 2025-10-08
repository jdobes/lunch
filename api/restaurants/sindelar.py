# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "Bistro Šindelář"
URL = "https://bistrosindelar.cz/"
RESTAURANT_ID = "3240"
GPS = (49.19915030432933, 16.624299790346296)


def parse_menu():
  menicka_html = fetch_menicka(RESTAURANT_ID)
  return parse_menicka(menicka_html)
