#!/bin/bash
# sends a JSON POST request to a URL as 1st args& displays body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
