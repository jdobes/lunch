import os
import importlib
import logging
import sys

from apscheduler.schedulers.background import BackgroundScheduler
import connexion

from .model import init_schema, Restaurant

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def sync():
    logger.info("Syncing...")


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

    for restaurant in enabled_restaurants:
        module = get_restaurant_module(restaurant)
        if module:
            record = Restaurant(name=restaurant)
            record.save()
            logger.info("Loaded restaurant module: %s", restaurant)
        else:
            logger.error("Unable to load restaurant module: %s", restaurant)
            sys.exit(1)

    sync()
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(sync, 'interval', minutes=1)
    sched.start()
    logger.info("Sync scheduler enabled.")

    app = connexion.FlaskApp(__name__, options={"swagger_ui": True, "swagger_url": "/api/"})
    app.add_api('openapi.spec.yml', validate_responses=True, strict_validation=True)
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
