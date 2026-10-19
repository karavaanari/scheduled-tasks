# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
import smtplib
import pandas
import random
import datetime as dt
import os

my_email = os.environ.get("my_email")
password = os.environ.get("password")

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as l:
        starting_letter = l.read()
        updated_letter = starting_letter.replace("[NAME]", birthday_dict[today]["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_dict[today]["email"],
            msg=f"Subject:Happy Birthday\n\n{updated_letter}".encode("utf-8")
        )
