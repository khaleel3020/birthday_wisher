# Extra Hard Starting Project #
import random
import smtplib
import datetime as dt
import pandas
my_mail = 'testpractice03@gmail.com'
password = 'bablu3001'

now = dt.datetime.now()
current_month = now.month
current_date = now.day
# 1.Update the birthdays.csv
data = pandas.read_csv('birthdays.csv')
# print(data)
# 2. Check if today matches a birthday in the birthdays.csv
with open('./letter_templates/letter_1.txt') as file_data1:
    letter_1 = file_data1.read()
with open('./letter_templates/letter_2.txt') as file_data2:
    letter_2 = file_data2.read()
with open('./letter_templates/letter_3.txt') as file_data3:
    letter_3 = file_data3.read()
letter_number = [letter_3, letter_2, letter_1]
connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
num = random.choice(letter_number)
for (index, row) in data.iterrows():
    # print('hi')
    if int(current_month) == row.month:
        if current_date == row.day:
            # print(row)
            # print(row.Name)
            new_letter = random.choice(letter_number).replace('NAME', str(row.Name))
            # print(new_letter)
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail, to_addrs=row.email, msg=f"subject:Birthday Wishes\n\n{new_letter}")
            connection.close()


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




