class MinHeap:
    def __init__(self):
        self.heap = []
        
    def insert(self, value):
        self.heap.append(value)
        self.heapify()
        
    def heapify(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break  
    
    def extract_min(self):
        if not self.heap: return None
        if len(self.heap) == 1: return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.min_order()
        return root
    
    def min_order(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 1
            smallest = index
            
            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index
            
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
            
# Example usage of Min Heap
min_heap = MinHeap()
min_heap.insert(4)
min_heap.insert(2)
min_heap.insert(7)
min_heap.insert(1)

# Print the current state of the Min Heap
print("Min Heap:", min_heap.heap)  # Output: [1, 2, 7, 4]

# Extract the minimum element
min_element = min_heap.extract_min()
print("Extracted Min Element:", min_element)  # Output: 1

# Print the updated state of the Min Heap
print("Updated Min Heap:", min_heap.heap)  # Output: [2, 4, 7]


# class MinHeap: Defines a class named MinHeap to represent a Min Heap.
# def __init__(self): Initializes the MinHeap object with an empty list to represent the heap.
# def insert(self, value): Method to insert a new element into the Min Heap.
# self.heap.append(value): Adds the new element to the end of the heap.
# self._heapify_up(): Calls the _heapify_up() method to maintain the heap property.
# def _heapify_up(self): Helper method to fix the heap property after an insertion.
# index = len(self.heap) - 1: Gets the index of the newly added element.
# while index > 0:: Loop until the element reaches the root.
# parent_index = (index - 1) // 2: Calculates the index of the parent node.
# if self.heap[index] < self.heap[parent_index]:: Compares the values of the child and parent.
# self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]: Swaps the child and parent if the child is smaller.
# index = parent_index: Updates the index to the parent for the next iteration.
# else: break: Breaks the loop if the heap property is satisfied.
# def extract_min(self): Method to extract and return the minimum element from the Min Heap.
# if not self.heap:: Checks if the heap is empty.
# return None: Returns None if the heap is empty.
# if len(self.heap) == 1:: Checks if there is only one element in the heap.
# return self.heap.pop(): Returns and removes the element if there is only one element.
# root = self.heap[0]: Stores the root (minimum element) of the heap.
# self.heap[0] = self.heap.pop(): Replaces the root with the last element and removes the last element from the heap.
# self._heapify_down(): Calls the _heapify_down() method to maintain the heap property.
# return root: Returns the minimum element.
# def _heapify_down(self): Helper method to fix the heap property after an extraction.
# index = 0: Starts from the root.
# while True:: Infinite loop for the heapify-down process.
# left_child_index = 2 * index + 1: Calculates the index of the left child.
# right_child_index = 2 * index + 2: Calculates the index of the right child.
# smallest = index: Assumes the current node is the smallest.
# if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:: Checks if the left child is smaller.
# smallest = left_child_index: Updates the smallest index.
# if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:: Checks if the right child is smaller.
# smallest = right_child_index: Updates the smallest index.
# if smallest != index:: Swaps the current node with the smallest child if necessary.
# self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]: Swaps the elements.
# index = smallest: Updates the index for the next iteration.
# else: break: Breaks the loop if the heap property is satisfied.


# MaxHeap
# In MinHeap, comparisons are done with < (less than), while in MaxHeap, comparisons are done with > (greater than).