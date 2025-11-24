#!/usr/bin/python3
#def islower(c):
#    if c=='':
#        print()
#    if c.islower():
#        return True
#    else:
#        return False

def islower(c):
    # Check that c is a single character string
    if not isinstance(c, str) or len(c) != 1:
        raise TypeError("c must be a single character string")

    # Use Python's built-in islower()
    return c.islower()


islower = __import__('7-islower').islower


