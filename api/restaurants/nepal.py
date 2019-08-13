# -*- coding: utf-8 -*-
from datetime import date
import logging

from .utils import fetch_html

NAME = "Nepál"
URL = "http://nepalbrno.cz/weekly-menu/"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    today = date.today()
    html = fetch_html(URL)
    result = {}
    if html:
        current_date = None
        table = html.find("table")
        if table:
            for td in table.find_all("td"):
                date_span = td.find("span")
                if date_span:
                    current_date = "%s.%s" % (date_span.text.split("/")[-1], today.year)
                    current_date_parts = current_date.split(".")
                    current_date = date(int(current_date_parts[2]),
                                        day=int(current_date_parts[0]),
                                        month=int(current_date_parts[1]))
                    if today <= current_date:
                        result[current_date] = []
                    else:
                        current_date = None
                elif current_date:
                    if td.text.endswith("Kč"):
                        result[current_date][-1] += " %s" % td.text
                    elif not td.text.isspace():
                        result[current_date].append(td.text)
    return result
