#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_keys = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    sum = 0
    for index, value in enumerate(roman_string):
        if roman_keys[roman_string[index-1]] >= roman_keys[value]:
            sum += roman_keys[value]
        else:
            sum = roman_keys[value] - sum
    return sum