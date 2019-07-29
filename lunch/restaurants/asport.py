import logging

from .utils import fetch_html

NAME = "A-Sport Hotel"
URL = "http://www.a-sporthotel.cz/menu/"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    html = fetch_html(URL)
    result = {}
    if html:
        current_date = None
        for tr in html.find_all("tr"):
            for td in tr.find_all("td"):
                if td.get("class") == ["tmain"]:
                    current_date = td.text.split()[1]
                    result[current_date] = []
                elif current_date:
                    result[current_date].append(td.text)
    return result