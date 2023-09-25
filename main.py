import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "mateuscesouza@gmail.com"
PASSWORD = "dcftzcsunebfmtvr"


now = dt.datetime.now()
month_day = now.day
month = now.month

random_number = random.randint(1,3)

data = pandas.read_csv('./birthdays.csv')
data_dict = data.to_dict(orient='records')

for user in data_dict:
    if user['month'] == month and user['day'] == month_day:
        with open(f'./letter_templates/letter_{random_number}.txt') as letter:
            new_letter = letter.read()
            name_letter = new_letter.replace('[NAME]', user['name'])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Happy birthday {user['name']}!\n\n{name_letter}")
        connection.close()



