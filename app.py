import os
import streamlit as st


# Streamlit app title
st.set_page_config(
    page_title="Data Recycling App",  # Title of the app in the browser tab
    page_icon="♻️",  # Emoji or custom icon for the app
    initial_sidebar_state="expanded",  # Sidebar state: "expanded", "collapsed", "auto"
)

st.title('Welcome to the Data Recycling App')

# Create the "data" directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')


st.write(
    "This app allows you to explore survey data by visualizing open-ended responses and evaluating course feedback.")
st.write("Use the sidebar to navigate between pages.")