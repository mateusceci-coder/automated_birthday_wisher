
import datetime as dt
import random
import smtplib

MY_EMAIL = "mateuscesouza@gmail.com"
PASSWORD = "dcftzcsunebfmtvr"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("./quotes.txt", "r") as file:
        lines = file.readlines()
        new_quote = random.choice(lines)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="mateuscesouza@yahoo.com", msg=f"Subject:Motivational\n\n{new_quote}")
        connection.close()


