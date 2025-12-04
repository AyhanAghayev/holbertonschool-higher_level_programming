#!/usr/bin/python3
def no_c(mystr):
    newstr = ""
    for char in mystr:
        if char != 'c' and char != 'C':
            newstr += char
    return newstr
