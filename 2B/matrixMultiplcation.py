def matrixMultiplication(matrix_a, matrix_b):
    n = len(matrix_a)
    if n != len(matrix_b):
        return 'The sizes of 2 matrix are not the same.'
    matrix_c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_c[i][j] += matrix_a[i][k]*matrix_b[k][j]
    return matrix_c

A = [[0,1],[2,3]]
B = [[4,5],[7,8]]
print(matrixMultiplication(A,B))