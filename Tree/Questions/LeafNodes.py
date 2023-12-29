# Print all leaf nodes of a Binary Tree from left to right
# Examples: 

#        10
#       /  \
#      5    20
#     / \   / \
#    3   7 15 25

# Output: 3, 7, 15, 25

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

def LeafNode(root):
    if not root:
        return 
    
    if (not root.left) and (not root.right):
        print(root.key, end=" ")
        return
    
    # Both methods are doing the same thing
    if root.left:
        LeafNode(root.left)
    if root.right:
        LeafNode(root.right)
    
    # left_root = LeafNode(root.left)
    # right_root = LeafNode(root.right)
    
    # if left_root:
    #     return left_root
    # if right_root:
    #     return right_root
    
        
root = BST(10)
list1 = [5,20,3,7,15,25]
for i in list1:
    root.insert(i)
    
print(LeafNode(root))