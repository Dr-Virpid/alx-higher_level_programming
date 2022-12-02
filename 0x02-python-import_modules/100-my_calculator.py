#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    
    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    sign = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    res = 0
    if sign == "+":
        res = add(a, b)
    elif sign == "-":
        res = sub(a, b)
    elif sign == "*":
        res = mul(a, b)
    elif sign == "/":
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, sign, b, res))
