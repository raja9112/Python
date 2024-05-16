# Turing interview question:

# Minimum steps to convert an Array into permutation of numbers from 1 to N

# Given an array arr of length N, the task is to count the minimum number of operations to convert given sequence into a permutation of first N natural numbers (1, 2, …., N). 
# In each operation, increment or decrement an element by one.

 
def min_operations_to_permutation(arr):
    arr = sorted(arr)
    n = len(arr)
    
    result = 0      # This variable will accumulate the total number of operations needed.
    for i in range(n):
        # For each element arr[i], compute the absolute difference between the element and the target value (i + 1). 
        # The target value is i + 1 because we want the array to contain numbers from 1 to N.
        # And add the difference in result
        result += abs(arr[i] - (i+1))
        
    return result

arr = [4, 1, 4, 2]
print(min_operations_to_permutation([3, 2, 1, 4]))  # Output: 0
print(min_operations_to_permutation([4, 1, 4, 2]))  # Output: 1
print(min_operations_to_permutation([2, 3, 4, 5]))  # Output: 4
        
        
