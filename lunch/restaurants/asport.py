from bs4 import BeautifulSoup
import logging
import requests

NAME = "A-Sport Hotel"
URL = "http://www.a-sporthotel.cz/menu/"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def sync():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text)
    logger.info(soup.prettify())
