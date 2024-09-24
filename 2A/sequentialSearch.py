def sequentialSearch(arr, x):
    i = 0
    n = len(arr)
    while i < n and arr[i] != x:
        i += 1
    if i < n:
        return i
    return -1

def linearSearch(arr,x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1
    
a = [1,2,3,4,6,0]
print(sequentialSearch(a,1))
print(linearSearch(a,1))