#!/usr/bin/env python3

## This script will monitor pc metrics such as cpu%, memory, disk, uptime and network interface

## Let us import the necessary modules
from datetime import datetime
import datetime, os, psutil, shutil, time, socket, requests

## Function to check CPU Metrics
def cpu_check():
	cpu_count = '{} core CPU'.format(psutil.cpu_count())
	cpu_percent = '{}%'.format(psutil.cpu_percent(10))
	cpu_speed = psutil.cpu_freq()
	active_cpu_speed = '{:.2f}ghz'.format(cpu_speed.current/1000)

	return cpu_count, cpu_percent, active_cpu_speed
	
## Function to check Memory Metrics
def mem_check():
	mem = psutil.virtual_memory()
	total = '{:.2f}GB'.format(mem.total / (1024 ** 3))
	free = '{:.2f}GB'.format(mem.available / (1024 ** 3))
	used = '{:.2f}GB'.format((mem.total - mem.available) / (1024 ** 3))
	percent_used = '{}%'.format(mem.percent)
	percent_free = '{:.2f}%'.format((mem.available / mem.total) * 100)
	mem_stats = []
	mem_stats.extend([total, free, used, percent_used, percent_free])

	return mem_stats

## Function to check Storage Metrics
def disks_check():
	disks_stats = shutil.disk_usage('/')
	disks_total = '{:.2f}GB'.format(disks_stats.total / (1024 ** 3))
	disks_free = '{:.2f}GB'.format (disks_stats.free / (1024 ** 3))
	disks_used = '{:.2f}GB'.format(disks_stats.used / (1024 ** 3))
	disks_percent_free = '{:.2f}%'.format((disks_stats.free / disks_stats.total) * 100)
	disks_percent_used = '{:.2f}%'.format((disks_stats.used / disks_stats.total) * 100)
	disks_os_managed = '{:.2f}GB'.format((disks_stats.total - (disks_stats.free + disks_stats.used)) / (1024 ** 3))  
	storages_stats =[]
	storages_stats.extend([disks_total, disks_free, disks_used, disks_percent_free, disks_percent_used, disks_os_managed])
	
	return storages_stats

## Function to check PC Uptime Metrics
def uptime_check():
	uptime_secs = time.time() - psutil.boot_time()
	uptime_hrs = uptime_secs / 3600
	mins_calc = uptime_hrs % 1
	mins_calc_conv = (mins_calc * 60)/100
	hrs_calc = uptime_hrs // 1
	uptime_fin = hrs_calc + mins_calc_conv
	uptime_fin_deci = '{:.2f}'.format(uptime_fin)
	last_reboot = psutil.boot_time()
	last_reboot_time = datetime.datetime.fromtimestamp(last_reboot)
	rev_up_hrs ='{:.1f}'.format(hrs_calc).split('.')[0] + ' hrs'
	rev_up_mins = '{:.2f} mins'.format(mins_calc_conv).split('.')[1] 
	uptime_stats =[]
	uptime_stats.extend([uptime_fin_deci, rev_up_hrs, rev_up_mins])
	
	return uptime_stats, last_reboot_time

## Function to check Network Connection
def network_check():
	my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	my_socket.connect(("8.8.8.8", 80))
	sockss = 'private address: working connection on {}'.format(my_socket.getsockname()[0])
	external_ip_check = requests.get('https://api.ipify.org')
	external_ip = 'public address: working connection on {}'.format(external_ip_check.text)
	network_stats = []
	network_stats.extend([sockss, external_ip])
	
	return network_stats
	
	


