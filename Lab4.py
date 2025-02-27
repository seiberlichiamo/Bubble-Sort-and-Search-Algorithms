from math import floor
#Lab 4 Code
# @author - Hayden Seiberlich
# @version 10/17/24

#Method to find the max value of an array.
def max(arr):
    maxValue = arr[0]
    for element in arr:
        if maxValue < element:
            maxValue = element
    return maxValue


#Method to use linear search in an array.
def linearSearch(arr, x):
    i = 0
    while i < len(arr) and arr[i] != x:
        print(i," is the index and ",arr[i]," is the value")
        i += 1

    if i < len(arr):
        location = i + 1
    else:
        location = 0

    return location

#Method to use binary search for an array.
def binarySearch(arr, x):
    i = 0
    j = len(arr)
    print("%7s%7s%7s%10s%10s" % ("i", "j", "m", "arr(i)", "arr(m)"))
    while i < j:
        m = floor((i+j)/2)
        print("%7s%7s%7s%10s%10s" % (i, j, m, arr[i], arr[m]))
        if x > arr[m]:
            i = m + 1
        else:
            j = m
    if x == arr[i]:
        location = i
    else:
        location = 0
    return location

#Bubble sort algorithm method.
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr



a = [3,4,5,1,6,8,7,9,2]
print("The maximum number in the array is ", max(a))
print(" ")
print("The location of the searched item with linear is ", linearSearch(a, 6))
print(" ")
print("The location of the searched item is ", binarySearch(a, 5))
print(" ")

a = [3, 4, 5, 1, 6, 8, 7, 9, 2]
print("original array is ", a)
print(" ")
print("sorted array using bubble sort is ", bubbleSort(a))

