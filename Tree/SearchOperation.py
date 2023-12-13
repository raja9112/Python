# Program to perform search operation in binary tree
class BST:
    def __init__(self, key):
        self.left = None
        self.key = key 
        self.right = None

    # Code for performing insert operation
    def insert(self, data):
        if self.key is None:
            self.key = BST(data)
            return
        if self.key ==  data:
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
                
    # Code for performing search operation
    def search(self, data):
        if self.key is None:
            print("The tree is empty...")
            return
        if self.key == data:
            print("The node has been found...")
            return
        if self.key > data:
            if self.left: 
                self.left.search(data)
            else: 
                print("The node has not been found...")
        else:
            if self.right:
                self.right.search(data)
            else: 
                print("The node has not been found...")
                
#Driver code
tree = BST(20)
list1 = [4,67,45,3,12,28,0]
for i in list1:
    tree.insert(i)
    
user = int(input("Enter the node you want to find: "))
tree.search(user)