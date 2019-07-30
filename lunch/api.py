from datetime import date
import logging

import flask

from .model import Restaurant, RestaurantMenu

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_main_page():
    response = flask.send_file("/lunch/index.html")
    response.direct_passthrough = False
    return response


def get_static_file(filename):
    response = flask.send_from_directory("/lunch/static", filename)
    response.direct_passthrough = False
    return response


def get_restaurants():
    response = {"restaurants": []}

    for restaurant in Restaurant.select():
        response["restaurants"].append({"label": restaurant.label, "name": restaurant.name,
                                        "url": restaurant.url})
    return response


def get_menus(day=None, restaurants=None):
    if day:
        try:
            requested_date = date.fromisoformat(day)
        except ValueError:
            return "Invalid day format: %s" % day, 400
    else:
        requested_date = date.today()
    
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
