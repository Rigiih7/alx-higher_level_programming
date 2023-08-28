#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):

    items = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            items += 1
        except IndexError:
            break
    print("")
    return items

