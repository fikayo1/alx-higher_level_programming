#!/usr/bin/python3
"""1-my_list"""


class MyList(list):
    """Inherits from class list"""
    def __init__(self):
        """To initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
