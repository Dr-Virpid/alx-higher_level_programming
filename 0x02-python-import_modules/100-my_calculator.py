#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit as exi
    from calculator_1 import add, sub, mul, div

    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exi(1)

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
        exi(1)
    print("{} {} {} = {}".format(a, sign, b, res))
