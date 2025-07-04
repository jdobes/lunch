from datetime import date, datetime, timedelta
import os
import importlib
import logging
import sys

from apscheduler.schedulers.background import BackgroundScheduler
from connexion import FlaskApp
from connexion.options import SwaggerUIOptions
from flask import send_from_directory
import pytz

from .model import init_schema, Restaurant, RestaurantMenu

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def get_first_day_of_week():
    now = datetime.now(pytz.timezone(os.getenv("TZ")))
    first_day = now - timedelta(days=now.weekday())
    return date(first_day.year, first_day.month, first_day.day)

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
    first_day_of_week = get_first_day_of_week()
    query = RestaurantMenu.delete().where(RestaurantMenu.day < first_day_of_week)
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
            record = Restaurant(label=restaurant, name=module.NAME, url=module.URL,
                                latitude=module.GPS[0], longitude=module.GPS[1])
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

    app = FlaskApp(__name__)
    app.add_api(
        'openapi.spec.yml',
        validate_responses=True,
        strict_validation=True,
        swagger_ui_options=SwaggerUIOptions(
            swagger_ui=True,
            swagger_ui_path="/api/ui/",
            spec_path="/api/openapi.json",
        )
    )

    @app.app.after_request
    def set_default_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers"
        response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        return response

    @app.route('/')
    def send_index():
        return send_from_directory('/lunch/html/', 'index.html') 

    @app.route('/<path:path>')
    def send_root(path):
        return send_from_directory('/lunch/html/', path)

    @app.route('/static/js/<path:path>')
    def send_js(path):
        return send_from_directory('/lunch/html/static/js/', path)

    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
