#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Use tuple slicing to get the first two elements of each tuple or 0 if they don't exist
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    # Calculate the sum of corresponding elements and return a new tuple
    result_tuple = (a1 + b1, a2 + b2)
    return result_tuple


# Test cases
if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)  # Output: (89, 100)
    print(add_tuple(tuple_a, (1, )))  # Output: (2, 89)
    print(add_tuple(tuple_a, ()))  # Output: (1, 89)
