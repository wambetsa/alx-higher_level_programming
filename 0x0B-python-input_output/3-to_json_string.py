#!usr/bin/python3
"""
    Defining a function that returns a json string
"""
import json


def to_json_string(my_obj):
    """a function that returns the JSON representation of object
    Arg:
        my_obj
    return:
        string
    """
    return json.dumps(my_obj)