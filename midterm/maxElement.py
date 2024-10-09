def maxElement(arr):
    max_val = 0
    for number in arr:
        max_val = max(number,max_val)
    return max_val
    
array = [1,2,3,4,5]
print(maxElement(array))