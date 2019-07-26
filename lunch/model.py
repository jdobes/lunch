from peewee import SqliteDatabase, Model, TextField

sqlite_db = SqliteDatabase(":memory:", pragmas={"journal_mode": "wal"})


class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = sqlite_db


class Restaurant(BaseModel):
    name = TextField()
