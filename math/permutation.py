import os
import sys

def permut(lst):
     if len(lst) == 0:
         return[]
     if len(lst) == 1:
         return [lst]
     l = []
     for ind in range(len(lst)):
         m = lst[ind]
         rlst = lst[:ind] + lst[ind+1:]
         for p in permut(rlst):
             l.append([m]+p)
     return l


data  = [1,2,3,4]

for p in permut(data):
   print(p)
