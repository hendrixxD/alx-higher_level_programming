#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.

    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages
     other than requests and sys
    You don’t need to check arguments
     passed to the script (number or type)

Only 17% of applicants for a backend position at
Holberton finished this task in less than 15 minutes.
"""
import requests
from sys import argv

if __name__ == '__main__':
    """
    argv[1] = repository
    argv[2] = owner
    """
    url = https://developer.github.com/argv[2]/argv[1]/commits/
    req = requests.get(url)
    req = req.json()

    for x in req[:10]
    print(x.get('sha'), end=": ")
    print(x.get('commit').get('author').get('name'))
