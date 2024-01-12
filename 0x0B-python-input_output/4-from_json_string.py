#!/usr/bin/python3
"""Defining a fro json string function"""
import json


def from_json_string(my_str):
    """" a function that returns an object represented by a JSON string
    Arg:
        my_str
    Return:
        object
    """
    return json.loads(my_str)