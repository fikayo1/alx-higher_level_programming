#!/usr/bin/python3
if __name__ == "__main__":
    """Import  from the calculator module to basic funcitons"""
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv[1:]
    a = args[0]
    b = args[1]
    c = args[2]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if args[1] == "+":
        print(f"{a} {b} {c} = {add(int(a), int(c))}")
    elif args[1] == "-":
        print(f"{a} {b} {c} = {sub(int(a), int(c))}")
    elif args[1] == "*":
        print(f"{a} {b} {c} = {mul(int(a), int(c))}")
    elif args[1] == "/":
        print(f"{a} {b} {c} = {div(int(a), int(c))}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
