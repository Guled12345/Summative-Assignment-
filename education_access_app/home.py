import streamlit as st

def home_page():
    st.title("Welcome to the Machine Learning App")
    st.write("""
        This app allows you to:
        - Make predictions using a pre-trained model.
        - Retrain the model with new data.
    """)
    st.image("https://via.placeholder.com/800x400", caption="Machine Learning in Action")
