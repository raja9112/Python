
# To solve this problem, you need to modify the array based on the following rules:

# Traverse the array from left to right.
# If two consecutive numbers are the same (non-zero), double the value of the first number and replace the second number with 0.
# After processing the entire array, shift all the zeros to the end.
# Example:
# Input:
# python
# Copy code
# arr = [2, 2, 0, 4, 4, 8]
# Output:
# python
# Copy code
# [4, 8, 8, 0, 0, 0]
# Explanation:
# The first two 2s are combined into 4, and the second 2 becomes 0. Intermediate array: [4, 0, 0, 4, 4, 8]
# The two 4s are combined into 8, and the second 4 becomes 0. Intermediate array: [4, 0, 0, 8, 0, 8]
# All zeros are shifted to the end: [4, 8, 8, 0, 0, 0].


def convert_array(arr):
    for i in range(len(arr)-1):
        if arr[i] != 0 and arr[i] == arr[i+1]:
            arr[i] *= 2
            arr[i+1] = 0

    # return [num for num in arr if num != 0] + [0] *arr.count(0)       # O(n) Space

    pos = 0
    # Space = O(1)
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]

            if i != pos:
                arr[i] = 0

            pos += 1

    return arr


arr = [2, 2, 0, 4, 4, 8]
print(convert_array(arr))  # Output: [4, 8, 8, 0, 0, 0]