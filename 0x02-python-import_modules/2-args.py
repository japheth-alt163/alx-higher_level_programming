#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    num_args = len(sys.argv) - 1

    if num_args == 0:
        print(f'0 arguments.')
    else:
        print(f'{num_args} {"argument" if num_args == 1 else "arguments"}:')

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f'{i}: {arg}')
