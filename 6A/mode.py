def mode(arr):
    from collections import Counter
    counter_arr = Counter(arr)
    return counter_arr.most_common(1)[0][1]

arr = [1,5,5,5,6,7,7]
print(mode(arr))