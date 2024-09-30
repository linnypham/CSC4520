def subset(arr):
    ans = set()
    for i in arr:
        if i not in ans:
            ans.add(i)
        for j in ans:
            sub = i+j
            ans.add(sub)
    return ans

arr = ['a','b','c']
print(subset(arr))