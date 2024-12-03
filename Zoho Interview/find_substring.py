# To solve the problem where you need to find the first occurrence of all characters of the second string in the first string 
# and print the substring between the least and highest indices, here's a solution:

def find_substring(str1, str2):
    indices = []

    for char in str2:
        if char in str1:
            indices.append(str1.index(char))
        else:
            return ""   

    if indices:
        min_idx = min(indices)
        max_idx = max(indices)
        return str1[min_idx: max_idx+1]
    

# Example usage
str1 = "abcfadghijk"
str2 = "ac"
print(find_substring(str1, str2))  # Output: "abc"

