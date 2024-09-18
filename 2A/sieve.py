def sieve_of_eratosthenes(n):
    A = [True] * (n + 1)# Create a boolean array "A[0..n]" and initialize all entries as True
    A[0] = A[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):# Loop from 2 to √n
        if A[i]:
            for j in range(i * i, n + 1, i):# Mark multiples of i as False, starting from i^2
                A[j] = False
    return [x for x in range(n + 1) if A[x]]# Collect and return all prime numbers
    