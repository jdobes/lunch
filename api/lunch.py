from datetime import date, datetime
import os
import importlib
import logging
import sys

from apscheduler.schedulers.background import BackgroundScheduler
import connexion
import pytz

from .model import init_schema, Restaurant, RestaurantMenu

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def sync(restaurants):
    logger.info("Syncing menus.")
    for restaurant in restaurants:
        logger.info("Parsing: %s" % restaurant)
        try:
            parsed_data = restaurants[restaurant].parse_menu()
        except:
            logger.exception("Unable to sync %s:", restaurant)
            continue
        if not parsed_data:
            logger.error("Unable to sync %s: empty response from module", restaurant)
            continue
        restaurant_obj = Restaurant.get(label=restaurant)
        for menu_day, menu_lines in parsed_data.items():
            RestaurantMenu.replace(restaurant=restaurant_obj, day=menu_day, menu="\n".join(menu_lines)).execute()
        logger.info("Synced: %s" % restaurant)
    logger.info("Menus synced.")
    logger.info("Deleting old menus.")
    now = datetime.now(pytz.timezone(os.getenv("TZ")))
    today = date(now.year, now.month, now.day)
    query = RestaurantMenu.delete().where(RestaurantMenu.day < today)
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
    sync_days = os.getenv("SYNC_DAYS", "mon-fri")
    sync_hours = os.getenv("SYNC_HOURS", "8-15")

    init_schema()
    logger.info("Database schema initialized.")

    restaurants = {}
    for restaurant in enabled_restaurants:
        module = get_restaurant_module(restaurant)
        if module:
            record = Restaurant(label=restaurant, name=module.NAME, url=module.URL)
            record.save()
            restaurants[restaurant] = module
            logger.info("Loaded restaurant module: %s", restaurant)
        else:
            logger.error("Unable to load restaurant module: %s", restaurant)
            sys.exit(1)

    sync(restaurants)
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(sync, 'cron', [restaurants], day_of_week=sync_days, hour=sync_hours)
    sched.start()
    logger.info("Sync scheduler enabled to run in following schedule: %s, %s", sync_days, sync_hours)

    app = connexion.FlaskApp(__name__, options={"swagger_ui": True, "swagger_url": "/api/",
                                                "openapi_spec_path": "/api/openapi.json"})
    app.add_api('openapi.spec.yml', validate_responses=True, strict_validation=True)

    @app.app.after_request
    def set_default_headers(response): # pylint: disable=unused-variable
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers"
        response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        return response

    app.run(host="0.0.0.0", port=8001)


if __name__ == "__main__":
    main()
