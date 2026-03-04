import logging
import os
import requests

from .facebook_utils import get_page_posts
from .utils import gemini_parse_menu

NAME = "Qwerty"
URL = "https://www.facebook.com/QwertyRestaurant"
GPS = (49.235655201154906, 16.573111921257983)

FACEBOOK_COOKIE = os.getenv("FACEBOOK_COOKIE", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

GEMINI_PROMPT = """Obrázek obsahuje denní menu na celý týden.
Pro každý den poskládej seznam, co je právě k dispozici - jídla pro konkrétní den + týdenní menu + stálá nabídka.
Vynechej alergeny označené čísly. Na konec každého řádku přidej cenu, pokud je k dispozici.
Na začátek řádku, který označuje polévku, přidej "Polévka: ".
Rozděl jídla do 3 kategorií - polévky, menu označená čísly, stálé menu - které jsou odděleny prázdným řádkem.
Pokud se nejedná o seznam jídel na celý týden, vrať prázdný výsledek.
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_menu():
    result = {}

    if not FACEBOOK_COOKIE or not GEMINI_API_KEY:
        logger.warning("Facebook cookie or Gemini API key not set! Can't sync.")
        return result

    page_posts = get_page_posts(URL.split("/")[-1])

    downloaded = []
    for idx, post in enumerate(page_posts):
        response = requests.get(post["full_picture"], timeout=10)
        if response.status_code == 200:
            filename = f"/tmp/qwerty_{idx}.jpg"
            with open(filename, "wb") as pic_f:
                pic_f.write(response.content)
            logger.debug("Downloaded image %s", filename)
            downloaded.append(filename)

    # Try the newest image, if the image isn't menu we are screwed
    if downloaded:
        result = gemini_parse_menu(downloaded[0], GEMINI_PROMPT)

    if not result:
        logger.warning("No menu found in the last image.")

    # Cleanup
    for image_path in downloaded:
        os.unlink(image_path)

    return result


if __name__ == "__main__":
    # Debugging
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    parse_menu()
