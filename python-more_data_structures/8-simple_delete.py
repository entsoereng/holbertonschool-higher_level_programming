#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Use pop method to remove the key if it exists, otherwise do nothing
    a_dictionary.pop(key, None)
    return a_dictionary
