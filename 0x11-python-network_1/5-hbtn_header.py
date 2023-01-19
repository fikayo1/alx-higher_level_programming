#!/usr/bin/python3
"""Send a request and display the reponse"""
import requests
import sys

if __name__ == "__main__":
    r = request.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
