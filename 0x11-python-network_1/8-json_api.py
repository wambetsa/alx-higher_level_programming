#!/usr/bin/python3
"""
    a Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == '__main__':
    import sys
    import requests

    if sys.argv <= 1:
        q = ''
    else:
        q = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user?{q}'
    res = requests.post(url)
    if isinstance(res.json(), json):
        print("[{}] {}".format(res.json().id, res.json().name))
