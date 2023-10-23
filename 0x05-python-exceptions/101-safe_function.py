#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None


# Define the my_div function and the print_list function from your example
def my_div(a, b):
    return a / b


def print_list(my_list, length):
    i = 0
    while i < length:
        print(my_list[i])
        i += 1
    return length


# Test the safe_function with the provided example
if __name__ == "__main__":
    result = safe_function(my_div, 10, 2)
    print("result of my_div: {}".format(result))

    result = safe_function(my_div, 10, 0)
    print("result of my_div: {}".format(result))

    result = safe_function(print_list, [1, 2, 3, 4], 10)
    print("result of print_list: {}".format(result))
