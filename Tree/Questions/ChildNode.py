# Number of children of given node in a Tree
# Examples: 

# Input: Node = 5
#        10
#       /  \
#      5    20
#     / \   / \
#    3   7 15 25

# Output: [3,7]
# 2

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
                
def ChildNode(root, target):
    if not root:
        return
    if root.key == target:
        childs = []
        if root.left:
            childs.append(root.left.key)
        if root.right:
            childs.append(root.right.key)
        return childs
    
    left_child = ChildNode(root.left, target)
    if left_child:
        return left_child
    
    right_child = ChildNode(root.right, target)
    if right_child:
        return right_child
    
    return None
            
# def count(root, target):
#     child_node = Sibling(root, target)
#     if child_node:
#         return len(child_node)
#     return 0
            
root = BST(10)
list1 = [5,20,3,7,15,25,100]
for i in list1:
    root.insert(i)
    
print("The sibling nodes present in the parent node are: ", (Sibling(root, 5)))    
print("The number of siblings node present in parent node are: ",len(Sibling(root, 5)))
            

# Step-by-Step Explanation:
# Base Case:

# if root is None: This checks if the current node is None (i.e., a leaf or an empty subtree). If so, it returns None, indicating that the target node was not found in this path or the tree is empty.
# Check for Target Node:

# if root.key == target: Checks if the current node (root) matches the target node.
# If the target node is found:
# Initializes an empty list childs to store child nodes.
# Appends the keys of left and right child nodes to childs, if they exist.
# Returns childs containing the keys of the child nodes.
# Recursion on Left Subtree:

# left_child = ChildNode(root.left, target): Initiates a recursive call to ChildNode with the left child of the current node as the new root for the recursive call.
# if left_child is not None: Checks if the target node was found in the left subtree.
# If found, propagates the result (child nodes of the target node) up the recursive calls.
# Recursion on Right Subtree:

# right_child = ChildNode(root.right, target): Initiates a recursive call to ChildNode with the right child of the current node as the new root for the recursive call.
# if right_child is not None: Checks if the target node was found in the right subtree.
# If found, propagates the result (child nodes of the target node) up the recursive calls.
# Return None If Not Found:

# If the target node is not found in the current subtree or any of its descendants, the function returns None.
