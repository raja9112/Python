# To decode a string recursively encoded as count[substring], where each encoded portion is represented by a number (count) followed by the substring enclosed in square brackets, you can use a stack-based approach or recursion.

# Problem Statement:
# Given a string encoded as count[substring], decode it recursively. For example:

# 3[a] → aaa
# 3[a2[b]] → abbabbabb
# Recursive Approach:
# We parse the string and decode it by repeatedly resolving innermost brackets.



def decode_string(s):
    def helper(index):
        decoded_string = ""
        count = 0

        while index < len(s):
            char = s[index]

            if char.isdigit():
                # Build the count (may have multiple digits)
                count = count * 10 + int(char)

            elif char == '[':
                # Decode the substring inside the brackets
                substring, index = helper(index + 1)
                decoded_string += count * substring
                count = 0  # Reset count after using it

            elif char == ']':
                # End of current decoding level
                return decoded_string, index

            else:
                # Add regular characters to the decoded string
                decoded_string += char

            index += 1

        return decoded_string, index

    # Start decoding from index 0
    decoded_result, _ = helper(0)
    return decoded_result

# Example usage
print(decode_string("3[a2[b]]"))  # Output: "abbabbabb"
print(decode_string("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"
