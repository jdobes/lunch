from datetime import date
import logging

import flask
from peewee import JOIN

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

    query = Restaurant.select(Restaurant.label, RestaurantMenu.menu).join(RestaurantMenu, JOIN.LEFT_OUTER) \
        .where((RestaurantMenu.day == requested_date) | (RestaurantMenu.day.is_null()))
    if restaurants:
        requested_restaurants = restaurants.split(",")
        query = query.where(Restaurant.label << requested_restaurants)

    response = {"day": requested_date, "menus": []}
    for menu in query.dicts():
        response["menus"].append({"restaurant": menu["label"], "menu": menu["menu"]})

    return response
