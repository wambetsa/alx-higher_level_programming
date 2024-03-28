#!/usr/bin/python3
"""
    a Python script that takes in a URL, sends a request to the URL
    displays the value of the X-Request-Id variable
    found in the header of the response
"""

if __name__ == '__main__':
    import urllib.request
    import sys
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        x_request_id_header = res.getheader('X-Request-Id')
        print("{}".format(x_request_id_header))

