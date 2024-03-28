#!/usr/bin/python3
"""
    a Python script that takes in a URL
    sends a request to the URL and
    displays the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    import sys
    import urllib.request
    from urllib.error import HTTPError

    try:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            result = res.read()
            print("{}".format(result.decode('utf-8')))
    except HTTPError as e:
        if hasattr(e, "code"):
            print("Error code: {}".format(e.code))
