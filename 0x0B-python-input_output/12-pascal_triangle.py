#!/usr/bin/python3


'''
    pascal_triangle - Function
'''


def pascal_triangle(n):
    '''
        Function to return pascal triangle
    '''
    triangle = []
    if n <= 0:
        return triangle
    for index in range(n):
        row = []
        if index == 0:
            row.append(1)
        else:
            for i in range(index + 1):
                if i - 1 < 0:
                    a = 0
                else:
                    a = triangle[index - 1][i - 1]
                if i >= len(triangle[index - 1]):
                    b = 0
                else:
                    b = triangle[index - 1][i]
                row.append(a + b)
        triangle.append(row)
    return triangle
