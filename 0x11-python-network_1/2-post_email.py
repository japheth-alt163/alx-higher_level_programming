#!/usr/bin/python3
"""
Takes a URL and an email as command-line arguments,
"""

import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Encode the email as a parameter
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    body = response.read().decode('utf-8')
    print("Your email is:", body)
