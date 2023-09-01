#!/usr/bin/python3
"""A python script that fetches the status of a website
using the package urllib
"""

import urllib.request

address = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(address) as open_url:
    body_content = open_url.read()
    print("Body response:")
    print("    - type: {}".format(type(body_content)))
    print("    - content: {}".format(body_content))
    print("    - utf8 content: {}".format(body_content.decode('utf-8')))
