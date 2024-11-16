import streamlit as st
from models import Question, is_database_empty
from scripts.data_queries import get_responses_by_question
from visualizations import create_word_cloud


if is_database_empty():
    st.error("The database is empty. Please upload survey data to access other features.")
else:

    st.subheader("Word Cloud of Open-Ended Responses")

    # Add a dropdown to select a question for which word cloud will be generated
    question_texts = [
        "What did you like the most in this course?",
        "What could be improved?"
    ]
    selected_question = st.selectbox('Select a Question for Word Cloud', question_texts)

    if selected_question:
        question_id = Question.get(Question.text == selected_question).id
        responses_data = get_responses_by_question(question_id)

        # Generate and display the word cloud for open-ended responses
        st.subheader(f'"{selected_question}"')
        st.pyplot(create_word_cloud(responses_data))