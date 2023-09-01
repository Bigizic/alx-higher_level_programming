#!/usr/bin/python3
"""A python script that fetches an address using the package
requests
"""

import requests

if __name__ == '__main__':
    address = 'https://alx-intranet.hbtn.io/status'

    get_r = requests.get(address)
    response = get_r.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(get_r.content.decode('utf-8')))
