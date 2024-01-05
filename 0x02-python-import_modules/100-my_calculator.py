#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sign = sys.argv[2]
    if sign == "+":
        print("{} {} {} = {}".format(a, sign, b, add(a, b)))
    elif sign == "-":
        print("{} {} {} = {}".format(a, sign, b, sub(a, b)))
    elif sign == "*":
        print("{} {} {} = {}".format(a, sign, b, mul(a, b)))
    elif sign == "/":
        print("{} {} {} = {}".format(a, sign, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
