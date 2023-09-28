#!/bin/bash
#sends a request to a URL passed as an arg,displays only status code of respons
curl -s -o /dev/null -w "%{http_code}" "$1"
