class HashMap:
    def __init__(self, initial_capacity):
        self.capacity = initial_capacity
        self.size = 0
        self.key = [None]*self.capacity
        self.value = [None]*self.capacity
        
    def _hash_func(self, key):
        return hash(key) % self.capacity
        
    def _load_factor(self):
        return self.size / self.capacity
    
    def _rehash(self):
        self.capacity *= 2
        old_key = self.key
        old_value = self.value
        self.key = [None]*self.capacity
        self.value = [None]*self.capacity
        
        for i in range(len(old_key)):
            if old_key[i] is not None:
                self.insert(old_key[i], old_value[i])
                
    def insert(self, key, value):
        load_factor = self._load_factor()
        if load_factor > 0.7:
            self._rehash()
            
        index = self._hash_func(key)
        while self.key[index]:
            if self.key[index] == key and self.key[index] != "Deleted":
                self.value[index] = value
                return
            index = (index + 1) % self.capacity
            
        self.key[index] = key
        self.value[index] = value
        self.size += 1
        
    def get(self, key):
        index = self._hash_func(key)
        initial_index = index
        while self.key[index] is not None:
            if self.key[index] == key and self.key[index] != "Deleted":
                return self.value[index]
            index = (index + 1) % self.capacity
            
            if index == initial_index:
                break
            
        return None
    
    def delete(self, key):
        index = self._hash_func(key)
        while self.key[index] is not None:
            if self.key[index] == key and self.key[index] != "Deleted":
                self.key[index] = "Deleted"
                self.value[index] = None
                return
            index = (index + 1) % self.capacity
            
        return None
    
    def display(self):    
        for i in range(self.capacity):
            if self.key[i] is not None and self.key[i] != "Deleted":
                print(f"Index [{i}]: (Key: {self.key[i]}, Value: {self.value[i]})")
            elif self.key[i] == "Deleted":
                print(f"Index [{i}]: Deleted")
            else: 
                print(f"Index [{i}]: None")
                
hash_map = HashMap(7)
hash_map.insert("apple", 5)
hash_map.insert("banana", 7)
hash_map.insert("orange", 3)
hash_map.insert("grapes", 10)
hash_map.insert("kiwi", 8)
hash_map.insert("melon", 12)

print("Hash Map contents:")
hash_map.display()

# Inserting more elements to trigger rehashing
hash_map.insert("strawberry", 15)
hash_map.insert("pineapple", 20)

print("\nUpdated Hash Map contents:")
hash_map.display()

print("\nGetting values of key: ")
print(hash_map.get("strawberry"))
print(hash_map.get("grapes"))

hash_map.delete("orange")
print(hash_map.get("orange")) # None

hash_map.delete("kiwi")
print(hash_map.get("kiwi")) # None

hash_map.display()

# Output
# Hash Map contents:
# Index [0]: (Key: kiwi, Value: 8)
# Index [1]: None
# Index [2]: None
# Index [3]: None
# Index [4]: None
# Index [5]: None
# Index [6]: None
# Index [7]: (Key: banana, Value: 7)
# Index [8]: (Key: orange, Value: 3)
# Index [9]: None
# Index [10]: (Key: apple, Value: 5)
# Index [11]: None
# Index [12]: (Key: grapes, Value: 10)
# Index [13]: (Key: melon, Value: 12)

# Updated Hash Map contents:
# Index [0]: None
# Index [1]: None
# Index [2]: None
# Index [3]: None
# Index [4]: None
# Index [5]: (Key: strawberry, Value: 15)
# Index [6]: (Key: pineapple, Value: 20)
# Index [7]: (Key: banana, Value: 7)
# Index [8]: (Key: orange, Value: 3)
# Index [9]: None
# Index [10]: None
# Index [11]: None
# Index [12]: (Key: melon, Value: 12)
# Index [13]: None
# Index [14]: (Key: kiwi, Value: 8)
# Index [15]: None
# Index [16]: None
# Index [17]: None
# Index [18]: None
# Index [19]: None
# Index [20]: None
# Index [21]: None
# Index [22]: None
# Index [23]: None
# Index [24]: (Key: apple, Value: 5)
# Index [25]: None
# Index [26]: (Key: grapes, Value: 10)
# Index [27]: None

# Getting values of key:
# 15
# 10

# Index [0]: None
# Index [1]: None
# Index [2]: None
# Index [3]: None
# Index [4]: None
# Index [5]: (Key: strawberry, Value: 15)
# Index [6]: (Key: pineapple, Value: 20)
# Index [7]: (Key: banana, Value: 7)
# Index [8]: Deleted
# Index [9]: None
# Index [10]: None
# Index [11]: None
# Index [12]: (Key: melon, Value: 12)
# Index [13]: None
# Index [14]: Deleted
# Index [15]: None
# Index [16]: None
# Index [17]: None
# Index [18]: None
# Index [19]: None
# Index [20]: None
# Index [21]: None
# Index [22]: None
# Index [23]: None
# Index [24]: (Key: apple, Value: 5)
# Index [25]: None
# Index [26]: (Key: grapes, Value: 10)
# Index [27]: None