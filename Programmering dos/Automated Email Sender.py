import smtplib


smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.starttls()

print("Welcome to the Automatic Email Sender by Goofball Studios")