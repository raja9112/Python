#Creating the binary search tree.
class BST:
    def __init__(self, key):       #Tree have a similar structure like linked list. Unlike linked list tree's node can store multiple reference addresses
        self.left = None
        self.key = key
        self.right = None
        
    #Code for inserting the node
    def insert(self, data):
        #Checking the tree is empty
        if self.key is None:
            self.key = BST(data)
            return
        
        # Checking the root node's key is same as the given data
        if self.key == data:
            return
        
        # Checking the key is is greater or lesser than the given data to assign it to the appropriate position (left or right)
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
            
#Driver's code
root = BST(10)
list1 = [20,5,4,60,45,9,15]
for i in list1:
    root.insert(i)