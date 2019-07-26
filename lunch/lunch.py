import importlib
import logging

from apscheduler.schedulers.background import BackgroundScheduler
import connexion
import yaml

from .model import sqlite_db, Restaurant

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def sync():
    logger.info("Syncing...")


def get_restaurant_module(restaurant):
    return importlib.import_module(".%s" % restaurant, package=".lunch.restaurants")


def main():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")

    with open("/lunch/config.yml", "rb") as config_file:
        config = yaml.safe_load(config_file)
    
    sqlite_db.create_tables([Restaurant])
    logger.info("Database schema initialized.")

    for restaurant in config["restaurants"]:
        get_restaurant_module(restaurant)
        #restaurants[restaurant] = module
        logger.info("Loaded restaurant: %s", restaurant)

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
