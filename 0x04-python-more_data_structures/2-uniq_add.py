#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set()
    sums= 0
    for i in my_list:
        a.add(i)
    for each in a:
        sums+=each
    return sums

