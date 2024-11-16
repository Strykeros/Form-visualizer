from models.database import db
from models.course import Course
from models.question import Question
from models.response import Response

def initialize_db():
    db.connect()
    db.create_tables([Course, Question, Response], safe=True)
    print("Tables created successfully!")