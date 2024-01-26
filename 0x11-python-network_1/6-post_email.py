#!/usr/bin/python3
"""
Takes a URL and an email as command-line arguments, sends a POST.
"""

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./6-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email as a parameter
data = {'email': email}

response = requests.post(url, data=data)

print("Your email is:", response.text)
