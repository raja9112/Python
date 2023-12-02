class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class Circular:
    def __init__(self):
        self.head = None
    
    def adding(self, element):
        new_node = Node(element)
        if self.head is None:       #checking the list empty. if yes creating a new node and assigning the new node's memory in new node's ref because in circular linked list the last node in the list contains the memory address of first node
            self.head = new_node
            new_node.ref = self.head       
        else:
            n = self.head
            while n.ref != self.head: #traversing to check that the n.ref is not equal to self.head, if it fails it will come out of loop. we can add the another node when the nref is equal to self.head
                n = n.ref
            n.ref = new_node            # here we are assigning the memory address of new node in n.ref and new node's ref will be self.head
            new_node.ref = self.head
 
            
    def printing(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.ref
            if temp == self.head:  # if the last node and self.head equals, it will break the loop of traversing
                break               #if this code is removed, it will create a infinite loop
        print()
        
c = Circular()
c.adding(10)
c.adding(20)
c.adding(30)
c.adding(40)
c.adding(50)    

c.printing()   
        