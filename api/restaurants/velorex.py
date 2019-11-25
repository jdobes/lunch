# -*- coding: utf-8 -*-
from datetime import date
import logging

from .utils import fetch_html

NAME = "Velorex"
URL = "http://www.restauracevelorex.cz/poledni-menu/"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    today = date.today()
    html = fetch_html(URL)
    result = {}
    if html:
        current_date = None
        clanek = html.find("div", {"id": "clanek"})
        if clanek:
            for h2 in clanek.find_all(["h2", "h3", "tr"]):
                if h2.text.lower().startswith("pondělí") or \
                    h2.text.lower().startswith("úterý") or \
                        h2.text.lower().startswith("středa") or \
                            h2.text.lower().startswith("čtvrtek") or \
                                h2.text.lower().startswith("pátek"):
                    current_date = "".join(h2.text.split()[1:])
                    current_date_parts = current_date.split(".")
                    current_date = date(int(current_date_parts[2]),
                                        day=int(current_date_parts[0]),
                                        month=int(current_date_parts[1]))
                    if today <= current_date:
                        result[current_date] = []
                    else:
                        current_date = None
                elif current_date:
                    if h2.text.endswith("Kč"):
                        result[current_date][-1] += " %s" % h2.text
                    elif not h2.text.isspace():
                        result[current_date].append(h2.text)
    return result


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    result = parse_menu()
    logger.info(result)