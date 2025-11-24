#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i.lower() == i:
            print("{}".format(chr(ord(i)-32)), end="")
print()

uppercase = __import__('8-uppercase').uppercase
