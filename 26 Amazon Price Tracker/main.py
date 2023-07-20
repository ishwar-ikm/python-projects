import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-IN,en;q=0.9,en-US;q=0.8,hi;q=0.7,fr;q=0.6'
}
response = requests.get(headers=headers, url="https://www.amazon.in/Sony-PS5-Digital-Standalone/dp/B0BSNHFVL4/?_encoding=UTF8&pd_rd_w=eD5N8&content-id=amzn1.sym.e5c03be3-10ba-4bc8-b9be-6fcea12320ed%3Aamzn1.symc.adba8a53-36db-43df-a081-77d28e1b71e6&pf_rd_p=e5c03be3-10ba-4bc8-b9be-6fcea12320ed&pf_rd_r=79JS5PXA31SDJ3ARD6WS&pd_rd_wg=NrIfk&pd_rd_r=84659370-2616-4552-9569-eb18be450ce7&ref_=pd_gw_ci_mcx_mr_hp_atf_m")
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

price = int(soup.select('.a-price-whole')[0].getText().replace(".", "").replace(",", ""))

if price <= 40000:
    connection = smtplib.SMTP("smtp.gmail.com")  # Establishing an SMTP connection with Gmail server
    connection.starttls()  # Starting a secure TLS connection
    connection.login("My Email", "My app password")  # Logging into the Gmail account
    connection.sendmail(
        from_addr="Sender's email",  # Sender's email address
        to_addrs="Receiver's email",  # Receiver's email address
        msg="subject:Weather Report\n\n" + message  # Composing the email message with the subject and body
    )
    connection.close()  # Closing the SMTP connection
