"""
Why is this back tracking?
Permutations are exhaustive. Since we need to walk back all paths 
we can't really optimizae it.

Approach here is DFS(Depth first search)
we walk two paths one with lower case and other apper case

        aA
     bB    bB
   cC cC  cC cC    

Each leter reprsent edge on the graph not node
Step1
 call dfs() twice, one for upper case and other lower case
Step2:
 Once len of the inp string reached string from each call will be returned.

"""
import sys
import os
def dfs1(istr, i, res):
    if i == len(istr):
        res.append(''.join(istr))
        return
    #print(res)
    istr[i] = istr[i].upper()
    #print(istr)
    dfs1(istr, i+1, res)
    istr[i] = istr[i].lower()
    dfs1(istr, i+1, res)

def find_perm(res, inp):
    """ Goa is to find all the permuations of the string passed"""
    res = []
    inp =["a","b","c"] 
    indx = 0;
    dfs1(inp, indx, res)
    print(res)


res=[]
inp="abcd"
ret = find_perm(res, inp)
