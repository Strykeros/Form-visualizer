import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.course import Course
from models.question import Question
from models.response import Response
from models.base_model import db

def initialize_db():
    db.connect()
    db.drop_tables([Course, Question, Response])
    db.create_tables([Course, Question, Response], safe=True)
    print("Tables created successfully!")

    # Optionally, seed some initial data
    course = Course.create(name="Sample Course", instructor="Dr. Example")
    question = Question.create(text="Did you enjoy the course?")
    Response.create(course=course, question=question, answer="Completely agree")
    print("Sample data inserted!")

if __name__ == "__main__":
    pass
