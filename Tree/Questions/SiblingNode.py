# Program to print the sibling nodes of given node
# Examples: 

# Input: Node = 15
#        10
#       /  \
#      5    20
#     / \   / \
#    3   7 15 25

# Output: 25

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
                
def SiblingNode(root, target):
    if root is None:
        return None
    
    if root.left and root.left.key == target:
        return root.right.key if root.right else None
    
    if root.right and root.right.key == target:
        return root.left.key if root.left else None
    
    left_node = SiblingNode(root.left, target)
    if left_node:
        return left_node
    
    right_node = SiblingNode(root.right, target)
    if right_node:
        return right_node
    
    return None
    
root = BST(10)
list1 = [5,20,3,7,15,25,100]
for i in list1:
    root.insert(i)
    
print(SiblingNode(root, 15))