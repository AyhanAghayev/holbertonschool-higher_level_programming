#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    za = a_dictionary.get(key, None)
    a_dictionary.update({key: value})

