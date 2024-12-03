# Kadane's Algorithm
# Kadane's Algorithm is used to find the maximum sum of a contiguous subarray in an array of integers (both positive and negative). It solves the problem in 

# O(n) time complexity, making it very efficient.

# Problem Statement:
# Given an integer array arr[], find the sum of the largest contiguous subarray.

# Key Idea:
# Use a dynamic programming approach to track the maximum sum at each index.
# Maintain two variables:
# current_sum: The maximum sum of the subarray ending at the current index.
# max_sum: The maximum sum found so far.
# Algorithm Steps:
# Initialize:

# current_sum = 0
# max_sum = negative infinity (or arr[0] if all numbers are negative)
# Iterate through the array:

# Add the current element to current_sum.
# If current_sum becomes negative, reset it to 0 (start a new subarray).
# Update max_sum with the maximum of max_sum and current_sum.
# Return max_sum as the result.


# def max_subarray_sum(arr):
#     max_val = float("-inf")
#     current_value = 0

#     for i in arr:
#         current_value += i
#         if current_value > max_val:
#             max_val = current_value
#         elif current_value < 0:
#             current_value = 0

#     return max_val



# # Example usage
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# print(max_subarray_sum(arr))  # Output: 7 (subarray [4, -1, -2, 1, 5])



#  With indices
def max_subarray_sum_with_indices(arr):
    max_value = float("-inf")
    current_sum = 0
    start= end= s = 0

    for i, num in enumerate(arr):
        current_sum += num

        if current_sum > max_value:
            max_value = current_sum
            start = s
            end = i

        if current_sum < 0:
            current_sum = 0
            s = i + 1

    return max_value, arr[start: end+1]


# Example usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray_sum_with_indices(arr))  # Output: 7 (subarray [4, -1, -2, 1, 5])