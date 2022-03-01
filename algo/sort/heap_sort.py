import os
import sys

arr=[6, 126, 193, 125, 90, 134, 67, 7, 105, 145, 178, 167, 118, 4, 96, 116, 200, 70, 126, 118, 167, 43, 30, 109]
arr = [12, 11, 13, 5, 6, 7]
def left(i):
        return (2*i+1)
def right(i):
        return (2*i+2)

def heapify(arr, ln, i):
    l = left(i)
    r = right(i)
    large = i

    if l < ln and arr[large] < arr[l]:
        large = l
    if r < ln and arr[large] < arr[r]:
        large = r

    if large != i:
        tmp = arr[i]
        arr[i] = arr[large]
        arr[large] = tmp
        heapify(arr, ln, large)

def build_heap(arr):
        #buidling heap
        for i in range(int(len(arr)/2), 0, -1):
            heapify(arr, i, 0)

def heap_sort(arr):
        build_heap(arr)

        for i in range(len(arr)-1, 0, -1):
            print(i)
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr,i, 0)

print(arr)
heap_sort(arr)
print(arr)
