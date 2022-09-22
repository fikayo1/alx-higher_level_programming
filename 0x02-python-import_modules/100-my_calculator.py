#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
args = sys.argv[1:]
if len(args) != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if args[1] == "+":
    print(f"{args[0]} {args[1]} {args[2]} = {add(int(args[0]), int(args[2]))}")
elif args[1] == "-":
    print(f"{args[0]} {args[1]} {args[2]} = {sub(int(args[0]), int(args[2]))}")
elif args[1] == "*":
    print(f"{args[0]} {args[1]} {args[2]} = {mul(int(args[0]), int(args[2]))}")
elif args[1] == "/":
    print(f"{args[0]} {args[1]} {args[2]} = {div(int(args[0]), int(args[2]))}")
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
