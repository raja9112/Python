# Problem Statement:
# Given an array of integers with repeated numbers, find the top three most repeated numbers in descending order of frequency. If there are ties in frequency, the smaller number should come first.

# Example:
# Input: 4,5,6,5,4,3,5,4,6,6,6,3

# Output: 6,4,5

# Explanation:
# 6 appears 4 times.
# 4 appears 3 times.
# 5 appears 3 times. (But 4 is smaller, so it comes first.)
# Example 2:
# Input:# 1,2,2,3,3,3,4,4

# Output:# 3,2,4

# Approach:
# Use a dictionary to count the frequency of each number.
# Sort the items of the dictionary:
# By frequency in descending order.
# If frequencies are equal, by number in ascending order.
# Extract the top three elements from the sorted list.

from collections import Counter

def top_three_repeated(arr):

    return [i[0] for i in sorted(Counter(arr).items(), key = lambda x: (-x[1], x[0]))[:3]]


# Example Usage
arr1 = [4, 5, 6, 5, 4, 3, 5, 4, 6, 6, 6, 3]
print(top_three_repeated(arr1))  # Output: [6, 4, 5]

arr2 = [1, 2, 2, 3, 3, 3, 4, 4]
print(top_three_repeated(arr2))  # Output: [3, 2, 4]


# Time complexity: O(n + k log k) iterating through loop to get res and sort will be log k and k will be the no unique elements
# Space complexity: O(n) freq of dict