#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
  echo "URL argument is missing"
  exit 1
fi

# Send a request to the URL and store the response
response=$(curl -sI "$1")

# Extract the Content-Length header value from the response headers
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

# Check if Content-Length is found in the response headers
if [ -z "$content_length" ]; then
  echo "Content-Length header not found in the response"
  exit 1
fi

# Print the size of the response body in bytes
echo "$content_length"


