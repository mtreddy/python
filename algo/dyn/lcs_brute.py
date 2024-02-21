"""
  This example show brute foce recusive lcs problem solving
  This solution runs in O(m*n) time
  where m and n are input string lengths
"""
def lcs(x, y, m, n):
    if m ==0 or n==0:
        return 0
    elif x[m-1] == y[n-1]:
        return  1 + lcs( x, y, m-1, n-1)
    else:
       return max(lcs( x, y, m-1, n), lcs(x, y, m, n-1))

def find_lcs():
    x="AGGTAB"
    y="GXTXAYB"
    print( x, y, lcs( x, y, len(x), len(y)))


find_lcs()
