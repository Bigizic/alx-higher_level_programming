#!/usr/bin/python3
"""A python script that takes in a URL, sends a request to the URL
and display the value of a variable using requests
"""

import requests
import sys


if __name__ == '__main__':
    address = sys.argv[1]

    get_r = requests.get(address)
    print(get_r.headers.get('X-Request-Id'))
