#!/usr/bin/python
'''
Use the ciscoconfparse library to find the crypto maps that are using pfs group2
'''

from ciscoconfparse import CiscoConfParse

def main():
    '''
    Use the ciscoconfparse library to find the crypto maps that are using pfs
    group2
    '''
    cisco_file = 'cisco.txt'

    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO',
                                                 childspec=r'AES-SHA')
    print "\nCrypto Maps not using AES-SHA encryption:"
    for entry in crypto_maps:
        print "  {0}".format(entry.text)
    print

if __name__ == "__main__":
    main()
