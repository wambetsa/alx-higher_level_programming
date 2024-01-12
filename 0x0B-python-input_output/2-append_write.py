#!/usr/bin/python3
"""Defining a function that append to a file"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8) 
    and returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as fp:
        return fp.write(text)