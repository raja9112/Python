# Program to perform Pre Order traversal algorithm.
class BST:
    def __init__(self, key):
        self.left = None
        self.key = key
        self.right = None
        
    def insert(self, data):
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
                
    # Code for In order traversal
    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print(self.key, end=" ")
        if self.right:
            self.right.InOrder()
            
    # Code for Post Order traversal
    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.key, end=" ")
        
        
#Driver's code
root = BST(10)
list1 = [20,5,4,60,45,5,9,15]
for i in list1:
    root.insert(i)
    
print("In Order traversal of Binary Tree...")
root.InOrder()

print()
print("Post Order traversal of binary tree...")
root.PostOrder()

# Output
# In Order traversal of Binary Tree...
# 4 5 9 10 15 20 45 60 
# Post Order traversal of binary tree...
# 4 9 5 15 45 60 20 10 