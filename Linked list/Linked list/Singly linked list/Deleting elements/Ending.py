class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self): self.head = None
    
    def adding(self, element):
        new_node = Node(element)
        new_node.ref = self.head
        self.head = new_node
        
    def ending(self):
        if self.head is None:
            print("Linked List is empty!")
        n = self.head
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
    
    def printing(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.ref
        print()
        
y = LinkedList()
y.adding(10)
y.adding(20)
y.adding(30)

print("Linked list: ")
y.printing()

y.ending()
print("Linked List: ")
y.printing()
            