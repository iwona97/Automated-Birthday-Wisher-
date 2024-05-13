import pandas
from datetime import datetime
import random
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")


def send_birthday_email(birthday_person, contents):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")


today = datetime.today()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {}
for (index, data_row) in data.iterrows():
    month = data_row["month"]
    day = data_row["day"]
    name = data_row["name"]
    email = data_row["email"]
    birthday_dict[(month, day)] = {"name": name,
                                   "email": email}

# Check if today matches a birthday in the birthdays.csv
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]

    # choose random letter_file
    random_number = random.randint(1, 3)
    file_path = f"letter_templates/letter_{random_number}.txt"
    with (open(file_path) as letter_file):

        # replace [NAME] with birthday_person__name
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # send email
    send_birthday_email(birthday_person, contents)













