#!/bin/bash
# send a POST request to get the body of the response of a JSON file
curl -sX POST "$1" -H "Content-Type: application/json" -d @$2
