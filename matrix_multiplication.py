def matrix_multiplication(arr1,arr2):
    row1 = len(arr1)
    row2 = len(arr2)
    col1 = len(arr1)
    col2 = len(arr2)
    if col1 !=  row2:
        return False
    grid = []
    for i in range(row2):
        row = []
        for j in range(col1):
            row.append(arr1[i][j]*arr2[i][i])
        grid.append(row)
    return grid

arr1 = [[2,1],[3,4]]
arr2 = [[4,5],[6,7]]
print(matrix_multiplication(arr1,arr2))