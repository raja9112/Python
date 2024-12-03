# This problem is commonly known as the "Equilibrium Index" problem. You need to find an index in an array such that the sum of elements on the left of the index is equal to the sum of elements on the right of the index.

# Approach:
# Compute the total sum of the array.
# Traverse the array while maintaining a running sum of elements seen so far (left sum).
# At each index, check if the left sum equals the total sum minus the left sum minus the current element. If so, return the element or index.
# If no such index is found, return a message stating no equilibrium exists.

def find_equilibrium(arr):

    left_sum = 0
    total_sum = sum(arr)

    for i in range(0, len(arr)):
        if left_sum == total_sum - left_sum - arr[i]:
            return arr[i]
        
        left_sum += arr[i]

    return "No Equilibrium found"




# Example Usage:
arr1 = [1, 3, 5, 2, 2]
print(find_equilibrium(arr1))  # Output: 5

arr2 = [2, 4, 6, 10, 1, 2]
print(find_equilibrium(arr2))  # Output: "No equilibrium found"