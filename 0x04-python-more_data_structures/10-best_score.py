#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    a = max(a_dictionary.values())
    for i in a_dictionary:
        if a_dictionary[i] == a:
            return a_dictionary[i]
