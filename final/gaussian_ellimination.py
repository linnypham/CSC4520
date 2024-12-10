def gaussian_elimination(matrix):
    n = len(matrix)  # Number of rows
    m = len(matrix[0])  # Number of columns, assuming augmented matrix
    
    # Forward elimination
    for i in range(n):
        # Pivoting
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        
        # Eliminate entries below pivot
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, m):
                matrix[j][k] -= factor * matrix[i][k]
    
    # Back substitution
    x = [0] * (m - 1)  # Solution vector
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][-1] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            matrix[j][-1] -= matrix[j][i] * x[i]
    
    return x
