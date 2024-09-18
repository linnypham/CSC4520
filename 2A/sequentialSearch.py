def sequentialSearch(arr, x):
    i = 0
    n = len(arr)
    while i < n and arr[i] != x:
        i += 1
    if i < n:
        return i
    return -1