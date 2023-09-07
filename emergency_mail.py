#!/usr/bin/env python3

## This script will generate an emergency email if certain PC metrics go below par 

import pc_emails, pc_monitor, reports_pdf_gen, psutil, time, datetime
import os, smtplib, ssl, mimetypes
from email.message import EmailMessage

## Lets denote the general PC checks 
mems = psutil.virtual_memory()
diskss = psutil.disk_usage('/')
uptimess = time.time() - psutil.boot_time()
uptime_hrs = uptimess / 3600
mins_calc = uptime_hrs % 1
mins_calc_conv = (mins_calc * 60)/100
hrs_calc = uptime_hrs // 1
last_reboot = psutil.boot_time()
last_rebooted_time = datetime.datetime.fromtimestamp(last_reboot)

## Lets instantiate a function to send a mail
def send_emergency():
    sender = "your_gmail@gmail.com"  
    password = 'diusfpftjnmfqyjg'
    recipient = ['example@mail.com']    
    body = '''
Attached to this email is a pdf report showing the pc metrics of this machine at a particular timestamp
    '''
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
    mail_server.set_debuglevel(1)
    mail_server.login(sender, password)
    mail_server.send_message(message)
    mail_server.quit()

## Lets set triggers to generate and send mail
if psutil.cpu_percent(10) >= 80:
    new_report = reports_pdf_gen.reports_generator()
    subject = "Warning!! Check CPU metrics for: "+ os.getlogin()
    emergency = send_emergency()

elif mems.percent >= 90:
    new_report = reports_pdf_gen.reports_generator()
    subject = "Warning!!! Outrageuos Memory Consumption on: " + os.getlogin()
    emergency = send_emergency()

elif diskss.percent >= 90:
    new_report = reports_pdf_gen.reports_generator()
    subject = "Warning!!! Low Storage Space on: " + os.getlogin()
    emergency = send_emergency()

elif hrs_calc == 0.1 and mins_calc == 0.1:
    new_report = reports_pdf_gen.reports_generator()
    subject = "Warning!!! A rebbot has occured on user: " + os.getlogin()
    emergency = send_emergency()

