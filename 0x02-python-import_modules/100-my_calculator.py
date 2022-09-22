#!/usr/bin/python3
if __name__ == "__main__":
    """Importfrom the calculator module to handlebasic operation"""
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv[1:]
    a = args[0]
    b = args[1]
    c = args[2]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if b == "+":
        print(f"{a} {b} {c} = {add(int(a), int(c))}")
    elif b == "-":
        print(f"{a} {b} {c} = {sub(int(a), int(c))}")
    elif b == "*":
        print(f"{a} {b} {c} = {mul(int(a), int(c))}")
    elif b == "/":
        print(f"{a} {b} {c} = {div(int(a), int(c))}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
