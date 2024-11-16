from peewee import *
from models.base_model import BaseModel


class Question(BaseModel):
    id = AutoField()
    text = TextField()
