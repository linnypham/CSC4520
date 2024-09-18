def gcd(m,n):
    while n==0:
        return m
    r = m % n
    return gcd(n,r)

print(gcd(24,60))