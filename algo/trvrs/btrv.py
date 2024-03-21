"""
    Code implements functions to traverse in Binary (Not bst)
"""
import sys
class btrv:
    def __init__(self):
        self.mdist = 0
    def dfs(self, node):
        if node == None:
            return 0
        # This doesn't have any affect except initialize
        dist = 0
        print(node.data, dist)
        dist = self.dfs(node.left)
        dist+=1
        print("L", dist, self.mdist)
        self. mdist=max(dist,self.mdist)
        dist = self.dfs(node.right)
        dist+=1
        print("R",dist, self.mdist)
        self.mdist=max(dist,self.mdist)
        return dist

    def node_depth(self, node, v):
        if node == None:
            return -1
        # This doesn't have any affect except initialize
        dist = -1
        if node.data == v:
            print("Found it")
            return dist+1
        print(node.data, dist)
        dist = self.node_depth(node.left,v )
        if dist >= 0:
           return  dist+1
        dist = self.node_depth(node.right, v)
        if dist >= 0:
            return dist+1
        return dist

    def node_height(self, node, v):
        global  height
        if node == None:
            return -1

        left = self.node_height(node.left, v)
        print("L", left)
        right = self.node_height(node.right, v)
        print("R", right)
        ans = max(left, right)+1
        if node.data == v:
            height = ans
        return ans



class Node:
     def __init__(self, x):
         self.data = x
         self.left = None
         self.right = None

root = Node(7)
root.left = Node(13)
root.right = Node(18)
root.left.left = Node(23)
root.left.right = Node(28)
root.left.right.right = Node(48)
root.left.right.right.right = Node(68)
root.right.left = Node(33)
root.right.right = Node(38)

bt = btrv()
#bt.dfs(root)
#print(" max depth", bt.mdist)

#print("Node depth for 13", bt.node_depth(root, 69))
print("Node height for 13", bt.node_height(root, 13))
