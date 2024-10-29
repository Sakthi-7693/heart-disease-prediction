import streamlit as st
import plotly.express as px

DATASET_PATH = "data/heart_2020_cleaned.csv"
LOG_MODEL_PATH = "model/logistic_regression.pkl"

# Set page configuration
st.set_page_config(page_title="Custom Navbar App", page_icon="🌐")

# Custom CSS for the navbar
st.markdown(
    """
    <style>
    /* Navbar styling */
    .navbar {
        background-color: #00008B; /* Dark Blue */
        padding: 10px;
        color: white;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display navbar
st.markdown('<div class="navbar">My Custom Heading</div>', unsafe_allow_html=True)

# Main content
st.write("Welcome to the main content of your Streamlit app!")