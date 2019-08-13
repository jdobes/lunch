# -*- coding: utf-8 -*-
from datetime import date
import logging

from .utils import fetch_html

NAME = "Taste of India"
URL = "https://www.taste-of-india.cz/#daily-menu"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    today = date.today()
    html = fetch_html(URL)
    result = {}
    if html:
        current_date = None
        ul = html.find("ul", {"class": "daily-menu"})
        if ul:
            for li in ul.find_all("li"):
                b = li.find("b")
                if b and b.text:
                    current_date = "%s%s" % (b.text.split()[1], today.year)
                    current_date_parts = current_date.split(".")
                    current_date = date(int(current_date_parts[2]),
                                        day=int(current_date_parts[0]),
                                        month=int(current_date_parts[1]))
                    if today <= current_date:
                        result[current_date] = []
                    else:
                        current_date = None
                    b.decompose()
                if current_date:
                    for content_part in li.contents:
                        if content_part.string:
                            result[current_date].append(content_part.string)
    return result
