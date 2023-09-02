#!/usr/bin/python3
"""A script that connects to the github api and get commit info
from a repo
"""

import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    api = f'https://api.github.com/repos/{owner}/{repo}/commits?per_page=10'
    get_r = requests.get(api)
    for commits in reversed(get_r.json()):
        sha = commits.get("sha")
        author = commits.get("commit").get("author")
        name = author.get("name")
        print("{}: {}".format(sha, name))
