#!/usr/bin/python3
"""
    a Python script that takes in a URL and an email address,
    sends a POST request to the passed URL with the email as a param,
    and finally displays the body of the response.
"""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    res = requests.post(url, data=value)
    print("{}".format(res.text))
