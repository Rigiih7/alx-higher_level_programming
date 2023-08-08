#!/usr/bin/python3
# 6-print_comb3.py

for digit0 in range(0, 10):
    for digit1 in range(digit0 + 1, 10):
        if digit0 == 8 and digit1 == 9:
            print("{}{}".format(digit0, digit1))
        else:
            print("{}{}".format(digit0, digit1), end=", ")
