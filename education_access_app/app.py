import streamlit as st
import sys
import os

# Add the parent directory of education_access_app to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import pages from education_access_app
from education_access_app.home import home_page
from education_access_app.prediction import prediction_page
from education_access_app.retrain_model import retrain_model_page

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "Retrain Model"])

# Load the selected page
if page == "Home":
    home_page()
elif page == "Prediction":
    prediction_page()
elif page == "Retrain Model":
    retrain_model_page()
