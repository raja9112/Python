# Problem Statement:
# Given a string, reverse only its alphabetic characters while leaving the positions of special characters unchanged.

# Example:
# Input:
# s = "a,b$c"
# Output:
# "c,b$a"

# Explanation:
# The alphabetic characters a, b, c are reversed to c, b, a.
# Special characters , and $ remain in their original positions.
# Approach
# Identify Alphabetic Characters: Use two pointers to traverse the string from the left and right, focusing only on alphabetic characters.

# Reverse Only Alphabetic Characters: Swap the alphabetic characters while skipping special characters.

# Keep Special Characters Intact: Use conditions to skip over non-alphabetic characters during traversal.

def reverse_string_keep_special(s):
    res = list(s)
    left, right = 0, len(res)-1

    while left < right:
        if not res[left].isalpha():
            left += 1

        elif not res[right].isalpha():
            right -= 1

        else:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1

    return ''.join(res)


# Example usage
print(reverse_string_keep_special("a,b$c"))  # Output: "c,b$a"
print(reverse_string_keep_special("Ab#c!d"))  # Output: "d#c!bA"