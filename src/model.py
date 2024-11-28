import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model(X_train, y_train, model_path):
    """Train a RandomForestClassifier and save the model to a file."""
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

def evaluate_model(X_test, y_test, model_path):
    """Load the saved model and evaluate it on the test set."""
    model = joblib.load(model_path)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
