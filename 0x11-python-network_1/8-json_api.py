#!/usr/bin/python3
"""
    a Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) == 1:
        search_key = ''
    else:
        search_key = sys.argv[1]

    payload = {'q': search_key}
    url = 'http://0.0.0.0:5000/search_user'
    res = requests.post(url, data=payload)

    if isinstance(res.json(), dict):
        print("[{}] {}".format(res.get('id'), res.get('name'))
    else:
        print('No result')
