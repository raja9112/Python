class Node:
    def __init__(self, data):
        self.pref = None
        self.data = data
        self.nref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
#Code for adding the element at the beginning of linked list
    def adding_at_beginning(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            
#Code for addig the element at the ending
    def adding_at_ending(self,element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
                
            n.nref = new_node
            new_node.pref = n 

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
print("Adding at beginning...")
d.adding_at_beginning(10)
d.adding_at_beginning(20)
d.printing_LL()

print("\nAdding at ending...")
d.adding_at_ending(100)
d.adding_at_ending(200)
d.printing_LL()

print("\nTraversing in backwards...")
d.printing_backward()
