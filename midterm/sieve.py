import math

def sieve(n):
    if n <= 1:
        return []
    
    # Initialize a boolean list for primality check
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            # Mark all multiples of p as not prime
            for j in range(p * p, n + 1, p):
                is_prime[j] = False
    
    # Collect all prime numbers
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    
    return primes

print(sieve(10))
