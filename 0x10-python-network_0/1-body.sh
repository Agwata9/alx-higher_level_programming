#!/bin/bash
# Takes in a URL, sends ia GET request to the URL, body of the response
curl -sX GET "$1" -L 200
