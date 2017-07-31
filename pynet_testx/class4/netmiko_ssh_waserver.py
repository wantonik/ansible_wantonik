#!/usr/bin/env python
'''Simple script to connect to my Linux server with Netmiko.'''
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

wa_server = {
    'device_type': 'linux',
    'ip': '192.168.1.8',
    'username': 'breadfan',
    'password': password,
    'port': 22,
    }

wa = ConnectHandler(**wa_server)
print wa
