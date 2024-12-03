# remove_chars from s1 which is presented in s2

def remove_chars(s1, s2):
    s2 = set(s2)

    return ''.join([i for i in s1 if i not in s2])


# Example Usage
s1 = "abcdef"
s2 = "bd"
print(remove_chars(s1, s2))  # Output: "acef"

s1 = "hello"
s2 = "world"
print(remove_chars(s1, s2))  # Output: "he"

# Time complexity: O(m + n)
# Space complexity: O(n)

# Suppose if we did not use set() for s2 for average of O(1) lookups then the time complexity will be O(m.n) which is slower than last one but we will get space complexity as O(1) as we didn't use set() data structure