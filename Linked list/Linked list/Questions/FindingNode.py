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
        
    def FindingNode(self, node):
        new_list = []
        while self.head.ref is not None:
            new_list.append(self.head.data)
            self.head = self.head.ref
        
        if node in new_list:
            print(f"The given node {node} is present in Linked list")
        else:
            print(f"the given node {node} is not presented in Linked list")
        
ll = LinkedList()

user_input = int(input("How many nodes you want to add: "))
for i in range(1, user_input + 1):
    ll.Adding(int(input(f"Enter the node {i} : ")))

print("\nLinked list...")
ll.printing()

user = int(input("\nEnter the node you want to find: "))
ll.FindingNode(user)

#output
# How many nodes you want to add: 5
# Enter the node 1 : 1
# Enter the node 2 : 3
# Enter the node 3 : 6
# Enter the node 4 : 4
# Enter the node 5 : 8

# Linked list...
# 1 3 6 4 8 

# Enter the node you want to find: 4
# The given node 4 is present in Linked list