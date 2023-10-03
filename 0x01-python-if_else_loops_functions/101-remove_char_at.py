#!/usr/bin/python3
def remove_char_at(str, n):
    a = 0
    new_str = ""
    for ch in str:
        if a != n:
            new_str += ch
        a += 1
    return new_str
