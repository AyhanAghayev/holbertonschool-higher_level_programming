#!/usr/bin/python3
if __name__ == "__main__":

    def square_matrix_simple(matrix=[]):
        newtrix = [3][3]
        for rows in matrix:
            for i in rows:
                newtrix[rows].append(i*i)
        return newtrix
