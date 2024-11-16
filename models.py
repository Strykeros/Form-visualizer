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


def is_database_empty():
    try:
        # Check if the table exists and has rows
        if not Course.table_exists() or not Question.table_exists() or not Response.table_exists():
            return True
        else:
            return False
    except Exception as e:
        return True