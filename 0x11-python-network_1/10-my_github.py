#!/usr/bin/python3
"""Script to Get your github ID from the GIbhub api"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    header = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = "https://api.github.com/user"
    resp = requests.get(url, headers=header, auth=auth)
    user = resp.json()
    print(user.get('id'))
