def missing_number(arr):
    # n = len(arr)

    # xor_all = 0
    # xor_array = 0

    # for i in range(n+1):
    #     xor_all ^= i

    # for num in arr:
    #     xor_array ^= num

    # return xor_all ^ xor_array



    # Method 2

    for i in range(len(arr)):
        if i not in arr:
            return i


    # Both methods has O(n) Time complexity and O(1) Space complexity
# Example Usage
print(missing_number([3, 0, 1]))  # Output: 2
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Output: 8