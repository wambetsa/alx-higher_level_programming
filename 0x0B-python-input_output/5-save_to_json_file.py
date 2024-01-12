#!/usr/bin/python3
"""Defining a function that saves to JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file, using a JSON representation
    Arg:
        my_obj, filename
    Return:
        object write
    """
    with open(filename, 'a', encoding='utf-8') as fp:
        return json.dump(my_obj, fp)