#!/usr/bin/python3
"""1-my_list"""


class MyList(list):
    """Inherits from class list"""

    def print_sorted(self):
        """prints the sorted list"""
        list.sort()
        print(list)
