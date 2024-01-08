#!/usr/bin/python3
"""
    Add integer module supplies a function, add_integer(),
    that adds 2 nums either (int or float) types
"""

def add_integer(a, b):
    """
        Sums two nums and raises a TypeError for incorrect argument type.
    """
    i = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    if all(i):
        return int(a) + int(b)

    for x, y in list(zip(i, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))