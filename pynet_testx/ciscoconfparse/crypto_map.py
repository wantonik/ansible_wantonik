#!/usr/bin/python
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")
crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")
print crypto_map
print type(crypto_map)

for i in crypto_map:
    print i.text
#    for j in i.text:
#        print j


quit()
