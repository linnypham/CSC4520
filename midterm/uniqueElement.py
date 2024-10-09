def uniqueElement(arr):
    unique = set()
    for num in arr:
        if num in unique:
            return False
        unique.add(num)
    return True

array = [1,2,3,4,5]
print(uniqueElement(array))