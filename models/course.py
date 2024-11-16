from peewee import *
from models.base_model import BaseModel

class Course(BaseModel):
    id = AutoField()
    name = CharField()
    instructor = CharField()