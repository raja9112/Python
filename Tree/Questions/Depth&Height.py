# Given a Binary Tree consisting of N nodes and a integer K, the task is to find the depth and height of the node with value K in the Binary Tree. 

# The depth of a node is the number of edges present in path from the root node of a tree to that node.
# The height of a node is the number of edges present in the longest path connecting that node to a leaf node.

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
# Depth of node 25 = 2
# Height of node 25 = 1
# Explanation:
# The number of edges in the path from root node to the node 25 is 2. Therefore, depth of the node 25 is 2.
# The number of edges in the longest path connecting the node 25 to any leaf node is 1. Therefore, height of the node 25 is 1.

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
                
def HeightOfTree(data):
    if data is None:
        return -1
    return max(HeightOfTree(data.left), HeightOfTree(data.right)) + 1

def DepthOfTree(root, k, depth):
    if root is None:
        return None, None
    
    if root.key == k:
        return root, depth
    
    node_left, depth_left = DepthOfTree(root.left, k, depth+1)
    node_right, depth_right = DepthOfTree(root.right, k, depth+1)
    
    if node_left:
        return node_left, depth_left
    else:
        return node_right, depth_right

root = BST(10)
list1 = [5,20,3,7,15,25,100]
for i in list1:
    root.insert(i)

node, depth = DepthOfTree(root, 25, 0) #25    2     25 will go to node, 2 will go to depth

if node:
    node_height = HeightOfTree(node)
    print(f"The depth the node is {depth}")
    print(f"\nThe Height of the node is {node_height}")
else:
    print("The given node is out of bounds")