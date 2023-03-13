import smtplib
import datetime

#Mailserver samt portid
smtp_mailInfo = smtplib.SMTP('smtp.gmail.com', 587)

#Krypterar mailet
smtp_mailInfo.starttls()

print("Welcome to the Automatic Email Sender by Goofballs dios")

email = input("Enter your email: ")
password = input("Enter your password: ")

smtp_mailInfo.login(email, password)

recipent = input("Enter the recipents email: ")
subject = input("Enter the email subject: ")
mainText = input("Enter the main text: ")