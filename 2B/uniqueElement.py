def unique_element(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                return False
    return True

a = [1,4,5,6,7,8]
print(unique_element(a))