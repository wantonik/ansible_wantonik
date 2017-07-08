#!/usr/bin/env python
'''Use processes and Netmiko to connect to each of the devices
in DB. Execute 'show version' on each device. Record the amount
of time required to do this.'''

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django
from multiprocessing import Process
import time

def show_version(a_device):
    '''Establish connection with Netmiko + 'show version' command.'''
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type, port=a_device.port, ip=a_device.ip_address, username=creds.username, password=creds.password, secret='')
    print 'Establishing connection via Netmiko to all net devices ', '\n', remote_conn
    print 80 * '_'
    command_outp =  remote_conn.send_command_expect('show version')
    print command_outp

def main():
    django.setup()
    start_time = datetime.now()    
    net_devices = NetworkDevice.objects.all()
 
    # Use processes
    procs = []
    for a_device in net_devices:
        my_proc = Process(target=show_version, args=(a_device,))
        my_proc.start()
        procs.append(my_proc)

    for some_proc in procs:
            print some_proc
            some_proc.join() 
        
    elapsed_time = datetime.now() - start_time
    print 'Elapsed time: {}'.format(elapsed_time)
 
if __name__ == "__main__":
    main()
