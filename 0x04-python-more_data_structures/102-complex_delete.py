#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]

    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary


# Testing the function with the provided example
if __name__ == '__main__':
    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}

    print_sorted_dictionary(a_dictionary)
    print("--")
    new_dict = complex_delete(a_dictionary, 'C')
    print_sorted_dictionary(new_dict)
    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(new_dict)
