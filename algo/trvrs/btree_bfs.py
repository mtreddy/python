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

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

bt = bbfs()
print(" level order lists", bt.bfs(root))

            
