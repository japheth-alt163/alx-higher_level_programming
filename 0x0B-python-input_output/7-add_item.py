#!/usr/bin/python3
"""Appends command line arguments to a list and saves it to a JSON file."""
import sys
from json import load, dump
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Check if the JSON file exists, and load the list or create an empty one
filename = 'add_item.json'
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Append command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
