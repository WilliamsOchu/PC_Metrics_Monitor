#!/usr/bin/env python3

## We shall generate a pdf report for our pc metrics

import os, pc_emails, pc_monitor
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

## Generate pdf name, size and margins
def reports_generator():
    styles = getSampleStyleSheet()
    reporter = SimpleDocTemplate('/tmp/PC_Metrics.pdf', pagesize=letter,
                                rightMargin=72,leftMargin=72,
                                topMargin=72,bottomMargin=18)
    story = [Spacer(1,0.5*inch)]
    style = styles['Normal']
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    ## Get current user and current timestamp
    current_user = os.getlogin()
    current_time = datetime.now()
    current_time_strip = current_time.strftime("%d/%m/%Y %H:%M:%S")

    ## Set pdf title and 
    items_spacer = Spacer(1,0.1*inch)
    title = Paragraph("Performace Metrics generated for the user: "+ current_user + " as at " + current_time_strip , styles['h3'])

    ## Generate CPU Metrics
    cpu_heads = Paragraph('<u>CPU Metrics</u>', styles['h4'])
    cpu_metrics = (pc_monitor.cpu_check())
    cpu_percents = Paragraph("Current CPU usage: " + cpu_metrics[1])
    cpu_core_counts = Paragraph("Number of CPUs: "+ cpu_metrics[0])
    cpu_speeds = Paragraph("The CPU is running at a speed of: "+ cpu_metrics[2])

    ## Generate Memory Metrics
    mem_heads = Paragraph('<u>Memory Metrics</u>', styles['h4'])
    mem_metrics = pc_monitor.mem_check()
    mem_tots = Paragraph('The Total Memory on this machine is: '+ mem_metrics[0])
    mem_free_used = Paragraph('Memory in use: '+ mem_metrics[2]+" "+'('+mem_metrics[3]+')' + ' and free Memory: ' + mem_metrics[1] +" "+ '(' +mem_metrics[4] + ')')

    ## Generate Storage Metrics
    storage_heads = Paragraph('<u>Storage Metrics</u>', styles['h4'])
    storage_metrics = pc_monitor.disks_check()
    storage_tots = Paragraph("Total storage : " + storage_metrics[0])
    storage_managed = Paragraph("OS managed storage: "+ storage_metrics[5])
    storage_var = Paragraph('Availabe storage: '+ storage_metrics[1]+ '('+ storage_metrics[3] + ')' +' and used Storage: ' + storage_metrics[2] + '(' + storage_metrics[4] + ')')

    ## Generate PC Uptime Metrics
    uptime_heads = Paragraph('<u>Uptime Metrics</u>', styles['h4'])
    uptime_metrics = pc_monitor.uptime_check()
    last_boot = Paragraph('Last boot time of this computer: '+ str(uptime_metrics[1]))
    uptimes_tots = Paragraph('Uptime: '+ uptime_metrics[0][0])
    uptime_long = Paragraph('This computer has been up: '+ uptime_metrics[0][1] + ', ' + uptime_metrics[0][2])

    ## Generate Network Metrics
    network_heads = Paragraph('<u>Network Metrics</u>', styles['h4'])
    network_metrics = pc_monitor.network_check()
    private_nets = Paragraph(network_metrics[0])
    public_nets = Paragraph(network_metrics[1])

    ## Adding contents to the pdf
    story.append(title)
    story.append(items_spacer)
    story.append(cpu_heads)
    story.append(cpu_percents)
    story.append(items_spacer)
    story.append(cpu_core_counts)
    story.append(items_spacer)
    story.append(cpu_speeds)
    story.append(Spacer(1,0.4*inch))
    story.append(mem_heads)
    story.append(mem_tots)
    story.append(items_spacer)
    story.append(mem_free_used)
    story.append(Spacer(1,0.4*inch))
    story.append(storage_heads)
    story.append(storage_tots)
    story.append(items_spacer)
    story.append(storage_managed)
    story.append(items_spacer)
    story.append(storage_var)
    story.append(Spacer(1,0.4*inch))
    story.append(uptime_heads)
    story.append(last_boot)
    story.append(items_spacer)
    story.append(uptimes_tots)
    story.append(items_spacer)
    story.append(uptime_long)
    story.append(Spacer(1,0.4*inch))
    story.append(network_heads)
    story.append(private_nets)
    story.append(items_spacer)
    story.append(public_nets)

    ## Build the report
    reporter.build(story)


