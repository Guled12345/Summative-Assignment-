import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Path to the model
MODEL_PATH = "models/education_access_model.pkl"

def load_model():
    """Load the trained model."""
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
    return model

def retrain_model(file):
    """Retrain the model with new data."""
    # Load new training data
    new_data = pd.read_csv(file)
    X = new_data.drop("target", axis=1)
    y = new_data["target"]
    
    # Train a new model
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    
    # Save the new model
    with open(MODEL_PATH, "wb") as file:
        pickle.dump(model, file)
