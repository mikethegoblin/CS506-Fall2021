import numpy as np

def get_determinant(matrix):
    # assuming matrix is a numpy array
    row, col = matrix.shape[0], matrix.shape[1]
    # if the input matrix is not a square matrix, return -1
    if row != col:
        return -1
    # recursion base case
    if row == 2:
        a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
        return (a*d) - (b*c)
    else:
        sign = 1
        result = 0
        for i, num in enumerate(matrix[0]):
            new_matrix = np.hstack((matrix[1:, :i], matrix[1:, i+1:]))
            if sign > 0:
                result += num * get_determinant(new_matrix)
            else:
                result -= num * get_determinant(new_matrix)
            sign = -sign
        return result



