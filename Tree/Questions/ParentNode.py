# Find the parent of a node in the given binary tree

# Given a tree and a node, the task is to find the parent of the given node in the tree. Print -1 if the given node is the root node.
# Examples: 

# Input: Node = 7
#        10
#       /  \
#      5    20
#     / \   / \
#    3   7 15 25

# Output: 5

# Input: Node = 10
#        10
#       /  \
#      5    20
#     / \   / \
#    3   7 15 25

# Output: -1
from collections import deque
class BST:
    def __init__(self, key):
        self.left = None
        self.key = key
        self.right = None
        
    def insert(self, data):
        if self.key is None:
            self.key = BST(data)
            return
        if self.key == data:
            return
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else: 
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
                
def ParentNode(root, target, parent):
    if not root:
        return 
    
    if root.key == target:
        print(parent)
    else:
        # It will take the current node's key as parent(root.key), current node's left child node as root.left, 
        # so if the child node's key meets the target value, the parent node's key will be printed
        ParentNode(root.left, target, root.key) 
        ParentNode(root.right, target, root.key)
    
        
root = BST(10)
list1 = [5,20,3,7,15,25,100]
for i in list1:
    root.insert(i)
    
ParentNode(root, 7, -1)

# ParentNode(root, 10, "root") If we want to show the fist node as "root"