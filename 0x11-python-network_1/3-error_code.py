#!/usr/bin/python3
"""
a python script that takes in a URL, sends a request to he URL and
displays the body of the response
"""
import urllib.request
from urllib.error import URLError, HTTPError
from sys import argv

if __name__ == "__main__":
    res = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(res) as response:
            print(response.read().decode(encoding="utf-8"))
    except HTTPError as err:
        print("Error code: {}". format(err.code))
