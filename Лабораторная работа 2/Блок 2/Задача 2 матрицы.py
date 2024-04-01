from random import randint
import numpy as np
matrix_1=[]
matrix_1=np.random.randint(0,20,(5,2))
print('Матрица:',matrix_1)
def transpose_matrix(matrix: list[list]) -> list[list]:
    transposed_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix
matrix_t=transpose_matrix(matrix_1)
print('Транспонированная матрица:',matrix_t)
