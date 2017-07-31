#!/usr/bin/env python
'''
This is simple script to connect to my home server via Paramiko.
Based on Kirk Byers' Python course.
'''
import paramiko
from getpass import getpass

ip_addr = '51.171.33.233'
username = 'breadfan'
password = getpass()
timeout = 10
port = 22

remote_conn_pre = paramiko.SSHClient()
#remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
add_host_key_policy = paramiko.AutoAddPolicy
remote_conn_pre.load_system_host_keys()
remote_conn_pre.connect(ip_addr, username=username, password=password, port=port, timeout=timeout)
#print remote_conn_pre.get_transport()
remote_conn = remote_conn_pre.invoke_shell()
outp = remote_conn.recv(5000)
#print outp
print 10 * '*'
remote_conn.send('uptime -a')
outp = remote_conn.recv(5000)
#print outp
print 10 * '#'
#remote_conn.send('ls -alh')
#outp = remote_conn.recv(5000
print outp.readlines()

