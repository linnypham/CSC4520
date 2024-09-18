def selectionSort(arr): #time:(n(n-1))/2
    for i in range(len(arr)-1): # Traverse through all array elements
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]# Swap the found minimum element with the first element  