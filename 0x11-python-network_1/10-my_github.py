#!/usr/bin/python3
"""A python script that uses the github api to display my github id
"""

import sys
import requests


if __name__ == '__main__':
    username = sys.argv[1]
    pswd = sys.argv[2]
    g_api = "https://api.github.com/user"
    get_api = requests.get(g_api, auth=(username, pswd))
    print(get_api.json().get("id"))
