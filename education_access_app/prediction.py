import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st

# Define a custom InputLayer to handle 'batch_shape' argument
class CustomInputLayer(tf.keras.layers.InputLayer):
    @classmethod
    def from_config(cls, config):
        # Remove unsupported arguments
        config.pop("batch_shape", None)
        return super().from_config(config)

# Custom object scope for loading the model
def prediction_page():
    try:
        st.title("Education Access Prediction")
        st.write("Provide the necessary input data below:")
        
        # Define user inputs
        input_features = []
        for i in range(1, 8):  # Assuming 7 input features
            value = st.number_input(f"Feature {i}", value=0.0, step=0.1)
            input_features.append(value)

        input_data = tf.convert_to_tensor([input_features], dtype=tf.float32)

        # Path to your model
        model_path = "./education_access_app/basic_model.h5"
        st.write(f"Model path used: {model_path}")

        # Load the model with the custom deserialization logic
        with tf.keras.utils.custom_object_scope({'InputLayer': CustomInputLayer}):
            model = load_model(model_path)
            st.success("Model loaded successfully.")

        # Make a prediction
        prediction = model.predict(input_data)
        st.write(f"Prediction: {prediction[0][0]:.2f}")

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        st.error("Error Details:")
        st.error(e)

# Run the app
if __name__ == "__main__":
    prediction_page()
