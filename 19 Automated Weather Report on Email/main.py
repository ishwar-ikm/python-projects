import requests
import smtplib


#-------- Parameters for API request --------#
parameters = {
    "lat": 30.361031,
    "lon": 76.848549,
    "appid": "My API key"
}

#-------- Requesting API --------#
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

#-------- Storing data in morning and night variables for today's date --------#
data_morning = response.json()['list'][:4]
data_night = response.json()['list'][4:7]

#-------- Variables to store the sum of temperatures --------#
morning_temp = 0
night_temp = 0

#-------- Variables to store max and min temperatures --------#
max_temp_morning = -400
min_temp_morning = 400

#-------- Variables to store the raining conditions --------#
will_rain_morning = "No"

# Calculating weather data for morning time
for hour_data in data_morning:
    morning_temp += hour_data['main']['temp']
    max_temp_morning = max(max_temp_morning, hour_data['main']['temp'])
    min_temp_morning = min(min_temp_morning, hour_data['main']['temp'])

    if hour_data['weather'][0]['id'] < 700:
        will_rain_morning = "Yes"


#-------- For night time --------#
max_temp_night = -400
min_temp_night = 400

will_rain_night = "No"

# Calculating weather data for night time
for hour_data in data_night:
    night_temp += hour_data['main']['temp']
    max_temp_night = max(max_temp_night, hour_data['main']['temp'])
    min_temp_night = min(min_temp_night, hour_data['main']['temp'])

    if hour_data['weather'][0]['id'] < 700:
        will_rain_night = "Yes"

# Constructing the weather report message
message = f'''
Daytime average temperature will be: {round(morning_temp/4-273.15, 2)}
Nighttime average temperature will be: {round(night_temp/3-273.15, 2)}
Maximum and minimum temperature during daytime: {round(max_temp_morning-273.15)}, {round(min_temp_morning-273.15)}
Maximum and minimum temperature during nighttime: {round(max_temp_night-273.15)}, {round(min_temp_night-273.15)}
Will it rain in the morning: {will_rain_morning}
Will it rain at night: {will_rain_night}
'''


################ Sending email about the weather condition ################
connection = smtplib.SMTP("smtp.gmail.com")  # Establishing an SMTP connection with Gmail server
connection.starttls()  # Starting a secure TLS connection
connection.login("My Email", "My app password")  # Logging into the Gmail account
connection.sendmail(
    from_addr="Sender's email",  # Sender's email address
    to_addrs="Receiver's email",  # Receiver's email address
    msg="subject:Weather Report\n\n" + message  # Composing the email message with the subject and body
)
connection.close()  # Closing the SMTP connection
