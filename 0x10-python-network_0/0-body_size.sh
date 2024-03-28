#!/bin/bash
# Bash script that takes in URL, sends request to that URL
# and displays the size of the body of the response
# curl -s "$1" | wc -c
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'

