import datetime as dt
import smtplib
import os
import requests

# Define the stock and company names
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Define the endpoints and API keys
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

# Prepare the parameters for the stock API request
stock_parameter = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
}

# Send a request to the stock API
response = requests.get(STOCK_ENDPOINT, params=stock_parameter)
response.raise_for_status()

# Extract the stock data from the response
data = response.json()['Time Series (Daily)']

# Get yesterday's and the day before yesterday's dates
yesterday = str(dt.datetime.now() - dt.timedelta(1)).split()[0]
day_before_yesterday = str(dt.datetime.now() - dt.timedelta(2)).split()[0]

# Extract the closing prices for yesterday and the day before yesterday
yesterday_data_close = float(data[yesterday]['4. close'])
day_before_yesterday_data_close = float(data[day_before_yesterday]['4. close'])

# Calculate the percentage change in the stock price
diff = abs(yesterday_data_close - day_before_yesterday_data_close)
percentage = round((diff / max(yesterday_data_close, day_before_yesterday_data_close)) * 100, 2)

# Prepare the parameters for the news API request
news_parameter = {
    'qInTitle': "Tesla",
    'from': yesterday,
    'sortBy': 'popularity',
    'apiKey': NEWS_API_KEY,
}

# Send a request to the news API
response2 = requests.get(NEWS_ENDPOINT, params=news_parameter)
response2.raise_for_status()

# Extract the news articles from the response
news_data = response2.json()['articles'][:3]

# Determine the symbol based on the stock price change
if yesterday_data_close > day_before_yesterday_data_close:
    symbol = "⏶"
else:
    symbol = "⏷"

# Prepare the email message
message = f'''
{STOCK_NAME}: {symbol}{percentage}%

Article 1:
Headline: {news_data[0]['title']}
Brief: {news_data[0]['description']}

Article 2:
Headline: {news_data[1]['title']}
Brief: {news_data[1]['description']}

Article 3:
Headline: {news_data[2]['title']}
Brief: {news_data[2]['description']}
'''

################ Sending email about the stock price ################

# Connect to the SMTP server
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

# Log in to the Gmail account
connection.login(os.environ.get("EMAIL_ID"), os.environ.get("APP_PASSWORD"))

# Encode the message using UTF-8
subject = "Stock Price Report"
message = f"Subject: {subject}\n\n{message}"
message = message.encode("utf-8")

# Send the email
connection.sendmail(
    from_addr=os.environ.get("EMAIL_ID"),
    to_addrs=os.environ.get("RECEIVER_EMAIL"),
    msg=message
)

# Close the connection
connection.close()
