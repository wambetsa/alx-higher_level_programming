#!/usr/bin/python3
"""Defining a load from json file function"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”:
    Arg:
        filename
    Return:
        object
    """
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)