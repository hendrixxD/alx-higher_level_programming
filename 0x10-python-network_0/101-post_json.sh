#!/bin/bash
# send a POST request to get the body of the response of a JSON file
curl -s -H "Content-Type: application/json" -d $"(cat "$2")" "$1"
