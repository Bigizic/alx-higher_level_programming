#!/bin/bash
# a bash script that takes in a URL, perfroms other actions
curl -s -w "%{size_download}\n" -o /dev/null $1
