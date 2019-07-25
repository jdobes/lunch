import importlib
import logging

import connexion
import flask
import yaml

logger = logging.getLogger(__name__)

restaurants = {}


def get_main_page():
    return flask.send_file("/lunch/index.html")


def get_static_file(filename):
    return flask.send_from_directory("/lunch/static", filename)


def get_restaurants():
    response = {"restaurants": []}
    for restaurant in restaurants:
        response["restaurants"].append({"name": restaurant})
    return response


def main():
    with open("/lunch/config.yml", "rb") as config_file:
        config = yaml.safe_load(config_file)

    for restaurant in config["restaurants"]:
        module = importlib.import_module(".%s" % restaurant, package=".restaurants")
        restaurants[restaurant] = module
        logger.warning("Loaded restaurant: %s", restaurant)

    app = connexion.FlaskApp(__name__, options={"swagger_ui": True, "swagger_url": "/api/"})
    app.add_api('openapi.spec.yml', validate_responses=True, strict_validation=True)
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
