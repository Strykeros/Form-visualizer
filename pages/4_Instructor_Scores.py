from models.base_model import is_database_empty
from scripts.data_queries import get_average_responses_by_course
import pandas as pd
import streamlit as st
import plotly.express as px


if is_database_empty():
    st.error("The database is empty. Please upload survey data to access other features.")
else:
    def get_instructor_reputation(courses, instructors):
        """
        Aggregates scores for each instructor based on the courses they teach.
        Args:
            courses: Dictionary mapping course names to course IDs.
            instructors: Dictionary mapping course names to instructors.

        Returns:
            DataFrame with instructor names and their overall average score.
        """
        instructor_scores = {}

        for course_name, course_id in courses.items():
            # Get the instructor for this course
            instructor = instructors[course_name]

            # Use the existing function to get average responses for this course
            average_scores = get_average_responses_by_course(course_id)

            # Compute the overall average for the course
            overall_average = sum(average_scores.values()) / len(average_scores) if average_scores else 0

            # Aggregate scores by instructor
            if instructor in instructor_scores:
                instructor_scores[instructor].append(overall_average)
            else:
                instructor_scores[instructor] = [overall_average]

        # Calculate the final average for each instructor
        instructor_reputation = {
            instructor: sum(scores) / len(scores) for instructor, scores in instructor_scores.items()
        }

        # Convert to DataFrame for visualization
        return pd.DataFrame(list(instructor_reputation.items()), columns=["Instructor", "Average Score"])

    # Mocked course and instructor data
    courses = {"Sample Course": 1, "Advanced Python": 2}
    instructors = {"Sample Course": "Dr. Example", "Advanced Python": "Dr. Code"}

    # Streamlit UI
    st.title("Instructor Reputation Comparison")

    # Get reputation data
    instructor_reputation_df = get_instructor_reputation(courses, instructors)

    # Display reputation data in a table
    st.write("### Instructor Reputation Scores")
    st.dataframe(instructor_reputation_df)

    # Display a bar chart for comparison
    st.write("### Reputation Comparison Bar Chart")
    fig = px.bar(
        instructor_reputation_df,
        x="Instructor",
        y="Average Score",
        title="Instructor Reputation Based on Average Scores",
        labels={"Average Score": "Reputation Score"},
        color="Instructor"
    )
    st.plotly_chart(fig)