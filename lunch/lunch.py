import os
import importlib
import logging
import sys

from apscheduler.schedulers.background import BackgroundScheduler
import connexion

from .model import init_schema, Restaurant, RestaurantMenu

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def sync(restaurants):
    for restaurant in restaurants:
        logger.info("Parsing %s." % restaurant)
        parsed_data = restaurants[restaurant].parse_menu()
        if not parsed_data:
            continue
        restaurant_obj = Restaurant.get(label=restaurant)
        for menu_day, menu_lines in parsed_data.items():
            RestaurantMenu.replace(restaurant=restaurant_obj, day=menu_day, menu="\n".join(menu_lines)).execute()
        logger.info("Synced %s." % restaurant)


def get_restaurant_module(restaurant):
    try:
        return importlib.import_module(".%s" % restaurant, package=".lunch.restaurants")
    except ModuleNotFoundError:
        return None


def main():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")

    enabled_restaurants = os.getenv("ENABLED_RESTAURANTS", "").split(",")

    init_schema()
    logger.info("Database schema initialized.")

    restaurants = {}
    for restaurant in enabled_restaurants:
        module = get_restaurant_module(restaurant)
        if module:
            record = Restaurant(label=restaurant, name=module.NAME)
            record.save()
            restaurants[restaurant] = module
            logger.info("Loaded restaurant module: %s", restaurant)
        else:
            logger.error("Unable to load restaurant module: %s", restaurant)
            sys.exit(1)

    sync(restaurants)
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(sync, 'interval', [restaurants], minutes=1)
    sched.start()
    logger.info("Sync scheduler enabled.")

    app = connexion.FlaskApp(__name__, options={"swagger_ui": True, "swagger_url": "/api/"})
    app.add_api('openapi.spec.yml', validate_responses=True, strict_validation=True)
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
