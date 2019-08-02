# -*- coding: utf-8 -*-
from .utils import fetch_zomato, parse_zomato

NAME = "U 3 Opic"
URL = "http://www.u3opic.cz/denni-menu/"
RESTAURANT_ID = "16505998"


def parse_menu():
    zomato_json = fetch_zomato(RESTAURANT_ID)
    return parse_zomato(zomato_json)
