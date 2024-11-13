import time
from random import randint
from sortLib import *

import matplotlib.pyplot as plt

def unsortedArray(n):
    arr = []
    for i in range(n):
        arr.append(randint(0,n))
    return arr

def algoTime(func,arr):
    start_time = time.time()

    func(arr)

    end_time = time.time()

    return end_time - start_time

    
    
def timeArray(arr100,arr200,arr300,arr400,arr500,arr1000):
    arr = [arr100,arr200,arr300,arr400,arr500,arr1000]
    for i in range(6):
        timeBubble.append(algoTime(bubble_sort, arr[i].copy()))
        timeSelection.append(algoTime(selection_sort, arr[i].copy()))
        timeInsertion.append(algoTime(insertion_sort, arr[i].copy()))
        
    
arr100 = unsortedArray(100)
arr200 = unsortedArray(200)
arr300 = unsortedArray(300)
arr400 = unsortedArray(400)
arr500 = unsortedArray(500)
arr1000 = unsortedArray(1000)
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
plt.title('Order of Growth - Random Data')
plt.legend()
plt.show()