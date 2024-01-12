#!usr/bin/python3
"""Defining a function that returns a json string"""


def to_json_string(my_obj):
    import json
    """a function that returns the JSON 
    representation of an object (string)
    """
    return json.dumps(my_obj)