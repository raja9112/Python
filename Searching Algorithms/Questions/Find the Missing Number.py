# # Find the Missing Number
# Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.

# Note: There are no duplicates in the list.

# Examples: 

# Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
# Output: 5
# Explanation: Here the size of the array is 7, so the range will be [1, 8]. The missing number between 1 to 8 is 5


# Input: arr[] = {1, 2, 3, 5}, N = 5
# Output: 4
# Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4

def MissingNumber(arr):
    h = [0] * (len(arr)+1)
    
    for i in range(len(arr)):
        func = arr[i] - 1       # Func will give index number
        h[func] = 1
    print(h)
    for j in range(len(arr)+1):
        if h[j] == 0:
            return j + 1
       
    # Method 2 using formula
    # n = len(arr)
    # formula = (n+1) * (n+2)/ 2
    # sum_of_arr = sum(arr)
    # return int(formula - sum_of_arr)
       
arr = [1, 2, 3, 5] 
print(MissingNumber(arr))