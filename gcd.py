from factor import factor
def gcd(m,n):
    a = factor(m)
    b = factor(n)
    result = 1
    for i in range(len(a)):
        for j in range(len(b)):
            if b[j] == a[i] and a[i]!=0:
                result *= a[i]
                a[i] = 0
                b[i] = 0
    return result
    