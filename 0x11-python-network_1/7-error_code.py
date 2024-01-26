#!/usr/bin/python3
"""
Takes a URL as a command-line argument, sends a request.
Prints an error message if the HTTP status code is greater.
"""

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./7-error_code.py <URL>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)

# Check if the HTTP status code is greater than or equal to 400
if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response.text)
