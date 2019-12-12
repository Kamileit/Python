from suma_macierzy import *
from iloczyn import scalar_sum
import numpy as np

macierz1 = generate_random_matrix(8, 8)
macierz2 = generate_random_matrix(8, 8)


def get_matrix_row(matrix, row_idx):
    return matrix[row_idx]


def get_matrix_column(matrix, row_idx):
    return [row[row_idx] for row in matrix]


def multiply_matrixes(macierz1, macierz2):
    result = []
    for i in range(len(macierz1[0])):
        temp = []
        row = get_matrix_row(macierz1, i)
        for j in range(len(macierz2[0])):
            column = get_matrix_column(macierz2, j)
            temp.append(scalar_sum(row, column))
        result.append(temp)
    return result

# multiply_matrixes()
#
# for element in macierz1:
#     print(element)
# print("")
# for element in macierz2:
#     print(element)
# print("")
# for element in result:
#     print(element)

# matrix1 = [[5, 1, 3], [1, 1, 1], [1, 2, 1]]
# matrix2 = [[1], [2], [3]]
# result = multiply_matrixes(matrix1, matrix2)
# sum_numpy = np.array(matrix1).dot(np.array(matrix2))
# print(sum_numpy)