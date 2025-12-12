#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squared_matrix = []
    for rows in matrix:
        row = []
        for i in rows:
            row.append(i)
        squared_matrix.append(row)
    return squared_matrix
