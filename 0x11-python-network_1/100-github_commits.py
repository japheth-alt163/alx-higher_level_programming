#!/usr/bin/python3
"""
Lists 10 most recent commits from a GitHub repository.
"""

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./100-github_commits.py <repository> <owner>")
    sys.exit(1)

repository = sys.argv[1]
owner = sys.argv[2]

url = f'https://api.github.com/repos/{owner}/{repository}/commits'
params = {'per_page': 10}

response = requests.get(url, params=params)

try:
    commits = response.json()
    for commit in commits:
        sha = commit.get('sha', '')
        author_name = commit['commit']['author'].get('name', '')
        print(f"{sha}: {author_name}")
except ValueError:
    print("Error: Not a valid JSON")
