def bubbleSort(arr):
    n = len(arr)
    for i in range(n):# Traverse through all array elements
        swapped = False
        for j in range(0, n-i-1):# Last i elements are already in place
            # Traverse the array from 0 to n-i-1
            if arr[j] > arr[j+1]:# Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break