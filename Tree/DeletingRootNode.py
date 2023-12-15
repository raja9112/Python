# Program to delete the root node
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
                
    def PreOrder(self):
        print(self.key, end=' ')
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()
            
    # program to delete root node as well as specified child nodes   
    def delete(self, data, current):  #Taking root node as current
        if self.key is None:
            print("Tree is empty...")
            return
        
        if self.key > data:
            if self.left:
                self.left = self.left.delete(data, current)
            else:
                print("The give node is out of bounds...")
        elif self.key < data:
            if self.right:
                self.right = self.right.delete(data, current)
            else:
                print("The give node is out of bounds...")
        else:
            if self.left is None:
                temp = self.right
                if data == current:              # Checking given data is equal to root node's key
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    return
                self = None
                return temp
            if self.right is None:
                temp = self.left
                if data == current:
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    return
                self = None
                return temp
            
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key, current)
        return self
    
    # Program to find the minimum and maximum node
    def min_node(self):
        current = self
        while current.left:
            current = current.left
        print("The lowest node in the tree is: ",current.key)
        
    def max_node(self):
        current = self
        while current.right:
            current = current.right
        print("the largest node in the tree is: ", current.key)
            
# Program to count the total number of nodes
def count(node):
    if node is None:        
        return 0
    return 1 + count(node.left) + count(node.right)  
        
root = BST(10)
list1 = [20,5,4,60,45,5,9,15]
for i in list1:
    root.insert(i)
        
print("PreOrder traversal after insertion...")
root.PreOrder()
print()
print("Total nodes available in the tree: ")
print(count(root))
print()
print("After deleting the node (9)...")
root.delete(9, root.key)
root.PreOrder()
print()
print("After deleting the root node...")
root.delete(10, root.key)
root.PreOrder()

print()
root.min_node()
root.max_node()

# Output
# PreOrder traversal after insertion...
# 10 5 4 9 20 15 60 45 
# Total nodes available in the tree: 
# 8

# After deleting the node (9)...
# 10 5 4 20 15 60 45 
# After deleting the root node...
# 15 5 4 20 60 45 
# The lowest node in the tree is:  4
# the largest node in the tree is:  60