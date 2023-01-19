#!/usr/bin/python3
"""Get the request ID from the header of a response"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
