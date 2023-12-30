class Tree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.mid = None
        self.right = None
        
    def insert(self, data):
        if self.key is None:
            self.key = Tree(data)
            return
        
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Tree(data)
        elif self.key < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Tree(data)
        else:
            self.mid = Tree(data)
            
def In_Order_Traversal(root):
    if root:
        In_Order_Traversal(root.left)
        print(root.key, end=" ")
        In_Order_Traversal(root.mid)
        In_Order_Traversal(root.right)
                    
root = Tree(5)
list1 = [3, 7, 2, 4, 6, 8]
for i in list1:
    root.insert(i)
    
    #     5
    #    /|\
    #   3 7  
    #  /| | \
    # 2 4 6 8
    
    
In_Order_Traversal(root) # 2 3 4 5 6 7 8


            
    
    