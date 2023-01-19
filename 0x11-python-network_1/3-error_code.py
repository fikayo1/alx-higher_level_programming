#!/usr/bin/python3
"""Sends a request to the url and displays the decoded response"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as resp:
            print(resp.read().decode("utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
