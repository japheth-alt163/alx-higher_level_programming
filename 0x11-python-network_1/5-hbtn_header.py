#!/usr/bin/python3
"""
Takes a URL as a command-line argument, sends a request, and displays.
"""

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./5-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)

# Check if 'X-Request-Id' is present in the headers
if 'X-Request-Id' in response.headers:
    x_request_id = response.headers['X-Request-Id']
    print(x_request_id)
