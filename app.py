import streamlit as st
from models import Question, Course
from scripts.data_queries import get_responses_by_question, get_average_responses_by_course
from visualizations import create_word_cloud, create_radar_chart

# Streamlit app title
st.title('Data Recycling App')

# Sidebar navigation
page = st.sidebar.radio("Select a page:", ("Home", "Word Cloud", "Average ratings"))

# Home page
if page == "Home":
    st.subheader("Welcome to the Data Recycling App")
    st.write("This app allows you to explore survey data by visualizing open-ended responses and evaluating course feedback.")
    st.write("Use the sidebar to navigate between pages.")

# Word Cloud page
elif page == "Word Cloud":
    st.subheader("Word Cloud of Open-Ended Responses")

    # Add a dropdown to select a question for which word cloud will be generated
    question_texts = [q.text for q in Question.select()]
    selected_question = st.selectbox('Select a Question for Word Cloud', question_texts)

    if selected_question:
        question_id = Question.get(Question.text == selected_question).id
        responses_data = get_responses_by_question(question_id)

        # Generate and display the word cloud for open-ended responses
        st.subheader(f'"{selected_question}"')
        st.pyplot(create_word_cloud(responses_data))

elif page == "Average ratings":
    st.subheader("Course Average Ratings")

    # Add a dropdown to select a course
    course_names = [course.name for course in Course.select()]
    selected_course = st.selectbox("Select a Course", course_names)

    if selected_course:
        # Get the course object
        course = Course.get(Course.name == selected_course)

        # Get average scores for this course
        average_scores = get_average_responses_by_course(course.id)

        # Display the radar chart for the average scores
        st.subheader(f"Average Scores for {selected_course}")
        radar_chart = create_radar_chart(average_scores)
        st.plotly_chart(radar_chart)
