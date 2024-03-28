#!/bin/bash
# bash script taking url and shows http methods accepted by server
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
