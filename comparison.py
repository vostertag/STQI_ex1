import time
from random import *
import matplotlib.pyplot as plt

def insertionSort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

def bubbleSort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,len(array)):
            if(array[i-1] > array[i]):
                temp = array[i]
                array[i] = array[i-1]
                array[i-1] = temp
                swapped = True
    return array

def merge(array1, array2):
    result = []
    while len(array1) > 0 and len(array2) > 0:
        if array1[0] <= array2[0]:
            result.append(array1[0])
            array1.pop(0)
        else:
            result.append(array2[0])
            array2.pop(0)
            
    while len(array1) > 0:
        result.append(array1[0])
        array1.pop(0)
    while len(array2) > 0:
        result.append(array2[0])
        array2.pop(0)
    return result


def mergeSort(array):
    if len(array) <= 1:
        return array
    left = []
    right = []
    for i in range(len(array)):
        if i < len(array)/2.0:
            left.append(array[i])
        else:
            right.append(array[i])
    return merge(mergeSort(left), mergeSort(right))

def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quickSort(less)+equal+quickSort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
    
# Python program for implementation of Radix Sort
 
# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):
 
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i]/exp1)
        count[ int(index)%10 ] += 1
 
    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1,10):
        count[i] += count[i-1]
 
    # Build the output array
    i = n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[ count[ int(index)%10 ] - 1] = arr[i]
        count[ int(index)%10 ] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def radixSort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
 
    return arr
    
def heapSort( aList ):
  # convert aList to heap
  length = len( aList ) - 1
  leastParent = length / 2
  for i in range ( int(leastParent), -1, -1 ):
    moveDown( aList, i, length )
 
  # flatten heap into sorted array
  for i in range ( length, 0, -1 ):
    if aList[0] > aList[i]:
      swap( aList, 0, i )
      moveDown( aList, 0, i - 1 )
  return aList

 
def moveDown( aList, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
      largest += 1
 
    # right child is larger than parent
    if aList[largest] > aList[first]:
      swap( aList, largest, first )
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
    else:
      return # force exit
 
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp
#
#array = [8,9,6,4,12]
#print(heapSort(array))

methods = [insertionSort, heapSort]
results = []
xAxis = []
start = 0
end = 50

for i in range(start, end):
    xAxis.append(i)
    for j in range(len(methods)):
        array = []
        results.append([])
        for k in range(i):
            array.append(randint(0, 100))
        start = time.clock()
        methods[j](array)
        end = time.clock()
        results[j].append(end-start);

for i in range(len(methods)):
    plt.plot(xAxis, results[i],label='Line ' + str(i))
plt.legend(["Insertion Sort", "Heap Sort", "Radix Sort"])
plt.xlabel('Number of elements in array')
plt.ylabel('Time in seconds')
plt.show()

##print(results)
#sum = 0
#
#for i in range(len(results)):
#    sum += results[i]
#
#print(sum/len(results))
