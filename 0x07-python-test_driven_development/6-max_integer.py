#!/usr/bin/python3
"""
    Determine max integer in list
"""


def max_integer(list=[]):
    """
        Finds and returns max int in int list
        Returns none for empty list
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result