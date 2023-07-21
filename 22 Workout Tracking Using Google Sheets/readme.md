# Exercise Tracker
This is a Python script that tracks exercises using the Nutritionix API and updates a Google Sheets spreadsheet using the Sheety API. The script prompts the user to input their exercise details, sends a request to the Nutritionix API to get exercise information, and then updates a Google Sheets spreadsheet with the exercise details using the Sheety API.

# Set up the environment variables:
=> Set NT_APP_ID to your Nutritionix API ID.<br>
=> Set NT_API_KEY to your Nutritionix API Key.<br>
=> Set SHEET_ENDPOINT to the Sheety API endpoint for updating the Google Sheets spreadsheet.

# How it works
Enter the exercise details you want to track for the day.<br>
The script will send a request to the Nutritionix API with the exercise details, and receive exercise information in response.<br>
The script will update the Google Sheets spreadsheet with the exercise details using the Sheety API.<br>

# Spreadsheet Data
The script updates the Google Sheets spreadsheet with the following exercise details for each tracked exercise:<br>

Date: The current date in the format dd-mm-yyyy.<br>
Time: The current time in the format HH:MM:SS.<br>
Exercise: The name of the exercise as provided by the user.<br>
Duration: The duration of the exercise in minutes.<br>
Calories: The number of calories burned during the exercise.<br>
