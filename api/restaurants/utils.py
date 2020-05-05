from datetime import datetime
import os
import logging

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ZOMATO_API_KEY = os.getenv("ZOMATO_API_KEY", "")
ZOMATO_API_URL = "https://developers.zomato.com/api/v2.1/dailymenu?res_id="
ZOMATO_API_HEADERS = {"Accept": "application/json", "user_key": ZOMATO_API_KEY}


def fetch_html(url):
    for _ in range(3):
        try:
            response = requests.get(url)
            response.encoding = "utf-8"
            if response.status_code == 200:
                return BeautifulSoup(response.text, features="lxml")
            logger.warning("Error during fetching url %s: HTTP %s, %s",
                           url, response.status_code, response.text)
        except requests.exceptions.RequestException:
            logger.warning("Error fetching url.")
    logger.error("URL not fetched.")
    return None


def fetch_zomato(restaurant_id):
    if ZOMATO_API_KEY:
        for _ in range(3):
            try:
                response = requests.get("%s%s" % (ZOMATO_API_URL, restaurant_id), headers=ZOMATO_API_HEADERS)
                if response.status_code == 200:
                    return response.json()
            except requests.exceptions.RequestException:
                logger.warning("Error fetching url.")
    else:
        logger.error("Zomato API key is not specified.")
    logger.error("URL not fetched.")
    return None


def parse_zomato(zomato_json):
    result = {}
    if zomato_json:
        daily_menus = zomato_json["daily_menus"]
        for daily_menu in daily_menus:
            daily_menu = daily_menu["daily_menu"]
            current_date = datetime.strptime(daily_menu["start_date"].split()[0], "%Y-%m-%d").date()
            result[current_date] = []
            for dish in daily_menu["dishes"]:
                dish = dish["dish"]
                result[current_date].append("%s %s" % (dish["name"], dish["price"]))

    return result
