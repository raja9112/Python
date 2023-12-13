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
                
    # Code for pre order traversal
    def preorder(self):
        print(self.key)
        if self.left:
            self.left.preorder()        # do not use return, because after printing the left node in subtree, the execution will pause ad go to next subtree.
        if self.right:                  # If we use return, the execution will stop instead of pause.
            self.right.preorder()       # After printing the left nodes, the existing executions will be resumed to print the right nodes

#Driver's code
root = BST(10)
list1 = [20,5,4,60,45,5,9,15]
for i in list1:
    root.insert(i)
    
print("Pre Order traversal of Binary Tree...")
root.preorder()

# Output
# Pre Order traversal of Binary Tree...
# 10
# 5
# 4
# 9
# 20
# 15
# 60
# 45