#!/usr/bin/python3
def raise_exception():
    raise TypeError


# Test the function with the provided example
if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
