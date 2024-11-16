import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.course import Course
from models.question import Question
from models.response import Response

def verify_data():
    print("Verifying data in the database...\n")

    # Verify courses
    print("Courses:")
    for course in Course.select():
        print(f"  - {course.name} (Instructor: {course.instructor})")

    # Verify questions
    print("\nQuestions:")
    for question in Question.select():
        print(f"  - {question.text}")

    # Verify responses
    print("\nResponses:")
    for response in Response.select():
        print(f"  - Course: {response.course.name}, Question: {response.question.text}, Answer: {response.answer}")

if __name__ == "__main__":
    verify_data()
