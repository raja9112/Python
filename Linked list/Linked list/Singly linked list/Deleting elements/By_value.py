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
        
    def ByValue(self,x):
        if self.head is None:
            print("Linked List is empty")
        if self.head == x:
            self.head = self.head.ref
            
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        
        if n is None:
            print("Node is not available")
        n.ref = n.ref.ref
                
    
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

y.ByValue(20)
print("Linked List: ")
y.printing()