def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j+1]<arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
array = [4,6,9,1,0,2]
bubbleSort(array)
print(array)