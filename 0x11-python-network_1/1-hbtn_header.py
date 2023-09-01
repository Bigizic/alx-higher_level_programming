#!/usr/bin/python3
"""A python script that takes in a url, sends a request to the url
and display the value of a particular variable found in the header
of the response
"""

import urllib.request
import sys

if __name__ == '__main__':
    address = sys.argv[1]

    with urllib.request.urlopen(address) as open_url:
        get_variable = open_url.getheader('X-Request-Id')
        print(get_variable)
