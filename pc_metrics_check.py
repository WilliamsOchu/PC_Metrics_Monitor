#!/usr/bin/env python3

## This script when run generate the pdf report and send a mail accordingly 

import pc_monitor, reports_pdf_gen, pc_emails

check_report = reports_pdf_gen.reports_generator()

mail_send = pc_emails.mail_report()
