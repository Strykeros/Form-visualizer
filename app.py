import streamlit as st
from models import Question
from scripts.data_queries import get_responses_by_question
from visualizations import create_word_cloud

# Streamlit app title
st.title('Data Recycling App')

# Add a dropdown to select a question
question_texts = [q.text for q in Question.select()]
selected_question = st.sidebar.selectbox('Select a Question', question_texts)

# Fetch the data for the selected question
if selected_question:
    question_id = Question.get(Question.text == selected_question).id
    responses_data = get_responses_by_question(question_id)

    # Create and display the word cloud for open-ended responses
    st.subheader("Word Cloud for Responses")
    st.pyplot(create_word_cloud(responses_data))