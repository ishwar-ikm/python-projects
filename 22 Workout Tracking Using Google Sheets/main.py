import datetime
import os
import requests

# Constants
API_ID = os.environ["NT_APP_ID"]  # Nutritionix API ID
API_KEY = os.environ["NT_API_KEY"]  # Nutritionix API Key
GENDER = "male"
WEIGHT = 82
HEIGHT = 177.8
AGE = 21


# Nutritionix Setup and getting the exercise details
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"  # API endpoint for exercise tracking
sheety_endpoint = os.environ["SHEET_ENDPOINT"]  # Sheety API endpoint for Google Sheets

header = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}

text = input("What you did today: ")  # Prompt the user for exercise details

parameters = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(endpoint, json=parameters, headers=header)  # Send request to Nutritionix API


# Using Sheety to update the Google Sheets
today = datetime.datetime.now().strftime("%d-%m-%Y")  # Current date
time = datetime.datetime.now().strftime("%X")  # Current time

# Iterate over each exercise in the response
for exercise in response.json()['exercises']:
    sheet_parameter = {
        'workout': {
            'date': today,
            'time': time,
            'exercise': exercise['user_input'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    # Update the Google Sheets spreadsheet using Sheety API
    print(requests.post(sheety_endpoint, json=sheet_parameter).text)
