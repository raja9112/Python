# Jump Search:
# Jump search is another searching algorithm, particularly useful for sorted arrays. 
# It works by jumping ahead by fixed steps to find an interval where the target element might be present 
# and then performing a linear search within that interval.
import math
def JumpSearch(arr, target):
    prev = 0
    n = len(arr)
    steps = int(math.sqrt(n))
    
    while arr[min(steps, n) - 1] < target:
        prev = steps
        steps += int(math.sqrt(n))
        if prev >= n:
            return -1
        
    # Linear search method 1
    
    # while arr[prev] < target:
    #     prev += 1
    #     if prev == min(steps, n):
    #         return -1
    # if arr[prev] == target:
    #     return prev


    # Linear search method 2
    for i in range(prev, steps):
        if arr[i] == target:
            return i
    return -1

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 10
print(JumpSearch(arr, target)) #4

# Advantages:

# Efficiency: Jump search has a time complexity of O(√n), where n is the number of elements in the list. It is faster than linear search.
# Works on Sorted Lists: Like binary search, jump search requires the list to be sorted but can be applied to large datasets efficiently.
# Disadvantages:

# Not Always Optimal: Jump search may not be as efficient as binary search for some datasets, particularly those with a highly variable distribution of values.
# Requires Sorted Input: Similar to binary search, jump search requires the list to be sorted before applying the algorithm.

#############################################################################################################################

# Now, let's step through the algorithm:

# Calculate the Jump Size:

# The length of the array is 10, so the square root of 10 is approximately 3.16, rounded down to the nearest integer is 3. So, our jump size will be 3.
# Jump Ahead in the Array:

# We start by jumping ahead in the array by fixed steps of 3.
# We start at index 0 and jump to index 3, then to index 6.
# Find the Interval:

# At index 6, the value is 14, which is not less than our target value, 14. So, we stop jumping.
# Now, we have found an interval where the target value might be present. Our interval is from index 3 to index 6.
# Perform Linear Search in the Interval:

# We start from the previous position (index 3) and linearly search through the elements until we find the target element or exceed the end of the interval.
# We search from index 3 to index 6 and find the target value, 14, at index 6.
# Return the Result:

# We return the index 6, where we found the target value.