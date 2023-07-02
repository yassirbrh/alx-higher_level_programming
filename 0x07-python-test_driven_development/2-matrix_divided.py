#!/usr/bin/python3

""" matrix_divided - Function
    @matrix: Matrix to divide its elements
    @div: divisor
    Return: New matrix with results
"""


def matrix_divided(matrix, div):

    """
        Creates a matrix with the elements of the prev matrix divided by div.
    """
    msg_err1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg_err2 = "Each row of the matrix must have the same size"
    new_matrix = []
    rows_size = []
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg_err1)
        if len(rows_size) == 0:
            rows_size.append(len(row))
        else:
            rows_size.append(len(row))
            for i in range(1, len(rows_size)):
                if rows_size[i] != rows_size[i - 1]:
                    raise TypeError(msg_err2)
        new_list = []
        for num in row:
            if not isinstance(num, float) and not isinstance(num, int):
                raise TypeError(msg_err1)
            new_list.append(round(num / div, 2))
        new_matrix.append(new_list)
    return new_matrix
