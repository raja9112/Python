# Question:

# You're given an array of integers. Write a function to find two numbers such that they add up to a specific target number.

# For example:

# Given nums = [2, 7, 11, 15] and target = 9,
# The function should return [0, 1] because nums[0] + nums[1] = 2 + 7 = 9.

# Task:

# Write a Python function that takes in an array of integers nums and an integer target. The function should return the indices of the two numbers (in the form of a list) such that they add up to the target.

# This problem can be efficiently solved using a hash table (dictionary in Python) to store the elements and their indices while traversing the array.

# Feel free to use this problem to practice your understanding of hash tables and their application in solving algorithmic problems!

def two_sum(arr, target):
    hash_table = {}
    for i, num in enumerate(arr):
        complement = target - num
        # print(num, complement) 2,7   7,2 -> complement.  
        if complement in hash_table:
            return hash_table[complement], i
        hash_table[num] = i
    return []
        
        
print(two_sum([2, 7, 11, 15] , 9))