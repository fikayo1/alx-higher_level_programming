#!/usr/bin/python3
"""2-is same class module"""

def is_same_class(obj, a_class):
    """return true id an object is exactly an instance of a class"""
    return obj.__class__ is a_class
