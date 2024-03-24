"""
    Code implements functions to traverse in Binary (Not bst)
"""
import sys
class btrv:
    def __init__(self):
        self.mdist = 0
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
            height = ans+1
        return ans


    def node_height_min(self, node):
        if node == None:
            return 0
        elif node.left == None and node.right == None:
            return 1
        elif node.left != None and node.right == None:
            return self.node_height_min(node.left) + 1
        elif node.right != None and node.left == None:
            return self.node_height_min(node.right) + 1
        else:
            return min(self.node_height_min(node.left), self.node_height_min(node.right)) + 1

class Node:
     def __init__(self, x):
         self.data = x
         self.left = None
         self.right = None
case =0
if case == 0:
    root = Node(7)
    root.left = Node(13)
    root.right = Node(18)
    root.left.left = Node(23)
    root.left.right = Node(28)
    root.left.right.right = Node(48)
    root.left.right.right.right = Node(68)
    root.right.left = Node(33)
    root.right.right = Node(38)
elif case == 1:
    root = Node(1)
    root.right= Node(2)
    root.right.right=Node(3)
    root.right.right.right=Node(4)
    root.right.right.right.right=Node(5)
elif case == 2:
    root = Node(1)
    root.left = Node(2)
    root.left.left=Node(3)
    root.left.left.left=Node(4)
    root.left.left.left.left=Node(5)
elif case == 3:
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
else:
    print("Invalid case")

bt = btrv()
## Max depth is found by getting the height of the root node

#print("Node depth for 13", bt.node_depth(root, 69))
if root != None:
    #print("Node height for ", bt.node_height(root, root.data))
    print("Node height for ", bt.node_height_min(root))
