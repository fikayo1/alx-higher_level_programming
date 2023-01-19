#!/usr/bin/python3
""" Sends a post request with email as parameter and display the response"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys

if __name__ == "__main__":
    data = urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = Request(sys.argv[1], data)
    with urlopen(req) as resp:
        print((resp.read()).decode("utf-8"))
