#!/usr/bin/python3
"""A python script that takes in a letter and sends a POST request
"""

import sys
import requests


if __name__ == '__main__':
    address = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 1:
        print("No result")
        q = ""
        sys.exit(1)
    else:
        q = sys.argv[1]
        get_r = requests.post(address, data={"q": q})
        try:
            get_r_json = get_r.json()
            if get_r_json:
                my_id = get_r_json.get("id")
                my_name = get_r_json.get("name")
                print("[{}] {}".format(my_id, my_name))
            else:
                print("No result")
                sys.exit(1)
        except ValueError:
            print("Not a valid JSON")
