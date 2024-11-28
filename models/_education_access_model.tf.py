import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
import numpy as np

# Create a synthetic dataset as an example (Replace with your real data)
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a simple TensorFlow/Keras model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile and train the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Define the directory and file path
model_dir = 'models'
os.makedirs(model_dir, exist_ok=True)
tf_path = os.path.join(model_dir, '_education_access_model.tf')

# Save the model in TensorFlow format
model.save(tf_path)

print(f"Model saved as TensorFlow format: {tf_path}")
