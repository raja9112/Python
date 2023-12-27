# write a function that returns level of the key. 

# For example, consider the following tree. If the input key is 3, 
# then your function should return 1. If the input key is 4, then your function should return 3. 
# And for key which is not present in key, then your function should return 0.

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
                
def LevelOfNode(root, k, level):
    if not root: 
        return None, None
    if root.key == k: 
        return root, level
    
    root_left, left_level = LevelOfNode(root.left, k, level + 1)
    root_right, right_level = LevelOfNode(root.right, k, level + 1)
    
    if root_left:
        return root_left, left_level
    return root_right, right_level

root = BST(10)
list1 = [5,20,3,7,15,25,100]
for i in list1:
    root.insert(i)
    
node, level = LevelOfNode(root, 25, 1)
print(f"The level of given node {node.key} is {level}")

# Examples:

# Input: K = 25, 
#         10
    #    /  \
    #   5    20
    #  / \   / \
    # 3   7 15 25
#                \
#               100  

# Output:
# The level of given node 25 is 3