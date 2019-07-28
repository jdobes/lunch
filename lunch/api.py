import logging

import flask

from .model import Restaurant

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
        response["restaurants"].append({"name": restaurant.name})
    return response
