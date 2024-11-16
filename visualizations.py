import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

def create_bar_chart(data):
    fig = px.bar(data, x='answer', y='count', title='Response Distribution')
    return fig

def create_word_cloud(data: pd.DataFrame):
    # Combine all answers into a single text string
    text = ' '.join(data['answer'].dropna().astype(str))

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400).generate(text)

    # Display the word cloud using Streamlit
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    return plt

def create_radar_chart(average_scores):
    """
    Creates a radar chart (spider chart) for average scores of questions.
    average_scores: a dictionary where keys are question texts and values are average scores.
    """
    questions = list(average_scores.keys())
    scores = list(average_scores.values())

    axis_text_values = ["Overall course enjoyment",
                        "Quality of materials",
                        "Did you feel challenged?",
                        "Were the requirements clear?",
                        "Course organization",
                        "No overlap with other courses",
                        "Presentation quality",
                        "The course encouraged interest",
                        "Provided feedback",
                        "Instructor's attitude",
                        "Would hear another course with this instructor",
                        ]

    # Create the radar chart
    fig = go.Figure(data=go.Scatterpolar(
        r=scores,
        theta=axis_text_values,
        fill='toself',
        name='Average Scores'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 7]  # Max score from 1 to 7 (you can adjust this based on your scoring range)
            )
        ),
        title="Course Feedback Average Scores",
        template='plotly_dark'
    )

    return fig