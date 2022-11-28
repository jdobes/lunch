# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
import logging

from .utils import fetch_html

NAME = "TikTok Nepal"
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
        for tr in html.find_all("tr"):
            for td in tr.find_all("td"):
                date_span = td.find("span")
                if date_span:
                    if "MONDAY" in date_span.text.upper():
                        current_date = last_monday
                    elif "TUESDAY" in date_span.text.upper():
                        current_date = last_monday + timedelta(days=1)
                    elif "WEDNESDAY" in date_span.text.upper():
                        current_date = last_monday + timedelta(days=2)
                    elif "THURSDAY" in date_span.text.upper():
                        current_date = last_monday + timedelta(days=3)
                    elif "FRIDAY" in date_span.text.upper():
                        current_date = last_monday + timedelta(days=4)
                    else:
                        current_date = None
                    if current_date:
                        result[current_date] = []
                elif current_date:
                    if td.text.endswith("Kč"):
                        result[current_date][-1] += " %s" % td.text
                    elif not td.text.strip().isspace() and td.text.strip() and td.text.strip() not in result[current_date]:
                        result[current_date].append(td.text.strip())
    return result
