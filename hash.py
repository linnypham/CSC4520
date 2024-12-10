def openHashing(arr,nb):
    open_arr = {i:[] for i in range(nb)}
    for num in arr:
        loc = num%nb
        open_arr[loc].append(num)
    return open_arr
def closeHashing(arr,nb):
    close_arr = [None]*nb
    for num in arr:
        loc = num%nb
        while 
            if close_arr[i] == None:
                close_arr[i] = num
                break
    return close_arr


input = [63, 42, 45, 64, 53, 41]
print(closeHashing(input,11))
            
        
