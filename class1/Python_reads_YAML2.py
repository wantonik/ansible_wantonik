filename = "e1v2-yaml_list2.yml"        # Replace with whatever you called the file
import yaml
from pprint import pprint

def read_yaml(filename):
    with open(filename) as f:
        return yaml.load(f)

pprint(read_yaml(filename))