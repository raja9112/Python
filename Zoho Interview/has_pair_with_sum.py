# To check if a pair exists in the array 

# A[] with a sum equal to x, you can use different approaches depending on the constraints. Here's an efficient way using a hash set.

# Optimal Approach (Using a Hash Set):
# We can iterate through the array while keeping track of the required complement for each element in a hash set. If we find the complement already exists, we have found a pair.

def has_pair_with_sum(arr, x):
    seen = set()        #Space and time will be O(n)
    for num in arr:
        complement = x - num
        if complement in seen:
            return True
        seen.add(num)

    return False

# Example usage
arr = [1, 4, 45, 6, 10, 8]
x = 16
print(has_pair_with_sum(arr, x))  # Output: True (6 + 10 = 16)

arr = [1, 2, 3, 9]
x = 8
print(has_pair_with_sum(arr, x))  # Output: False



# 2 Pointer approach
# Time = O(n log n)
# Space = O(n)

# def has_pair_with_sum(arr, x):
#     # Step 1: Sort the array
#     arr.sort()

#     # Step 2: Use two pointers
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         current_sum = arr[left] + arr[right]

#         if current_sum == x:
#             return True  # Pair found
#         elif current_sum < x:
#             left += 1  # Move the left pointer to increase the sum
#         else:
#             right -= 1  # Move the right pointer to decrease the sum

#     return False  # No pair found

# # Example usage
# arr = [1, 4, 45, 6, 10, 8]
# x = 16
# print(has_pair_with_sum(arr, x))  # Output: True (6 + 10 = 16)

# arr = [1, 2, 3, 9]
# x = 8
# print(has_pair_with_sum(arr, x))  # Output: False
