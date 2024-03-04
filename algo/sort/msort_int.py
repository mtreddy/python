"""
 This prog sorts integers uinsg mergesor
"""
import random as rnd
def mSort(inp):
     if len(inp) > 1:
         mid = int(len(inp)/2)
         L = inp[:mid]
         R = inp[mid:]
         mSort(L)
         mSort(R)
         #merge here
         i=j=k=0
         while i<len(L) and j<len(R):
             if L[i] <= R[j]:
                 inp[k] = L[i]
                 i +=1
             else:
                 inp[k] = R[j]
                 j += 1
             k += 1
         while i < len(L):
             inp[k] = L[i]
             i += 1
             k += 1
         while k < len(R):
             inp[k] = R[j]
             j += 1
             k += 1


inp = [rnd.randrange(100, 200) for ind in range(0,10)]
print(inp)
mSort(inp)
print(inp)
