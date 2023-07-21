# Automated Weather Report
This code retrieves weather data from the OpenWeatherMap API for a specific location and sends an email containing the weather report. Here's a breakdown of how the code works:

# Dependencies:
- `requests`: A library for making HTTP requests to the API.
- `smtplib`: A library for sending emails using the Simple Mail Transfer Protocol (SMTP).

# API Parameters:
- `lat`: The latitude of the location.<br>
- `lon`: The longitude of the location.<br>
- `appid`: Your API key for accessing the OpenWeatherMap API.<br>

# API Request:
- The code sends a GET request to the OpenWeatherMap API's forecast endpoint (`https://api.openweathermap.org/data/2.5/forecast`).<br>
- The request includes the API parameters (`lat`, `lon`, and `appid`).<br>
- The response is stored in the `response` variable.<br>

# Data Retrieval:
- The code extracts the weather data for the morning and night for the current date from the API response.<br>
- The morning data consists of the first 4 3 hourly forecasts, and the night data consists of the next 3 3 hourly forecasts.<br>
- The temperature, maximum and minimum temperatures, and rain condition for both morning and night are extracted and stored in variables.<br>

# Email Composition:
- A message string is constructed using the extracted weather data.<br>
- The message includes the average temperatures for morning and night, the maximum and minimum temperatures for both periods, and the rain condition.<br>
- The message is formatted using f-string syntax.<br>

# Sending Email:
- The code establishes a connection with the SMTP server of Gmail (`smtp.gmail.com`).<br>
- The connection is secured using the Transport Layer Security (TLS) protocol.<br>
- The code logs in to the Gmail account using the email address and the application password.<br>
- An email is composed with the sender's and receiver's email addresses, and the weather report message as the email body.<br>
- The email is sent using the `sendmail` function of the SMTP connection.<br>
- Finally, the connection is closed.<br>

# Note: 
You need to replace the placeholder values with your actual API key, email addresses, and app password for the code to work correctly.

Please ensure that you have the necessary permissions and configurations set up for accessing the OpenWeatherMap API and sending emails through the Gmail SMTP server.

