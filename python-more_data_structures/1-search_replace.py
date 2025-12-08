#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for index, value in my_list:
        if value == search:
           new_list[index] = replace
        else:
            new_list[index] = value
    return new_list 