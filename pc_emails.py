#!/usr/bin/env python3

## We shall use this function to generate mails to be sent to our mailboxes 

import os, smtplib, mimetypes
from email.message import EmailMessage

password = os.environ.get('pass')
## Function to generate mail and attach pdf report


def mail_report():
    sender = "your_gmail@gmail.com"
    password = os.environ.get('pass')
    recipient = ['example@mail.com']
    subject = "Pc Metrics for user: "+ os.getlogin()
    body = 'Attached to this email is a pdf report showing the pc metrics of this machine at a particular timestamp'

    attchment_path = '/tmp/PC_Metrics.pdf'
    attchment_filename = os.path.basename(attchment_path)
    mime_type, _ = mimetypes.guess_type(attchment_path)
    mime_type, sub_type = mime_type.split('/')

    message = EmailMessage()
    message['From'] = sender
    message['To'] = ','.join(recipient)
    message['Subject'] = subject
    message.set_content(body)

    with open(attchment_path, 'rb') as attach:
        message.add_attachment(attach.read(),
                            maintype=mime_type,
                            subtype=sub_type,
                            filename=attchment_filename)

    mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail_server.login(sender, password)
    mail_server.send_message(message)
    mail_server.quit()



mail_report()