#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    intargs = []
    total = 0
    for arg in args:
        intargs.append(int(arg))
    for num in intargs:
        total += num
    print(total)
