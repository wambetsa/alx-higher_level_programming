#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8) and 
returns the number of characters written
"""


def write_file(filename="", text=""):
    """open file with name filepath and write text into our filename"""
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(text)