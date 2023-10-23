import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import threading 
import time  # Import the time module
from keras.models import load_model


loaded_model = load_model('C:/Users/danny/OneDrive/Desktop/coffee_model.keras')
# Check a new day and time to predict if an action should happen

# Room and day name-to-integer mapping
room_mapping = {"Kitchen": 1, "Room": 2, "Garage": 3}
day_mapping = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}

while True:
    room_name = input("Enter Room (Kitchen, Room, or Garage):\n")
    room = room_mapping.get(room_name, None)

    if room is None:
        print("Invalid room name. Please enter a valid room.")
    else:
        day_name = input("Enter Day of the week (Sunday, Monday, etc.):\n")
        day = day_mapping.get(day_name, None)

        if day is None:
            print("Invalid day name. Please enter a valid day.")
        else:
            time = int(input("Enter time (e.g., 730 for 7:30 AM):\n"))

            coffee_test = np.array([[room, day, time]])  # Example new data

            prediction = loaded_model.predict(coffee_test)

            if prediction >= 0.5:
                print("Coffee is going to be made in 5 minutes.")

                def user_response():
                    global x
                    x = input("Do you want it to stop? (Yes)\n")

                response_thread = threading.Thread(target=user_response)
                response_thread.start()

                timeout_seconds = 5  # Adjust the timeout as needed

                response_thread.join(timeout=timeout_seconds)

                if response_thread.is_alive():
                    print("No response received within the timeout. Action Happens")
                else:
                    if x == "Yes":
                        print("Action Stopped")
            else:
                print("No action happens")
            break  # Exit the loop if valid inputs are provided