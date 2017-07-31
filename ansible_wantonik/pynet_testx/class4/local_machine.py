#!/usr/bin/env python
'''
Simple script to connect to my servers and execute shell commands,
to monitor CPU, memory and harddrive usage.
'''
import paramiko
from getpass import getpass

ip_addr = '127.0.0.1'
username = input(str('Enter username: '))
#username = 'breadfan'
password = getpass()
timeout = 15
port = 22
command_to_run = 'uptime'

def conn_to_host():
    try:
        print 'Establishing SSH connection...'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip_addr, username=username, password=password, timeout=timeout)
        print('Connection established with host ip address: %s') %(ip_addr)
        stdin, stdout, stderr = ssh.exec_command(command_to_run)
        type(stdin)
        print('Output of %s command ran on the remote host is: ...') %(command_to_run)
        print stdout.readlines() 
    except:
        print('Error occured')

conn_to_host()

