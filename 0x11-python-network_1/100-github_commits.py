#!/usr/bin/python3
"""
    a Python script that takes 2 arguments in order to solve this challenge
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    name = argv[2]
    repo = argv[1]
    params = {'per_page': 10}
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(name, repo), params=params)
    r = r.json()
    for arg in r:
        print("{}: {}".format(arg.get('sha'),
                              arg.get('commit').get('author').get('name')))
