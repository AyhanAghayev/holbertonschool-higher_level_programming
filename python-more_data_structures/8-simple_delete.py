#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    value = a_dictionary.get(key, None)
    if value != None:
        a_dictionary.pop(key)
    return a_dictionary
