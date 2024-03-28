#!/bin/bash
# Bash script that takes in URL, sends request to that URL
# and displays the size of the body of the response
curl -sI "$1" | grep -oiE 'Content-Length: [0-9]+' | cut -d ' ' -f2

