from models import Response, Question
import pandas as pd

def get_responses_by_question(question_id):
    query = (Response
             .select(Response.answer)
             .where(Response.question == question_id))
    return pd.DataFrame(query.dicts())

def get_average_responses_by_course(course_id):
    # 1. Define the dictionary which will contain the question and the average score
    results = {}

    # 2. Define a list of all questions that have close-ended answers
    questions = ["Did you enjoy the course?",
                 "Was the material clear?",
                 "Did you feel challenged?",
                 "At the beginning of the course the instructor explained its objectives and requirements.",
                 "The course was well organized and systematic.",
                 "The content of the course did not overlap with other courses.",
                 "The instructor presented the course topics in an understandable way.",
                 "The course was intellectually stimulating and encouraged interest.",
                 "The instructor provided feedback on my performance.",
                 "The instructor's attitude toward students was respectful and accommodating.",
                 "I would gladly attend another course with this instructor.",
                 ]

    # Mapping of answers to numerical values
    answers_grading = {
        "Completely disagree": 1,
        "Disagree": 2,
        "Somewhat disagree" : 3,
        "Neither agree nor disagree" : 4,
        "Somewhat agree" : 5,
        "Agree": 6,
        "Completely agree": 7,
    }

    # 3. Go through each question and calculate the average value
    for question_text in questions:
        # 3.1 Get the question object from the database
        question = Question.get(Question.text == question_text)

        # 3.2 Retrieve the responses for this question and course
        responses = Response.select().where(
            Response.course == course_id, 
            Response.question == question.id
        )
        # 3.3 Calculate the total score and count of responses for averaging
        total_score = 0
        response_count = 0

        for response in responses:
            # Get the numerical value of the response
            total_score += answers_grading.get(response.answer, 0)  # Default to 0 if response.answer is invalid
            response_count += 1

        # Calculate the average score
        if response_count > 0:
            average_score = total_score / response_count
        else:
            average_score = 0  # If no responses, assign 0 or handle it as needed

        # Store the average score for this question
        results[question_text] = average_score

    return results
