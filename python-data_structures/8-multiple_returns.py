#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence) if len(sentence) > 0 else None
    return (length, sentence[0])
