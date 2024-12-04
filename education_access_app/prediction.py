import streamlit as st
import pandas as pd
from model_utils import load_model

def prediction_page():
    st.title("Prediction Page")
    st.write("Upload your data below to get predictions.")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.write(data.head())
        
        # Load model
        model = load_model()
        predictions = model.predict(data)
        
        st.write("Predictions:")
        st.write(predictions)
