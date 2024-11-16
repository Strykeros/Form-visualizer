from peewee import *
from models.database import BaseModel


class Question(BaseModel):
    id = AutoField()
    text = TextField()