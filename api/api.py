import os
from datetime import date, datetime
import logging

import pytz

from .model import Restaurant, RestaurantMenu

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_restaurants():
    response = {"restaurants": []}

    for restaurant in Restaurant.select():
        response["restaurants"].append({"label": restaurant.label, "name": restaurant.name,
                                        "url": restaurant.url})
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

    query = RestaurantMenu.select(Restaurant.label, RestaurantMenu.menu).join(Restaurant) \
        .where(RestaurantMenu.day == requested_date) \
        .where(Restaurant.label << requested_restaurants) \
        .dicts()
    menus = {}
    for row in query:
        menus[row["label"]] = row["menu"]

    return {"day": requested_date, "menus": [{"restaurant": restaurant, "menu": menus.get(restaurant)}
                                             for restaurant in requested_restaurants]}
