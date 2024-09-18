def string_matching(text,pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n-m+1):
        j = 0
        while j<m and pattern[j] == text[i+j]:
            j+=1
        if j == m:
            return i
    return -1

P = [7,8,9]
T = [1,2,3,4,5,6,7,8,9]

print(string_matching(T,P))