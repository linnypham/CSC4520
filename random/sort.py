def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
            print(arr)
        arr[j + 1] = key
        print(arr) 

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):# Traverse through all array elements
        swapped = False
        for j in range(0, n-i-1):# Last i elements are already in place
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

def quickSort(array, low, high):
    def partition(array, low, high):

        # choose the rightmost element as pivot
        pivot = array[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])

        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # Return the position from where partition is done
        return i + 1
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

def selectionSort(arr): #time:(n(n-1))/2
    for i in range(len(arr)-1): # Traverse through all array elements
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]# Swap the found minimum element with the first element  


arr = [A, L, G, O ,R, I, T, H, M, S]
insertionSort(arr)