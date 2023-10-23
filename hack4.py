import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import threading 
import time  # Import the time module
from keras.models import load_model

# Load your real data from a CSV file
coffee_data = pd.read_csv("real_data.csv")

# Shuffle the dataset
coffee_data = shuffle(coffee_data, random_state=42)

# Extract features (location, day, and time) and labels from the loaded data
X = coffee_data[['location', 'day', 'time']].values
y = coffee_data['action_label'].values

# Split the dataset into a training set (70%) and a test set (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Keras model
model = Sequential()
model.add(Dense(32, input_dim=3, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model on the training set
model.fit(X_train, y_train, epochs=389, batch_size=10, verbose=0)


# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

model.save('C:/Users/danny/OneDrive/Desktop/coffee_model.keras')


print("Test Accuracy:", test_accuracy)


