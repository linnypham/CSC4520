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

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)