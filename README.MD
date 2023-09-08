# PC Metrics Monitor
### Monitor Computer Performance 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

PC Metrics Monitor is a python suite developed to help users monitor the performance of their units.  
This suite returns a nicely formatted PDF report that highlights current CPU usage, curent CPU speed, memory and storage statistcis as well as PC uptime.<br> It also tests the users network connection and returns both the private and public ip configurations.<br>The suite contains a script that can send the generated PDf report to a mail address or cetain mailboxes.<br>
The suite also contains an emergency script that can kick and send a report if certain thresholds are exceeded.



## Contents of this Suite
- pc_monitor.py
- reports_pdf_gen.py
- pc_emails.py
- emergency_mail.py
- pc_metrics_check.py
 

## Explaining the contents of the suite

##### pc_monitor.py
This module is imported and run by reports_pdf_gen.py
##### reports_pdf_gen.py
This script imports the pc_monitor.py and generates a PDF report of the PC metrics obtained
##### pc_emails.py
This script sends an email with the PDF report attached to mailboxes 
##### emergency_mail.py
This script will automatically send a mail if certain thresholds are exceeded
##### pc_metrics_check.py
This is an AIO script that when run will generate the report and send a corresponding mail at a go

## How to use 
#### <ins>Use Case 1</ins>
To Check pc metrics and generate PDF report on current machine only, kindly edit the reports_pdf_gen.py script and call the reports_generator() function.<br>
By default the pdf generated is stored at /tmp directory on linux.<br>You can change it by editing its location under the reports_generator function as shown below.<br>
**reporter = SimpleDocTemplate('/tmp/PC_Metrics.pdf'** <br>
N:B: A change in pdf location will mandate you to also change its location in the pc_emails.py and emergency_mail.py scripts. <br> 
Run the script to generate a pdf report containing pc metrics 

#### <ins>Use Case 2</ins> 
Retrieve PC Metrics, generate report and send report to mailboxes. <br> 
First you need to edit the pc_emails.py script as stated below,<br>
You need to have an understanding of sending emails using the python smtplib. The smtp module has already been setup, however you will input your mail address and app password as well as the recipient or recipients. <br>
**sender = "your_gmail@gmail.com"** <br>
**password = os.environ.get('pass')** <br>
**recipient = ['example@mail.com']**   

Attached here is a link to a video showing how to setup smtp on gmail. <br>In this video you only need to generate an app password which will be used as your smtp password [How to setup SMTP for python on gmail](https://www.youtube.com/watch?v=g_j6ILT-X0k&t=604s) <br>
If you use a different mail provider, you might have to look up how to setup SMTP for your mail provider. <br>
Under the mail_report function, you can edit the sender and password variables to your gmail address and generated password. For security we set the password variable as an environment variable. In your current shell you can export your password as an environment variable or you may wish to enter your password as plain text.<br> 
You can add destination mailboxes under the recipient variable. This variable is a list and can take as many mailboxes as you wish. Kindly seprate the addresses with a comma.

After setting the sender, password and recipients varibales kindly run the pc_metrics_check.py script. This will import the the other modules, generate a pdf report and send the report to mailboxes you specified.

#### <ins>Use Case 3</ins>
The emergency_mail.py script can be automated to run. This script will generate a PDF report and send a mail once certain thresholds are exceeded.


## Need for Automation
Automation depends on the user and the OS running the machine. On linux you can use the cron scheduler to automate scripts

For our use case the emergency_mail.py script was deployed on a remote machine and scheduled to run every 2 minutes, each hour, each day of the week. This way we could monitor the remote pc closely. If any of the metrics being monitored exceeds the threshold we instantly get a mail with the affected metrics as mail subject. The abscence of a mail means we can infer our remote Pc is operating within its acceptable limits. Intermittently, we ran the pc_metrics_check.py script to know the current status of the remote machine.

## Python Techniques Employed
- PDF generation in python using reportlab module
- Email generation in python usuing Emailmessage module
- Python smtplib module 
- The use of python modules such as psutil, shutil, requests and socket

I will continue to modify this script as time goes on<br>
This work of mine is open source, feel free to make changs and commits if you deem it fit.<br>
Work Hard, Have Fun and Make History.