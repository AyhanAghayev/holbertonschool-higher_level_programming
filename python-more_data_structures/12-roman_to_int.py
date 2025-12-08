#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_keys = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    sum = 0
    for i in roman_string:
        if sum < roman_keys[i]:
            sum += roman_keys[i]
        else:
            sum = roman_keys[i] - sum
    return sum