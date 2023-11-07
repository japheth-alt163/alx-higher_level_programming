#!/usr/bin/python3


def read_file(filename=""):
    """Read a text file (UTF8) and print its contents to stdout.

    Args:
    filename (str): The name of the text file to read.
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")


# Example usage:
if __name__ == "__main__":
    read_file("my_file_0.txt")
