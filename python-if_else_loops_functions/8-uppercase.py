#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print"{}".format(chr(ord(str)+32)), end="")

uppercase = __import__('8-uppercase').uppercase
