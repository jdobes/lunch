from datetime import datetime
import logging
from datetime import date

import requests
from bs4 import BeautifulSoup
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

MENICKA_URL = "https://www.menicka.cz/api/iframe/?id=%s"

EMPTY_RESPONSES = {
    "Pro tento den nebylo zadáno menu.",
    "Restaurace má tento den zavřeno.",
    "Denní menu dle nabídky v restauraci",
}

GEMINI_MODEL = "gemini-3-flash-preview"
#GEMINI_MODEL = "gemma-3-27b-it"


class DailyMenu(BaseModel):
    day: date = Field()
    menu_lines: List[str]


class WeeklyMenu(BaseModel):
    days: List[DailyMenu]


def fetch(url, encoding=None, stream=False):
    for _ in range(3):
        try:
            response = requests.get(url, stream=stream)
            if encoding:
                response.encoding = encoding
            if response.status_code == 200:
                return response
            logger.warning("Error during fetching url %s: HTTP %s, %s",
                           url, response.status_code, response.text)
        except requests.exceptions.RequestException:
            logger.warning("Error fetching url.")
    logger.error("URL not fetched.")
    return None


def fetch_html(url, encoding="utf-8"):
    response = fetch(url, encoding=encoding)
    if response:
        return BeautifulSoup(response.text, features="lxml")
    return None


def fetch_menicka(restaurant_id):
    return fetch_html(MENICKA_URL % restaurant_id, encoding="windows-1250")


def parse_menicka(html):
    result = {}
    for content in html.find_all("div", {"class": "content"}):
        h2 = content.find("h2")
        if h2:
            current_date = datetime.strptime(h2.text.split()[1], "%d.%m.%Y").date()
            for tr in content.find_all("tr"):
                for alergen in tr.find_all("em"):
                    alergen.extract()
                if tr.text not in EMPTY_RESPONSES:
                    result.setdefault(current_date, []).append(tr.text)
    return result


def gemini_parse_menu(image_path, prompt):
    result = {}
    with open(image_path, "rb") as f:
        image_bytes = f.read()
    client = genai.Client()
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/jpeg",
            ),
            prompt
        ],
        config={
            "response_mime_type": "application/json",
            "response_json_schema": WeeklyMenu.model_json_schema(),
        },
    )
    weekly_menu = WeeklyMenu.model_validate_json(response.text)
    for daily_menu in weekly_menu.days:
        for menu_line in daily_menu.menu_lines:
            result.setdefault(daily_menu.day, []).append(menu_line)
    return result
