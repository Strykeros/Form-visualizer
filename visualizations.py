import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

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