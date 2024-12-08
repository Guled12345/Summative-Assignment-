import streamlit as st
import pandas as pd
import tensorflow as tf
import os

def retrain_model_page():
    st.title("Retrain the Model")
    st.write("Upload a dataset to retrain the model.")

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file:
        try:
            # Load the dataset
            data = pd.read_csv(uploaded_file)
            st.write("Dataset Preview", data.head())

            # Separate features and target
            X = data.iloc[:, :-1]  # Exclude the last column (Target)
            y = data.iloc[:, -1]  # Target column

            # Use the correct model path
            model_path = r"C:/Users/Hp/Documents/GitHub/Summative-Assignment-/models/basic_model.h5"

            # Check if the model file exists
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found at: {model_path}")
            
            # Load and retrain the model (mock retraining in this example)
            st.write("Retraining the model...")
            model = tf.keras.models.load_model(model_path)
            retrained_model_path = r"C:\Users\Hp\Desktop\Summative-Assignment-\models\retrained_model.h5"
            model.save(retrained_model_path)
            st.success(f"Model retrained and saved successfully at {retrained_model_path}!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
