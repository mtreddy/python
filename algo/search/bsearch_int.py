"""
  Searches for a int valfue. 
  inp is array

"""
import random as rnd
def bsearch(inp, val, st, end):
    
    if st < end:
        mid = int((st+end)/2)
        if inp[mid] == val:
            return mid
        elif inp[mid] > val:
            return bsearch(inp, val, st, mid)
        else:
            return bsearch(inp, val, mid+1, end)
    return -1




#if '__name__' == '__main__':
inp = [rnd.randrange(100, 200) for ind in range(0, 10)]
inp = [rnd.randrange(100, 200) for ind in range(0,10)]
inp.sort()
print("search", inp[0], inp)
print("indx", bsearch(inp, inp[0], 0, len(inp)))
