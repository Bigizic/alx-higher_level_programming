#!/usr/bin/python3
"""A python script that takes in a url sends a request to the url
and display the response of the body while managing httperror
"""

import sys
from urllib import request, error


if __name__ == '__main__':
    try:
        address = sys.argv[1]
        with request.urlopen(address) as open_url:
            print(open_url.read().decode('utf-8'))

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
