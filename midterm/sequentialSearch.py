def sequentialSearch(arr,target):
    for num in arr:
        if num == target:
            return arr.index(num)
        
array = [1,2,3,4,5,6]
target = 5
print(sequentialSearch(array,target))