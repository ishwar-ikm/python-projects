import datetime as dt
import random
import smtplib
import pandas


data = pandas.read_csv("birthdays.csv")
MY_EMAIL =  # Your email here
MY_PASSWORD =  # Your app password here
RECEIVER_NAME = ""
RECEIVER_EMAIL = ""


def is_birthday():
    """
    Check if today is someone's birthday.

    Returns:
        bool: True if it's someone's birthday, False otherwise.
    """
    global RECEIVER_NAME, RECEIVER_EMAIL

    today = dt.datetime.now()
    day = today.day
    month = today.month

    dob_day = data['day'].to_list()
    dob_month = data['month'].to_list()

    if day in dob_day and month in dob_month:
        RECEIVER_NAME = str(data[data.day == day].name.values[0])
        RECEIVER_EMAIL = str(data[data.day == day].email.values[0])
        return True
    return False


if is_birthday():
    # Choose a random letter template
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        content = file.read()
        content = content.replace("[NAME]", RECEIVER_NAME)

    # Connect to SMTP server and send the email
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=RECEIVER_EMAIL,
        msg=f"subject:HAPPY BIRTHDAY!!\n\n{content}"
    )
    connection.close()
