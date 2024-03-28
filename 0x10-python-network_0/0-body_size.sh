#!/bin/bash
# Bash script returns size of body response
curl -s "$1" | wc -c
