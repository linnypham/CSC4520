def power(x,n):
    if n == 0:
        return 1
    return x*power(x,n-1)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def function(n):
    if n == 0:
        return 1
    return function(n/3) + 1