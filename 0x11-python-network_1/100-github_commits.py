#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    header = {
        "Accept": "application/vnd.github+json"
        "X-GitHub-Api-Version": "2022-11-28"
    }
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    param = {"per_page": "10"}
    req = requests.get(url, headers=header, params=param)
    resp = req.json()
    for commit in resp:
        print(f"{commit['sha']}: {commit['commit']['author']['name]}")
