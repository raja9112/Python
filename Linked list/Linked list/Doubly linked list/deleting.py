class Node:
    def __init__(self, data):
        self.pref = None
        self.data = data
        self.nref = None
        
class DoublyLinkedList:
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
                
     
        
#Deleting the beginning node of the list        
    def AtBeginning(self):
        if self.head is None:
            print("The linked list is empty")
            return()
        
        if self.head.nref is None:      #Checking the list contains only one node, if yes then it sets the head as none
            self.head = None
            print("Linked list is empty after deleting the only one node")
            return()
        
        self.head = self.head.nref      #changing the head by the current head's reference
        self.head.pref = None           #after changing the head, set the previous reference to None
        
#Deleting the last node of the list
    def AtEnding(self):
        if self.head is None:
            print("Linked list is empty")
            return()
        
        if self.head.nref is None:
            self.head = None
            print("Linked list is empty after deleting the only one node")   
            return()
        
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None
        # self.head = n.pref
        # self.head.nref = None
        
#Deleting the node by the given value
    def DeletingByValue(self, value):
        #Checking the list empty
        if self.head is None:
            print("The linked list is empty")
            return
    
        #Checking if the list have only one node and the given node is same as the node presented in list, then deletes it
        if self.head.nref is None:
            if value == self.head.data:
                self.head = None
                print("Node is deleted")
            else:
                print("The given value is not present in the list")
                
        #if the list contains many nodes and the given value is same as the first node
        if self.head.data == value:
            self.head == self.head.nref    
            self.head.pref == None
            return
        
        n = self.head
        while n.nref is not None: #traversing through the node to find the specified node
            if n.data == value:     #If it finds the specified node or not, it will come out of the loop
                break
            n = n.nref

        if n.nref is not None:      #Then it will check the node's reference is none or not. if yes, it will delete it
            n.nref.pref = n.pref
            n.pref.nref = n.nref
            return
        else:
            if n.data == value:     #Suppose if node's reference is None, the previous node's reference will set to None (Considered as last node)
                n.pref.nref = None
            else:
                print("The given node is not presented in the list") 
                
#traversing in forward direction
    def printing_LL(self):
        n = self.head
        if n is None:
            print("Linked List is empty")
        while n is not None:
            print(n.data, end=" ")
            n = n.nref
        
dd = DoublyLinkedList()
dd.adding_at_beginning(10)
dd.adding_at_beginning(20)
dd.adding_at_beginning(30)
dd.adding_at_beginning(40)
dd.adding_at_beginning(50)
print("Linked List...")
dd.printing_LL()

dd.AtBeginning()
print("\nLinked list after deleting the beginning node...")
dd.printing_LL()

dd.AtEnding()
print("\nLinked list after deleting the end node...")
dd.printing_LL()

print("\nLinked list after deleting a given node...")
dd.DeletingByValue(30)
dd.printing_LL()

# Linked List...
# 50 40 30 20 10 
# Linked list after deleting the beginning node...
# 40 30 20 10 
# Linked list after deleting the end node...
# 40 30 20 
# Linked list after deleting a given node...
# 40 20 