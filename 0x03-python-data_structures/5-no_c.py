#!/usr/bin/python3
def no_c(my_string):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through the characters in the input string
    for char in my_string:
        # Check if the character is not 'c' or 'C', then add it to the result
        if char != 'c' and char != 'C':
            result += char

    return result


# Example usage
if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
