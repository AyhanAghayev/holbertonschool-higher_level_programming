#!/usr/bin/python3
def square(i):
    return i * i

def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(square, x)), matrix))
