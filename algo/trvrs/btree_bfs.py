import sys
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class bbfs:
    def __init__(self):
        self.x = 0
    def bfs(self, node):
        items = []
        q = deque()
        q.append(node)
        while q:
            qlen = len(q)
            level = []
            for it in range(qlen):
                nd = q.popleft()
                if nd:
                    level.append(nd.val)
                    q.append(nd.left)
                    q.append(nd.right)
            if level:
                items.append(level)
        return items
    def print_level_order(self, node):
        q = deque()
        q.append(node)
        while q:
            nd = q.popleft()
            if nd:
                print(nd.val)
                q.append(nd.left)
                q.append(nd.right)
    def ser_dfs(self, node):
        global res
        if node == None:
            res.append('N')
            return
        res.append(node.val)
        self.ser_dfs(node.left)
        self.ser_dfs(node.right)

    def deser_dfs(self ):
        global ind
        global inp
        if inp[ind] == 'N':
            ind+=1
            return None
        node = Node(inp[ind])
        ind+=1
        node.left = self.deser_dfs()
        node.right = self.deser_dfs()
        return node


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

bt = bbfs()
test = "level_order"
test = "level_order_print"
test = "serialize"
test = "deserialize"
if test == "level_order":
    print(" level order lists", bt.bfs(root))
if test == "level_order_print":
    print(" level order lists", bt.print_level_order(root))
if test == "serialize":
    global res
    res = []
    print("serialize", bt.ser_dfs(root), res)
if test == "deserialize":
    global inp
    global ind
    ind = 0
    inp = [3, 9, 'N', 'N', 20, 15, 'N', 'N', 7, 'N', 'N']
    root = None
    root = bt.deser_dfs()
    


            
