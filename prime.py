def sieve_of_eratosthenes(n):
    # Create a boolean array "A[0..n]" and initialize all entries as True
    A = [True] * (n + 1)
    A[0] = A[1] = False  # 0 and 1 are not prime numbers
    
    # Loop from 2 to √n
    for i in range(2, int(n**0.5) + 1):
        if A[i]:
            # Mark multiples of i as False, starting from i^2
            for j in range(i * i, n + 1, i):
                A[j] = False
    
    # Collect and return all prime numbers
    return [x for x in range(n + 1) if A[x]]
    