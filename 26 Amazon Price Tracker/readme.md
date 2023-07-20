# Amazon Price Alert Script
This is a Python script that fetches the price of a product from Amazon and sends an email notification if the price drops below a specified threshold. The script uses the requests library to fetch the webpage content and BeautifulSoup to parse the HTML and extract the price. If the price is less than or equal to the specified amount, the script sends an email notification using Gmail's SMTP server.

# Note
-> Replace "Your user agent" and "Your accept language" with appropriate values for your browser's user agent and language preferences. Also, set "Product URL" to the actual URL of the Amazon product you want to monitor.

-> Replace "YourEmail@gmail.com" with your Gmail email address and "YourAppPassword" with your Gmail app password. Also, set the appropriate "ReceiverEmail@gmail.com" where you want to receive the email notifications.

-> Ensure that your Gmail account allows "less secure apps" to access it. Alternatively, you can set up two-factor authentication and create an "App password" for your script to use.

-> The script fetches the price from Amazon's website, and the code might break if the website structure changes.
