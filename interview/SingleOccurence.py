# GeeksforGeeks
# Find element occuring once when all other are present thrice

# Given an array of integers arr[] of length N, every element appears thrice except for one which occurs once.
# Find that element which occurs once.

# Example 1:

# Input:
# N = 4
# arr[] = {1, 10, 1, 1}
# Output:
# 10
# Explanation:
# 10 occurs once in the array while the other
# element 1 occurs thrice.
# Example 2:

# Input:
# N = 10
# arr[] = {3, 2, 1, 34, 34, 1, 2, 34, 2, 1}
# Output:
# 3
# Explanation:
# All elements except 3 occurs thrice in the array.
# Your Task:
# You do not need to take any input or print anything. You task is to complete the function singleElement() which takes an array of integers arr and an integer N which finds and returns the element occuring once in the array.

# Constraints:
# 1 ≤ N ≤ 105
# -109 ≤ A[i] ≤ 109

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).

#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        # code here 
        # for i in arr:
        #     if arr.count(i) == 1:
                # return i                #Total time taken to run this method 1.48s
        
        # Another approach
        #Total time taken to run this method 0.2s
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        for j, k in d.items():
            if k == 1:
                return j

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
# } Driver Code Ends