# Fibonacci Search:
# Fibonacci search is a searching algorithm that works on sorted arrays. 
# It is similar to binary search but uses Fibonacci numbers to divide the array into smaller segments.

def FibonacciSearch(arr, target):
    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = 1
    
    while fib < len(arr):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
        fib = fib_minus_1 + fib_minus_2
        
    offset = -1
    
    while fib > 1:
        
        i = min(offset + fib_minus_2, len(arr) - 1)
        
        if arr[i] < target:
            fib = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            
            offset = i
            
        elif arr[i] > target:
            fib = fib_minus_2
            fib_minus_1 = fib_minus_1 - fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            
        else:
            return i
        
    if fib_minus_1 and arr[offset + 1] == target:
        return offset + 1
    return -1

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14
print(FibonacciSearch(arr, target))
            
            
# Advantages:

# Efficiency: Fibonacci search has a time complexity of O(log n), similar to binary search. It efficiently narrows down the search space using Fibonacci numbers.
# Adaptive: Like other search algorithms, Fibonacci search can adapt to different types of datasets.
# Disadvantages:

# Complexity: The implementation of Fibonacci search is more complex compared to binary search, which might make it harder to understand and debug.
# Requires Sorted Input: Fibonacci search, like other search algorithms, requires the list to be sorted before applying the algorithm.

###########################################

# Now, let's step through the algorithm:

# Initialize Fibonacci Numbers:

# Initialize three variables: fib_minus_2, fib_minus_1, and fib, representing the previous two Fibonacci numbers and the current Fibonacci number, respectively.
# Start with fib_minus_2 = 0, fib_minus_1 = 1, and fib = 1.
# Find the Smallest Fibonacci Number Greater Than or Equal to the Length of the Array:

# Update the Fibonacci numbers until fib is greater than or equal to the length of the array.
# In our case, the length of the array is 10, and the smallest Fibonacci number greater than or equal to 10 is 13.
# Search Process:

# Initialize an offset variable to -1.
# Compare the target value with the value at index min(offset + fib_minus_2, len(arr) - 1).
# If the target value is smaller, update fib, fib_minus_1, fib_minus_2, and offset accordingly to search in the lower half of the array.
# If the target value is larger, update fib, fib_minus_1, fib_minus_2, and offset accordingly to search in the upper half of the array.
# Repeat the process until fib is greater than 1.
# Check for Target Value:

# If fib_minus_1 is not 0 and the value at index offset + 1 is equal to the target value, return offset + 1.
# If the target value is not found in the array, return -1.