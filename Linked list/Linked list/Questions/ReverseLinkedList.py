#Given a pointer to the head node of a linked list, 
# the task is to reverse the linked list. 
# We need to reverse the list by changing the links between nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def Adding(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else: 
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    def printing(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.ref
        print()
        
    def Reverse(self):
        prev = None
        current_node = self.head
        while current_node:
           next_node = current_node.ref
           current_node.ref = prev
           prev = current_node
           current_node = next_node
           
        self.head = prev
        
ll = LinkedList()
ll.Adding(1)
ll.Adding(2)
ll.Adding(3)
ll.Adding(4)
ll.Adding(5)
print("Linked List...")
ll.printing()

print("After reversing the linked list")
ll.Reverse()
ll.printing()

# Output:
# Linked List...
# 1 --> 2 --> 3 --> 4 --> 5 --> 
# After reversing the linked list
# 5 --> 4 --> 3 --> 2 --> 1 --> 