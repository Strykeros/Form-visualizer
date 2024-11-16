from peewee import *

db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class Course(BaseModel):
    id = AutoField()
    name = CharField()
    instructor = CharField()

class Question(BaseModel):
    id = AutoField()
    text = TextField()

class Response(BaseModel):
    id = AutoField()
    course = ForeignKeyField(Course, backref='responses')
    question = ForeignKeyField(Question, backref='responses')
    answer = CharField()