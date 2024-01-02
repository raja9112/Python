class HashMap:
    def __init__(self):
        self.size = 10
        self.key = [None]*self.size
        self.value = [None]*self.size
        
    def hash_function1(self, key):
        return hash(key) % self.size
    
    def hash_function2(self, key):
        # Choose a prime number smaller than the size
        return 7 - (hash(key) % 7)
    
    def insert(self, key, value):
        index_func1 = self.hash_function1(key)
        index_func2 = self.hash_function2(key)
        while self.key[index_func1] is not None:
            if self.key[index_func1] == key and self.key[index_func1] != "Deleted":
                self.value[index_func1] = value
                return
            index_func1 = (index_func1 + index_func2) % self.size
            
        self.key[index_func1] = key
        self.value[index_func1] = value
            
    def get(self, key):
        index_func1 = self.hash_function1(key)
        index_func2 = self.hash_function2(key)
        while self.key[index_func1] is not None:
            if self.key[index_func1] == key and self.key[index_func1] != "Deleted":
                return self.value[index_func1]
            index_func1 = (index_func1 + index_func2) % self.size
            
            if index_func1 == index_func2:
                break
            
        return None
            
    def delete(self, key):
        index_func1 = self.hash_function1(key)
        index_func2 = self.hash_function2(key)
        while self.key[index_func1] is not None:
            if self.key[index_func1] == key and self.key[index_func1] != "Deleted":
                self.key[index_func1] = "Deleted"
                self.value[index_func2] = None
                return
            
            index_func1 = (index_func1 + index_func2) % self.size
            
            if index_func1 == index_func2:
                break
            
        return None
    
    def display(self):
        for i in range(self.size):
            if self.key[i] is not None and self.key[i] != "Deleted":
                print(f"Index [{i}]: (Key: {self.key[i]}, Value: {self.value[i]})")
            else:
                print(f"(Index [{i}]: None)")
                
hash_map = HashMap()
hash_map.insert("apple", 5)
hash_map.insert("banana", 7)
hash_map.insert("orange", 3)
hash_map.insert("grapes", 10)
hash_map.insert("kiwi", 8)
hash_map.insert("melon", 12)

hash_map.display()

print(hash_map.get("banana")) # 7
print(hash_map.get("kiwi")) # 8

hash_map.delete("orange")
print(hash_map.get("orange")) # None

hash_map.delete("orange")
print(hash_map.get("orange")) # None

hash_map.display()

# Output
# Index [0]: (Key: apple, Value: 5)
# (Index [1]: None)
# Index [2]: (Key: grapes, Value: 10)
# Index [3]: (Key: orange, Value: 3)
# (Index [4]: None)
# Index [5]: (Key: melon, Value: 12)
# (Index [6]: None)
# Index [7]: (Key: banana, Value: 7)
# (Index [8]: None)
# Index [9]: (Key: kiwi, Value: 8)
# 7
# 8
# None
# None
# Index [0]: (Key: apple, Value: 5)
# (Index [1]: None)
# Index [2]: (Key: grapes, Value: 10)
# Index [3]: (Key: orange, Value: 3)
# (Index [4]: None)
# Index [5]: (Key: melon, Value: 12)
# (Index [6]: None)
# Index [7]: (Key: banana, Value: 7)
# (Index [8]: None)
# Index [9]: (Key: kiwi, Value: 8)
