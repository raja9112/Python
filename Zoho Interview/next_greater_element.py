# Problem Statement:
# Given an array of integers, for each element in the array, find the next greater element. The next greater element for an element 
# x is the first greater element to the right of 
# x in the array. If no such element exists, return 
# −1 for that position.

# Example:
# Example 1:
# Input: 4,5,2,10,8

# Output: 5,10,10,−1,−1

# Explanation:

# Next greater for 4 is 5.
# Next greater for 5 is 10.
# Next greater for 2 is 10.
# Next greater for 10 is −1 (no greater element).
# Next greater for 8 is −1.

# Example 2:
# Input:
# 3,1,2,4

# Output:
# 4,2,4,−1

# Approach:
# 1. Brute Force (O(n²)):
# Iterate through the array for each element.
# For every element, traverse the remaining part of the array to find the next greater element.
# 2. Optimized Approach Using a Stack (O(n)):
# Use a stack to efficiently find the next greater element.
# Traverse the array from right to left:
# For each element, pop elements from the stack until the top of the stack is greater than the current element.
# If the stack is empty, the next greater element is −1.
# Otherwise, the next greater element is the top of the stack.
# Push the current element onto the stack.

def next_greater_element(arr):

    n = len(arr)
    res = [-1] * n
    current_stack = []

    for i in range(n-1, -1, -1):

        while current_stack and current_stack[-1] <= arr[i]:
            current_stack.pop()

        if current_stack:
            res[i] = current_stack[-1]

        current_stack.append(arr[i])

    return res


# Example Usage
arr = [4, 5, 2, 10, 8]
print(next_greater_element(arr))  # Output: [5, 10, 10, -1, -1]

arr = [3, 1, 2, 4]
print(next_greater_element(arr))  # Output: [4, 2, 4, -1]