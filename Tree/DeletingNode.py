# Program to delete the specified node in a Binary tree.
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
        print(self.key, end=" ")
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()
            
    def delete(self, data):
        if self.key is None:
            print("The Tree is empty")
            return
        
        # Traverse left subtree if data is smaller
        if self.key > data:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print("The given node is not present in the tree")
                
        # Traverse right subtree if data is greater
        elif self.key < data:
            if self.right:
                self.right = self.right.delete(data)
            else: 
                print("The given node is not present in the tree")
        else:
             # Node with only one child or no child
            if self.left is None:
                temp = self.right
                self = None             # Here the particular node will become None (deleted)
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            
            # Node with two children
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key        # After finding the smallest node in right subtree, the self.key that means the specified node.key can become same as a smallest node of right subtree (Copy of small node.key)
            self.right = self.right.delete(node.key)   # after the changing the node.key, the samllest node is in same position without removed, so using recursion deleting the that node.
        return self
    
root = BST(10)
list1 = [20,5,4,60,45,5,9,15]
for i in list1:
    root.insert(i)
print("Pre Oder traversal before delete opration...")
root.PreOrder()

print()
print("Pre Oder traversal after delete opration...")
root.delete(60)
root.PreOrder()

#Output
# Pre Oder traversal before delete opration...
# 10 5 4 9 20 15 60 45 
# Pre Oder traversal after delete opration...
# 10 5 4 9 20 15 45 