import os
import sys
import re
import queue

class Node:
    def __init__(self, name, v):
        self.name = name
        self.v = v
        self.lst= []

def clean_list(lst):
    slst = set(lst)
    for it in lst:
        #print(it)
        mt = re.match(r'^[A-Za-z0-9\-_\ ]+', it)
        #print(mt)
        if mt == None:
            slst.remove(it)
    return list(slst)

def bfs_dir(cur_dir):
    files = []
    q = queue.Queue() # queue to maintain each level of dirs
    node = Node(cur_dir, True)
    q.put(node)
    cnt = 0
    while q.empty() == False:
        tnode = q.get()
        if os.path.isdir(tnode.name) == False:
            continue
        tlst = os.listdir(tnode.name)
        #print("node", tnode.name)
        #Create Adjacency list of nodes
        for it in tlst:
            nnode = Node(tnode.name + "/"+ it, False)
            tnode.lst.append(nnode)
        #print("adj list", tnode.lst)
        for it in tnode.lst:
            if it.v == False:
                it.v = True
                tstr = it.name
                #print(tstr)
                q.put(it)	
                files.append(tstr+"\n")
    return files 
    #return tnode
		
	

#cur_dir="/Users/tirumalamarri/Movies"
cur_dir="/Users/tirumalamarri/Documents/tiru_docs/technical/education/pustakalu/"
fls = bfs_dir(cur_dir)
