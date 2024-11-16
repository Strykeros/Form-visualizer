from peewee import *
from models.base_model import BaseModel
from models.course import Course
from models.question import Question


class Response(BaseModel):
    id = AutoField()
    course = ForeignKeyField(Course, backref='responses')
    question = ForeignKeyField(Question, backref='responses')
    answer = CharField()
