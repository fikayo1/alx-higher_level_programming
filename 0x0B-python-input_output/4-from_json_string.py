#!/usr/bin/python3
"""From json string  to object"""
import json


def from_json_string(my_str):
    """Converts a Json string to a python object (deseralizing)"""
    return json.loads(my_str)
