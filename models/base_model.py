from peewee import *


db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db


def is_database_empty():
    try:
        from models.course import Course
        from models.question import Question
        from models.response import Response
        # Check if the table exists and has rows
        if not Course.table_exists() or not Question.table_exists() or not Response.table_exists():
            return True
        else:
            return False
    except Exception as e:
        return True