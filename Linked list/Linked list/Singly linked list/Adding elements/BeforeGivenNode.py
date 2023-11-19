class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Function add the element to the at the beginning of the list
    def adding_element(self, element_add):
        new_node = Node(element_add)
        new_node.ref = self.head
        self.head = new_node

    def AddingBeforeGivenNode(self, element, x):
        n = self.head
        while n.ref is not None:
            if x == n.data:
                break
            else:
                n = n.ref

        if n is None:
            print("Node is present in the Linked List")
        else:
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
y.adding_element(5)
y.adding_element(50)
y.adding_element(200)
y.AddingBeforeGivenNode(100, 50)

y.Printing()