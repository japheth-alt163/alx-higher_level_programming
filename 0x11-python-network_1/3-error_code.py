#!/usr/bin/python3
"""
Takes a URL as a command-line argument, sends a request.
Handles urllib.error.HTTPError exceptions and prints the HTTP.
"""

import urllib.request
import urllib.error
import sys

if len(sys.argv) != 2:
    print("Usage: ./3-error_code.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
