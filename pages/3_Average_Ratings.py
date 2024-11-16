import streamlit as st
from models import Course, is_database_empty
from scripts.data_queries import get_average_responses_by_course
from visualizations import create_radar_chart


if is_database_empty():
    st.error("The database is empty. Please upload survey data to access other features.")
else:

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
