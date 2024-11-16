import streamlit as st
from scripts.check_data import verify_data
from scripts.import_data import import_data
from scripts.init_database import initialize_db
import os


st.set_page_config(page_title="Upload data", page_icon="📈")

st.subheader("Upload survey")

# Ensure the "data" folder exists
data_folder = "data"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)


# Function to delete existing files in the "data" folder
def clear_data_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


# File uploader
uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])

if uploaded_file is not None:
    # Clear the "data" folder
    clear_data_folder(data_folder)

    # Save the new file to the "data" folder
    file_path = os.path.join(data_folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File '{uploaded_file.name}' has been uploaded and saved. Analyzing data, please wait...")

    # Call functions to process the uploaded file
    initialize_db()
    import_data(file_path)
    verify_data()

    # Switch to the Word Cloud page
    st.switch_page("pages/2_Word_Cloud.py")
