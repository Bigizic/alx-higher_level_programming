#!/usr/bin/python3
"""A python script that takes in a url and an email sends a post
request to the passed url
"""

import sys
from urllib import parse, request

if __name__ == '__main__':
    address = sys.argv[1]
    email = sys.argv[2]
    email_dict = parse.urlencode({"email": email}).encode('utf-8')

    with request.urlopen(address, email_dict) as post_req:
        body = post_req.read().decode('utf-8')
        print(body)
