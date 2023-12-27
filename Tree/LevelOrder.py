from collections import deque

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
                
# Program to print the tree in level order method
def LevelOrder(root):
    if root is None:
        return 
        
    queue = deque()
    queue.append(root)
    
    while queue:
        node = queue.popleft()
        print(node.key, end=" ")
        
        if node.left:
            queue.append(node.left)     # Both functions will run if the return is not used here
        if node.right:
            queue.append(node.right)
        
root = BST(10)
list1 = [5,20,3,7,15,25]
for i in list1:
    root.insert(i)
    
LevelOrder(root)

# Node Class:

# The Node class represents each node of the binary tree. Each node contains a key value, left pointer, and right pointer.
# Level Order Traversal Function:

# level_order_traversal(root) performs level order traversal of the binary tree.
# It takes the root node of the binary tree as an argument.
# If the root is None, it returns immediately.
# It initializes a deque (queue) to store nodes during traversal and appends the root node to it.
# While the queue is not empty:
# Dequeue the node at the front of the queue.
# Print the key of the dequeued node.
# If the dequeued node has a left child, enqueue the left child.
# If the dequeued node has a right child, enqueue the right child.
# Continues this process until all nodes are traversed, printing the keys in level order.
# Constructing a Sample Binary Tree:

# The sample binary tree is constructed with nodes and their connections to form a tree structure.
# Printing Level Order Traversal:

# Calls the level_order_traversal(root) function with the root of the constructed binary tree to perform the level order traversal.
# Prints the keys of the nodes in level order.