"""
Copy right MIT license 2024
This program parses all the directories recursively and find the files and captures absolute paths 
to a list. It walks in BFS (Breadth first search). While searching it creates adjecncy list for each dir
and marks it if already visisted. Each directory or file name is allocated a node object and name and 
visted flag is set. Each node has refence to list . If the given files is not a directory then it adds 
to the list and skip any further search.
"""
import os
import sys
import re
import queue
from collections import defaultdict

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
        tlst = clean_list(tlst)
        #Create Adjacency list of nodes. Dont add to queue if its not a dir
        for it in tlst:
            nnode = Node(tnode.name + "/"+ it, False)
            #if this is not a directory add it to file list
            if os.path.isdir(nnode.name) == False:
                    tstr = nnode.name
                    files.append(tstr)
            else:
                tnode.lst.append(nnode)
        #print("adj list", tnode.lst)
        for it in tnode.lst:
            if it.v == False:
                it.v = True
                q.put(it)	
    return files 
    #return tnode
		
	

#cur_dir="/Users/tirumalamarri/Movies"
cur_dir="/Users/tirumalamarri/Documents/tiru_docs/technical/education/pustakalu"
fls = bfs_dir(cur_dir)
hs = defaultdict(list)
#Remove any duplicates
nlst = []
for ln in fls:
    if ln not in hs.keys():
        hs[ln] = 1
        nlst.append(ln)

print("Before clean no of entries", len(fls), "After dups removed", len(nlst))
fd = open("./file.txt", 'w', encoding="utf-8")
for ln in nlst:
    fd.write(ln)
fd.close()
