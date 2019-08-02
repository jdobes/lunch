import logging

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def fetch_html(url):
    for _ in range(3):
        try:
            response = requests.get(url)
            response.encoding = "utf-8"
            if response.status_code == 200:
                return BeautifulSoup(response.text, features="html.parser")
            logger.warning("Error during fetching url %s: HTTP %s, %s",
                           url, response.status_code, response.text)
        except requests.exceptions.RequestException:
            logger.warning("Error fetching url.")
    logger.error("URL not fetched.")
    return None
