#!/usr/bin/python3
"""
    a Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) == 1:
        q = ''
    else:
        q = sys.argv[1]

    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'
    res = requests.post(url, data=payload)

    try:
        json_result = res.json()
        if json_result:
            print("[{}] {}".format(json_result['id'], json_result['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
