# Find the middle of a given linked list
# Auxiliary Given a singly linked list, find the middle of the linked list. For example, if the given linked list is 1->2->3->4->5 then the output should be 3. 
# If there are even nodes, then there would be two middle nodes, we need to print the second middle element. 
# For example, if the given linked list is 1->2->3->4->5->6 then the output should be 4

#Approaching 2-pointers method

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
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
        
    def printing(self):
        n = self.head 
        while n:
            print(n.data, end=" ")
            n = n.ref
        print()
        
    def Middle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        
        while fast_ptr and fast_ptr.ref:
            slow_ptr = slow_ptr.ref
            fast_ptr = fast_ptr.ref.ref
        return slow_ptr.data
    
ll = LinkedList()
ll.Adding(1)
ll.Adding(2)
ll.Adding(3)
ll.Adding(4)
ll.Adding(5)
ll.Adding(6)
print("Linked list...")
ll.printing()

print("Middle node of Linked list...")
print(ll.Middle())

#Output
# Linked list...
# 1 2 3 4 5 6
# Middle node of Linked list...
# 4


# Approach Explanation:
# Two-Pointer Technique:

# The method uses two pointers - a slow pointer and a fast pointer.
# The slow pointer moves one node at a time (slow_ptr = slow_ptr.next), while the fast pointer moves two nodes at a time (fast_ptr = fast_ptr.next.next).
# This approach allows the fast pointer to traverse the list twice as quickly as the slow pointer.
# Finding the Middle Element:

# While the fast pointer (fast_ptr) is not None and its next node is also not None, the loop continues.
# At each iteration, the slow pointer moves one node forward, and the fast pointer moves two nodes forward.
# When the fast pointer reaches the end of the list (fast_ptr or fast_ptr.next becomes None), the slow pointer will be at the middle of the list.
# Handling Odd and Even Nodes:

# If the linked list has an odd number of nodes, the slow pointer will exactly reach the middle node.
# If the linked list has an even number of nodes, the slow pointer will be at the second middle node.
# Returning the Middle Element:

# Once the loop exits, the data value of the node where the slow pointer is positioned represents the middle element(s) of the linked list.
# In the code, return slow_ptr.data returns the data value of the middle node(s).