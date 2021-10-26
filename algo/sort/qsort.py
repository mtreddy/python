import os
import sys


## partitioning

def partition(A, l, h):
    ## last element as pivot
    pivot=A[h]
    ## lists indexed starting 0
    low = l-1
    for ind in range(l, h+1):
        print("ind:", ind)
        if A[ind] < pivot:
            low = low + 1;
            A[ind], A[low]= A[low], A[ind]
            print("----pivot  ----", pivot)
            for i in range(l,h+1):
                print(A[i])
    ## move thepivot to it's meaningful place
    A[low+1], A[h] = A[h], A[low+1]
    return low+1
## quick sort

def quicksort(A, l, h):
    if(l < h):
        pivot = partition(A, l, h)
        print("l,Pivot,h", l,pivot,h)
        for i in range(l,h+1):
            print(A[i])
        quicksort(A, l, pivot-1)
        quicksort(A, pivot+1, h )

A = [183,153,104,109,161,168,70,163,38,67,89,162,65,20,140,138,178,145,153,42,61,74,75,141,161,175,150,55,118,195,81,69,47,177,153,35,158,29,82,126,38,96,121,1,176,192,65,93,94,79,165,193,133,70,89,45,109,79,146,85,111,62,9,122]

num = len(A) - 1
for i in range(0,num):
    print(A[i])

quicksort(A,0,num-1)
print("---- sorted ----")

for i in range(0,num):
    print(A[i])
