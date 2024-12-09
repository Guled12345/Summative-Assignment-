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
            data = pd.read_csv(uploaded_file)
            st.write("Dataset Preview", data.head())

            X = data.iloc[:, :-1]
            y = data.iloc[:, -1]

            # Update this path to match the actual directory where your model is stored
            model_path = "./models/basic_model.h5"  # Replace this with the correct path if necessary
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found at: {model_path}")

            st.write("Retraining the model...")
            model = tf.keras.models.load_model(model_path)
            retrained_model_path = "./models/retrained_model.h5"  # Save the retrained model here
            model.save(retrained_model_path)
            st.success(f"Model retrained and saved successfully at {retrained_model_path}!")

        except Exception as e:
            st.error(f"An error occurred: {e}")
