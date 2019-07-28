from peewee import SqliteDatabase, Model, TextField

sqlite_db = SqliteDatabase("/tmp/lunch.db", pragmas={"journal_mode": "wal"})


class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = sqlite_db


class Restaurant(BaseModel):
    label = TextField()
    name = TextField()


def init_schema():
    sqlite_db.create_tables([Restaurant])
