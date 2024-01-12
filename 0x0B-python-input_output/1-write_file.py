#!/usr/bin/python3
"""Defines a file writing function"""


def write_file(filename="", text=""):
    """open file with name filepath and write text into our filename"""
    with open(filename, 'w', encoding='utf-8') as fp:
        return fp.write(text)