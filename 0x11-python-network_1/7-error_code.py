#!/usr/bin/python3
"""A python script that  takes in a URL, sends a request to the
URL and displays the body of the response. handles http error
"""

import requests
import sys


if __name__ == '__main__':

    address = sys.argv[1]
    get_r = requests.get(address)

    if get_r.status_code >= 400:
        print("Error code: {}".format(get_r.status_code))
    else:
        print(get_r.text)
