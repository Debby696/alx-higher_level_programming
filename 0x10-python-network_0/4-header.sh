#!/bin/bash
# takes in aURL as an arg,sends GET request to the URL,displays body ofresponse
curl -sH "X-School-User-Id: 98" "$1"
