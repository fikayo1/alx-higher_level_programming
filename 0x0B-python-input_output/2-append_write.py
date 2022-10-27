#!/usr/bin/python3
"""Appending file module"""


def append_write(filename="", text=""):
    """appendsd a string to the end of a text file"""
    with open(filename, "a", encoding="utf-8") as file_:
        return file_.write(text)
