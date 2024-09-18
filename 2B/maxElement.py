def max(arr):
    max_var = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max_var:
            max_var = arr[i]
    return max_var

