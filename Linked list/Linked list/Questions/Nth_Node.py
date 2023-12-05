# Write a function that takes a linked list and an integer index and returns the data value stored in the node at that index position. 
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
            print(temp.data, end=" ")
            temp = temp.ref
        print()
        
    def func(self, position):
        if self.head is None:
            print("List is empty")
            return
        
        #Method 1
        if position == 0:
                return self.head.data
        
        index = 0
        current = self.head
        while current and index < position:
            current = current.ref
            index += 1
            
        if index < position:
                print("The given position is out of bounds")
        else:
            return current.data
        
        
        #Method 2
                
        # index = 0
        # current = self.head
        # while current:
        #     if position == index:
        #         return current.data
        #     current = current.ref
        #     index += 1
            
        # if index < position:
        #     print("The given position is out of bounds")
        #     return
            
ll = LinkedList()
ll.Adding(1)
ll.Adding(11)
ll.Adding(14)
ll.Adding(41)
ll.Adding(13)

print("linked list...")
ll.printing()

print("\nAfter the finding the node by given index number...")
print(ll.func(2))

#output
# linked list...
# 1 11 14 41 13

# After the finding the node by given index number...
# 14