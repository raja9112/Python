#Program to delete a node by a given position

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
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.ref
        print()
        
    def DeletingNodeByPosition(self, position):
        if self.head is None:
            print("List is empty!")
            return
        if position == 0:                 #checking if the given position is 0. if yes, i will delete the first node
            self.head = self.head.ref
            return
        
        index = 0
        current_node = self.head
        while current_node and index < position:        #checking the index is lesser than given position and current_node is not None,
            prev_node = current_node             # if the condition passes it will traverse through the list and index will be increase by 1
            current_node = current_node.ref     #The current node will be set as prev node and the next node of current node will be set as current node
            index += 1
            
        if index < position:   
            print("The position number that you have given is out of range.")
        else:
            prev_node.ref = current_node.ref
        
        
ll = LinkedList()
ll.Adding(1)
ll.Adding(2)
ll.Adding(3)
ll.Adding(4)
ll.Adding(5)

print("linked list...")
ll.printing()

print("\nlinked list after deleting the node by given value...")
ll.DeletingNodeByPosition(3)
ll.printing()

#output
# linked list...
# 1 2 3 4 5

# linked list after deleting the node by given value...
# 1 2 3 5