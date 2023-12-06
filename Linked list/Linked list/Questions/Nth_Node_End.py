# # Program for Nth node from the end of a Linked List
# Follow the given steps to solve the problem using this approach: 

# Calculate the length of the Linked List. Let the length be len. 
# Print the (len – n + 1)th node from the beginning of the Linked List. 

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
            return
        n = self.head
        while n.ref:
            n = n.ref
        n.ref = new_node
        
    def printing(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.ref
        print()
        
    def finding(self, position):
        # Store the original head reference
        n = self.head              
        length = 0               # If the length is -1, the range starts from 0 

        #Finding the length of linked list
        while n:                    
            n = n.ref
            length += 1
            
        # Check for invalid position
        if position > length or position < 0:               
            print("The given index is out of bounds...")
            return
        
        # Reset to the original head reference
        n = self.head
        
        # Traverse to the (length - position)th node from the beginning
        for i in range(0, length-position):
            n = n.ref
        return n.data
          
ll = LinkedList()

# Adding elements to the linked list
ll.Adding(1) 
ll.Adding(2)
ll.Adding(3)
ll.Adding(4)
ll.Adding(5) 
print("Linked list...") 
ll.printing()

user = int(input("Enter the Index number: "))
print(ll.finding(user))      
        
#Output
# Linked list...
# 1 2 3 4 5 
# Enter the Index number: 2
# 4