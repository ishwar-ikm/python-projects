import requests

# Set the parameters for the API request
parameters = {
    'amount': 100,  # Number of questions to fetch
    'type': 'boolean'  # Type of questions (in this case, boolean for true/false questions)
}

# Send a GET request to the trivia API with the parameters
response = requests.get("https://opentdb.com/api.php", params=parameters)

# Raise an exception if the request was unsuccessful
response.raise_for_status()

# Extract the question data from the response
question_data = response.json()['results']
