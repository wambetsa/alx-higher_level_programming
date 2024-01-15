#!/usr/bin/python3
"""Function defining a Python class-to-JSON."""


def class_to_json(obj):
    """Returns dictionary represntation of a data structure."""
    return obj.__dict__