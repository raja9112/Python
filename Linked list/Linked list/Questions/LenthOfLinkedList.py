#program to find the lenght of linked list
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
        
#iterative method 
# Time complexity: O(N), Where N is the size of the linked list
# Auxiliary Space: O(1), As constant extra space is used.

    # def Length(self):
    #     n = self.head
    #     count = 0
    #     while n:
    #         count += 1
    #         n = n.ref
    #     return count
    
#Recursive method
#LengthCount takes argument as self.head which is given in Length() and it counts the iteration
#In Length we are collecting the count from LengthCount by giving the self.head as parameter.
# Time Complexity: O(N), As we are traversing the linked list only once.
# Auxiliary Space: O(N), Extra space is used in the recursion call stack.

    def LengthCount(self, node):
        if node is None:
            return 0
        else: 
            return 1 + self.LengthCount(node.ref)
        
    def Length(self):
        return self.LengthCount(self.head)
     
    
ll = LinkedList()
ll.Adding(1)
ll.Adding(2)
ll.Adding(3)
ll.Adding(4)
ll.Adding(5)
print("Linked List...")
ll.printing()

print(f"\nThe length og the Linked list is {ll.Length()}")

#Output
# Linked List...
# 1 2 3 4 5 

# The length og the Linked list is 5