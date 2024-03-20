import sys
class btrv:
	def __init__(self):
		self.mdist = 0
	def dfs(self, node):
		if node == None:
			return 0
		dist = -1
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


class Node:
     def __init__(self, x):
         self.data = x
         self.left = None
         self.right = None

root = Node(5)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(20)
root.left.right = Node(25)
root.left.right.right = Node(45)
root.left.right.right.right = Node(45)
root.right.left = Node(30)
root.right.right = Node(35)
bt = btrv()
bt.dfs(root)
print(" max depth", bt.mdist)
