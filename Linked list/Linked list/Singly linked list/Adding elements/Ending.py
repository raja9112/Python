class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def AddToEnd(self, element):
        new_node = Node(element)  # Assigning the new node
        if self.head is None:       #Checking the head is null. If yes, then the new node will be assigned to the head
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:    #Else, we have to traverse into the list to find the node which has null memory (basically to the end node)
                n = n.ref
            n.ref = new_node        #if the ref is null, The new node will be assigned 

    def PrintingTheAnswer(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.ref
        print()
        

x = LinkedList()
x.AddToEnd(3)
x.AddToEnd(2)
x.AddToEnd(5)

x.PrintingTheAnswer()