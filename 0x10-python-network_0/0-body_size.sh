#!/bin/bash
# takes in a URL,sends a request to it &displays the size of body response
curl -s "$1" | wc -c
