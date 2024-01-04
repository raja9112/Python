# Problem: Find the Most Frequent Element in an Array
# You're given an array of integers. Write a function to find the most frequent element(s) in the array.

# For example:

# Given nums = [1, 2, 3, 4, 2, 2, 3, 1, 1, 5],
# The function should return [1, 2] because both 1 and 2 appear 3 times, which is the maximum frequency in the array.

# Task:
# Write a Python function that takes in an array of integers (nums) and returns a list of the most frequent element(s). If there are multiple elements with the same maximum frequency, return all of them.

# This problem can be solved efficiently using a hash table to count the frequency of each element in the array.

# Feel free to implement this problem and explore how hash tables can help in finding the most frequent elements!

from collections import defaultdict

def frequency(arr):
    hash_table = defaultdict(int)
    
    # Count the frequency of each element
    for num in arr:
        hash_table[num] += 1  # Value will be updated by adding 1 to existing value
        # print(hash_table.items())
# dict_items([(1, 1)])
# dict_items([(1, 1), (2, 1)])
# dict_items([(1, 1), (2, 1), (3, 1)])
# dict_items([(1, 1), (2, 1), (3, 1), (4, 1)])
# dict_items([(1, 1), (2, 2), (3, 1), (4, 1)])
# dict_items([(1, 1), (2, 3), (3, 1), (4, 1)])
# dict_items([(1, 1), (2, 3), (3, 2), (4, 1)])
# dict_items([(1, 2), (2, 3), (3, 2), (4, 1)])
# dict_items([(1, 3), (2, 3), (3, 2), (4, 1)])
# dict_items([(1, 3), (2, 3), (3, 2), (4, 1), (5, 1)])
        
    maxx = max(hash_table.values()) # 3
    # print(hash_table.items()) #([(1, 3), (2, 3), (3, 2), (4, 1), (5, 1)])
    
    result = [(num,count) for num, count in hash_table.items() if count == maxx]
    print(result)
    
        
nums = [1, 2, 3, 4, 2, 2, 3, 1, 1, 5]
frequency(nums) # [(1, 3), (2, 3)]
