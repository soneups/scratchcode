#!/usr/bin/python
# HT - http://trevorappleton.blogspot.de/2014/11/sending-email-using-python.html
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'your_username@gmail.com'
GMAIL_PASSWORD = 'your_gmail_password' #CAUTION: This is stored in plain text!

recipient = 'recipient@email_address.com'
subject = 'Email Subject'
emailText = 'This is the content of the e-mail.'

emailText = "" + emailText + ""

headers = ["From: " + GMAIL_USERNAME,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

session.ehlo()
session.starttls()
session.ehlo

session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + emailText)
session.quit()
