# Given an array arr[] of size n, find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.

# Note:- The position you return should be according to 1-based indexing. 

# Example 1:

# Input:
# n = 7
# arr[] = {1, 5, 3, 4, 3, 5, 6}
# Output: 2
# Explanation: 
# 5 is appearing twice and 
# its first appearence is at index 2 
# which is less than 3 whose first 
# occuring index is 3.

# Example 2:

# Input:
# n = 4
# arr[] = {1, 2, 3, 4}
# Output: -1
# Explanation: 
# All elements appear only once so 
# answer is -1.

# Your Task:
# You don't need to read input or print anything. Complete the function firstRepeated() which takes arr and n as input parameters and returns the position of the first repeating element. If there is no such element, return -1.
 

# Expected Time Complexity: O(n)
# Expected Auxilliary Space: O(n)

 

# Constraints:
# 1 <= n <= 106
# 0 <= Ai<= 106

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        h = {}
        
        for i in range(n-1):
            if arr[i] not in h:
                h[arr[i]] = 1
            else:
                h[arr[i]] += 1
                
        for j in range(len(h)):
            if h[arr[j]] > 1:
                return j+1          #We are getting index of the key, and the arr starts with index 1 not 0
        return -1
            
            
        # Method 2
        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)): 
        #         if arr[i] == arr[j]:
        #             return i + 1
        # return -1
            
            
arr = [1, 5, 3, 4, 3, 5, 6]
n = len(arr)
obj = Solution()
print(obj.firstRepeated(arr, n))


