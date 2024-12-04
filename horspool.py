def shift(pattern):
    n = len(pattern)
    unique = set()
    dic = {}
    for i in range(n-2,-1,-1):
        if pattern[i] not in unique:
            dic[pattern[i]] = n-1-i
            unique.add(pattern[i])
    dic['**'] = n
    return dic

pattern = 'TCCTATTCTTT'
print(shift(pattern))