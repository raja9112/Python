# Basic implementation of Hash mapping
class HashMap:
    def __init__(self):
        self.size = 10                  # Size of the hash map
        self.map = [None]*self.size     # Initialize the hash map with None values
        
    def get_hash_index(self, key):
        return hash(key) % self.size    # Hash function to determine the index
    
    def add(self, key, value):
        index = self.get_hash_index(key)    # Get the hash of the key
        if self.map[index] is None:         # If the slot is empty, create a new list with (key, value) tuple
            self.map[index] = [(key, value)]
        else:                                    
            # If slot is not empty, check for existing key and update its value or add a new (key, value) pair
            for pair in self.map[index]:
                if pair[0] == key:
                    pair = (key, value)  # Update value if key exists
                    return
            self.map[index].append((key, value))    # Add new (key, value) pair
            
    def get(self, key):
        index = self.get_hash_index(key)    # Get the hash of the key
        if self.map[index] is not None:     # If the slot is empty
            for pair in self.map[index]:    # Search for the key and return its value
                if pair[0] == key:
                    return pair[1]
        return None                         # Return None if key not found
    
    def delete(self, key):
        index = self.get_hash_index(key)
        if self.map[index] is not None:         # If the slot is not empty
            for pair in range(len(self.map[index])):       # Iterate through the slot
                if self.map[index][pair][0] == key:        # If the key is found, delete the (key, value) pair
                    self.map[index].pop(pair)
                    return
    
hash_map = HashMap()
hash_map.add('apple', 10)
hash_map.add('orange', 20)
hash_map.add('banana', 30)

print(f"The value of the key 'orange' is: {hash_map.get('orange')}") # 20
hash_map.delete('banana')
print(f"The value of the key 'banana' is: {hash_map.get('banana')}") # None
