import streamlit as st
import sys
import os

# Add the parent directory of education_access_app to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from education_access_app
from education_access_app.home import home_page
from education_access_app.prediction import prediction_page
from education_access_app.retrain_model import retrain_page
from education_access_app.model_utils import load_model

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "Retrain Model"])

# Load selected page
if page == "Home":
    home_page()
elif page == "Prediction":
    prediction_page()
elif page == "Retrain Model":
    retrain_page()
