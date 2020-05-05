# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
import logging

from .utils import fetch_html

NAME = "Nepál"
URL = "http://nepalbrno.cz/weekly-menu/"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    today = date.today()
    last_monday = today - timedelta(days=today.weekday())
    html = fetch_html(URL)
    result = {}
    if html:
        current_date = None
        table = html.find("table")
        if table:
            for td in table.find_all("td"):
                date_span = td.find("span")
                if date_span:
                    if "PONDĚLÍ" in date_span.text.upper() or \
                        "ÚTERÝ" in date_span.text.upper() or \
                            "STŘEDA" in date_span.text.upper() or \
                                "ČTVRTEK" in date_span.text.upper() or \
                                    "PÁTEK" in date_span.text.upper():
                                    if current_date is None:
                                        current_date = last_monday
                                    else:
                                        current_date += timedelta(days=1)
                    result[current_date] = []
                elif current_date:
                    if td.text.endswith("Kč"):
                        result[current_date][-1] += " %s" % td.text
                    elif not td.text.strip().isspace() and td.text.strip() not in result[current_date]:
                        result[current_date].append(td.text.strip())
    return result
