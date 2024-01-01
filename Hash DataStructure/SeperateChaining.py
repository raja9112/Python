# Collision handling by Seperate Chaining method
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class HashMap:
    def __init__(self, size):
        self.size = size
        self.map = [None]*self.size
        
    def get_hash_index(self, key):
        return hash(key) % self.size
    
    def add(self, key, value):
       index = self.get_hash_index(key)
       if self.map[index] is None:
           self.map[index] = Node(key, value)
       else:
           current = self.map[index]
           while current.next:
               current = current.next
           current.next = Node(key, value)
                
    def get(self, key):
        index = self.get_hash_index(key)
        current = self.map[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def delete(self, key):
        index = self.get_hash_index(key)
        current = self.map[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.map[index] = current.next
                return
            prev = current
            current = current.next
    
# Creating a hash map with size 10
hash_map = HashMap(10)

# Adding key-value pairs
hash_map.add("apple", 5)
hash_map.add("banana", 7)
hash_map.add("orange", 3)

# Index 0: -> None
# Index 1: -> [Node1 (Key: "apple", Value: 5)] -> [Node2 (Key: "banana", Value: 7)] -> None
# Index 2: -> None
# Index 3: -> [Node3 (Key: "orange", Value: 3)] -> None
# Index 4: -> None

# Getting values by keys
print("Accessing apple value: ",hash_map.get("apple"))  # Output: 5
print("Accessing banana value: ",hash_map.get("banana"))  # Output: 7
print("Accessing orange value: ",hash_map.get("orange"))  # Output: 3
print("Accessing grapes value which is not added in hash table: ",hash_map.get("grapes"))  # Output: None (as it's not present)

# Deleting values by key
hash_map.delete('orange')
print("Accessing orange key after deleting: ",hash_map.get('orange')) # Output: None