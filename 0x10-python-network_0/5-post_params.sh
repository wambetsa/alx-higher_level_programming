#!/bin/bash
# bash script taking url sends post request and shows body response
curl -sX POST "$1"?email=test@gmail.com&subject=I will always be here for PLD
