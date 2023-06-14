#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for arr in matrix:
        new_matrix.append(list(map(lambda number: number ** 2, arr)))
    return new_matrix
