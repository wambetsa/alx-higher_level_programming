#!/bin/bash
# bash script sending request to url and showing response status code
curl -s -w "%{response_code}" -o /dev/null "$1"
