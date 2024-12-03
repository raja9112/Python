def singleNumber(nums):
    ones, twos = 0, 0

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones


# Test Cases
print(singleNumber([2, 2, 3, 2]))  # Output: 3
print(singleNumber([0, 1, 0, 1, 0, 1, 99]))  # Output: 99