import time
from sortLib import *
import matplotlib.pyplot as plt

def algoTime(func,arr):
    start_time = time.time()

    func(arr)

    end_time = time.time()

    elapsed_time = end_time - start_time

    return elapsed_time
    
def timeArray(arr100,arr200,arr300,arr400,arr500,arr1000):
    timeBubble.append(algoTime(bubble_sort, arr100.copy()))
    timeBubble.append(algoTime(bubble_sort, arr200.copy()))
    timeBubble.append(algoTime(bubble_sort, arr300.copy()))
    timeBubble.append(algoTime(bubble_sort, arr400.copy()))
    timeBubble.append(algoTime(bubble_sort, arr500.copy()))
    timeBubble.append(algoTime(bubble_sort, arr1000.copy()))
    
    timeSelection.append(algoTime(selection_sort, arr100.copy()))
    timeSelection.append(algoTime(selection_sort, arr200.copy()))
    timeSelection.append(algoTime(selection_sort, arr300.copy()))
    timeSelection.append(algoTime(selection_sort, arr400.copy()))
    timeSelection.append(algoTime(selection_sort, arr500.copy()))
    timeSelection.append(algoTime(selection_sort, arr1000.copy()))
    
    timeInsertion.append(algoTime(insertion_sort, arr100.copy()))
    timeInsertion.append(algoTime(insertion_sort, arr200.copy()))
    timeInsertion.append(algoTime(insertion_sort, arr300.copy()))
    timeInsertion.append(algoTime(insertion_sort, arr400.copy()))
    timeInsertion.append(algoTime(insertion_sort, arr500.copy()))
    timeInsertion.append(algoTime(insertion_sort, arr1000.copy()))
    
def sortedArr(n):
    arr = []
    for i in range(n):
        arr.append(i)
    return arr

arr100 = sortedArr(100)
arr200 = sortedArr(200)
arr300 = sortedArr(300)
arr400 = sortedArr(400)
arr500 = sortedArr(500)
arr1000 = sortedArr(1000)

timeBubble = []
timeSelection = []
timeInsertion = []

timeArray(arr100,arr200,arr300,arr400,arr500,arr1000)

x = [len(arr100),len(arr200),len(arr300),len(arr400),len(arr500),len(arr1000)]
y1 = timeBubble
y2 = timeSelection
y3 = timeInsertion

plt.plot(x,y1,label = 'Bubble Sort',marker='o')
plt.plot(x,y2,label = 'Selection Sort',marker='o')
plt.plot(x,y3,label = 'Insertion Sort',marker='o')
plt.xlabel('Input Size')
plt.ylabel('Time Travel(s)')
plt.title('Order of Growth - Sorted Data')
plt.legend()
plt.show()
