#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for i in my_list[:x]:
            num += 1
            print(i, end="")
            return num
    except:
        print("An error occured")
