import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from models import Course, Question, Response

# Load CSV into pandas
df = pd.read_csv('data/sample_data.csv')

# Insert data into the database
for _, row in df.iterrows():
    course, _ = Course.get_or_create(name=row['course_name'], instructor=row['instructor'])
    question, _ = Question.get_or_create(text=row['question_text'])
    Response.create(course=course, question=question, answer=row['answer'])