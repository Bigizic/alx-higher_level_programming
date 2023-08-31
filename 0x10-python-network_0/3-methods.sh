#!/bin/bash
# a bash script that takes in a URL and displays all HTTP methods
curl -sI $1 | awk -F': ' '/Allow/{print $2}'
