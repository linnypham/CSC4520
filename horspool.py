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
def horspool(pattern,text):
    table = shift(pattern)
    n = len(text)-1
    m = len(pattern)
    p_pattern = len(pattern)-1
    while pointer <= n:
        for i in range(m-1,-1,-1):
            if 
pattern = 'TCCTATTCTTT'
print(shift(pattern))