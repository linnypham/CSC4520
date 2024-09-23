def problem_4(A):
    min_val = A[0]
    max_val = A[0]
    for i in range(1,len(A)):
        if A[i]<min_val:
            min_val = A[i]
        if A[i]>max_val:
            max_val = A[i]
    return (max_val - min_val)
def problem_5(n):
    if n == 1:
        return n
    return problem_5(n-1)+n**3

n = 5
print(problem_5(n))