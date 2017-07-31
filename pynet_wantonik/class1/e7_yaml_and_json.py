#!/usr/bin/env python
import yaml, json, pprint

'''
Write a Python program that reads both the YAML file and the JSON file created in exercise6
and pretty prints the data structure that is returned.
'''

print('')

## Reading YAML file in Python
def yaml2py():        ## Name of the converter
    with open("e6yaml.yaml") as f:
        new_yaml_list = yaml.load(f)
    print('YAML data converted to Python and displayed on screen:')
    pprint.pprint(new_yaml_list)
    ## pprint module used to make it nice to read - same as default_flow_style=False
    print(80 * '-')

## Reading JSON file in Python
def json2py():        ## Name of the converter
    with open("e6json.json") as f:
        new_json_list = json.load(f)
    print('JSON data converted to Python and displayed on screen:')
    print(new_json_list)
    print(80 * '-')

yaml2py()
json2py()

## Add here a something like %s or to get the script finding .yaml and .json files generated earlier.
## We should be avoiding changing the 'lesson....yaml' or ...'json' file manually.
