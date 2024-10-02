def median(arr):
    arr.sort()
    n = len(arr)
    left, right = 0, n-1
    while left<right:
        left+=1
        right-=1
    if left == right:
        return arr[left]
    else:
        return (arr[left]+arr[right])/2
    
arr= [5,7,2,9,1,10]
print(sorted(arr))
print(median(arr))