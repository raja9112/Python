#Program to Reverse a linked list using recursion.

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def Adding(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    def printing(self):
        n = self.head
        if n is None:
            print("Linked list is empty")
            return
        while n:
            print(n.data, end=" ")
            n = n.ref
        print()
        
    #Reversing the Linked list using Recursion method
    def recursion(self, current_node, prev):
        if current_node is None:
            self.head = prev
            return
        next_node = current_node.ref
        current_node.ref = prev
        self.recursion(next_node, current_node)
        
    #Wrapper function to start the reversal of recursive
    def reverse(self):
        if self.head is None or self.head.ref is None:
            return
        self.recursion(self.head, None)
    
ll = LinkedList()
ll.Adding(1)
ll.Adding(2)
ll.Adding(3)
ll.Adding(4)
ll.Adding(5)

print("Linked list...")
ll.printing()

print("\nAfter reversing the linked list...")
ll.reverse()
ll.printing()

#Output
# Linked list...
# 1 2 3 4 5 

# After reversing the linked list...
# 5 4 3 2 1 