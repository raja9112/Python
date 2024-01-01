class HashMap:
    def __init__(self):
        self.size = 10
        self.key = [None]*self.size
        self.value = [None]*self.size
        
    def get_hash_index(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.get_hash_index(key)
        while self.key[index] is not None and self.key[index] != "Deleted":
            if self.key[index] == key:                    # Key exists, update value
                self.value[index] = value
                return
            index = (index + 1) % self.size               # Move to next index (linear probing)
        
        # Found an empty slot, insert key and value
        self.key[index] = key
        self.value[index] = value
        
    def get(self, key):
        index = self.get_hash_index(key)
        initial_index = index
        
        while self.key[index] is not None:
            if self.key[index] == key and self.key[index] != "Deleted":
                return self.value[index]
            index = (index + 1) % self.size
            
            if index == initial_index:     # Reached the starting point
                break
        return None

    def delete(self, key):
        index = self.get_hash_index(key)
        initial_index = index
        while self.key[index] is not None:
            if self.key[index] == key:
                self.key[index] = "Deleted"
                self.value[index] = None
            elif self.key[index] == "Deleted":
                print("The given key is already deleted...")
            else:
                index = (index + 1) % self.size
            
            if index == initial_index:
                break
        return None
            
    def display(self):
        for i in range(self.size):
            if self.key[i] is not None and self.key[i] != "Deleted":
                print(f"Index [{i}]: (Key: {self.key[i]}, Value: {self.value[i]})")
            else:
                print(f"Index[{i}]: None")
            
        
hash_map = HashMap()
hash_map.insert("apple", 5)
hash_map.insert("banana", 7)
hash_map.insert("orange", 3)
hash_map.insert("grapes", 10)
hash_map.insert("kiwi", 8)
hash_map.insert("melon", 12)

hash_map.display()
# Output
# Index [0]: (Key: grapes, Value: 10)
# Index [1]: (Key: orange, Value: 3)
# Index[2]: None
# Index[3]: None
# Index [4]: (Key: apple, Value: 5)
# Index [5]: (Key: banana, Value: 7)
# Index [6]: (Key: kiwi, Value: 8)
# Index[7]: None
# Index [8]: (Key: melon, Value: 12)
# Index[9]: None

print(hash_map.get("banana")) # 7
print(hash_map.get("kiwi")) # 8

hash_map.delete("orange")
print(hash_map.get("orange")) # None

hash_map.delete("orange")
print(hash_map.get("orange")) # None

hash_map.display()
# Output
# Index [0]: (Key: grapes, Value: 10)
# Index[1]: None
# Index[2]: None
# Index[3]: None
# Index [4]: (Key: apple, Value: 5)
# Index [5]: (Key: banana, Value: 7)
# Index [6]: (Key: kiwi, Value: 8)
# Index[7]: None
# Index [8]: (Key: melon, Value: 12)
# Index[9]: None