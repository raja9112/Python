# The task is to search and check if the given node exists in the binary tree or not. If it exists, print YES otherwise print NO.

# Input: Node = 7
# Output: YES

# Input: Node = 40
# Output: NO

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
                
def Searching(root, target):
    if root is None:
        return False
    
    if root.key == target:
        return True
    
    left = Searching(root.left, target)    
    right = Searching(root.right, target)
    
    if left:
        return left
    return right
    
root = BST(10)
list1 = [5,20,3,7,15,25,100]
for i in list1:
    root.insert(i)
        
if Searching(root, 7):  #Yes
    print("Yes")
else:
    print("No")