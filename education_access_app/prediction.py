import streamlit as st
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import InputLayer

# Custom InputLayer to handle deserialization issues
class CustomInputLayer(InputLayer):
    @classmethod
    def from_config(cls, config):
        # Remove unsupported arguments from config
        config.pop("batch_shape", None)
        config.pop("sparse", None)  # Remove sparse if it exists
        return super().from_config(config)

def prediction_page():
    st.title("Predict Potential Dropouts")
    st.write("Fill out the fields below to predict if a student will drop out.")

    # Form to input data
    with st.form("prediction_form"):
        daytime_evening = st.selectbox("Daytime/Evening Attendance", [0, 1])
        mother_occupation = st.number_input("Mother's Occupation", min_value=1, max_value=20, value=1)
        father_occupation = st.number_input("Father's Occupation", min_value=1, max_value=20, value=1)
        gender = st.selectbox("Gender", ["Male", "Female"])
        displaced = st.selectbox("Displaced", ["Yes", "No"])
        special_needs = st.selectbox("Educational Special Needs", ["Yes", "No"])
        missing_feature = st.number_input("Missing Feature Placeholder", min_value=0, value=0)

        submitted = st.form_submit_button("Predict")

    # Handle form submission
    if submitted:
        try:
            # Path to your model
            model_path = "./education_access_app/basic_model.h5"
            st.write(f"Model path used: {model_path}")

            # Check if the model file exists
            if not os.path.exists(model_path):
                st.error(f"Model file not found at: {model_path}")
                return

            # Load the model with the custom object scope
            with tf.keras.utils.custom_object_scope({'InputLayer': CustomInputLayer}):
                model = load_model(model_path)

            st.success("Model loaded successfully.")

            # Prepare input data
            input_data = np.array([[
                daytime_evening,
                mother_occupation,
                father_occupation,
                1 if gender == "Male" else 0,  # Encode gender as binary
                1 if displaced == "Yes" else 0,  # Encode displaced as binary
                1 if special_needs == "Yes" else 0,  # Encode special needs as binary
                missing_feature
            ]])

            # Predict
            prediction = model.predict(input_data)
            result = "Dropout" if prediction[0][0] > 0.5 else "No Dropout"
            st.success(f"The prediction is: {result}")

        except Exception as e:
            # Log the full exception for better debugging
            st.error(f"An unexpected error occurred: {str(e)}")
            st.write("Error Details:", e)
