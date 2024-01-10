#!/usr/bin/python3
"""returns a list of available methods and attributes of an object"""


def lookup(obj):
    """
    returns a list of available attributes and methods of an object

    args:
        obj: python object

    Returns:
        list[]
    """
    return dir(obj)