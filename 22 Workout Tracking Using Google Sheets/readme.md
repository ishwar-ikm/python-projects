# Exercise Tracker
This is a Python script that tracks exercises using the Nutritionix API and updates a Google Sheets spreadsheet using the Sheety API. The script prompts the user to input their exercise details, sends a request to the Nutritionix API to get exercise information, and then updates a Google Sheets spreadsheet with the exercise details using the Sheety API.

# Set up the environment variables:
=> Set NT_APP_ID to your Nutritionix API ID.

=> Set NT_API_KEY to your Nutritionix API Key.

=> Set SHEET_ENDPOINT to the Sheety API endpoint for updating the Google Sheets spreadsheet.

# How it works
Enter the exercise details you want to track for the day.
The script will send a request to the Nutritionix API with the exercise details, and receive exercise information in response.
The script will update the Google Sheets spreadsheet with the exercise details using the Sheety API.

# Spreadsheet Data
The script updates the Google Sheets spreadsheet with the following exercise details for each tracked exercise:

Date: The current date in the format dd-mm-yyyy.
Time: The current time in the format HH:MM:SS.
Exercise: The name of the exercise as provided by the user.
Duration: The duration of the exercise in minutes.
Calories: The number of calories burned during the exercise.
