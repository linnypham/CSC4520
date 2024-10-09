def johnson(n):
    digits = []
    for i in range(1,n):
        digits.append(i)
    while digits[-1]<digits[-2]:
        k = digits.index(max(digits))
        if digits[k] < w:
            digits[k],digits[k+1] = digits[k+1],digits[k]
        elif digits[k] >
