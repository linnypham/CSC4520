from collections import Counter
def sort_count(arr):
    output = []
    dic = Counter(arr)
    unique = set()

    for key in dic.keys():
        if key not in unique:
            unique.add(key)

    for num in unique:
        for i in range(dic[num]):
            output.append(num)
    return output
    

arr = [1,0,2,5,3,7,3,4,0,6]
print(sort_count(arr))