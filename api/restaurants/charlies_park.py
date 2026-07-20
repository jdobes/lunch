from datetime import datetime

from .utils import fetch_html
from .utils import gemini_parse_menu

NAME = "Charlie's Park"
URL = "https://charliespark.cz/menu/"
GPS = (49.22818841008108, 16.57621211364726)

GEMINI_PROMPT = f"""Následující text obsahuje jídla k dispozici konkrétní dny v týdnu a týdenní nabídku, která je k dispozici každý den.
Pro každý den poskládej seznam, co je právě k dispozici - jídla pro konkrétní den + týdenní nabídka.
Vynechej alergeny označené čísly, specifikace objemu, hmotnosti a nápoje. Na konec každého řádku přidej cenu, pokud je k dispozici.
Ignoruj překlady jídel do angličtiny.
Na začátek řádku, který označuje polévku, přidej "Polévka: ".
Rozděl jídla do 3 kategorií - polévky, menu k dispozici jen konkrétní den, týdenní menu - které jsou odděleny prázdným řádkem.
Pokud datum neobsahuje rok, uvažuj {datetime.now().year}.
Pokud se nejedná o seznam jídel, vrať prázdný výsledek.

Text:


"""


def parse_menu():
    result = {}
    html = fetch_html(URL)
    main = html.find("main")
    if main:
        prompt = f"{GEMINI_PROMPT}{main.text}"
        result = gemini_parse_menu(prompt)
    return result


if __name__ == "__main__":
    parse_menu()
