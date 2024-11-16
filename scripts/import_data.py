import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from models.course import Course
from models.question import Question
from models.response import Response

def import_data(file):
    # Load CSV into pandas
    df = pd.read_csv(file)

    # Insert data into the database
    for _, row in df.iterrows():
        course, _ = Course.get_or_create(name=row['course_name'], instructor=row['instructor'])
        question, _ = Question.get_or_create(text=row['question_text'])
        Response.create(course=course, question=question, answer=row['answer'])