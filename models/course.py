from peewee import *
from models.database import BaseModel


class Course(BaseModel):
    id = AutoField()
    name = CharField()
    instructor = TextField()
    reputation = FloatField()
