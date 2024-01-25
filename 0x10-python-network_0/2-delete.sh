#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and displays the body of the response

response=$(curl -sw "%{http_code}\n" -sX DELETE "$1")
status_code=$(echo "$response" | tail -n 1)
response_body=$(echo "$response" | sed '$d')

echo "HTTP Status Code: $status_code"
echo "Response body:"
echo "$response_body"
