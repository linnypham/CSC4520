#Find the number of binary digits in the binary representation of a positive decimal integer
def counting_binary(n): 
    count = 0
    while n > 1:
        count +=1
        n /= 2
    return count
