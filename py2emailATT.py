# HT - http://pastebin.com/zCbGPDQx
import email
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import mimetypes
import smtplib
import datetime


def GMailFile(filenames, MailRecipients, subject):

    GmailUser      = '<whatever>@gmail.com'
    GmailPassword  = '<whatever>'
    
    d = datetime.date.today()
    if type(filenames) is str:
        filenames = [filenames]
    if type(MailRecipients) is str:
        MailRecipients = [MailRecipients]
        
    msg = MIMEMultipart()
    msg['From'] = GmailUser
    msg['To'] = ", ".join(MailRecipients)
    msg['Subject'] = subject
    for filename in filenames:
        part = MIMEApplication(open(filename,"rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(part)
    smtpserver = smtplib.SMTP('smtp.gmail.com:587')
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GmailUser, GmailPassword)
    smtpserver.sendmail(msg['From'], MailRecipients, msg.as_string())
    smtpserver.close()
