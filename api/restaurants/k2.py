# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "K2"
URL = "https://www.k2gastro.cz/"
RESTAURANT_ID = "3912"
GPS = (49.199286292912774, 16.624712486703416)


def parse_menu():
  menicka_html = fetch_menicka(RESTAURANT_ID)
  return parse_menicka(menicka_html)
