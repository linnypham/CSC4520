def partition(arr):
    s = 0
    i = 1
    pivot = arr[s]
    for i in range(len(arr)):
        if arr[i]>arr[s]:
            