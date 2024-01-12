#!/usr/bin/python3
"""Defining a function that saves to JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as fp:
        return fp.dumps(my_obj, fp)