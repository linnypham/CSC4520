def partition(A):
    l,r = 0, len(A)-1
    p = l
    i = p
    j = r+1
    while i<j:
        while A[i]<p:
            i+=1
        while A[j]>p:
            j-=1
        A[i],A[j] = A[j],A[i]
    A[i],A[j] = A[j],A[i]
    A[l],A[j] = A[j],A[l]
    return j

arr = [9,8,6,5,3]
print(partition(arr))
