
"""
In python there are no extended data type . Class is struct
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
""" Insert nodes recursively each insertion takes O(log(n)) . For N nodes O(Nlog(N))"""

def insert(node , val):
        if node is None:
            return Node(val)
        #we move left of the root
        if val < node.val:
            #Make sure reference returned 
            node.left = insert(node.left, val)
        else:
            #Make sure reference returned 
            node.right = insert(node.right, val)
        #This is imortant . New node needs to be reurned.
        return node


def print_bst_inorder(node):
    if node != None:
        print_bst_inorder(node.left)
        print(node.val)
        print_bst_inorder(node.right)



if __name__ == '__main__':
    root = None
    root = insert(root, 500)
    insert(root, 600)
    insert(root, 400)
    insert(root, 300)
    insert(root, 450)
    insert(root, 600)
    insert(root, 650)
    print_bst_inorder(root)
