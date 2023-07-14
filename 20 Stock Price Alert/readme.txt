Stock Price Report
This code retrieves the stock price of a specified company, in this case, Tesla Inc (TSLA), from the Alpha Vantage API. It also fetches the top news articles related to the company from the News API. The script calculates the percentage change in the stock price between the most recent two trading days and sends an email with the stock price report and the news articles.

Before running this script, ensure that you have the following:
=> Alpha Vantage API key
=> News API key
=> Gmail account credentials (Email ID and App Password) for sending emails

Configuration
Before running this code, you need to configure the following variables in the code:

=> STOCK_API_KEY: Replace os.environ.get("STOCK_API_KEY") with your Alpha Vantage API key.
=> NEWS_API_KEY: Replace os.environ.get("NEWS_API_KEY") with your News API key.
=> EMAIL_ID: Replace os.environ.get("EMAIL_ID") with your Gmail account's email ID.
=> APP_PASSWORD: Replace os.environ.get("APP_PASSWORD") with your Gmail account's app password.
=> RECEIVER_EMAIL: Replace os.environ.get("RECEIVER_EMAIL") with the email address where you want to receive the stock price report.
