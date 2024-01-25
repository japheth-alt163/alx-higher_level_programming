#!/bin/bash
# send a request to an URL with curl, and displays the size of the body of the response
curl -vs "$1" 2>&1 | wc -c
