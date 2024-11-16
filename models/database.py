from peewee import *

db = SqliteDatabase('feedbacks.db')


class BaseModel(Model):
    class Meta:
        database = db
