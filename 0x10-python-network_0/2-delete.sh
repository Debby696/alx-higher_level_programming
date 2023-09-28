#!/bin/bash
# sends a DELETE request to URL passed as 1st args&displays body of response
curl -sX DELETE "$1"
