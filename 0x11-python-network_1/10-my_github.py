#!/usr/bin/python3
"""
Takes GitHub username and personal access token as command-line arguments.
uses Basic Authentication, and displays GitHub id.
"""

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./10-my_github.py <username> <token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

url = 'https://api.github.com/user'

response = requests.get(url, auth=(username, token))

try:
    user_info = response.json()
    print(user_info.get('id', 'None'))
except ValueError:
    print("Error: Not a valid JSON")
