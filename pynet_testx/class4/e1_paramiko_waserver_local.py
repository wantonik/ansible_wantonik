#!/usr/bin/env python
'''
This is simple script to connect to my home server via Paramiko.
Based on Kirk Byers' Python course.
'''
import paramiko, time
from getpass import getpass

ip_addr = '192.168.1.8'
username = 'breadfan'
password = getpass()
timeout = 10
port = 22

remote_conn_pre = paramiko.SSHClient()
#remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#add_host_key_policy = paramiko.AutoAddPolicy
remote_conn_pre.load_system_host_keys()
remote_conn_pre.connect(ip_addr, username=username, password=password, port=port, timeout=timeout, look_for_keys=False, allow_agent=False)
#print remote_conn_pre.get_transport()
remote_conn = remote_conn_pre.invoke_shell()
outp = remote_conn.recv(5000)
print 'If prompt received, you are connected.', '\n', outp
remote_conn.settimeout(6.0)    ## Wait for the data 6sec
print

print 10 * '*'
## The below section removed for Linux host-'terminal lenght' is not shell command error
#remote_conn.send("\n")
#time.sleep(1)
#remote_conn.send("terminal length 0\n")
#time.sleep(1)
#outp = remote_conn.recv(5000)
#time.sleep(1)
#print outp

remote_conn.send("\n")
time.sleep(1)
remote_conn.send('ls -alh /home/breadfan/vsftpd/')
time.sleep(1)
remote_conn.send("\n")
time.sleep(1)
outp = remote_conn.recv(65535)
time.sleep(1)
print outp    ## outp.readlines() method doesn't work here
