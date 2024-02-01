# Find the largest three distinct elements in an array
# Given an array with all distinct elements, find the largest three elements. Expected time complexity is O(n) and extra space is O(1). 

# Examples :

# Input: arr[] = {10, 4, 3, 50, 23, 90}
# Output: 90, 50, 23

import sys
def largestThreeElements(arr):
    n = len(arr) 
    
    first = second = third = -sys.maxsize
    # print(third, first, second)         -9223372036854775807 -9223372036854775807 -9223372036854775807
    
    for i in range(0, n):
        
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
            
            
        elif arr[i] > second:
            third = second
            second = arr[i]
            
        else:
            third = arr[i]
            
    return first, second, third

arr = [10, 4, 3, 50, 23, 90]
print(largestThreeElements(arr))