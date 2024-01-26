#!/usr/bin/python3
"""
Takes a letter as a command-line argument, sends a POST request.
"""

import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = 'http://0.0.0.0:5000/search_user'
data = {'q': q}

response = requests.post(url, data=data)

try:
    user_info = response.json()
    if user_info:
        print("[{}] {}".format(user_info['id'], user_info['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
