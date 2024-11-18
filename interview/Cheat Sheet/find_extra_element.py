def find_extra_element(arr1, arr2):
    """
    Find the extra element in arr1 that is not in arr2.
    Assumes arr1 has one extra element compared to arr2.
    """
    # Ensure arr1 is the larger array
    if len(arr2) > len(arr1):
        arr1, arr2 = arr2, arr1

    # Compare elements at corresponding indices
    for i in range(len(arr2)):
        if arr1[i] != arr2[i]:
            return arr1[i], i

    # If no mismatch found, the extra element is the last one in arr1
    return arr1[-1], len(arr1) - 1


# Test cases
arr1 = [2, 4, 6, 8, 10]
arr2 = [2, 4, 6, 8]
print(find_extra_element(arr1, arr2))  # Output: (10, 4)

arr1 = [1, 2, 3, 5, 6]
arr2 = [1, 2, 3, 6]
print(find_extra_element(arr1, arr2))  # Output: (5, 3)

arr1 = [7, 8, 9]
arr2 = [7, 9]
print(find_extra_element(arr1, arr2))  # Output: (8, 1)
