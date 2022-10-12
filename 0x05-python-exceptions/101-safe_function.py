#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except (ValueError, TypeError, IndexError, ZeroDivisionError) as exc:
        stderr.write("Exception: {}".format(exc))
        return None
