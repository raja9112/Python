class Node:
    def __init__ (self, data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def AddingElement(self, element):
        new_node = Node(element)
        new_node.ref = self.head
        self.head = new_node
        
    def AddAtEnd(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
        
    def AddingAfterGivenElement(self, element, x):
        n = self.head
        while n.ref is not None:
            if x == n.data:
                break
            n = n.ref
            
        if n is None:
            print("Node is not avaialable")
        new_node = Node(element)
        new_node.ref = n.ref
        n.ref = new_node
        
    def Printing(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.ref
        print()
        
y = LinkedList()
y.AddingElement(70)
y.AddingElement(90)
y.AddingElement(10)
y.AddingAfterGivenElement(100, 90)
y.AddAtEnd(1000)
y.AddAtEnd(2000)

print("Linked List")
y.Printing()