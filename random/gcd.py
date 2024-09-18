def factor(number):
    prime = [2,3,5,7]
    factor = []
    for i in range(len(prime)):
        while number % prime[i] == 0:
            factor.append(prime[i])
            number /= prime[i]
    if number != 1:
        factor.append(int(number))
    return factor

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

print(gcd(60,24)) 