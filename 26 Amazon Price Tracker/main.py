import requests
from bs4 import BeautifulSoup
import smtplib

# Set user-agent headers and the product URL
headers = {
    'User-Agent': 'Your user agent',
    'Accept-Language': 'Your accept language'
}

product_url = "Product URL"

try:
    # Fetch the webpage and parse it
    response = requests.get(headers=headers, url=product_url)
    response.raise_for_status()  # Raise an exception for any unsuccessful HTTP response
    webpage = response.text
    soup = BeautifulSoup(webpage, 'html.parser')

    # Extract the price from the webpage
    price = int(soup.select('.a-price-whole')[0].getText().replace(".", "").replace(",", ""))

    # Set the desired price threshold
    threshold_price = 40000

    # Check if the current price is below the threshold
    if price <= threshold_price:
        # Establish an SMTP connection with Gmail server
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()  # Start a secure TLS connection

        # Replace "Your Email" and "Your app password" with your Gmail credentials
        connection.login("Your Email", "Your app password")

        # Compose the email message with the subject and body
        subject = "Price Drop Alert"
        body = "The price of the product has dropped below the specified threshold. Check it out on Amazon!"
        message = f"Subject: {subject}\n\n{body}"

        # Replace "Sender's email" and "Receiver's email" with appropriate email addresses
        from_addr = "Sender's email"
        to_addrs = "Receiver's email"

        # Send the email notification
        connection.sendmail(from_addr, to_addrs, message)

        # Close the SMTP connection
        connection.close()

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
