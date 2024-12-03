# Problem Statement:
# Given a string s and a dictionary of strings wordDict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Constraints:
# Each word in wordDict can be used multiple times.
# The input string s may be empty.
# Words in wordDict are non-empty.
# Example Input and Output:
# Example 1:
# Input:

# plaintext
# Copy code
# s = "leetcode"
# wordDict = ["leet", "code"]
# Output:

# plaintext
# Copy code
# True
# Explanation: The string can be segmented as "leet code".

# Example 2:
# Input:

# plaintext
# Copy code
# s = "applepenapple"
# wordDict = ["apple", "pen"]
# Output:

# plaintext
# Copy code
# True
# Explanation: The string can be segmented as "apple pen apple". Note that "apple" and "pen" can be reused.

# Example 3:
# Input:

# plaintext
# Copy code
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:

# plaintext
# Copy code
# False
# Explanation: The string "catsandog" cannot be segmented into a valid sequence of dictionary words.

# Key Idea (Dynamic Programming Approach):
# Use a boolean DP array dp[] of size 

# n+1, where 

# n is the length of the string s.
# dp[i] represents whether the substring ]
# s[0:i] can be segmented into dictionary words.
# Initialize: True

# dp[0]=True (empty string is always valid).
# Iterate over the string, checking all possible substrings s[j:i] for j<i:
# If dp[j] is True and ∈ wordDict s[j:i]∈wordDict, set = True
# dp[i]=True.
# Return 
# dp[n] as the result.

def wordBreak(s, wordDict):

    # Converting wordDict to set for O(1) lookups
    wordDict = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[len(s)]


# Example Usage
s1 = "leetcode"
wordDict1 = ["leet", "code"]
print(wordBreak(s1, wordDict1))  # Output: True

s2 = "catsandog"
wordDict2 = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s2, wordDict2))  # Output: False


# Time complexity: O(n^2)
# Space complexity: O(n)