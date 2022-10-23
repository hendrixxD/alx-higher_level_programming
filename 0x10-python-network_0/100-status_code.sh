#!/bin/bash
# a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -s -0 /dev/null "%{http_code}" "$1"
