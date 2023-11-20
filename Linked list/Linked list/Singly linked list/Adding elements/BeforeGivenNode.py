class Node():
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Function add the element to the at the beginning of the list
    def adding_element(self, element):
        new_node = Node(element)
        new_node.ref = self.head
        self.head = new_node

    def AddingBeforeGivenElement(self, element, x):
        if self.head is None:
           print("Linked List is empty")
        if self.head.data == x:
            new_node = Node(element)
            new_node.ref = self.head
            self.head = new_node
            return
        
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
            
        if n is None:
            print("Node is not found")
        new_node = Node(element)
        new_node.ref = n.ref
        n.ref = new_node
            
                
    
    #Function to print the Linked List
    def printing_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.ref
        print()

llist = LinkedList()
llist.adding_element(5)
llist.adding_element(10)
llist.adding_element(15)
llist.AddingBeforeGivenElement(2,10)

print("Linked list: ")
llist.printing_list()