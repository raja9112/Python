class Node:
    def __init__(self, data):
        self.pref = None
        self.data = data
        self.nref = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def adding(self, element):
        new_node = Node(element)
        if self.head is None:
#            print("Linked list is empty, so adding at the beginning")
            self.head = new_node
            return() #if you remove this return() It will create a infinite loop : ) or you can use else:
        
        new_node.nref = self.head
        self.head.pref = new_node
        self.head = new_node    
        
#Adding node after the specified node        
    def add_after(self, element, x):           
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.nref
        if n is None:
            print(f"\nThe given node data {x} is not present in the linked list")
        elif n.nref is None:
            new_node = Node(element) 
            new_node.pref = n
            n.nref = new_node
        else:
            new_node = Node(element) 
            new_node.pref = n
            new_node.nref = n.nref
            n.nref.pref = new_node
            n.nref = new_node
            
#Adding node before the specified node
    def add_before(self,element,x):
        if self.head is None:
            print("Unable to add the Node before the specified node, coz' the linked list is empty")
            return()
            
        if self.head.data == x:
            new_node = Node(element)
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            return()
            
        n = self.head
        while n.nref is not None:
            if n.nref.data == x:
                break
            n = n.nref
            
        if n is None:
            print("The given node is not present in Linked list")
            return()
        new_node = Node(element)
        new_node.pref = n
        new_node.nref = n.nref
        n.nref = new_node
        n.nref.pref = new_node

    def printing(self):
        temp = self.head
        if temp is None:
            print("Linked List is empty")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.nref
        
        
dd = DoublyLinkedList()
print("Linked List after adding elements...")
dd.adding(200)
print("\nafter the given node...")
dd.add_after(400, 200)
dd.printing()
dd.add_after(500, 300)
dd.printing()
print("\nBefore the given node...")
dd.add_before(150, 400)
dd.printing()