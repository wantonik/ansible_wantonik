#!/usr/bin/env python
import yaml, json


routers = [{'rtr1': [{'hostname':'pynet-rtr1'}, {'ip_addr':'184.105.247.70'}, {'username':'pyclass'}, {'password':'secret'}]},\
           {'rtr2': [{'hostname':'pynet-rtr2'}, {'ip_addr':'184.105.247.71'}, {'username':'pyclass'}, {'password':'secret'}]},\
           {'model': 'Cisco_881'}]

switches = [{'sw1': [{'hostname':'pynet-sw1'}, {'ip_addr':'184.105.247.72'}, {'username':'admin1'}, {'password':'secret'}]},\
            {'sw2': [{'hostname':'pynet-sw2'}, {'ip_addr':'184.105.247.73'}, {'username':'admin1'}, {'password':'secret'}]},\
            {'sw3': [{'hostname':'pynet-sw3'}, {'ip_addr':'184.105.247.74'}, {'username':'admin1'}, {'password':'secret'}]},\
            {'sw4': [{'hostname':'pynet-sw4'}, {'ip_addr':'184.105.247.75'}, {'username':'admin1'}, {'password':'secret'}]},\
            {'model': 'Arista_vEOS'}]

juniper = [{'srx1': [{'hostname':'pynet-jnpr-srx1'}, {'ip_addr':'184.105.247.76'}, {'username':'pyclass'}, {'password':'secret'}]},\
           {'model': 'Juniper_SRX'}]


nods = [routers, switches, juniper]

print('')
print(nods)

## Writing Python complex data structure to YAML file
def py2yaml():        ## Name of the converter
    with open("class1e6-yaml.yaml", "w") as f:
        f.write(yaml.dump(nods, default_flow_style=False))
    print('Python data converted to YAML and saved in .yaml file')

## Writing Python complex data structure to JSON file
def py2json():        ## Name of the converter
    with open("class1e6-json.json", "w") as f:
        json.dump(nods, f)
    print('Python data converted to JSON and saved in .json file')

print(80 * '-')
py2yaml()
py2json()
print(80 * '-')
exit
