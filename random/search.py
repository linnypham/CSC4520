def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

def linearSearch(arr,x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1   

def searchMax(arr):
    maxValue = arr[0]
    for i in range(1,len(arr)):
        maxValue = max(maxValue,arr[i])
    return maxValue

def verifyUnique(arr):
    unique = set()
    for i in arr:
        if i in unique:
            return False
        unique.add(i)
    return True

def linearSearch(arr,x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1