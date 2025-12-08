#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for index, value in enumerate(my_list):
        if len(new_list) != 0 and new_list[index] != value:
            new_list.append(value)
    for i in new_list:
        sum += i
    return sum