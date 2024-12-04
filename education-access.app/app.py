import streamlit as st
from home import home_page
from prediction import prediction_page
from retrain_model import retrain_page

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
