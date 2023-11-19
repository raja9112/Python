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

print("Linked list: ")
llist.printing_list()

# Explanation:
# Node class:

# Represents a node in the linked list.
# Each node contains data to hold the value and ref (reference) to point to the next node.
# LinkedList class:

# Represents the linked list data structure.
# Has an attribute head that points to the first node in the list.
# adding_element method:

# Adds a new element to the beginning of the linked list.
# Creates a new node (new_node) with the given element.
# Sets the ref of the new node to the current head.
# Updates the head to the new node, making it the new starting node of the list.
# printing_list method:

# Traverses the linked list starting from the head.
# Prints the data of each node in the list, iterating through each node using the ref pointer until it reaches the end (where temp becomes None).
# Creating the linked list and adding elements:

# An instance of LinkedList (llist) is created.
# Elements (5, 10, and 15) are added to the linked list using the adding_element method. They are added at the beginning of the list, so 15 becomes the first element added, followed by 10, and then 5.
# Printing the linked list:

# Finally, the printing_list method is called on the linked list instance (llist) to print the elements of the linked list.