# -*- coding: utf-8 -*-
from datetime import date, timedelta
import logging
import re
import subprocess
import tempfile

from unidecode import unidecode

from .utils import fetch, fetch_html

NAME = "Jean Paul's"
URL = "https://www.jpbistro.cz/technologicky-park/"
GPS = (49.230641595778884, 16.576966498445827)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    html = fetch_html(URL)
    if not html:
        return {}
    menu_link = html.find("a", string="Obědové menu")
    if not menu_link:
        logger.warning("Could not find Jean Paul's lunch menu button")
        return {}
    response = fetch(menu_link.get("href"), stream=True)
    with tempfile.NamedTemporaryFile() as fp:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                fp.write(chunk)
        fp.flush()

        pdf_raw_text = subprocess.check_output(["pdftotext", "-q", "-layout", "-f", "1", "-l", "1", fp.name, "-"])
        lines = pdf_raw_text.decode("utf-8").split("\n")


    result = {}
    last_monday = date.today() - timedelta(days=date.today().weekday())

    all_week_menu_started = False
    all_week_menu = []

    current_date = None
    for line in lines:
        if "pondeli" in unidecode(line.lower()):
            current_date = last_monday
        elif "utery" in unidecode(line.lower()):
            current_date = last_monday + timedelta(days=1)
        elif "streda" in unidecode(line.lower()):
            current_date = last_monday + timedelta(days=2)
        elif "ctvrtek" in unidecode(line.lower()):
            current_date = last_monday + timedelta(days=3)
        elif "patek" in unidecode(line.lower()):
            current_date = last_monday + timedelta(days=4)
        elif "obedove menu" in unidecode(line.lower()):
            pass
        elif "tydenni menu" in unidecode(line.lower()):
            current_date = None
            all_week_menu_started = True
            all_week_menu.append("")
            all_week_menu.append(line.strip())
        elif current_date and line.strip():
            result.setdefault(current_date, []).append(line.strip())
        elif all_week_menu_started and not line.startswith(" "):
            all_week_menu.append(line.strip())

    # Copy all week menu to all days
    for days_offset in range(5):
        current_date = last_monday + timedelta(days=days_offset)
        result.setdefault(current_date, []).extend(all_week_menu)

    return result


if __name__ == "__main__":
    # Debugging
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    parse_menu()
