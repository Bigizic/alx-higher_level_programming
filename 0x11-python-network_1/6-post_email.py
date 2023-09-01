#!/usr/bin/python3
"""A python script that takes in a URL and an email address,
sends a POST request to the passed URL
"""

import sys
import requests


if __name__ == '__main__':
    address = sys.argv[1]
    email = sys.argv[2]

    get_r = requests.post(address, data={"email": email})
    print(get_r.text)
