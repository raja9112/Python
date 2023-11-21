class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def adding(self, element):
        new_element = Node(element)
        new_element.ref = self.head
        self.head = new_element    
        
    def deleting(self):
        if self.head is None:
            print("The Linked List is empty")
        self.head = self.head.ref
        
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
print("Linked List:")
y.printing()

y.deleting()

print("Linked List after deleting the Node:")
y.printing()

#Output
# Linked List:
# 30 20 10
# Linked List after deleting thee:
# 20 10