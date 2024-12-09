import streamlit as st
import numpy as np
import os
import tensorflow as tf

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
            # Relative path to model
            model_path = "./basic_model.h5"
            st.write(f"Model path used: {model_path}")

            # Check if the model file exists
            if not os.path.exists(model_path):
                st.error(f"Model file not found at: {model_path}")
                return
            
            # Load the model
            model = tf.keras.models.load_model(model_path)
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
            # Log detailed errors
            st.error(f"An unexpected error occurred: {e}")
