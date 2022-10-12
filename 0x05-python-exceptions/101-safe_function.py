#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except Exception as exc:
        stderr.write("Exception: {}".format(exc))
        return None
