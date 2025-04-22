import os
from datetime import date, datetime
import logging

import pytz

from .model import Restaurant, RestaurantMenu

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

OFFICE_GPS = (49.231635142558865, 16.576317775011656)


def get_restaurants():
    response = {"restaurants": []}

    for restaurant in Restaurant.select():
        response["restaurants"].append({"label": restaurant.label, "name": restaurant.name,
                                        "url": restaurant.url, "latitude": restaurant.latitude,
                                        "longitude": restaurant.longitude})
    return response


def get_menus(day=None, restaurants=None):
    if day:
        try:
            requested_date = datetime.strptime(day, "%Y-%m-%d").date()
        except ValueError:
            return "Invalid day format: %s" % day, 400
    else:
        now = datetime.now(pytz.timezone(os.getenv("TZ")))
        requested_date = date(now.year, now.month, now.day)

    if restaurants:
        requested_restaurants = restaurants.split(",")
    else:
        requested_restaurants = [restaurant.label for restaurant in Restaurant.select()]

    query = RestaurantMenu.select(Restaurant.label, RestaurantMenu.menu, RestaurantMenu.day, Restaurant.url).join(Restaurant) \
        .where(RestaurantMenu.day == requested_date) \
        .where(Restaurant.label << requested_restaurants) \
        .dicts()
    menus, menu_metadata = {}, {}
    for row in query:
        menus[row["label"]] = row["menu"]
        menu_metadata[row["label"]] = {"day": row["day"].strftime("%d.%m.%Y"), "url": row["url"]}

    return {"day": requested_date, "menus": [{"restaurant": restaurant, "menu": menus.get(restaurant), "menu_metadata": menu_metadata.get(restaurant)}
                                             for restaurant in requested_restaurants]}


def get_origins():
    return {"origins": [{"label": "office",
                         "name": "Office",
                         "latitude": OFFICE_GPS[0],
                         "longitude": OFFICE_GPS[1]}]}
