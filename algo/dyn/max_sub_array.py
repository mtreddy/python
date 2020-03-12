# code to solve max sub array


import os
import sys

array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
def find_max_crossing_sub_array(array, l, m, h):
        lsum = -65536
        rsum = -65536
        tsum = 0
        lmax = rmax = 0
        for i in range(m,l-1,-1):
            tsum = tsum+array[i] 
            if tsum > lsum:
                lsum = tsum
                lmax = i
        tsum = 0 
        for j in range(m+1,h+1):
            tsum = tsum + array[j] 
            if tsum > rsum:
                rsum = tsum
                rmax = j
        return (lmax, rmax, lsum+rsum)

def find_max_sub_array(array, l,h):
        #m = 0
        #ll=lh=rl=rh=cl=ch=0
        #lsum = rsum = csum=0
        if l == h:
            return(l,h, array[l])
        else:
            m = int((l + h)/2)
            ll, lh, lsum = find_max_sub_array(array, l, m)
            rl, rh, rsum = find_max_sub_array(array, m+1, h)
            cl, ch, csum = find_max_crossing_sub_array(array,l,m,h)
        if lsum >= rsum and lsum >= csum:
            return (ll, lh, lsum)
        elif rsum >= lsum and rsum >= csum:
            return(rl, rh, rsum)
        else:
            return(cl, ch, csum)


print(array)
low, high, bsum =find_max_sub_array(array, 0, len(array)-1)
print(low, high, bsum)
        

