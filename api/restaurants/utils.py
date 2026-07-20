from datetime import datetime
import functools
import json
import logging
from datetime import datetime
import base64
import os

import requests
from bs4 import BeautifulSoup
from openai import OpenAI, OpenAIError


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-6-luna")

MENICKA_URL = "https://www.menicka.cz/api/iframe/?id=%s"

EMPTY_RESPONSES = {
    "Pro tento den nebylo zadáno menu.",
    "Restaurace má tento den zavřeno.",
    "Denní menu dle nabídky v restauraci",
}

SYSTEM_PROMPT = """
Uživatel zadá formátovací instrukce pro týdenní menu restaurace a samotný obsah menu.
Obsah menu může být ve formě přiloženého obrázku.
Vrať výsledek ve formátu JSON. 

PŘÍKLAD JSON VÝSTUPU:
{
    "days": [
      {
        "day": "2026-05-12",
        "menu_lines": [
            "item1",
            "item2"
        ]
      }
    ]
}
"""


def fetch(url, encoding=None, stream=False):
    for _ in range(3):
        try:
            response = requests.get(
                url,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"},
                stream=stream
            )
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
    return fetch_html(MENICKA_URL % restaurant_id)


def parse_menicka(html):
    result = {}
    for content in html.find_all("div", {"class": "content"}):
        h2 = content.find("h2")
        if h2:
            current_date = datetime.strptime(h2.text.split()[1], "%d.%m.%Y").date()
            for tr in content.find_all("tr"):
                for alergen in tr.find_all("em"):
                    alergen.extract()
                line = ""
                for td in tr.find_all("td"):
                    td_text = td.text.strip()
                    if line and td_text:
                        line += " "
                    line += td_text
                if line not in EMPTY_RESPONSES:
                    result.setdefault(current_date, []).append(line)
    return result


def is_llm_available() -> bool:
    return all((
        OPENAI_BASE_URL,
        OPENAI_MODEL,
        os.getenv("OPENAI_API_KEY", ""),
    ))


def llm_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not is_llm_available():
            logger.warning("LLM is required for %s parser!", func.__name__)
            return {}
        return func(*args, **kwargs)
    return wrapper


def llm_parse_menu(prompt, image_path=None):
    result = {}
    
    messages = [{"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": [{"type": "text", "text": prompt}]}]
    if image_path:
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        image_b64 = base64.b64encode(image_bytes).decode("utf-8")
        messages[1]["content"].append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"},
        })

    extra_headers = {}
    # Workaround for OpenCode Go API
    if "opencode" in OPENAI_BASE_URL and "go" in OPENAI_BASE_URL:
        extra_headers["x-opencode-session"] = "lunch"

    client = OpenAI()
    try:
        # Make sure to set correctly in environment:
        #   OPENAI_BASE_URL
        #   OPENAI_API_KEY
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            response_format={
                "type": "json_object",
            },
            reasoning_effort="medium",
            extra_headers=extra_headers,
        )
    except OpenAIError as exc:
        logger.warning("OpenAI-like API returned error: %s", exc)
        return result

    try:
        weekly_menu = json.loads(response.choices[0].message.content)
    except json.JSONDecodeError as exc:
        logger.warning("Unable to parse JSON returned from LLM: %s", exc)
        return result

    for daily_menu in weekly_menu["days"]:
        for menu_line in daily_menu["menu_lines"]:
            day = datetime.strptime(daily_menu["day"], "%Y-%m-%d").date()
            result.setdefault(day, []).append(menu_line)
    return result
