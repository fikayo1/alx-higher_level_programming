#!/usr/bin/python3
"""Gets the request ID from the header of a response"""
from urllib.request import urlopen, Request
import sys

if __name__ == "__main__":
    req = Request(sys.argv[1])
    with urlopen(req) as resp:
        print(resp.getheader('X-Request-Id'))
