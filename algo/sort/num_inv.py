import os
import sys

def getNimInvArray(lines):
    nInv = 0
    print("len of array %d" % len(lines))
    for i in range(0, len(lines)-1):
        for j in range(i+1,len(lines)):
            if int(lines[i]) > int(lines[j]):
                print(lines[i],lines[j])
                nInv = nInv + 1
    return nInv

def getNumInv(file):
    fd = open(file, 'r')
    nInv = 0
    lines = fd.read().split()
    print("len of array %d" % len(lines))
    for i in range(0, len(lines)-1):
        for j in range(i+1,len(lines)):
            if int(lines[i]) > int(lines[j]):
                nInv = nInv + 1
    return nInv


print(getNumInv("num100k.txt"))
#arr[] = " 9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0".split(",")
#print(getNumInvArray(arr))
