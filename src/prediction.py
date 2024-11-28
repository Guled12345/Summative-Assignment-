import joblib

def predict(model_path, input_features):
    """Load the model and predict the class for input features."""
    model = joblib.load(model_path)
    prediction = model.predict([input_features])
    return prediction[0]
