#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
