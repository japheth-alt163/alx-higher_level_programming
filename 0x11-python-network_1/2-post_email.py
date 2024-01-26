#!/usr/bin/python3
"""
Takes a URL and an email as command-line arguments, sends.
a POST request, and displays the body of the response.
"""

import urllib.parse
import urllib.request
import sys


def post_email(url, email):
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print("Your email is:", body)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    post_email(url, email)
