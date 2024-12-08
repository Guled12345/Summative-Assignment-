import streamlit as st
import numpy as np
import os
import tensorflow as tf

# Register DTypePolicy to avoid errors with deserialization
from tensorflow.keras import backend as K
from tensorflow.keras.utils import get_custom_objects

# Add this custom dtype policy registration to handle deserialization of custom layers or policies
def register_custom_objects():
    from tensorflow.keras.layers import Dense
    from tensorflow.keras import layers

    # Registering DTypePolicy for deserialization
    get_custom_objects().update({
        'DTypePolicy': K.float32,
        'Dense': Dense
    })

def prediction_page():
    st.title("Predict Potential Dropouts")
    st.write("Fill out the fields below to predict if a student will drop out.")

    with st.form("prediction_form"):
        daytime_evening = st.selectbox("Daytime/Evening Attendance", [0, 1])
        mother_occupation = st.number_input("Mother's Occupation", min_value=1, max_value=20, value=1)
        father_occupation = st.number_input("Father's Occupation", min_value=1, max_value=20, value=1)
        gender = st.selectbox("Gender", ["Male", "Female"])
        displaced = st.selectbox("Displaced", ["Yes", "No"])
        special_needs = st.selectbox("Educational Special Needs", ["Yes", "No"])
        missing_feature = st.number_input("Missing Feature Placeholder", min_value=0, value=0)

        submitted = st.form_submit_button("Predict")

    if submitted:
        try:
            # Use the correct model path
            model_path = os.path.join(os.getcwd(), "models", "basic_model.h5")
            st.write(f"Model path used: {model_path}")
            
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found at: {model_path}")

            # Register custom objects before loading the model
            register_custom_objects()
            
            # Load the model with compile=False to avoid unnecessary recompilation
            model = tf.keras.models.load_model(model_path, compile=False)

            # Prepare the input data
            input_data = np.array([[daytime_evening, mother_occupation, father_occupation, gender, displaced, special_needs, missing_feature]])

            # Make prediction
            prediction = model.predict(input_data)
            result = "Dropout" if prediction[0][0] > 0.5 else "No Dropout"
            st.success(f"The prediction is: {result}")

        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
