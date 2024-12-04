import streamlit as st
from model_utils import retrain_model

def retrain_page():
    st.title("Retrain Model")
    st.write("Upload new training data to retrain the model.")
    
    # File uploader for new training data
    uploaded_file = st.file_uploader("Choose a CSV file for retraining", type="csv")
    
    if uploaded_file:
        st.write("File uploaded successfully.")
        
        if st.button("Retrain Model"):
            retrain_model(uploaded_file)
            st.success("Model retrained successfully and saved!")
