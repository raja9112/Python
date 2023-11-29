class Node:
    def __init__(self, data):
        self.pref = None
        self.data = data
        self.nref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
#traversing in forward direction
    def printing_LL(self):
        n = self.head
        if n is None:
            print("Linked List is empty")
        while n is not None:
            print(n.data, end=" ")
            n = n.nref
            
#traversing in backward direction
    def printing_backward(self):
        n = self.head
        if n is None:
            print("Linked List is empty")
        while n.nref is not None:
            n = n.nref
        while n is not None:
            print(n.data, end=" ")
            n= n.pref
            
d = LinkedList()
print("Traversing from forward to backward...")
d.printing_LL()
print("Traversing from backward to forward...")
d.printing_backward()