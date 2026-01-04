#!/usr/bin/python3
"""suckerton"""


def write_file(filename="", text=""):
    """dumb"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
