#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and
displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    status_code = reponse.stattus_code
    if status_code >= 400:
        print("Error code: {}".format(code))
    else:
        print(response.text)
