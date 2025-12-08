#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dicti = a_dictionary.copy()
    for i in dicti.keys():
        dicti.update({i: dicti[i] * 2})
    return dicti
