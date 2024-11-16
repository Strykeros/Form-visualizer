import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import db, Course, Question, Response

def initialize_db():
    db.connect()
    db.create_tables([Course, Question, Response], safe=True)
    print("Tables created successfully!")

    # Optionally, seed some initial data
    course = Course.create(name="Sample Course", instructor="Dr. Example")
    question = Question.create(text="Did you enjoy the course?")
    Response.create(course=course, question=question, answer="Completely agree")
    print("Sample data inserted!")

if __name__ == "__main__":
    initialize_db()