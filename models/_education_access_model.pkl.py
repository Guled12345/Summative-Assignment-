import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Create a synthetic dataset as an example (Replace with your real data)
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Define the directory and file path
model_dir = 'models'
os.makedirs(model_dir, exist_ok=True)
pickle_path = os.path.join(model_dir, '_education_access_model.pkl')

# Save the model as a Pickle file
with open(pickle_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model saved as Pickle: {pickle_path}")
