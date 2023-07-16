import datetime
import os
import requests

# Constants
API_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
GENDER = "male"
WEIGHT = 82
HEIGHT = 177.8
AGE = 21


# Nutritionix Setup and getting the exercise details
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["SHEET_ENDPOINT"]

header = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}

text = input("What you did today: ")

parameters = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(endpoint, json=parameters, headers=header)


# Using sheety to update the google sheets
today = datetime.datetime.now().strftime("%d-%m-%Y")
time = datetime.datetime.now().strftime("%X")

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

    print(requests.post(sheety_endpoint, json=sheet_parameter).text)
