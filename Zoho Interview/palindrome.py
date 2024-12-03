# To determine if a given number is a palindrome without using arrays or strings, you can reverse the number mathematically and compare it with the original number.

# Palindrome Check Explanation:
# A number is a palindrome if it reads the same backward as forward, e.g., 121, 1331, etc.

# Steps:
# Reverse the number using arithmetic operations.
# Compare the reversed number with the original number.
# If they are the same, the number is a palindrome; otherwise, it is not.


def is_palindrome(n):
    # Handle negative numbers (they cannot be palindromes)

    original = n    # Store the original number
    reversed_num = 0  

    # Reverse the number mathematically
    while n > 0:
        digit = n % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit    # Add digit to reversed_num
        n = n // 10           # Remove the last digit from n

    # Compare the reversed number with the original
    return original == reversed_num

# Example usage
print(is_palindrome(121))  # Output: True
print(is_palindrome(123))  # Output: False
print(is_palindrome(-121)) # Output: False
