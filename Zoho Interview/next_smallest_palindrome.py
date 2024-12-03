def next_smallest_palindrome(num):
    num_str = str(num)
    n = len(num_str)

    # Case 1: All digits are 9 (e.g., 999 → 1001)
    if all(ch == '9' for ch in num_str):
        return int('1' + '0' * (n - 1) + '1')

    # Split the number into left half and right half
    left_half = num_str[:(n + 1) // 2]  # Include the middle digit if odd length
    mirrored = left_half + left_half[:n // 2][::-1]

    # Case 2: If mirrored number is greater, it's the next palindrome
    if int(mirrored) > num:
        return int(mirrored)

    # Case 3: Increment the left half and re-mirror
    left_half = str(int(left_half) + 1)
    new_palindrome = left_half + left_half[:n // 2][::-1]
    return int(new_palindrome)

# Example Usage
print(next_smallest_palindrome(12345))  # Output: 12421
print(next_smallest_palindrome(999))    # Output: 1001
print(next_smallest_palindrome(808))    # Output: 818


# Time complexity: O(n)
# Space complexity: O(n)