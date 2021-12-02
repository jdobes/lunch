import os
from peewee import SqliteDatabase, Model, TextField, ForeignKeyField, DateField

DB_FILE = "/tmp/lunch.db"
if os.path.isfile(DB_FILE):
    os.unlink(DB_FILE)
sqlite_db = SqliteDatabase(DB_FILE, pragmas={"journal_mode": "wal",
                                             "foreign_keys": 1})


class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = sqlite_db


class Restaurant(BaseModel):
    label = TextField(null=False, unique=True)
    name = TextField(null=False)
    url = TextField(null=False)


class RestaurantMenu(BaseModel):
    restaurant = ForeignKeyField(model=Restaurant, null=False)
    day = DateField(null=False)
    menu = TextField(null=False)

    class Meta:
        indexes = (
            (('restaurant_id', 'day'), True),
        )


def init_schema():
    sqlite_db.create_tables([Restaurant, RestaurantMenu])
