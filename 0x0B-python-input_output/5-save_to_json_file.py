#!/usr/bin/python3
"""objects to file json format"""
import json


def save_to_json_file(my_obj, filename):
    """writing a python object to a json file"""
    with open(filename, "w", encoding="utf-8") as file_:
        json.dump(my_obj, file_)
