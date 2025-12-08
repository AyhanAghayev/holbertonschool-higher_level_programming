#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newtrix = [3][3]
    for rows in matrix:
        for i in rows:
            print(i, rows)
            newtrix[rows].append(i*i)
    return newtrix
