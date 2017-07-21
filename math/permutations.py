import os
import sys
import numpy as np

done = 0
small = 0
def find_rs_small(arr, fval, ind2, size):
    not_too_small = ind2
    for i in range(ind2, size+1):
        if arr[i] > fval and  arr[not_too_small] > arr[i] :
            not_too_small = i;
    return not_too_small

def next_permut(arr):
    # zero based array
    size = len(arr) - 1
    rs_val = 0
    tarr = []
    arr.sort()
    finished = False
    while finished != True:
        print( ''.join(str(x) for x in arr))
        for ind in range(size-1,-2,-1):
            if arr[ind] < arr[ind+1]:
                break
        if ind < 0 :
            finished = True
        else:
            rs_val = find_rs_small(arr, arr[ind], ind+1, size)
            #swap
            arr[ind], arr[rs_val] = arr[rs_val], arr[ind]
            # sort rest of the string after ind
            tarr = arr[ind+1:size+1]
            tarr.sort()
            arr[ind+1:size+1] = tarr






arr = np.array([4,5,6,7])
next_permut(arr)

