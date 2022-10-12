#!/usr/bin/python3
def safe_print_division(a, b):
    ret = None
    try:
        div = a / b
        ret = div
        return ret
    except (TypeError, ValueError):
        return ret
    finally:
        print("Inside result: {}".format(ret))
