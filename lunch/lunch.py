from datetime import date
import os
import importlib
import logging
import sys

from apscheduler.schedulers.background import BackgroundScheduler
import connexion
from peewee import DateField

from .model import init_schema, Restaurant, RestaurantMenu

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def sync(restaurants):
    logger.info("Syncing menus.")
    for restaurant in restaurants:
        logger.info("Parsing: %s" % restaurant)
        parsed_data = restaurants[restaurant].parse_menu()
        if not parsed_data:
            logger.warning("Unable to sync: %s", restaurant)
            continue
        restaurant_obj = Restaurant.get(label=restaurant)
        for menu_day, menu_lines in parsed_data.items():
            RestaurantMenu.replace(restaurant=restaurant_obj, day=menu_day, menu="\n".join(menu_lines)).execute()
        logger.info("Synced: %s" % restaurant)
    logger.info("Menus synced.")
    logger.info("Deleting old menus.")
    query = RestaurantMenu.delete().where(RestaurantMenu.day < date.today())
    deleted = query.execute()
    logger.info("%s old menu(s) deleted.", deleted)


def get_restaurant_module(restaurant):
    try:
        return importlib.import_module(".%s" % restaurant, package=".lunch.restaurants")
    except ModuleNotFoundError:
        return None


def main():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")

    enabled_restaurants = os.getenv("ENABLED_RESTAURANTS", "").split(",")
    sync_interval_mins = int(os.getenv("SYNC_INTERVAL_MINS", "1"))

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
    sched.add_job(sync, 'interval', [restaurants], minutes=sync_interval_mins)
    sched.start()
    logger.info("Sync scheduler enabled to run sync every %s minute(s).", sync_interval_mins)

    app = connexion.FlaskApp(__name__, options={"swagger_ui": True, "swagger_url": "/api/"})
    app.add_api('openapi.spec.yml', validate_responses=True, strict_validation=True)
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
